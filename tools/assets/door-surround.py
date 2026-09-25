# The stone surround a Vaneth front door stands in: two jambs, a lintel across
# them, and a step worn into the street. Run headless:
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/door-surround.py
#
# Writes assets/door-surround.glb; tools/assets/inline-glb.js folds it into
# app/renderer/index.html, which has to stay one file.
#
# It is built around the door the generator already makes: a panel 1.0 wide and
# 1.9 tall, set in the front wall, its centre 0.95 off the ground (wardHouse).
# The surround sits proud of that wall by DEPTH, so the model's origin is the
# wall face, x across the frontage, y up, z out into the street — which is how
# the placement code hands it a matrix.
#
# Flat-shaded boxes on purpose: the city is boxes and cones, and a bevelled,
# smooth-shaded doorway would read as pasted in from another game.
import bpy, bmesh, os, math

DOOR_W, DOOR_H = 1.0, 1.9
JAMB_W, DEPTH = 0.17, 0.22
LINTEL_H = 0.23
STEP_OUT, STEP_H = 0.34, 0.11

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('door_surround')
bm = bmesh.new()

def box(w, h, d, x, y, z):
    """A box of that size with its centre at x,y,z — Blender Z-up, so y here is depth."""
    m = bmesh.new()
    bmesh.ops.create_cube(m, size=1.0)
    bmesh.ops.scale(m, vec=(w, d, h), verts=m.verts)
    bmesh.ops.translate(m, vec=(x, -z, y), verts=m.verts)
    m.to_mesh(mesh)
    bm.from_mesh(mesh)
    m.free()

half = DOOR_W / 2 + JAMB_W / 2
# Jambs, one either side of the opening, standing from the ground to the lintel.
for side in (-1, 1):
    box(JAMB_W, DOOR_H + 0.08, DEPTH, side * half, (DOOR_H + 0.08) / 2, DEPTH / 2)
# The lintel, a little wider than the pair of jambs and a little deeper, so it
# reads as a stone laid across them rather than as part of the wall.
box(DOOR_W + JAMB_W * 2 + 0.12, LINTEL_H, DEPTH + 0.05, 0, DOOR_H + 0.08 + LINTEL_H / 2, (DEPTH + 0.05) / 2)
# The step: wider than the door, low, worn out into the street.
box(DOOR_W + 0.34, STEP_H, STEP_OUT, 0, STEP_H / 2, STEP_OUT / 2)

bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new('door_surround', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
# Blender is Z-up; the glTF exporter hands three.js Y-up, and the boxes above
# were authored with that in mind (z argument is depth, y is height).
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'door-surround.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(p.vertices) - 2 for p in mesh.polygons)
print('ASSET_OK name=door-surround triangles=%d bytes=%d out=%s' % (tris, os.path.getsize(out), out))
