# Dunna Wex, the chandler of Lowmere — reference NPC role design preview.
#
# A merchant of the lower town: a human woman in an artisan's apron over an
# amber dress, hair in a practical bun, leaning over her stall counter with a
# bundle of tapers in one hand and the other arranging the wares. Gameplay
# flavour: a vendor figure — the kind of role a playable Emberwatch would buy
# from and hear gossip from.
#
# HYBRID BUILD (the sculpted-character pipeline, first used here):
# the figure is no longer assembled from discrete kit primitives. The same
# tapered forms the old script placed (same pose, same palette) are built as
# separate coloured parts, joined, and fused into ONE continuous mesh with a
# voxel remesh — an SDF-style union: shoulders melt into the torso, the neck
# into the jaw, the hair into the head, no primitive seams anywhere. A
# code-driven sculpt pass follows (deterministic, seeded — no hand work, so
# the script alone reproduces the figure): skirt pleats are re-cut radially,
# a procedural clay breakup roughens the surface, a polish pass smooths it
# back the way a sculptor's rake would. The result is decimated to a period
# poly budget and its self-occlusion is baked into the vertex colours with
# Cycles, so the folds and armpits carry their own shading. The stall,
# tapers and wax stains stay kit-built — furniture never needed sculpting.
#
#   ~/workspace/blender/blender-4.5.14-linux-x64/blender --background \
#     --python tools/assets/dunna-wex.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset, g2b
import bpy

SKIN   = (.90, .72, .58)
SKIN_D = (.80, .60, .47)
HAIR   = (.24, .15, .09)
DRESS  = (.56, .37, .19)
DRESS_D= (.43, .27, .13)
APRON  = (.79, .72, .59)
APRON_D= (.64, .57, .45)
WAX    = (.90, .82, .60)
STOCK  = (.62, .52, .40)
SHOE   = (.20, .14, .10)
TIMBER = (.33, .24, .15)
TIMBER_D=(.26, .18, .11)
CREAM  = (.93, .86, .68)
AMBER  = (.86, .64, .32)
MADDER = (.62, .22, .14)

SEED = 20261015
VOXEL = 0.02          # remesh resolution: the union's "clay" grain
TARGET_TRIS = 3000    # whole asset, stall included — period budget

bpy.ops.wm.read_factory_settings(use_empty=True)


def part(name, fn):
    """Build one coloured body part with the kit, as its own object."""
    pa = Asset(name, seed=SEED)
    fn(pa)
    return pa.build()


def tris_of(obj):
    return sum(len(p.vertices) - 2 for p in obj.data.polygons)


# ---- the figure's tapered forms (the old script's pose, verbatim) -----------
def _legs(a):
    for sx in (-1, 1):
        x = sx * .095
        a.box(.11, .09, .24, x, .045, .03, SHOE, taper=1.1)      # shoe
        a.tube([(x, .09, 0), (x, .25, .005), (x, .42, .01)],    # calf, tapering
               [.052, .045, .038], STOCK, sides=8)


def _skirt(a):
    a.tube([(0, .98, 0), (0, .76, .008), (0, .54, .014), (0, .34, .02)],
           [.185, .225, .265, .30], [DRESS, DRESS, DRESS_D],
           sides=10, folds=7, amps=[0, .05, .07, .09])


def _torso(a):
    a.tube([(0, .98, 0), (0, 1.20, .02), (0, 1.40, .05)],
           [.180, .172, .158], DRESS, sides=10)
    # apron: bib panel + waistband — cloth masses, unioned with the dress
    a.box(.34, .82, .028, 0, .90, .205, APRON, rx=-.07, taper=.82)
    a.box(.40, .055, .035, 0, 1.29, .175, APRON_D, rx=-.05)


def _head(a):
    a.cyl(.045, .050, .10, 0, 1.47, .05, SKIN_D, sides=8)         # neck
    a.tube([(0, 1.50, .05), (0, 1.58, .058), (0, 1.66, .052),
            (0, 1.73, .042), (0, 1.775, .035)],
           [.052, .098, .104, .078, .028], SKIN, sides=10)
    # hair: mass over the back of the head + a bun
    a.tube([(0, 1.70, .05), (0, 1.755, .015), (0, 1.71, -.035), (0, 1.63, -.055)],
           [.104, .092, .096, .062], HAIR, sides=8)
    a.tube([(0, 1.695, -.055), (0, 1.69, -.115), (0, 1.685, -.155)],
           [.052, .058, .030], HAIR, sides=8)


