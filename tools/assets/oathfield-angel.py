# The Oathfield's witness (r143): a winged figure in pale stone on a plinth,
# head bowed, both hands folded on the grip of a greatsword planted point-down
# in front of her, wings half-raised in a V behind. She stands at the head of
# the sword rows with the moon behind her, so her silhouette is the thing the
# field is composed around: from the lychgate the moon sits between the wings.
#
#   python tools/assets/oathfield-angel.py      (pip bpy, or blender --background --python)
#
# Writes assets/oathfield-angel.glb and tools/assets/_preview-oathfield-angel*.png.
# Origin: the centre of the plinth's foot on the ground; +Z is the way she
# faces. The figure is drawn at human scale (1.8 m) and enlarged by FIG_SCALE
# onto the plinth top, so the proportions stay readable in the numbers below.
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset
from mathutils import Vector

FIG_SCALE = 2.4
PLINTH_TOP = 1.88
MARBLE = (.74, .74, .78)
WING = (.80, .80, .84)
WING_FRONT = (.75, .75, .80)
HAIR = (.60, .60, .65)
SHADE = (.40, .40, .45)
BLADE = (.56, .59, .66)
FULLER = (.42, .52, .95, .30)          # alpha < 1: glows cobalt in the game
BRONZE = (.50, .44, .34)
PLINTH = (.43, .42, .47)
PLINTH_DARK = (.30, .30, .34)
MOSS = (.26, .33, .25)

a = Asset('oathfield-angel', seed=7)

# ---- the figure, at human scale -------------------------------------------
fig_start = len(a.verts)

# Gown: a loft of horizontal rings, hem to neck, pleated below the waist.
# (y, half-width, half-depth, forward offset, pleat depth)
rings = [(0.00, .40, .36, .02, .075), (0.10, .385, .345, .02, .07), (0.35, .32, .285, .015, .065),
         (0.65, .255, .215, .01, .05), (0.92, .20, .155, .0, .03), (1.05, .165, .12, .0, .012),
         (1.18, .175, .125, .01, .0), (1.30, .19, .13, .02, .0), (1.40, .20, .12, .01, .0),
         (1.47, .185, .105, .0, .0), (1.52, .07, .065, .01, .0)]
a.tube([(0, y, dz) for (y, _, _, dz, _) in rings], [(w, d) for (_, w, d, _, _) in rings], MARBLE,
       sides=22, ref=(0, 0, 1), folds=11, amps=[p for (*_, p) in rings], phase=.4)
# A girdle at the waist, and the shoulders' round.
a.tube([(0, 1.02, 0), (0, 1.08, 0)], [(.175, .13), (.172, .128)], SHADE, sides=16)
for side in (-1, 1):
    a.tube([(side * .15, 1.44, 0), (side * .20, 1.445, 0), (side * .235, 1.42, .005)], [.06, .068, .05], MARBLE, sides=10, ref=(0, 1, 0))

# Neck and bowed head: the head's own axis leans 35 degrees forward.
a.tube([(0, 1.49, .0), (0, 1.555, .02), (0, 1.595, .05)], [.052, .05, .048], MARBLE, sides=10)
bow = math.radians(35)
hax = Vector((0, math.cos(bow), math.sin(bow)))
hc = Vector((0, 1.645, .085))
prof = [(-.115, .03), (-.09, .06), (-.05, .077), (0, .086), (.05, .084), (.09, .064), (.118, .025)]
a.tube([tuple(hc + hax * t) for (t, _) in prof], [(r, r * .96) for (_, r) in prof], MARBLE, sides=12, ref=(1, 0, 0))
# Hair: over the crown and down the back to the shoulder blades.
a.tube([(0, 1.745, .06), (0, 1.70, -.035), (0, 1.60, -.085), (0, 1.47, -.105), (0, 1.33, -.10)],
       [(.095, .07), (.105, .075), (.10, .06), (.085, .045), (.05, .025)], HAIR, sides=12, ref=(1, 0, 0))
# Two locks falling forward past the bowed face, over the collarbones.
for side in (-1, 1):
    a.tube([(side * .072, 1.715, .10), (side * .085, 1.62, .105), (side * .09, 1.52, .09), (side * .085, 1.42, .075)],
           [(.03, .025), (.034, .026), (.032, .024), (.018, .014)], HAIR, sides=8, ref=(0, 0, 1))

