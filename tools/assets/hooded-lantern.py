# A warm hooded lantern and crooked bracket for selected Vaneth doors.  It is
# visual only: city lighting remains under the fixed point-light budget.
#
# Run headless:
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/hooded-lantern.py
#
# Writes assets/hooded-lantern.glb; it is inlined into the one-file game by
# tools/assets/inline-glb.js. Origin is the door centre on the wall face.
import bpy, bmesh, os

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('hooded_lantern')
bm = bmesh.new()

def box(w, h, d, x, y, z):
    piece = bmesh.new()
    bmesh.ops.create_cube(piece, size=1.0)
    bmesh.ops.scale(piece, vec=(w, d, h), verts=piece.verts)
    bmesh.ops.translate(piece, vec=(x, -z, y), verts=piece.verts)
    piece.to_mesh(mesh)
    bm.from_mesh(mesh)
    piece.free()

# The bracket climbs the wall then comes forward, giving each lantern a dark
# silhouette against the facade rather than a floating point of colour.
box(.11, .72, .12, .52, 2.63, .06)
box(.11, .11, .56, .52, 2.94, .28)
box(.09, .36, .09, .52, 2.77, .52)
# Hood, small body and lower cap. The game supplies the amber emissive material.
box(.42, .10, .42, .52, 2.91, .54)
box(.30, .46, .30, .52, 2.64, .54)
box(.38, .09, .38, .52, 2.39, .54)
# Cross bars turn the light into a little carried object rather than a cube.
box(.05, .42, .05, .37, 2.64, .54)
box(.05, .42, .05, .67, 2.64, .54)

bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new('hooded_lantern', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'hooded-lantern.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(poly.vertices) - 2 for poly in mesh.polygons)
print('ASSET_OK name=hooded-lantern triangles=%d bytes=%d out=%s' % (tris, os.path.getsize(out), out))
