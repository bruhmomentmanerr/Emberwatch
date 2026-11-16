# Orren of the Broken Hall (r175), sculpted: the ruin wizard after the
# owner's reference frame, seen as the reference sees him, from behind on his
# rock. Until r175 he was the residents' kit, which made a stiff cone of a
# hat, a flat sheet of hair to the ground and a robe as narrow as a coat.
# The reference's wizard is old and stooped: a heavy mantle over a long robe
# that pools at the feet, a broad floppy hat whose crown bends back, white
# hair falling in locks over his shoulders to the middle of his back, a long
# white beard, and a gnarled staff held out in his right hand with a violet
# crystal in its claw.
#
# Built with Muse's hybrid pipeline (tools/assets/dunna-wex.py): the body's
# forms are coloured kit parts, fused into one skin by a voxel remesh, the
# robe's folds re-cut, a little clay noise and a polish pass, decimated, and
# the occlusion baked into the vertex colours. The hat, the hair's locks and
# the staff stay kit-built on top: their edges should stay sharp.
#
# Local frame (game axes): he faces +Z, his right hand is on -X, y=0 is his
# feet. About 1.85 m to the top of his head, 2.4 m to his hat's tip; the staff
# stands to 2.25 m. The crystal carries the vertex-alpha glow mask.
#
#   python tools/assets/orren.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset, g2b
import bpy

ROBE = (.13, .12, .24)
ROBE_D = (.08, .07, .15)
ROBE_L = (.20, .18, .34)
MANTLE = (.10, .09, .19)
HAT = (.09, .08, .15)
HAT_L = (.15, .13, .24)
HAIR = (.78, .78, .84)
HAIR_D = (.60, .58, .68)
SKIN = (.82, .64, .54)
WOOD = (.20, .14, .10)
WOOD_D = (.13, .09, .07)
CRYSTAL = (.80, .62, 1.0, .1)

SEED = 1752
VOXEL = 0.018
TARGET_TRIS = 5200

bpy.ops.wm.read_factory_settings(use_empty=True)


def part(name, fn):
    pa = Asset(name, seed=SEED)
    fn(pa)
    return pa.build()


def tris_of(obj):
    return sum(len(p.vertices) - 2 for p in obj.data.polygons)


# ---- the body's forms ---------------------------------------------------------
# He stoops: the line of his back leans forward from the hips, the head
# carried ahead of the shoulders.
def _robe(a):
    a.tube([(0, .01, -.01), (0, .30, 0), (0, .62, .01), (0, .95, .03), (0, 1.18, .06), (0, 1.36, .10)],
           [(.36, .33), (.30, .27), (.25, .22), (.22, .18), (.21, .16), (.20, .15)],
           [ROBE_D, ROBE, ROBE, ROBE, ROBE], sides=14, folds=9, amps=[.10, .09, .07, .05, .03, .01])


def _mantle(a):
    # a heavy cape over the shoulders and down the back to the knees, broad
    # across the shoulders; and the stoop's hump under it
    a.tube([(0, 1.50, .11), (0, 1.40, .07), (0, 1.15, .01), (0, .85, -.04), (0, .55, -.07)],
           [(.27, .19), (.30, .22), (.29, .21), (.28, .21), (.30, .23)],
           [MANTLE, MANTLE, ROBE_D, ROBE_D], sides=14, folds=7, amps=[0, .02, .05, .07, .09])
    a.tube([(0, 1.43, -.02), (0, 1.33, -.07), (0, 1.20, -.06)], [.13, .15, .10], MANTLE, sides=10)


def _head(a):
    a.tube([(0, 1.48, .14), (0, 1.55, .17)], [.06, .055], SKIN, sides=8)                   # neck
    a.tube([(0, 1.53, .19), (0, 1.60, .21), (0, 1.68, .20), (0, 1.74, .18), (0, 1.77, .16)],
           [.06, .095, .10, .08, .03], SKIN, sides=10)
    # the hair's mass behind and over the head
    a.tube([(0, 1.74, .17), (0, 1.70, .10), (0, 1.58, .07), (0, 1.40, .03)],
           [.11, .12, .13, .10], HAIR, sides=10)