def _arms(a):
    # tend-wares: forward over the counter. Right hand holds the taper
    # bundle; left hand stays open, arranging.
    a.tube([(.205, 1.40, .05), (.255, 1.20, .20), (.185, 1.045, .40)],
           [.062, .050, .040], [DRESS, SKIN], sides=8)
    a.tube([(-.205, 1.40, .05), (-.265, 1.22, .17), (-.145, 1.06, .35)],
           [.062, .050, .040], [DRESS, SKIN], sides=8)
    a.tube([(.185, 1.045, .40), (.185, 1.03, .52)], [.036, .022], SKIN, sides=7)
    a.tube([(-.145, 1.06, .35), (-.105, 1.045, .47)], [.036, .022], SKIN, sides=7)


parts = [part('dw-legs', _legs), part('dw-skirt', _skirt),
         part('dw-torso', _torso), part('dw-head', _head),
         part('dw-arms', _arms)]

# ---- join the parts: the colour + shape source -------------------------------
bpy.ops.object.select_all(action='DESELECT')
for o in parts:
    o.select_set(True)
bpy.context.view_layer.objects.active = parts[0]
bpy.ops.object.join()
src = bpy.context.view_layer.objects.active
src.name = 'dw-src'
print('HYBRID src tris=%d' % tris_of(src))

# ---- SDF-style union: voxel remesh the joined forms into one skin ------------
body = src.copy()
body.data = src.data.copy()
body.name = 'dw-body'
bpy.context.collection.objects.link(body)
body.data.remesh_mode = 'VOXEL'
body.data.remesh_voxel_size = VOXEL
body.data.use_remesh_preserve_volume = True
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True)
bpy.context.view_layer.objects.active = body
bpy.ops.object.voxel_remesh()
print('HYBRID remeshed tris=%d' % tris_of(body))

# paint the union from the parts: nearest-face colour transfer
dt = body.modifiers.new('dt', 'DATA_TRANSFER')
dt.object = src
dt.use_loop_data = True
dt.data_types_loops = {'COLOR_CORNER'}
dt.loop_mapping = 'NEAREST_POLY'
bpy.ops.object.modifier_apply(modifier=dt.name)
bpy.data.objects.remove(src, do_unlink=True)

# ---- ZBrush-style pass, in code: pleats, clay breakup, polish -----------------
# Re-cut the skirt pleats the remesh softened: radial displacement, seven
# folds plus a finer harmonic, bellied between hem and waist (game axes:
# blender (x, -z, y), so game height is blender z, game front is -y).
me = body.data
for v in me.vertices:
    gy = v.co.z
    if 0.30 <= gy <= 1.03:
        th = math.atan2(-v.co.y, v.co.x)
        fall = math.sin(math.pi * (gy - 0.30) / 0.73) ** 0.7
        d = (0.011 * math.sin(7 * th + 0.6) + 0.004 * math.sin(14 * th + 1.7)) * fall
        v.co.x += math.cos(th) * d
        v.co.y += -math.sin(th) * d
me.update()

# surface breakup: a whisper of procedural clay noise, so no surface is
# mathematically perfect (Blender's noise is a fixed function — same every run)
tex = bpy.data.textures.new('dw-clay', type='CLOUDS')
tex.noise_scale = 0.12
tex.noise_depth = 2
disp = body.modifiers.new('clay', 'DISPLACE')
disp.texture = tex
disp.texture_coords = 'GLOBAL'
disp.direction = 'NORMAL'
disp.strength = 0.0025
disp.mid_level = 0.5
bpy.ops.object.modifier_apply(modifier=disp.name)

# polish: low-factor smoothing iterations — the sculptor's rake
pol = body.modifiers.new('polish', 'SMOOTH')
pol.factor = 0.35
pol.iterations = 2
bpy.ops.object.modifier_apply(modifier=pol.name)
print('HYBRID sculpted tris=%d' % tris_of(body))

# ---- the stall, the tapers, the stains: kit-built, as before ------------------
p = Asset('dunna-props', seed=SEED)
# wax stains sit proud of the (now slightly moved) apron face
p.box(.10, .15, .008, .07, .72, .232, WAX, rx=-.07)
p.box(.07, .05, .008, -.08, 1.05, .225, WAX, rx=-.07)
# the taper bundle in her right hand
for k, (dx, dz, col, tilt) in enumerate([
        (0, 0, CREAM, .06), (.028, .012, AMBER, -.05),
        (-.028, .010, CREAM, .10), (.012, -.026, MADDER, -.09),
        (-.014, -.024, AMBER, .04)]):
    p.cyl(.011, .013, .34, .185 + dx, 1.20, .52 + dz, col,
          sides=6, rx=tilt, rz=tilt * .7)
