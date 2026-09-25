# A banner on a short arm, standing out of a wall into the street. Run headless:
#
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/wall-banner.py
#
# Writes assets/wall-banner.glb, inlined into app/renderer/index.html by
# tools/assets/inline-glb.js.
#
# Origin is the point on the wall face where the arm leaves it: x across the
# frontage, y up, z out into the street. The arm runs out along +z at y=0 and
# the cloth hangs from it, its face turned along the street so it reads from a
# distance down the road — which is how a banner is seen in a real street.
# Arm and cloth are one mesh in one colour; the placement picks the colour.
import bpy, bmesh, os

ARM_LEN, ARM_T = 0.95, 0.07
CLOTH_T = 0.03
CLOTH_W, CLOTH_H, TAIL = 0.62, 1.35, 0.3

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('wall_banner')
bm = bmesh.new()

# The arm.
arm = bmesh.new()
bmesh.ops.create_cube(arm, size=1.0)
bmesh.ops.scale(arm, vec=(ARM_T, ARM_LEN, ARM_T), verts=arm.verts)
# Blender (x, y, z) exports as three.js (x, z, -y) rotated: authored y is depth
# out into the street, z is up.
bmesh.ops.translate(arm, vec=(0, -ARM_LEN / 2, 0), verts=arm.verts)
arm.to_mesh(mesh)
bm.from_mesh(mesh)
arm.free()

# The cloth: a swallow-tailed strip hanging from the arm's outer half, thin in
# x. Outline in (depth, height) with the tail cut into the bottom edge.
z0 = 0.22
outline = [(z0, -ARM_T / 2), (z0 + CLOTH_W, -ARM_T / 2),
           (z0 + CLOTH_W, -CLOTH_H), (z0 + CLOTH_W / 2, -CLOTH_H + TAIL), (z0, -CLOTH_H)]
cloth = bmesh.new()
front = [cloth.verts.new((-CLOTH_T / 2, -d, h)) for d, h in outline]
back = [cloth.verts.new((CLOTH_T / 2, -d, h)) for d, h in outline]
cloth.faces.new(front)
cloth.faces.new(list(reversed(back)))
n = len(outline)
for i in range(n):
    j = (i + 1) % n
    cloth.faces.new((front[i], front[j], back[j], back[i]))
bmesh.ops.recalc_face_normals(cloth, faces=cloth.faces)
bmesh.ops.triangulate(cloth, faces=cloth.faces)
cloth.to_mesh(mesh)
bm.from_mesh(mesh)
cloth.free()

bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new('wall_banner', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'wall-banner.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(p.vertices) - 2 for p in mesh.polygons)
print('ASSET_OK name=wall-banner triangles=%d bytes=%d out=%s' % (tris, os.path.getsize(out), out))