def _arms(a):
    # his right arm (on -X) out and forward to the staff at shoulder height;
    # the left arm down and forward, its hand in the bell of its sleeve
    a.tube([(-.24, 1.40, .07), (-.36, 1.25, .14), (-.44, 1.16, .26)], [.085, .075, .07], ROBE, sides=9)
    a.tube([(-.44, 1.16, .26), (-.46, 1.14, .33)], [.075, .10], ROBE_L, sides=10)          # sleeve's bell
    a.tube([(-.46, 1.15, .30), (-.47, 1.15, .37)], [.04, .035], SKIN, sides=7)              # the hand round the staff
    a.tube([(.23, 1.40, .07), (.28, 1.14, .14), (.22, .96, .24)], [.085, .075, .07], ROBE, sides=9)
    a.tube([(.22, .96, .24), (.19, .90, .30)], [.075, .11], ROBE_L, sides=10)


parts = [part('or-robe', _robe), part('or-mantle', _mantle), part('or-head', _head), part('or-arms', _arms)]

bpy.ops.object.select_all(action='DESELECT')
for o in parts:
    o.select_set(True)
bpy.context.view_layer.objects.active = parts[0]
bpy.ops.object.join()
src = bpy.context.view_layer.objects.active
print('HYBRID src tris=%d' % tris_of(src))

body = src.copy()
body.data = src.data.copy()
bpy.context.collection.objects.link(body)
body.data.remesh_mode = 'VOXEL'
body.data.remesh_voxel_size = VOXEL
body.data.use_remesh_preserve_volume = True
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True)
bpy.context.view_layer.objects.active = body
bpy.ops.object.voxel_remesh()
dt = body.modifiers.new('dt', 'DATA_TRANSFER')
dt.object = src
dt.use_loop_data = True
dt.data_types_loops = {'COLOR_CORNER'}
dt.loop_mapping = 'NEAREST_POLY'
bpy.ops.object.modifier_apply(modifier=dt.name)
bpy.data.objects.remove(src, do_unlink=True)

# re-cut the robe's folds the remesh softened: deep at the hem, gone by the
# waist (blender axes: game height is z, game front is -y)
me = body.data
for v in me.vertices:
    gy = v.co.z
    if gy < 1.0:
        th = math.atan2(-v.co.y, v.co.x)
        fall = (1.0 - gy / 1.0) ** 1.2
        d = (0.018 * math.sin(9 * th + .4) + 0.006 * math.sin(19 * th + 1.3)) * fall
        v.co.x += math.cos(th) * d
        v.co.y += -math.sin(th) * d
me.update()
tex = bpy.data.textures.new('or-clay', type='CLOUDS')
tex.noise_scale = 0.10
tex.noise_depth = 2
disp = body.modifiers.new('clay', 'DISPLACE')
disp.texture = tex
disp.texture_coords = 'GLOBAL'
disp.direction = 'NORMAL'
disp.strength = 0.004
disp.mid_level = 0.5
bpy.ops.object.modifier_apply(modifier=disp.name)
pol = body.modifiers.new('polish', 'SMOOTH')
pol.factor = 0.35
pol.iterations = 2
bpy.ops.object.modifier_apply(modifier=pol.name)

# ---- kit-built on top: the hat, the hair's locks, the beard, the staff ----------
p = Asset('orren-props', seed=SEED)
r = p.rng
# The hat: a broad brim that droops all round, lower behind and to his left,
# and a tall crown that bends back and to the side at its tip. The brim is a
# ring of quads, two rings deep, built by hand, with a top and an underside
# a centimetre and a half apart and an edge between: one sheet with both
# windings on the same vertices had its normals cancel in the game.
HX, HY, HZ = 0, 1.76, .15
N = 24
verts, faces, cols = [], [], []
TH = .015
for lay in (0, 1):
    for k, (rad, drop) in enumerate([(.13, 0), (.30, .05), (.47, .17)]):
        for j in range(N):
            th = j / N * math.tau
            x, z = math.cos(th) * rad, math.sin(th) * rad
            sag = drop * (1.0 + .45 * max(0.0, -math.sin(th)) + .25 * max(0.0, math.cos(th)))
            verts.append((HX + x, HY - sag + (.01 if k == 0 else 0) - lay * TH, HZ + z))
R = 3 * N                                         # the underside's offset
for k in range(2):
    for j in range(N):
        jj = (j + 1) % N
        a0, a1, b0, b1 = k * N + j, k * N + jj, (k + 1) * N + j, (k + 1) * N + jj
        faces.append((a0, b0, b1, a1)); cols.append(HAT if k else HAT_L)                 # the top, facing up
        faces.append((R + a0, R + a1, R + b1, R + b0)); cols.append(HAT)                 # the underside
