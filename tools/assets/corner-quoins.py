# A corner column of dressed stone, laid long-side-out and short-side-out on
# alternate courses so the two walls look tied together. Run headless:
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/corner-quoins.py
#
# Writes assets/corner-quoins.glb, inlined into app/renderer/index.html by
# tools/assets/inline-glb.js.
#
# Origin is the outside corner of a wall at ground level, y up. The blocks are
# centred on the corner and symmetric, so the same piece serves the left and
# the right corner of a front without a mirrored (inside-out) copy. It is one
# storey-and-a-bit tall, 2.7 m; the placement scales it in y to the building.
import bpy, bmesh, os

COURSES = 6
COURSE_H = 2.7 / COURSES
LONG, SHORT = 0.62, 0.34      # a block's two faces; the wall is proud by half of SHORT

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('corner_quoins')
bm = bmesh.new()

def box(w, h, d, x, y, z):
    m = bmesh.new()
    bmesh.ops.create_cube(m, size=1.0)
    bmesh.ops.scale(m, vec=(w, d, h), verts=m.verts)
    bmesh.ops.translate(m, vec=(x, z, y), verts=m.verts)
    m.to_mesh(mesh)
    bm.from_mesh(mesh)
    m.free()

for i in range(COURSES):
    y = COURSE_H * i + COURSE_H / 2
    # a hair under full height so neighbouring courses show a joint
    h = COURSE_H - 0.03
    if i % 2 == 0:
        box(LONG, h, SHORT, 0, y, 0)
    else:
        box(SHORT, h, LONG, 0, y, 0)

bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new('corner_quoins', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'corner-quoins.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(p.vertices) - 2 for p in mesh.polygons)
print('ASSET_OK name=corner-quoins triangles=%d bytes=%d out=%s' % (tris, os.path.getsize(out), out))