# Arms: shoulder -> elbow -> wrist, both reaching forward to the grip.
for side in (-1, 1):
    sh, el, wr = (side * .195, 1.43, .0), (side * .22, 1.17, .10), (side * .075, 1.11 - (side < 0) * .07, .27)
    a.tube([sh, el], [.056, .046], MARBLE, sides=9)
    a.tube([el, wr], [.043, .035], MARBLE, sides=9)
    # A bell sleeve hanging from the elbow, darker inside its open end.
    ev, wv = Vector(el), Vector(wr)
    a.tube([tuple(ev + Vector((0, .01, -.01))), tuple(ev + (wv - ev) * .55 + Vector((0, -.035, 0))), tuple(ev + (wv - ev) * .9 + Vector((0, -.07, 0)))],
           [.062, .085, .105], MARBLE, sides=10, cap1=True, cap_color=SHADE)
# Hands folded on the grip, the right over the left.
a.box(.075, .085, .105, .0, 1.115, .305, MARBLE, rx=.25)
a.box(.075, .08, .10, .0, 1.035, .31, MARBLE, rx=.2)

# The greatsword, point down in front of her, leaning a little forward.
grip_top, guard, tip = Vector((0, 1.17, .31)), Vector((0, .955, .315)), Vector((0, .0, .47))
a.cyl(.045, .045, .03, 0, 1.19, .31, BRONZE, sides=10, rx=math.pi / 2)            # wheel pommel
a.tube([tuple(grip_top), tuple(guard)], [.02, .022], PLINTH_DARK, sides=8, ref=(1, 0, 0))
a.span((-.19, .96, .315), (.0, .945, .315), .035, .04, BRONZE)
a.span((.0, .945, .315), (.19, .96, .315), .035, .04, BRONZE)
blade_dir = (tip - guard).normalized()
a.tube([tuple(guard), tuple(guard + (tip - guard) * .5), tuple(tip + Vector((0, .02, 0)))],
       [(.034, .009), (.028, .008), (.006, .004)], BLADE, sides=4, ref=(0, 0, 1))
for face in (-1, 1):   # the fuller, down both faces of the blade
    n = Vector((0, .163, .987)).normalized() * face     # square to the blade, which leans 9.4 degrees
    a.span(tuple(guard + blade_dir * .06 + n * .0095), tuple(guard + blade_dir * .62 + n * .0085), .012, .003, FULLER, up=tuple(n))

# Wings: a leading-edge bone from between the shoulder blades up, out and
# back; flight feathers wide enough to overlap two deep, so the wing reads as
# one surface with a scalloped trailing edge rather than a fan of blades; and
# three rows of coverts shingled over their roots on the front face.
def lerp(p, q, f):
    return p + (q - p) * f

def slerp_dir(d0, d1, f):
    return (d0 * (1 - f) + d1 * f).normalized()

def along_bone(bone, f):
    # A point a fraction f of the way along a polyline, by length.
    segs = [(bone[i], bone[i + 1], (bone[i + 1] - bone[i]).length) for i in range(len(bone) - 1)]
    total, d = sum(L for (_, _, L) in segs), f * sum(L for (_, _, L) in segs)
    for p, q, L in segs:
        if d <= L:
            return lerp(p, q, d / L)
        d -= L
    return bone[-1].copy()