# her stall counter
p.box(1.30, .07, .55, 0, .865, .78, TIMBER)                       # counter top
for sx in (-1, 1):
    for sz in (0, 1):
        p.box(.08, .83, .08, sx * .58, .415, .55 + sz * .46, TIMBER_D)
p.box(1.16, .05, .44, 0, .18, .78, TIMBER_D)                      # low shelf
# a rack of finished tapers on the counter
p.box(.34, .05, .12, -.38, .925, .72, TIMBER_D)
for k, col in enumerate([CREAM, AMBER, CREAM, MADDER, AMBER, CREAM]):
    p.cyl(.011, .013, .30, -.50 + k * .048, 1.10, .72, col, sides=6,
          rx=.05 * (1 if k % 2 else -1))
# a crate of tallow blocks under the counter
p.box(.34, .26, .30, .42, .31, .78, TIMBER_D)
p.box(.30, .05, .26, .42, .465, .78, WAX)
props = p.build()
props.name = 'dw-props'
prop_tris = tris_of(props)
print('HYBRID props tris=%d' % prop_tris)

# ---- decimate the sculpted body to the period budget ---------------------------
body_tris = tris_of(body)
ratio = max(0.02, min(1.0, (TARGET_TRIS - prop_tris) / body_tris))
dec = body.modifiers.new('dec', 'DECIMATE')
dec.ratio = ratio
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True)
bpy.context.view_layer.objects.active = body
bpy.ops.object.modifier_apply(modifier=dec.name)
print('HYBRID decimated body tris=%d (ratio %.3f)' % (tris_of(body), ratio))

# ---- bake the sculpt's occlusion into the vertex colours (Cycles) -------------
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 48
scene.cycles.seed = SEED
scene.cycles.bake_type = 'AO'
scene.render.bake.target = 'VERTEX_COLORS'
scene.render.bake.use_selected_to_active = False
scene.render.bake.margin = 2
ao = me.color_attributes.new('AO', 'FLOAT_COLOR', 'CORNER')
for d in ao.data:
    d.color = (1.0, 1.0, 1.0, 1.0)
me.color_attributes.active_color = ao
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True)
bpy.context.view_layer.objects.active = body
bpy.ops.object.bake(type='AO')
base = me.color_attributes.get('Col')
for i, d in enumerate(base.data):
    a = ao.data[i].color[0] ** 0.85
    d.color = (d.color[0] * a, d.color[1] * a, d.color[2] * a, d.color[3])
me.color_attributes.remove(ao)
me.color_attributes.active_color = base
print('HYBRID AO baked: min=%.3f max=%.3f' % (
    min(d.color[0] for d in base.data), max(d.color[0] for d in base.data)))

# ---- join body + stall, then preview + export exactly as _kit.finish does -----
bpy.ops.object.select_all(action='DESELECT')
body.select_set(True)
props.select_set(True)
bpy.context.view_layer.objects.active = body
bpy.ops.object.join()
obj = bpy.context.view_layer.objects.active
obj.name = 'dunna-wex'
obj.data.name = 'dunna-wex'

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
world.node_tree.nodes['Background'].inputs['Color'].default_value = (0.04, 0.045, 0.09, 1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.6
s = bpy.data.objects.new('sun', bpy.data.lights.new('sun', type='SUN'))
s.data.energy = 3.4
s.rotation_euler = tuple(math.radians(a) for a in (35, 0, 35))
bpy.context.collection.objects.link(s)
cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam'))
cam.data.lens = 35
bpy.context.collection.objects.link(cam)
scene.camera = cam
scene.render.resolution_x, scene.render.resolution_y = 700, 900
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
previews = []
for suffix, at, look in (('', (1.5, 1.45, 2.7), (0, 1.0, 0.3)),
                         ('-back', (-1.5, 1.45, -2.7), (0, 1.0, 0.1))):
    cam.location = g2b(at)
    cam.rotation_euler = (g2b(look) - g2b(at)).to_track_quat('-Z', 'Y').to_euler()
    path = os.path.join(HERE, '_preview-dunna-wex' + suffix + '.png')
    scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    previews.append(path)
obj.data.materials.clear()
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
out = os.path.join(ROOT, 'assets', 'dunna-wex.glb')
kw = dict(filepath=out, export_format='GLB', use_selection=True, export_apply=True,
          export_materials='NONE', export_normals=False)
try:
    bpy.ops.export_scene.gltf(**kw, export_vertex_color='ACTIVE')
except TypeError:
    bpy.ops.export_scene.gltf(**kw, export_colors=True)
print('ASSET_OK name=dunna-wex triangles=%d bytes=%d out=%s previews=%s' % (
    tris_of(obj), os.path.getsize(out), out, ','.join(previews)))
