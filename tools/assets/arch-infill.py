# The stone that fills a sealed arch (Ember Hour). Run headless:
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/arch-infill.py
#
# Writes assets/arch-infill.glb, which tools/assets/inline-glb.js folds into
# variants/src/emberhour.js as base64 — a variant has to stay one file.
#
# The opening it fills: posts 0.7 square at x = +-1.9, so the gap between their
# inner faces is 3.1 wide; the lintel sits at y 5.0. The infill is built a
# little inside that on every side so nothing z-fights with the arch itself.
# Courses of blocks, seeded so the same run gives the same stone, flat-shaded
# and kept under a few hundred triangles: the city is boxes and cones, and a
# smooth-shaded panel would read as pasted in.
import bpy, bmesh, os, math, random

WIDTH, HEIGHT, DEPTH = 3.06, 4.96, 0.30
COURSE = 0.44                      # height of a course of stone
SEED = 7

random.seed(SEED)
bpy.ops.wm.read_factory_settings(use_empty=True)

mesh = bpy.data.meshes.new('arch_infill')
bm = bmesh.new()

def block(cx, cy, w, h, d, tilt):
    """One stone, as a box, tilted a hair so the courses are not machine-true."""
    m = bmesh.new()
    bmesh.ops.create_cube(m, size=1.0)
    bmesh.ops.scale(m, vec=(w, h, d), verts=m.verts)
    bmesh.ops.rotate(m, verts=m.verts, cent=(0, 0, 0),
                     matrix=bpy.data.objects.data.__class__ and __import__('mathutils').Matrix.Rotation(tilt, 3, 'Z'))
    bmesh.ops.translate(m, vec=(cx, cy, 0), verts=m.verts)
    m.to_mesh(mesh)
    bm.from_mesh(mesh)
    m.free()

courses = int(HEIGHT / COURSE)
gap = 0.012                        # a hair of shadow between stones
y = -HEIGHT / 2 + COURSE / 2
for row in range(courses):
    # Every other course starts half a stone over, the way a wall is laid.
    offset = 0.0 if row % 2 == 0 else 0.38
    x = -WIDTH / 2
    run = []
    while x < WIDTH / 2 - 0.05:
        w = random.uniform(0.52, 0.92) if not run or offset == 0 else random.uniform(0.44, 0.88)
        if run == [] and offset:
            w = offset
        w = min(w, WIDTH / 2 - x)
        run.append((x + w / 2, w))
        x += w + gap
    for cx, w in run:
        d = DEPTH * random.uniform(0.72, 1.0)
        block(cx, y, max(0.08, w - gap), COURSE - gap, d, random.uniform(-0.015, 0.015))
    y += COURSE

bm.to_mesh(mesh)
bm.free()

obj = bpy.data.objects.new('arch_infill', mesh)
bpy.context.collection.objects.link(obj)
# Blender is Z-up and the exporter turns it into three.js's Y-up, so the panel
# is built in the XY plane here and arrives standing in XY there.
obj.rotation_euler = (math.radians(90), 0, 0)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'arch-infill.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(p.vertices) - 2 for p in mesh.polygons)
size = os.path.getsize(out)
print('ASSET_OK name=arch-infill triangles=%d bytes=%d out=%s' % (tris, size, out))