for j in range(N):                                                                        # the edge
    jj = (j + 1) % N
    a0, a1 = 2 * N + j, 2 * N + jj
    faces.append((a0, a1, R + a1, R + a0)); cols.append(HAT)
p.mesh(verts, faces, cols)
p.tube([(HX, HY - .02, HZ), (HX, HY + .14, HZ - .01), (HX - .01, HY + .30, HZ - .04), (HX + .03, HY + .44, HZ - .10),
        (HX + .10, HY + .53, HZ - .19), (HX + .17, HY + .56, HZ - .27)],
       [.15, .13, .10, .07, .04, .012], [HAT_L, HAT, HAT, HAT, HAT], sides=12, folds=3, amps=[0, .04, .06, .05, .03, 0])
p.tube([(HX, HY + .02, HZ), (HX, HY + .07, HZ)], [.152, .148], HAT_L, sides=16, cap0=False, cap1=False)   # the band

# The hair: long locks from under the brim round the back of his head and at
# the sides, each in two lengths: out from the head over the mantle's
# shoulder, then down along the mantle's surface to the middle of his back,
# or over the shoulder at the sides. Two layers overlap into one mass with a
# ragged edge. Each length is a thin tapering blade, pale, every third with
# a lavender shade.
MANTLE_AT = lambda y: (.30 if y > 1.2 else .29, .22 if y > 1.2 else .21)   # its half widths (x, z) about z=.03
for layer, (n, lmin, lmax, wmin, wmax, out) in enumerate([(24, .30, .42, .10, .13, .025), (30, .40, .62, .07, .10, .045)]):
    for k in range(n):
        f = (k + .5 * layer) / n
        th = math.pi * (1.02 + .96 * f)
        c, s = math.cos(th), math.sin(th)
        col = HAIR_D if (k + layer) % 3 == 0 else HAIR
        root = (HX + c * .13, 1.72 - layer * .02, HZ + s * .11)
        mx, mz = MANTLE_AT(1.45)
        bend = (c * (mx + out), 1.47 - layer * .02, .03 + s * (mz + out + .06))
        length = r.uniform(lmin, lmax) * (1.0 - .25 * abs(c))
        mx2, mz2 = MANTLE_AT(1.45 - length)
        tip = (c * (mx2 + out) + r.uniform(-.03, .03), 1.47 - length, .03 + s * (mz2 + out + .03))
        w = r.uniform(wmin, wmax)
        p.leaf(root, bend, w * .9, .014, col, (c, .6, s), segs=4, quill=.8, belly=.7, round_tip=1.4)
        p.leaf(bend, tip, w, .014, col, (c, .05, s), segs=7, quill=.95, belly=.15, round_tip=.5)
# The beard: long, white, past his chest, just showing at his left cheek from behind.
p.tube([(0, 1.58, .24), (0, 1.48, .28), (0, 1.32, .30), (0, 1.18, .29)], [.07, .08, .06, .015], HAIR, sides=8)
for side in (-1, 1):
    p.leaf((side * .07, 1.62, .20), (side * .12, 1.36, .25), .07, .012, HAIR, (side, 0, .3), segs=5, quill=.7)

# The staff: gnarled, bending, its foot on the ground ahead of his right foot,
# up through his right hand to a claw of three prongs round the crystal.
SX, SZ = -.50, .40
pts = []
for k in range(9):
    f = k / 8
    pts.append((SX + .03 * math.sin(f * 7.0) + .05 * f, .0 + 2.12 * f, SZ + .03 * math.cos(f * 5.0) - .04 * f))
p.tube(pts, [.032, .030, .028, .030, .026, .025, .027, .024, .026], [WOOD, WOOD_D] * 4, sides=7)
for k in range(5):                                   # knots
    f = r.uniform(.1, .9)
    q = pts[int(f * 8)]
    p.rock(.07, .06, .07, q[0], q[1], q[2], WOOD_D, jag=.3, sides=5)
