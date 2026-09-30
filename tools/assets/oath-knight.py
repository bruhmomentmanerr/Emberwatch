# The rain-oath kneeling knight — first Blender attempt at this (see the
# preview it left behind) used per-part rotations guessed by eye and produced
# a figure whose thigh pointed backward into empty air and whose forearm
# didn't reach the hilt it was supposed to hold. Fixed by building every
# jointed limb from two anchor points (the joint it hangs from, the joint it
# ends at) and deriving the box's length, center and rotation from that pair,
# so a limb is connected to its neighbour by construction instead of by a
# hand-guessed number lining up.
#
# Run headless:
#   "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background \
#     --python tools/assets/oath-knight.py
#
# Writes assets/oath-knight.glb and tools/assets/_preview-oath-knight.png.
# Origin is the ground point between the knight's knee and planted foot, +Z
# is the direction the knight faces.
import bpy, bmesh, os, math
import mathutils

bpy.ops.wm.read_factory_settings(use_empty=True)
mesh = bpy.data.meshes.new('oath_knight')
bm = bmesh.new()

def box(w, h, d, x, y, z, rx=0):
    # rx tilts the piece forward/back (three.js pitch, round the X axis).
    # Because Blender-Z=three.js-Y and Blender-Y=-three.js-Z, a rotation by rx
    # around three.js X turns out to be *exactly* the same rotation by rx
    # around Blender's own X axis, no sign flip — verified against the arch in
    # foxglove-bridge.py, which rotates around the same axis and is correct.
    piece = bmesh.new()
    bmesh.ops.create_cube(piece, size=1.0)
    bmesh.ops.scale(piece, vec=(w, d, h), verts=piece.verts)
    if rx:
        bmesh.ops.rotate(piece, cent=(0, 0, 0), matrix=mathutils.Matrix.Rotation(rx, 4, 'X'), verts=piece.verts)
    bmesh.ops.translate(piece, vec=(x, -z, y), verts=piece.verts)
    piece.to_mesh(mesh)
    bm.from_mesh(mesh)
    piece.free()

def limb(joint_a, joint_b, thick, x=0.0, taper=1.0):
    # joint_a/joint_b are (y, z) pairs. The box's own "up" axis (its h
    # dimension) is rotated and centered to run exactly from a to b, so
    # consecutive limb() calls that share an endpoint always touch there.
    ya, za = joint_a; yb, zb = joint_b
    dy, dz = yb - ya, zb - za
    length = math.hypot(dy, dz)
    rx = math.atan2(dz, dy)
    cy, cz = (ya + yb) * 0.5, (za + zb) * 0.5
    box(thick, length, thick * taper, x, cy, cz, rx)

# Ground contacts: the down knee (kneeling leg) and the forward planted foot.
# Every other joint is an offset from the hip or the shoulder.
HIP = (0.60, 0.02)
DOWN_KNEE = (0.16, -0.22)
DOWN_FOOT = (0.08, -0.46)
FWD_KNEE = (0.58, 0.30)
FWD_FOOT = (0.06, 0.40)
SHOULDER = (1.15, 0.10)
ELBOW = (0.90, 0.24)
HAND = (0.77, 0.32)

# Pelvis and torso, leaning forward slightly the way a bowed head and weight
# on a sword actually sit.
box(0.46, 0.42, 0.30, 0, 0.56, 0.02, rx=0.12)
box(0.42, 0.58, 0.28, 0, 1.02, 0.06, rx=0.20)

# Cloak, draped from the shoulders down the back and pooling behind the
# down knee — the single biggest thing that reads as "kneeling" from a
# distance, since it hides exactly where the primitive version had nothing.
box(0.50, 0.60, 0.10, 0, 0.95, -0.14, rx=0.25)
box(0.40, 0.34, 0.22, 0, 0.32, -0.26, rx=0.38)

# Down leg: knee planted on the ground behind, foot trailing back with the
# ankle low. Up leg: thigh roughly horizontal from hip to a raised knee,
# shin down to the planted foot.
limb(HIP, DOWN_KNEE, 0.20)
limb(DOWN_KNEE, DOWN_FOOT, 0.17)
box(0.19, 0.11, 0.26, 0, 0.05, -0.50, rx=0)
limb(HIP, FWD_KNEE, 0.20)
limb(FWD_KNEE, FWD_FOOT, 0.17)
box(0.19, 0.11, 0.32, 0, 0.055, FWD_FOOT[1] + 0.08, rx=0)

# Head, bowed forward and down over the sword.
box(0.26, 0.28, 0.26, 0, 1.42, 0.14, rx=0.42)
box(0.30, 0.09, 0.30, 0, 1.52, 0.20, rx=0.42)  # helm brim

# Arms reach down from the shoulder to both hands resting on the hilt.
for side in (-1, 1):
    limb(SHOULDER, ELBOW, 0.11, x=side * 0.17)
    limb(ELBOW, HAND, 0.10, x=side * 0.08)

# The planted sword: blade point-down in the ground up to the grip the hands
# rest on, crossguard where blade meets grip, pommel capping the top.
GUARD_Y = 0.66
box(0.045, GUARD_Y, 0.03, 0, GUARD_Y * 0.5, HAND[1], rx=0)
box(0.26, 0.055, 0.055, 0, GUARD_Y, HAND[1], rx=0)
box(0.05, 0.20, 0.05, 0, GUARD_Y + 0.10, HAND[1], rx=0)
box(0.09, 0.09, 0.09, 0, GUARD_Y + 0.235, HAND[1], rx=0)

bm.to_mesh(mesh)
bm.free()
obj = bpy.data.objects.new('oath_knight', mesh)
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
mat = bpy.data.materials.new('preview')
mat.diffuse_color = (0.42, 0.40, 0.45, 1.0)
obj.data.materials.append(mat)
sun = bpy.data.objects.new('sun', bpy.data.lights.new('sun', type='SUN'))
sun.data.energy = 3.2
sun.rotation_euler = (math.radians(55), 0, math.radians(35))
bpy.context.collection.objects.link(sun)
cam_data = bpy.data.cameras.new('cam')
cam = bpy.data.objects.new('cam', cam_data)
cam.location = (2.6, -2.4, 1.05)
cam.rotation_euler = (math.radians(82), 0, math.radians(48))
bpy.context.collection.objects.link(cam)
scene.camera = cam
scene.render.resolution_x = 700
scene.render.resolution_y = 900
preview = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_preview-oath-knight.png'))
scene.render.filepath = preview
bpy.ops.render.render(write_still=True)
obj.data.materials.clear()
bpy.data.materials.remove(mat)

out = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'oath-knight.glb'))
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True,
                          export_apply=True, export_materials='NONE', export_normals=True)
tris = sum(len(poly.vertices) - 2 for poly in mesh.polygons)
print('ASSET_OK name=oath-knight triangles=%d bytes=%d out=%s preview=%s' % (tris, os.path.getsize(out), out, preview))
