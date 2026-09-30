# A real stone arch bridge for the Foxglove crossing — replacing the primitive
# pile currently there (a flat cobble slab plus two mismatched parapet stubs,
# spanning nothing: the site has no water at all). This carries the water:
# addBridgeCastleCanon() in app/renderer/index.html is rewritten alongside this
# script to add an actual river beneath it.
#
# Run headless:
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/foxglove-bridge.py
#
# Writes assets/foxglove-bridge.glb and, for a look before it ever touches the
# game, a render preview to tools/assets/_preview-foxglove-bridge.png.
#
# Axis: the box() and arc() helpers below take (x, y, z) already in three.js
# terms (x right, y up, z depth) and translate as (x, -z, y) internally, which
# is the one rule this project's asset scripts must never get backwards.
import bpy, bmesh, os, math

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('foxglove_bridge')
bm = bmesh.new()

def box(w, h, d, x, y, z):
    piece = bmesh.new()
    bmesh.ops.create_cube(piece, size=1.0)
    bmesh.ops.scale(piece, vec=(w, d, h), verts=piece.verts)
    bmesh.ops.translate(piece, vec=(x, -z, y), verts=piece.verts)
    piece.to_mesh(mesh)
    bm.from_mesh(mesh)
    piece.free()

# The visible arch: a faceted semicircle of voussoir blocks between the two
# piers, each block a short radial box so the curve reads at this game's
# chunky low-poly scale rather than needing a smooth cylinder.
def arc(cx, cy, cz, radius, thickness, width, start_deg, end_deg, segments):
    # The curve has to vary height (y) and position-along-the-span (z), with x
    # (the bridge's width) held constant — every voussoir already reaches the
    # full width via its own "width" scale. Varying x and y instead, as a first
    # pass here did, traces the arc sideways off the end of the bridge rather
    # than underneath it: caught in the preview render below, not in the game.
    for i in range(segments):
        t0 = math.radians(start_deg + (end_deg - start_deg) * i / segments)
        t1 = math.radians(start_deg + (end_deg - start_deg) * (i + 1) / segments)
        tm = (t0 + t1) * 0.5
        span = math.hypot((math.cos(t1) - math.cos(t0)) * radius, (math.sin(t1) - math.sin(t0)) * radius)
        z = cz + math.cos(tm) * radius
        y = cy + math.sin(tm) * radius
        piece = bmesh.new()
        bmesh.ops.create_cube(piece, size=1.0)
        bmesh.ops.scale(piece, vec=(width, thickness, span * 1.04), verts=piece.verts)
        # Each voussoir rotates round the width axis to stay tangent to the
        # arc at its own midpoint angle.
        bmesh.ops.rotate(piece, cent=(0, 0, 0), matrix=bpy_rot_x(-tm), verts=piece.verts)
        bmesh.ops.translate(piece, vec=(cx, -z, y), verts=piece.verts)
        piece.to_mesh(mesh)
        bm.from_mesh(mesh)
        piece.free()

def bpy_rot_x(angle):
    import mathutils
    return mathutils.Matrix.Rotation(angle, 4, 'X')

HALF_SPAN = 4.3      # deck runs z -4.3..4.3, matching the site's water width
DECK_W = 3.4
DECK_TOP = 0.0       # walkable surface stays at ground level, no stepped terrain
DECK_THK = 0.4
PIER_LEN = 1.7
PIER_H = 1.7
PIER_TOP = DECK_TOP - DECK_THK

# Deck: one slab the full length, top face exactly at y=0.
box(DECK_W, DECK_THK, HALF_SPAN * 2, 0, DECK_TOP - DECK_THK / 2, 0)

# Two abutment piers, one at each end, hanging below the deck into the bank.
for side in (-1, 1):
    pz = side * (HALF_SPAN - PIER_LEN / 2)
    box(DECK_W, PIER_H, PIER_LEN, 0, PIER_TOP - PIER_H / 2, pz)

# The arch: a faceted half-round connecting the two piers' inner faces,
# springing from pier-top height and rising to meet the deck's underside at
# the span's midpoint. Radius set so the crown just touches the deck.
inner_gap = HALF_SPAN - PIER_LEN            # clear water opening, one side
crown_y = PIER_TOP
radius = inner_gap
arc(0, crown_y - radius, 0, radius, 0.55, DECK_W - 0.3, 0, 180, 9)

# Parapets along both long edges, standing on the deck.
for side in (-1, 1):
    box(0.28, 0.55, HALF_SPAN * 2, side * (DECK_W / 2 - 0.05), DECK_TOP + 0.275, 0)
    # A cap band reads as a coping stone rather than a plain wall top.
    box(0.36, 0.10, HALF_SPAN * 2, side * (DECK_W / 2 - 0.05), DECK_TOP + 0.55, 0)

# End posts, so the parapet does not just stop mid-air at the bank.
for side_x in (-1, 1):
    for side_z in (-1, 1):
        box(0.42, 0.85, 0.42, side_x * (DECK_W / 2 - 0.05), DECK_TOP + 0.425, side_z * (HALF_SPAN - 0.21))

bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new('foxglove_bridge', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
for poly in mesh.polygons:
    poly.use_smooth = False

# A quick lit preview, rendered BEFORE export, so this is judged as a finished
# model instead of being placed blind and checked only once it is already in
# the game — which is exactly the class of bug this asset replaces.
scene = bpy.context.scene
scene.render.engine = 'BLENDER_EEVEE_NEXT' if hasattr(bpy.types, 'BlenderEEVEE_Next') else 'BLENDER_EEVEE'
try:
    scene.render.engine = 'BLENDER_EEVEE'
except Exception:
    pass
mat = bpy.data.materials.new('preview_stone')
mat.diffuse_color = (0.43, 0.39, 0.32, 1.0)
obj.data.materials.append(mat)
sun = bpy.data.objects.new('sun', bpy.data.lights.new('sun', type='SUN'))
sun.data.energy = 3.2
sun.rotation_euler = (math.radians(55), 0, math.radians(35))
bpy.context.collection.objects.link(sun)
cam_data = bpy.data.cameras.new('cam')
cam = bpy.data.objects.new('cam', cam_data)
cam.location = (13.5, 0, 0.2)
cam.rotation_euler = (math.radians(90), 0, math.radians(90))
bpy.context.collection.objects.link(cam)
scene.camera = cam
scene.render.resolution_x = 900
scene.render.resolution_y = 620
preview = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_preview-foxglove-bridge.png'))
scene.render.filepath = preview
bpy.ops.render.render(write_still=True)
obj.data.materials.clear()
bpy.data.materials.remove(mat)

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'foxglove-bridge.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(poly.vertices) - 2 for poly in mesh.polygons)
print('ASSET_OK name=foxglove-bridge triangles=%d bytes=%d out=%s preview=%s' % (tris, os.path.getsize(out), out, preview))
