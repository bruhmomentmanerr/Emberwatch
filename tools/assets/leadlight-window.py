# A small irregular leaded-glass insert for Vaneth's arcane windows. It carries
# no copied reference content: only the reference's jewel-colour / heavy-frame
# visual grammar, sized to Emberwatch's existing 0.5 x 0.66 window opening.
#
# Run headless:
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/leadlight-window.py
#
# Writes assets/leadlight-window.glb; tools/assets/inline-glb.js folds it into
# the one-file game. Origin is the window centre at the wall face.
import bpy, bmesh, os

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('leadlight_window')
bm = bmesh.new()

def box(w, h, d, x, y, z):
    piece = bmesh.new()
    bmesh.ops.create_cube(piece, size=1.0)
    bmesh.ops.scale(piece, vec=(w, d, h), verts=piece.verts)
    bmesh.ops.translate(piece, vec=(x, -z, y), verts=piece.verts)
    piece.to_mesh(mesh)
    bm.from_mesh(mesh)
    piece.free()

# A luminous inset divided by asymmetrical lead bars. It sits just proud of the
# existing pane but inside the outer timber frame, so the city remains legible
# from a distance and rewards a closer street view.
box(.43, .57, .028, 0, 0, .032)
box(.045, .58, .045, -.05, 0, .065)
box(.45, .045, .045, .015, .08, .067)
box(.045, .23, .045, .15, .18, .067)
box(.045, .20, .045, -.19, -.18, .067)

bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new('leadlight_window', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'leadlight-window.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(poly.vertices) - 2 for poly in mesh.polygons)
print('ASSET_OK name=leadlight-window triangles=%d bytes=%d out=%s' % (tris, os.path.getsize(out), out))
