# Read the exported city in Blender and report on it as geometry, not as
# screenshots. In-game shots only ever show one standpoint at a time; this
# walks every mesh in the export and answers the questions a walkthrough
# cannot: what is floating, what is buried, what stands alone in the middle of
# nothing, and how the mass is distributed across the map.
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/audit-city.py -- <city.glb> <outdir>
#
# Writes a plain-text report and, if renders are asked for, orthographic
# overviews. Prints AUDIT_ lines so the caller sees the findings without
# opening anything.
import bpy, os, sys, math, json
from mathutils import Vector

argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
if len(argv) < 2:
    print('AUDIT_ERR usage: audit-city.py -- <city.glb> <outdir> [render]')
    sys.exit(1)
glb, outdir = os.path.abspath(argv[0]), os.path.abspath(argv[1])
do_render = len(argv) > 2 and argv[2] == 'render'
os.makedirs(outdir, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
print('AUDIT_INFO importing %s' % os.path.basename(glb))
bpy.ops.import_scene.gltf(filepath=glb)

meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH']
print('AUDIT_INFO meshes=%d' % len(meshes))

# World-space bounds for every mesh, once.
rows = []
for o in meshes:
    mw = o.matrix_world
    pts = [mw @ Vector(c) for c in o.bound_box]
    xs = [p.x for p in pts]; ys = [p.y for p in pts]; zs = [p.z for p in pts]
    rows.append({
        'name': o.name,
        'minx': min(xs), 'maxx': max(xs),
        'miny': min(ys), 'maxy': max(ys),   # Blender Y is the game's -Z
        'minz': min(zs), 'maxz': max(zs),   # Blender Z is up = the game's Y
        'tris': len(o.data.polygons),
    })

def centre(r):
    return ((r['minx'] + r['maxx']) / 2, (r['miny'] + r['maxy']) / 2)

# --- floating: not "high up" — plenty of legitimate geometry is high up, every
# spire finial and chimney cap in the city. Floating means nothing is holding
# it: no other mesh whose footprint overlaps it reaches up to within 3 m
# underneath. Bucketed on a 16 m grid so this is not 20k x 20k comparisons.
CELL = 16.0
grid = {}
for i, r in enumerate(rows):
    for gx in range(int(r['minx'] // CELL), int(r['maxx'] // CELL) + 1):
        for gy in range(int(r['miny'] // CELL), int(r['maxy'] // CELL) + 1):
            grid.setdefault((gx, gy), []).append(i)

def supported(idx):
    r = rows[idx]
    for gx in range(int(r['minx'] // CELL), int(r['maxx'] // CELL) + 1):
        for gy in range(int(r['miny'] // CELL), int(r['maxy'] // CELL) + 1):
            for j in grid.get((gx, gy), ()):
                if j == idx:
                    continue
                o = rows[j]
                # footprints must actually overlap, not merely share a cell
                if o['maxx'] < r['minx'] or o['minx'] > r['maxx']:
                    continue
                if o['maxy'] < r['miny'] or o['miny'] > r['maxy']:
                    continue
                if o['maxz'] >= r['minz'] - 3.0 and o['minz'] <= r['minz'] + 0.5:
                    return True
    return False

candidates = [i for i, r in enumerate(rows)
              if r['minz'] > 2.2 and (r['maxz'] - r['minz']) < 4.0
              and math.hypot(*centre(r)) < 420]
floating = [rows[i] for i in candidates if not supported(i)]
floating.sort(key=lambda r: -r['minz'])
print('AUDIT_FLOATING count=%d' % len(floating))
for r in floating[:14]:
    cx, cy = centre(r)
    print('AUDIT_FLOAT %-26s bottom=%5.2f height=%4.2f at=%7.1f,%7.1f tris=%d'
          % (r['name'][:26], r['minz'], r['maxz'] - r['minz'], cx, -cy, r['tris']))

# --- buried: sitting well below the ground plane inside the walled city, where
# the ground is flat and nothing should be underneath it.
buried = [r for r in rows if r['maxz'] < -0.4 and math.hypot(*centre(r)) < 240]
print('AUDIT_BURIED count=%d' % len(buried))
for r in buried[:8]:
    cx, cy = centre(r)
    print('AUDIT_BURY  %-26s top=%5.2f at=%7.1f,%7.1f' % (r['name'][:26], r['maxz'], cx, -cy))

# --- mass by ring, so thin and crowded parts of the map are visible as numbers
bands = [(0, 70), (70, 140), (140, 240), (240, 320), (320, 400), (400, 520)]
counts = {b: [0, 0] for b in bands}
for r in rows:
    cx, cy = centre(r)
    d = math.hypot(cx, cy)
    for b in bands:
        if b[0] <= d < b[1]:
            counts[b][0] += 1
            counts[b][1] += r['tris']
            break
print('AUDIT_BANDS ring meshes triangles')
for b in bands:
    n, t = counts[b]
    area = math.pi * (b[1] ** 2 - b[0] ** 2) / 10000.0
    print('AUDIT_BAND  %3d-%3dm %5d %9d  %6.1f per hectare' % (b[0], b[1], n, t, n / area if area else 0))

report = os.path.join(outdir, 'city-audit.txt')
with open(report, 'w', encoding='utf-8') as fh:
    json.dump({'meshes': len(rows), 'floating': floating[:80], 'buried': buried[:40]}, fh, indent=1)
print('AUDIT_REPORT %s' % report)

if do_render:
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = 8
    scene.cycles.use_denoising = False
    scene.render.resolution_x = 1400
    scene.render.resolution_y = 1400
    scene.render.image_settings.file_format = 'PNG'
    world = bpy.data.worlds.new('flat'); scene.world = world
    world.use_nodes = True
    world.node_tree.nodes['Background'].inputs[1].default_value = 1.8
    cam_data = bpy.data.cameras.new('top'); cam_data.type = 'ORTHO'
    cam = bpy.data.objects.new('top', cam_data); scene.collection.objects.link(cam); scene.camera = cam
    views = [('whole', 0, 0, 900), ('inner', 0, 0, 330), ('north', 0, 180, 260), ('south', 0, -180, 260)]
    for name, cx, cz, span in views:
        cam_data.ortho_scale = span
        cam.location = (cx, -cz, 400)      # game (x,z) -> blender (x,-y)
        cam.rotation_euler = (0, 0, 0)
        scene.render.filepath = os.path.join(outdir, 'top-%s.png' % name)
        bpy.ops.render.render(write_still=True)
        print('AUDIT_RENDER top-%s.png' % name)
print('AUDIT_DONE')
