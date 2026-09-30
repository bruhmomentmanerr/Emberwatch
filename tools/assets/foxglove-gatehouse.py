# The Foxglove gate tower (r143): a small square bridge-tower at the far end of
# the Foxglove bridge, the "castle" of the moonlit river frame. The road
# passes through it under a pointed arch; a corner turret with a cone roof
# gives it a silhouette against the sky; two windows are lit.
#
# Local frame (game axes): the passage runs along Z through the tower; width
# along X; y=0 is the ground. Front (+Z) faces the bridge.
#
#   python tools/assets/foxglove-gatehouse.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset, pointed_arch_curve

STONE = (0.64, 0.62, 0.60)
STONE2 = (0.55, 0.53, 0.52)
DARK = (0.16, 0.15, 0.17)
SLATE = (0.30, 0.33, 0.44)
TIMBER = (0.30, 0.22, 0.15)
LIT = (1.0, .80, .48, .12)             # alpha < 1 glows amber in the game

a = Asset('foxglove-gatehouse', seed=91)
W, D, H, T = 6.4, 5.6, 10.5, .9        # footprint, height to the wall walk, wall thickness
GATE_HW, SPRING, RISE = 1.3, 2.6, 1.1

# Piers either side of the passage, front and back walls above its arches.
for zf in (-1, 1):
    z = zf * (D / 2 - T / 2)
    for side in (-1, 1):
        pw = W / 2 - GATE_HW
        a.box(pw, H, T, side * (GATE_HW + pw / 2), H / 2, z, STONE if side > 0 else STONE2)
    a.arch_wall(GATE_HW, SPRING, RISE, H, T, STONE, at=(0, 0, z), side_color=STONE2)
    # a dressed-stone ring round the arch, proud of the face
    pts = pointed_arch_curve(GATE_HW + .12, SPRING, RISE + .1, 4)
    for i in range(len(pts) - 1):
        p0, p1 = pts[i], pts[i + 1]
        a.span((p0[0], p0[1], z + zf * (T / 2 + .04)), (p1[0], p1[1], z + zf * (T / 2 + .04)), .3, .1, (0.72, 0.70, 0.67), up=(0, 0, 1))
# Side walls.
for side in (-1, 1):
    a.box(T, H, D - 2 * T, side * (W / 2 - T / 2), H / 2, 0, STONE)
# The passage's vault and a floor slab for the road through it.
a.box(2 * GATE_HW + .02, .5, D - 2 * T + .02, 0, SPRING + RISE + .25, 0, STONE2)
a.box(2 * GATE_HW, .12, D + .4, 0, .06, 0, STONE2)
# A plinth course round the foot and a string course under the parapet.
for (y, h, grow) in [(.3, .6, .18), (H - .15, .3, .12)]:
    for zf in (-1, 1):
        for side in (-1, 1):
            pw = W / 2 - GATE_HW
            a.box(pw + grow, h, T + grow, side * (GATE_HW + pw / 2), y, zf * (D / 2 - T / 2), STONE2)
    for side in (-1, 1):
        a.box(T + grow, h, D - 2 * T, side * (W / 2 - T / 2), y, 0, STONE2)
# Crenellated parapet round the roof: a low wall and merlons.
for zf in (-1, 1):
    a.box(W + .3, .6, .5, 0, H + .3, zf * (D / 2 - .1), STONE)
    for k in range(5):
        a.box(.7, .75, .5, -W / 2 + .45 + k * (W - .9) / 4, H + .95, zf * (D / 2 - .1), STONE2)
for side in (-1, 1):
    a.box(.5, .6, D, side * (W / 2 - .1), H + .3, 0, STONE)
    for k in range(4):
        a.box(.5, .75, .7, side * (W / 2 - .1), H + .95, -D / 2 + .5 + k * (D - 1.0) / 3, STONE2)
a.box(W - .6, .2, D - .6, 0, H + .1, 0, STONE2)        # the roof deck
# The corner turret, corbelled out from the wall and capped with a cone.
tx, tz = W / 2 - .2, D / 2 - .2
a.cyl(1.05, 1.15, 6.2, tx, H + 1.1, tz, STONE, sides=10)
a.cyl(.55, 1.15, .9, tx, H - 2.45, tz, STONE2, sides=10)             # corbel
a.cyl(1.25, 1.25, .3, tx, H + 4.3, tz, STONE2, sides=10)
a.cyl(1.35, .0, 2.6, tx, H + 5.75, tz, SLATE, sides=10)
a.box(.34, .7, .12, tx + .1, H + 2.6, tz + 1.06, LIT)                # the turret's window
# Windows: a lit one over the gate facing the bridge, one on the side; slits.
a.box(.7, 1.1, .12, 0, 6.6, D / 2 + .02, LIT)
a.box(.9, .14, .2, 0, 6.0, D / 2 + .08, STONE2)                      # its sill
a.box(.12, 1.0, .6, -W / 2 - .02, 5.8, -.8, LIT)
for (x, y, z) in [(-1.9, 4.8, D / 2 + .02), (1.9, 7.8, -D / 2 - .02), (W / 2 + .02, 3.6, 1.2), (-1.9, 8.2, D / 2 + .02)]:
    if abs(x) > W / 2:
        a.box(.12, .9, .22, x, y, z, DARK)
    else:
        a.box(.22, .9, .12, x, y, z, DARK)
# A raised portcullis showing in the arch's head, and a timber door leaf
# folded back against the passage wall.
for k in range(5):
    a.box(.08, 1.0, .08, -GATE_HW + .3 + k * (2 * GATE_HW - .6) / 4, SPRING + .55, D / 2 - T - .1, DARK)
a.box(2 * GATE_HW - .3, .08, .08, 0, SPRING + .2, D / 2 - T - .1, DARK)
a.box(.12, 2.4, 1.2, -GATE_HW + .08, 1.25, -.4, TIMBER)

a.finish(cam_at=(9.0, 4.0, 14.0), cam_look=(0, 5.0, 0), res=(800, 900), lens=32,
         extra_views=[('back', (-8.0, 3.0, -12.0), (0, 5.0, 0))])
