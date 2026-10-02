# The lower-town overlook's hooded watcher and the north-skywatch companions
# share one archetype — a standing or seated cloaked figure — so this one
# script builds all three, each its own object exported to its own .glb, using
# the box() helper proven correct in oath-knight.py (a rotation around
# Blender's X axis needs no sign flip against three.js X — verified there
# after a first, wrong attempt scattered the geometry).
#
# (r159) Neither model is in the game any more. The hooded watcher and the two
# companions are the NPC kit's people now, posed on its rig (placePosedFigures
# in index.html); this script and its .glb files are kept as the history.
#
# Run headless:
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/hooded-watcher.py
import bpy, bmesh, os, math
import mathutils

def new_mesh(name):
    return bpy.data.meshes.new(name), bmesh.new()

def make_box_fn(mesh, bm):
    def box(w, h, d, x, y, z, rx=0):
        piece = bmesh.new()
        bmesh.ops.create_cube(piece, size=1.0)
        bmesh.ops.scale(piece, vec=(w, d, h), verts=piece.verts)
        if rx:
            bmesh.ops.rotate(piece, cent=(0, 0, 0), matrix=mathutils.Matrix.Rotation(rx, 4, 'X'), verts=piece.verts)
        bmesh.ops.translate(piece, vec=(x, -z, y), verts=piece.verts)
        piece.to_mesh(mesh)
        bm.from_mesh(mesh)
        piece.free()
    return box

def finish_and_export(name, mesh, bm, cam_loc, cam_rot, res=(700, 900)):
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    for poly in mesh.polygons:
        poly.use_smooth = False

    scene = bpy.context.scene
    try:
        scene.render.engine = 'BLENDER_EEVEE_NEXT'
    except Exception:
        scene.render.engine = 'BLENDER_EEVEE'
    mat = bpy.data.materials.new('preview_' + name)
    mat.diffuse_color = (0.42, 0.40, 0.45, 1.0)
    obj.data.materials.append(mat)
    for o in list(bpy.data.objects):
        if o.type == 'LIGHT' or o.type == 'CAMERA':
            bpy.data.objects.remove(o, do_unlink=True)
    sun = bpy.data.objects.new('sun', bpy.data.lights.new('sun', type='SUN'))
    sun.data.energy = 3.2
    sun.rotation_euler = (math.radians(55), 0, math.radians(35))
    bpy.context.collection.objects.link(sun)
    cam_data = bpy.data.cameras.new('cam')
    cam = bpy.data.objects.new('cam', cam_data)
    cam.location = cam_loc
    cam.rotation_euler = cam_rot
    bpy.context.collection.objects.link(cam)
    scene.camera = cam
    scene.render.resolution_x, scene.render.resolution_y = res
    preview = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_preview-%s.png' % name))
    scene.render.filepath = preview
    bpy.ops.render.render(write_still=True)
    obj.data.materials.clear()
    bpy.data.materials.remove(mat)

    out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', '%s.glb' % name))
    bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                              export_apply=True, export_materials='NONE', export_normals=True)
    tris = sum(len(poly.vertices) - 2 for poly in mesh.polygons)
    print('ASSET_OK name=%s triangles=%d bytes=%d out=%s preview=%s' % (name, tris, os.path.getsize(out), out, preview))
    bpy.data.objects.remove(obj, do_unlink=True)
    bpy.data.meshes.remove(mesh)


# ---------------------------------------------------------------- watcher --
# Standing, weight on one leg, hood up, a bow held loosely at the side —
# "dark foreground watcher above warm lower town".
bpy.ops.wm.read_factory_settings(use_empty=True)
mesh, bm = new_mesh('hooded_watcher')
box = make_box_fn(mesh, bm)

box(0.36, 0.62, 0.26, 0, 1.02, 0, rx=0.06)             # torso, upright
box(0.30, 0.34, 0.34, 0, 1.58, -0.02, rx=0.10)         # head under the hood
box(0.44, 0.30, 0.40, 0, 1.68, -0.05, rx=0.10)         # hood, a size proud of the head
box(0.40, 0.92, 0.20, 0, 0.78, -0.14, rx=0.05)         # cloak body, hanging past the hips
box(0.34, 0.30, 0.10, 0, 1.30, -0.24, rx=0.35)         # cloak shoulder drape
box(0.16, 0.80, 0.16, -0.11, 0.40, 0.04, rx=-0.12)     # weight leg, straight
box(0.16, 0.76, 0.16, 0.13, 0.42, -0.08, rx=0.32)      # trail leg, bent back
box(0.19, 0.11, 0.30, -0.11, 0.055, 0.10)              # feet
box(0.19, 0.11, 0.28, 0.13, 0.075, -0.20)
box(0.11, 0.46, 0.11, -0.20, 0.86, 0.04, rx=0.55)      # near arm, holding the bow low
box(0.10, 0.40, 0.10, 0.18, 0.90, -0.02, rx=0.15)      # far arm, at the side
box(0.035, 1.02, 0.03, -0.24, 0.62, 0.10, rx=0.02)     # the bow stave

finish_and_export('hooded-watcher', mesh, bm, (2.4, -2.6, 1.15), (math.radians(82), 0, math.radians(43)))


# ---------------------------------------------------------------- skywatch -
# Seated, knees drawn up, looking up at the sky — the pair sit side by side in
# the game with a light and bare trees between them; the wings on the winged
# variant are added by dressPoints placing a second, tiny wing-only piece so
# the base figure stays shared. Simpler here: one seated figure, no wings on
# the model itself — the winged copy keeps its cloth-cone wing pair from the
# original code, which reads fine and is cheap; modelling effort goes to the
# body, which was the part actually unreadable at ground level.
bpy.ops.wm.read_factory_settings(use_empty=True)
mesh, bm = new_mesh('skywatch_companion')
box = make_box_fn(mesh, bm)

box(0.34, 0.42, 0.30, 0, 0.52, -0.02)                    # torso, upright — no tilt, so nothing
box(0.26, 0.28, 0.28, 0, 0.885, 0.02)                    # separates from it at the neck seam
box(0.32, 0.11, 0.32, 0, 0.965, 0.01)                    # hat, flush on the head, also untilted
box(0.15, 0.30, 0.34, -0.14, 0.30, 0.28, rx=1.15)        # near thigh, raised knee
box(0.14, 0.30, 0.14, -0.14, 0.12, 0.42, rx=-0.15)       # near shin, foot tucked under the knee
box(0.15, 0.30, 0.34, 0.14, 0.30, 0.28, rx=1.15)         # far thigh
box(0.14, 0.30, 0.14, 0.14, 0.12, 0.42, rx=-0.15)        # far shin
box(0.18, 0.10, 0.24, -0.14, 0.05, 0.36)                 # feet
box(0.18, 0.10, 0.24, 0.14, 0.05, 0.36)
box(0.09, 0.30, 0.09, -0.19, 0.55, 0.16, rx=0.55)        # forearm resting on the raised knee
box(0.09, 0.30, 0.09, 0.19, 0.55, 0.16, rx=0.55)

finish_and_export('skywatch-companion', mesh, bm, (1.9, -2.1, 1.0), (math.radians(80), 0, math.radians(42)))
