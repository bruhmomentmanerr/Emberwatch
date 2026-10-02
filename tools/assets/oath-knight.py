# The Rain Oath's kneeling knight (r143 rebuild). The r140 figure was right in
# pose (one knee down, hands on a planted sword, head bowed) but built of
# boxes, and at the centre of the oath ring it read as a block with a pole.
# This one is lofted with the kit: a surcoat falling over the thighs, plate at
# the shoulders and arms, a great helm bowed over the pommel, a cloak spread
# on the ground behind, and the blade's fuller glowing cobalt (vertex-alpha
# glow mask, see placeLandmark).
#
# Origin: the ground under the figure, between the down knee and the planted
# foot; +Z is the way the knight faces. Drawn at 1.8 m and scaled by SCALE.
#
#   python tools/assets/oath-knight.py
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset
from mathutils import Vector

SCALE = 1.15
PLATE = (.52, .54, .60)
PLATE_DARK = (.34, .35, .40)
SURCOAT = (.20, .28, .58)
SURCOAT_DARK = (.14, .19, .40)
CLOAK = (.13, .14, .21)
LEATHER = (.20, .15, .12)
BLADE = (.60, .63, .70)
FULLER = (.42, .55, 1.0, .25)
GOLD = (.62, .52, .30)

a = Asset('oath-knight', seed=12)

# Legs: the right knee on the ground with the shin back along it, the left
# foot planted ahead with its knee up.
HIP_L, HIP_R = Vector((-.11, .60, .02)), Vector((.11, .58, -.02))
KNEE_L, FOOT_L = Vector((-.13, .54, .42)), Vector((-.13, .04, .47))
KNEE_R, FOOT_R = Vector((.13, .09, -.06)), Vector((.13, .07, -.48))
a.tube([tuple(HIP_L), tuple(KNEE_L)], [.085, .07], PLATE_DARK, sides=9, ref=(1, 0, 0))
a.tube([tuple(KNEE_L), tuple(FOOT_L + Vector((0, .06, 0)))], [.062, .052], PLATE, sides=9, ref=(1, 0, 0))
a.cyl(.07, .075, .09, KNEE_L.x, KNEE_L.y, KNEE_L.z + .03, PLATE, sides=8, rx=math.pi / 2)          # poleyn
a.box(.11, .08, .26, FOOT_L.x, .04, FOOT_L.z + .06, PLATE_DARK)                                      # sabaton
a.tube([tuple(HIP_R), tuple(KNEE_R)], [.085, .07], PLATE_DARK, sides=9, ref=(0, 0, 1))
a.tube([tuple(KNEE_R), tuple(FOOT_R)], [.06, .05], PLATE, sides=9, ref=(0, 1, 0))
a.cyl(.075, .07, .1, KNEE_R.x, KNEE_R.y + .02, KNEE_R.z + .04, PLATE, sides=8, rx=math.pi / 2)
a.box(.1, .16, .1, FOOT_R.x, .09, FOOT_R.z - .02, PLATE_DARK, rx=.5)                                  # toes tucked under

# Body: hips to shoulders, leaning a little over the sword.
body = [(0, .56, 0, .19, .14), (0, .70, .01, .18, .13), (0, .86, .03, .20, .14), (0, 1.00, .045, .215, .135),
        (0, 1.10, .05, .20, .12), (0, 1.15, .05, .10, .08)]
a.tube([(x, y, z) for (x, y, z, _, _) in body], [(w, d) for (*_, w, d) in body], PLATE, sides=14)
# The surcoat over it, falling in pleats over the thighs, open at the sides.
coat = [(0, 1.05, .05, .225, .145, 0), (0, .80, .03, .215, .15, .02), (0, .62, .04, .23, .17, .05),
        (0, .45, .12, .24, .22, .09), (0, .30, .16, .24, .25, .12)]
a.tube([(x, y, z) for (x, y, z, *_ ) in coat], [(w, d) for (_, _, _, w, d, _) in coat], [SURCOAT, SURCOAT, SURCOAT_DARK, SURCOAT_DARK],
       sides=18, folds=9, amps=[p for (*_, p) in coat], cap0=False, cap1=True, cap_color=SURCOAT_DARK)
a.tube([(0, .60, .02), (0, .66, .02)], [(.205, .15), (.2, .148)], LEATHER, sides=14)                   # belt
a.box(.06, .07, .03, 0, .63, .17, GOLD)                                                                # buckle

