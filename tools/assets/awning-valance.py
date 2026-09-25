# The scalloped fringe that hangs from the front edge of a shop awning. Run headless:
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/awning-valance.py
#
# Writes assets/awning-valance.glb, inlined into app/renderer/index.html by
# tools/assets/inline-glb.js.
#
# Origin is the middle of the awning's front edge, at the height the awning
# slab is bottom-flush with; x across (1 unit wide, the placement scales it to
# the awning), y up, z out into the street. A straight flap with a row of
# hanging points along its lower edge, thin front to back so it reads as cloth.
import bpy, bmesh, os

TEETH = 8
WIDTH = 1.0
FLAP_H = 0.16          # the straight part
POINT_H = 0.16         # the teeth below it
THICK = 0.04

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('awning_valance')
bm = bmesh.new()

# The flap: one thin box hanging just below the edge.
flap = bmesh.new()
bmesh.ops.create_cube(flap, size=1.0)
bmesh.ops.scale(flap, vec=(WIDTH, THICK, FLAP_H), verts=flap.verts)
bmesh.ops.translate(flap, vec=(0, 0, -FLAP_H / 2), verts=flap.verts)
flap.to_mesh(mesh)
bm.from_mesh(mesh)
flap.free()

# The teeth: a triangular prism per tooth, point down.
tw = WIDTH / TEETH
for i in range(TEETH):
    cx = -WIDTH / 2 + tw * (i + 0.5)
    m = bmesh.new()
    a = m.verts.new((cx - tw / 2, -THICK / 2, -FLAP_H))
    b = m.verts.new((cx + tw / 2, -THICK / 2, -FLAP_H))
    c = m.verts.new((cx, -THICK / 2, -FLAP_H - POINT_H))
    a2 = m.verts.new((cx - tw / 2, THICK / 2, -FLAP_H))
    b2 = m.verts.new((cx + tw / 2, THICK / 2, -FLAP_H))
    c2 = m.verts.new((cx, THICK / 2, -FLAP_H - POINT_H))
    m.faces.new((a, b, c))
    m.faces.new((c2, b2, a2))
    m.faces.new((a, c, c2, a2))
    m.faces.new((c, b, b2, c2))
    m.faces.new((b, a, a2, b2))
    bmesh.ops.recalc_face_normals(m, faces=m.faces)
    m.to_mesh(mesh)
    bm.from_mesh(mesh)
    m.free()

bm.to_mesh(mesh)
bm.free()
# Blender is Z-up and the glTF exporter turns Z into Y-up and -Y into +Z, so the
# authored "thin in y" becomes thin in z and "down" (-Z) becomes down in y.
obj = bpy.data.objects.new('awning_valance', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'awning-valance.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(p.vertices) - 2 for p in mesh.polygons)
print('ASSET_OK name=awning-valance triangles=%d bytes=%d out=%s' % (tris, os.path.getsize(out), out))