for side in (-1, 1):
    X = lambda v: Vector((side * v[0], v[1], v[2]))
    R0, W1, W2, W3, W4 = [X(p) for p in [(.07, 1.38, -.10), (.21, 1.54, -.18), (.58, 1.95, -.34), (.86, 2.32, -.46), (1.08, 2.62, -.52)]]
    bone = [W1, W2, W3, W4]
    a.tube([tuple(p) for p in [R0] + bone], [.065, .06, .05, .036, .016], WING, sides=8, ref=(0, 0, 1))
    arm = (W4 - W1).normalized()
    down_in = X((.06, -1.0, -.08)).normalized()
    down_out = X((.42, -1.0, -.16)).normalized()
    out_up = X((.72, .20, -.20)).normalized()
    front = arm.cross(down_in)
    if front.z < 0:
        front = -front
    # A thick marginal band along the bone so the wing has a solid top edge.
    a.tube([tuple(along_bone(bone, f)) for f in (0, .2, .4, .6, .8, .95)],
           [(.12, .04), (.13, .04), (.12, .035), (.10, .03), (.07, .025), (.04, .02)], WING, sides=8, ref=tuple(front))
    # Scapulars: the inner wing's root, where it leaves the back.
    for k in range(3):
        root = lerp(R0, W1, .3 + .35 * k)
        a.leaf(tuple(root - front * .03), tuple(root - front * .03 + down_in * (.42 + .08 * k)), .17, .018, WING, tuple(front),
               segs=6, quill=.4, belly=.45, round_tip=.45, face_color=WING_FRONT)
    # Secondaries: ten, hanging from the inner 55% of the bone.
    for k in range(10):
        f = (k + .5) / 10 * .55
        root = along_bone(bone, f) - front * .02
        d = slerp_dir(down_in, down_out, (k / 9) ** 1.3)
        L = .74 - .05 * (k / 9) + (.025 if k % 2 else 0)
        a.leaf(tuple(root), tuple(root + d * L), .165, .016, WING, tuple(front), segs=6, quill=.35, belly=.45, round_tip=.45, face_color=WING_FRONT)
    # Primaries: eight, from the wrist out past the tip, the outer ones longest.
    for k in range(8):
        f = .55 + .45 * k / 7
        root = along_bone(bone, min(f, .97)) - front * (.03 + .01 * k / 7)
        d = slerp_dir(down_out, out_up, (k / 7) ** 1.1)
        L = [.70, .76, .82, .88, .92, .92, .86, .74][k]
        a.leaf(tuple(root), tuple(root + d * L), .14 - .025 * k / 7, .016, WING, tuple(front), segs=6, quill=.3, belly=.42, round_tip=.5, face_color=WING_FRONT)
    # Coverts: greater, median and lesser rows, each shorter and further forward.
    for (count, L, wdt, lift, reach) in [(13, .36, .14, .018, .97), (11, .24, .13, .03, .9), (9, .15, .12, .042, .82)]:
        for k in range(count):
            f = (k + .5) / count * reach
            root = along_bone(bone, f) + front * lift
            g = f / reach
            d = slerp_dir(down_in, down_out, min(1, g / .6)) if g < .6 else slerp_dir(down_out, out_up, (g - .6) / .4 * .8)
            a.leaf(tuple(root), tuple(root + d * L), wdt, .014, WING, tuple(front), segs=4, quill=.4, belly=.45, round_tip=.45, face_color=WING_FRONT)

# Lift the figure onto the plinth at statue scale.
for i in range(fig_start, len(a.verts)):
    a.verts[i] = a.verts[i] * FIG_SCALE + Vector((0, PLINTH_TOP, 0))

# ---- the plinth ----------------------------------------------------------------
# Deeper than it is wide and set forward, so the sword's point stands on it.
a.box(3.0, .28, 3.4, 0, .14, .15, MOSS)
a.box(2.6, .24, 3.0, 0, .40, .15, PLINTH)
a.box(2.05, 1.10, 2.45, 0, 1.07, .15, PLINTH)
a.box(2.40, .16, 2.80, 0, 1.70, .15, PLINTH)
a.box(2.15, .10, 2.55, 0, 1.83, .15, PLINTH)
# The inscription panel and a raised blade in relief on the front of the die.
a.box(1.10, .58, .04, 0, 1.08, .15 + 1.225 + .01, PLINTH_DARK)
a.box(.07, .44, .03, 0, 1.06, .15 + 1.225 + .04, PLINTH)
a.box(.30, .05, .03, 0, 1.20, .15 + 1.225 + .04, PLINTH)

a.finish(cam_at=(3.2, 3.2, 12.0), cam_look=(0, 4.3, 0), res=(900, 1100), lens=40, sun=(55, 0, 150),
         extra_views=[('side', (12.0, 3.5, 2.0), (0, 4.3, 0)), ('back', (-5.0, 4.0, -11.0), (0, 4.6, 0)),
                      ('low', (0.5, 1.6, 11.5), (0, 5.8, 0))])