# Shoulders, arms and gauntlets on the grip.
for side in (-1, 1):
    sh = Vector((side * .21, 1.08, .03))
    el = Vector((side * .25, .86, .20))
    wr = Vector((side * .06, .92 - (side < 0) * .07, .48))
    a.tube([tuple(sh + Vector((side * -.04, .04, 0))), tuple(sh + Vector((side * .05, -.02, 0))), tuple(sh + Vector((side * .03, -.10, .02)))],
           [(.10, .10), (.12, .11), (.09, .09)], PLATE, sides=10, ref=(0, 0, 1))                     # pauldron
    a.tube([tuple(sh), tuple(el)], [.055, .05], PLATE_DARK, sides=8)
    a.tube([tuple(el), tuple(wr)], [.048, .045], PLATE, sides=8)
    a.cyl(.058, .058, .07, el.x, el.y, el.z, PLATE, sides=8)                                          # couter
    a.box(.085, .08, .11, wr.x * .4, wr.y + .01, wr.z + .06, PLATE_DARK, rx=.3)                       # gauntlet

# Head: a great helm bowed over the pommel, a slit across it, a crest ridge.
bow = math.radians(28)
hax = Vector((0, math.cos(bow), math.sin(bow)))
hc = Vector((0, 1.27, .10))
helm = [(-.12, .085), (-.06, .105), (.02, .108), (.09, .1), (.12, .07)]
a.tube([(0, 1.14, .06), (0, 1.19, .08)], [.06, .06], PLATE_DARK, sides=8)
a.tube([tuple(hc + hax * t) for (t, _) in helm], [(r, r * 1.02) for (_, r) in helm], PLATE, sides=12, ref=(1, 0, 0))
slit = hc + hax * .03 + Vector((0, -math.sin(bow), math.cos(bow))) * .105
a.box(.13, .012, .02, slit.x, slit.y, slit.z - .004, (.05, .05, .07), rx=-bow)
a.span(tuple(hc + hax * .05 + Vector((0, 0, -.1))), tuple(hc + hax * .125), .02, .1, PLATE_DARK, up=(1, 0, 0))

# The cloak: a closed drape round the body whose front half stays inside the
# torso and surcoat, so what shows is its back and sides falling from the
# shoulders and pooling on the ground behind the knee.
cl = [(0, 1.10, -.02, .24, .14, .0), (0, .86, -.10, .28, .19, .05), (0, .52, -.21, .34, .25, .09),
      (0, .22, -.34, .40, .29, .12), (0, .03, -.50, .46, .31, .12)]
a.tube([(x, y, z) for (x, y, z, *_ ) in cl], [(w, d) for (_, _, _, w, d, _) in cl], CLOAK, sides=16, ref=(0, 0, 1),
       folds=7, amps=[p for (*_, p) in cl], cap0=True, cap1=True)

# The sword, point down ahead of the knee, fuller glowing.
tip, guard, top = Vector((0, 0, .63)), Vector((0, .72, .585)), Vector((0, .93, .575))
d = (guard - tip).normalized()
a.tube([tuple(tip - d * .03), tuple(tip + (guard - tip) * .4), tuple(guard)], [(.006, .004), (.03, .008), (.034, .009)], BLADE, sides=4, ref=(0, 0, 1))
for face in (-1, 1):
    n = Vector((0, .06, 1)).normalized() * face
    a.span(tuple(tip + (guard - tip) * .22 + n * .0092), tuple(tip + (guard - tip) * .95 + n * .0095), .011, .003, FULLER, up=tuple(n))
a.span((-.17, guard.y - .01, guard.z), (.17, guard.y - .01, guard.z), .03, .035, GOLD)
a.tube([tuple(guard + d * .02), tuple(top)], [.018, .017], LEATHER, sides=8)
a.cyl(.036, .036, .03, 0, top.y + .02, top.z, GOLD, sides=10, rx=math.pi / 2)

for i in range(len(a.verts)):
    a.verts[i] = a.verts[i] * SCALE

a.finish(cam_at=(1.6, 1.3, 2.6), cam_look=(0, .75, 0), res=(700, 800), lens=40, sun=(55, 0, 150),
         extra_views=[('side', (2.8, 1.0, .2), (0, .7, 0)), ('back', (-1.4, 1.5, -2.6), (0, .7, 0))])
