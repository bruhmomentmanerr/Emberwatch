# The frame a Vaneth window sits in: a surround, a sill that throws the rain
# clear, and a pair of shutters folded back against the wall. Run headless:
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/window-frame.py
#
# Writes assets/window-frame.glb, inlined into app/renderer/index.html by
# tools/assets/inline-glb.js.
#
# Sized to the window the generator already makes: a pane 0.5 wide, 0.66 tall,
# set in the front wall (wardHouse). Origin is the wall face at the centre of
# the pane, x across the frontage, y up, z out into the street.
#
# It is kept deliberately cheap. A door is one per building; windows are two or
# three per storey across 1,400 buildings, so every triangle here is paid for
# thousands of times over.
import bpy, bmesh, os

PANE_W, PANE_H = 0.5, 0.66
FRAME = 0.09          # width of the surround
DEPTH = 0.1           # how far the surround stands off the wall
SILL_OUT, SILL_H = 0.2, 0.08
SHUTTER_W, SHUTTER_D = 0.26, 0.05

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('window_frame')
bm = bmesh.new()

def box(w, h, d, x, y, z):
    m = bmesh.new()
    bmesh.ops.create_cube(m, size=1.0)
    bmesh.ops.scale(m, vec=(w, d, h), verts=m.verts)
    bmesh.ops.translate(m, vec=(x, -z, y), verts=m.verts)
    m.to_mesh(mesh)
    bm.from_mesh(mesh)
    m.free()

half_w = PANE_W / 2 + FRAME / 2
half_h = PANE_H / 2 + FRAME / 2
# Surround: two uprights and two crosspieces, so the pane sits in a frame
# rather than in a hole.
for side in (-1, 1):
    box(FRAME, PANE_H + FRAME * 2, DEPTH, side * half_w, 0, DEPTH / 2)
for updown in (-1, 1):
    box(PANE_W, FRAME, DEPTH, 0, updown * half_h, DEPTH / 2)
# Sill, wider than the opening and proud of it.
box(PANE_W + FRAME * 2 + 0.1, SILL_H, SILL_OUT, 0, -half_h - SILL_H / 2, SILL_OUT / 2 - 0.02)
# Shutters, folded flat against the wall either side.
for side in (-1, 1):
    box(SHUTTER_W, PANE_H + FRAME, SHUTTER_D, side * (half_w + FRAME / 2 + SHUTTER_W / 2), 0, SHUTTER_D / 2)

bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new('window_frame', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'window-frame.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(p.vertices) - 2 for p in mesh.polygons)
print('ASSET_OK name=window-frame triangles=%d bytes=%d out=%s' % (tris, os.path.getsize(out), out))