top = pts[-1]
cx, cy, cz = top[0] - .01, top[1] + .17, top[2]
for k in range(3):                                   # the claw
    a = k / 3 * math.tau + .3
    p.tube([top, (top[0] + math.cos(a) * .07, top[1] + .10, top[2] + math.sin(a) * .07),
            (cx + math.cos(a) * .045, cy + .07, cz + math.sin(a) * .045), (cx + math.cos(a) * .02, cy + .14, cz + math.sin(a) * .02)],
           [.02, .018, .012, .004], WOOD, sides=5)
p.rock(.09, .26, .09, cx, cy, cz, CRYSTAL, jag=.15, sides=5)
props = p.build()

# ---- decimate the body, bake its occlusion, join -------------------------------
prop_tris = tris_of(props)
ratio = max(0.02, min(1.0, (TARGET_TRIS - prop_tris) / tris_of(body)))
dec = body.modifiers.new('dec', 'DECIMATE')
dec.ratio = ratio
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True)
bpy.context.view_layer.objects.active = body
bpy.ops.object.modifier_apply(modifier=dec.name)
print('HYBRID body tris=%d props tris=%d' % (tris_of(body), prop_tris))

scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 48
scene.cycles.seed = SEED
scene.render.bake.target = 'VERTEX_COLORS'
scene.render.bake.use_selected_to_active = False
me = body.data
ao = me.color_attributes.new('AO', 'FLOAT_COLOR', 'CORNER')
for d in ao.data:
    d.color = (1.0, 1.0, 1.0, 1.0)
me.color_attributes.active_color = ao
bpy.ops.object.bake(type='AO')
base = me.color_attributes.get('Col')
for i, d in enumerate(base.data):
    k = ao.data[i].color[0] ** 0.8
    d.color = (d.color[0] * k, d.color[1] * k, d.color[2] * k, d.color[3])
me.color_attributes.remove(ao)
me.color_attributes.active_color = base

bpy.ops.object.select_all(action='DESELECT')
body.select_set(True)
props.select_set(True)
bpy.context.view_layer.objects.active = body
bpy.ops.object.join()
obj = bpy.context.view_layer.objects.active
obj.name = 'orren'
obj.data.name = 'orren'

# ---- preview and export, as _kit.finish does ------------------------------------
scene.cycles.samples = 24
mat = bpy.data.materials.new('preview')
mat.use_nodes = True
nt = mat.node_tree
bsdf = nt.nodes.get('Principled BSDF')
attr = nt.nodes.new('ShaderNodeVertexColor')
attr.layer_name = 'Col'
nt.links.new(attr.outputs['Color'], bsdf.inputs['Base Color'])
bsdf.inputs['Roughness'].default_value = .9
obj.data.materials.append(mat)
world = bpy.data.worlds.new('w')
scene.world = world
world.use_nodes = True
world.node_tree.nodes['Background'].inputs['Color'].default_value = (0.06, 0.05, 0.12, 1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value = 2.0
s = bpy.data.objects.new('sun', bpy.data.lights.new('sun', type='SUN'))
s.data.energy = 3.0
s.rotation_euler = tuple(math.radians(a) for a in (40, 0, 160))
bpy.context.collection.objects.link(s)
cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam'))
cam.data.lens = 35
bpy.context.collection.objects.link(cam)
scene.camera = cam
scene.render.resolution_x, scene.render.resolution_y = 540, 960
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
previews = []
for suffix, at, look in (('', (-.7, 1.9, -2.2), (-.15, 1.25, .2)), ('-front', (.9, 1.6, 2.6), (0, 1.2, 0)),
                         ('-side', (2.8, 1.5, .2), (0, 1.2, .1))):
    cam.location = g2b(at)
    cam.rotation_euler = (g2b(look) - g2b(at)).to_track_quat('-Z', 'Y').to_euler()
    path = os.path.join(HERE, '_preview-orren' + suffix + '.png')
    scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    previews.append(path)
obj.data.materials.clear()
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
out = os.path.join(ROOT, 'assets', 'orren.glb')
kw = dict(filepath=out, export_format='GLB', use_selection=True, export_apply=True,
          export_materials='NONE', export_normals=False)
try:
    bpy.ops.export_scene.gltf(**kw, export_vertex_color='ACTIVE')
except TypeError:
    bpy.ops.export_scene.gltf(**kw, export_colors=True)
print('ASSET_OK name=orren triangles=%d bytes=%d out=%s previews=%s' % (
    tris_of(obj), os.path.getsize(out), out, ','.join(previews)))
