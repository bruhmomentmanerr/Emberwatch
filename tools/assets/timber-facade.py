# A heavy, slightly crooked upper-storey timber frame for Vaneth's two-storey
# infill houses.  It gives the city the hand-built, deep-shadowed construction
# of the supplied visual reference without changing a single seeded footprint.
#
# Run headless:
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/timber-facade.py
#
# Writes assets/timber-facade.glb; tools/assets/inline-glb.js folds it into the
# one-file game. Origin: the centre of a facade's upper storey, with x across
# the front, y up and z out from the wall after glTF's Blender-to-three mapping.
import bpy, bmesh, os, math
from mathutils import Matrix

WIDTH, HEIGHT = 8.0, 2.42
BEAM, DEPTH = 0.24, 0.18

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('timber_facade')
bm = bmesh.new()

def box(w, h, d, x, y, z, tilt=0.0):
    """Hard-edged box, with optional lean in the facade plane."""
    piece = bmesh.new()
    bmesh.ops.create_cube(piece, size=1.0)
    bmesh.ops.scale(piece, vec=(w, d, h), verts=piece.verts)
    if tilt:
        bmesh.ops.rotate(piece, verts=piece.verts, cent=(0, 0, 0),
                          matrix=Matrix.Rotation(tilt, 4, 'Y'))
    bmesh.ops.translate(piece, vec=(x, -z, y), verts=piece.verts)
    piece.to_mesh(mesh)
    bm.from_mesh(mesh)
    piece.free()

# A low sill and a hefty head beam make the upper floor read as a constructed
# timber panel, not a texture stamped on a rectangular wall.
box(WIDTH, BEAM, DEPTH, 0, BEAM * .5, DEPTH * .5)
box(WIDTH + .12, BEAM * 1.12, DEPTH * 1.08, 0, HEIGHT - BEAM * .56, DEPTH * .54)

# Uneven upright spacing deliberately avoids a machine-perfect Tudor grid.
for x, lean in [(-WIDTH*.475, -.018), (-WIDTH*.18, .012), (WIDTH*.16, -.014), (WIDTH*.475, .018)]:
    box(BEAM, HEIGHT - BEAM * 1.25, DEPTH, x, HEIGHT * .5, DEPTH * .5, lean)

# Two braces make a readable zig-zag silhouette at street distance.  They are
# thin enough to let the existing lit windows remain legible behind them.
diag_w = WIDTH * .42
diag_h = HEIGHT - BEAM * 1.7
diag_len = math.hypot(diag_w, diag_h)
angle = math.atan2(diag_w, diag_h)
box(BEAM * .84, diag_len, DEPTH * .9, -WIDTH * .245, HEIGHT * .5, DEPTH * .58, -angle)
box(BEAM * .84, diag_len, DEPTH * .9, WIDTH * .245, HEIGHT * .5, DEPTH * .58, angle)

bm.to_mesh(mesh)
bm.free()

obj = bpy.data.objects.new('timber_facade', mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
for poly in mesh.polygons:
    poly.use_smooth = False

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'timber-facade.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(poly.vertices) - 2 for poly in mesh.polygons)
print('ASSET_OK name=timber-facade triangles=%d bytes=%d out=%s' % (tris, os.path.getsize(out), out))
