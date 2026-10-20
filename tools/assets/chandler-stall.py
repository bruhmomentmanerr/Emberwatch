# Dunna Wex's stall (r174): the chandler of Lowmere sells from a trestle
# counter in the lane under the Watcher's Bluff. Until r174 she leaned over a
# counter that was not there.
#
#   chandler-stall   a trestle counter with an amber cloth hung from its front
#                    edge; on it a candle tree with five lit tapers, two lit
#                    pillar candles, bundles of tapers tied with twine, blocks
#                    of beeswax and a basket of rushlights; beside it a drying
#                    frame of tapers hung in pairs by their wicks, and behind
#                    that the dipping pot on an iron tripod over its embers
#
# Local frame (game axes): the customer side is +Z, y=0 is the ground, and the
# keeper stands at the origin, behind the counter. Everything stands inside
# x -1.0..1.95, z -.85..1.0, the footprint the game places it on (Lowmere's
# lane: a house wall on the keeper's right, open on her left). Flames and
# embers carry the vertex-alpha glow mask, warm in the game.
#
#   python tools/assets/chandler-stall.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

TIMBER = (.30, .22, .15)
TIMBER2 = (.24, .17, .12)
CLOTH = (.58, .36, .14)
CLOTH2 = (.70, .60, .40)
IRON = (.14, .14, .15)
BRASS = (.62, .46, .18)
WICKER = (.46, .34, .18)
TWINE = (.42, .30, .17)
WAX = [(.91, .85, .69), (.85, .66, .31), (.66, .23, .13), (.93, .90, .80)]
FLAME = (1.0, .82, .46, .1)
EMBER = (1.0, .42, .14, .1)

COUNTER_W, COUNTER_D, COUNTER_H = 1.8, .56, .86
CZ = .64                                      # the counter's centre, in front of the keeper


def flame(a, x, y, z, s=1.0):
    a.cyl(.016 * s, .0, .05 * s, x, y + .025 * s, z, FLAME, sides=4)


a = Asset('chandler-stall', seed=1740)
r = a.rng

# The counter: a plank top on two trestles, an amber cloth with a cream band
# hung from its front edge, a stretcher between the trestles.
a.box(COUNTER_W, .06, COUNTER_D, 0, COUNTER_H - .03, CZ, TIMBER)
for sx in (-1, 1):
    x = sx * (COUNTER_W / 2 - .2)
    for sz in (-1, 1):
        a.span((x, COUNTER_H - .06, CZ), (x, 0, CZ + sz * (COUNTER_D / 2 - .04)), .06, .06, TIMBER2)
    a.box(.07, .07, COUNTER_D - .06, x, COUNTER_H - .1, CZ, TIMBER2)
a.box(COUNTER_W - .5, .05, .05, 0, .28, CZ, TIMBER2)
a.box(COUNTER_W + .02, .5, .02, 0, COUNTER_H - .31, CZ + COUNTER_D / 2 + .012, CLOTH)
a.box(COUNTER_W + .03, .07, .025, 0, COUNTER_H - .1, CZ + COUNTER_D / 2 + .014, CLOTH2)
for k in range(7):                            # the cloth's scalloped hem
    x = -COUNTER_W / 2 + (k + .5) * COUNTER_W / 7
    h = COUNTER_W / 14
    a.extrude([(-h, 0), (-h * .55, -.07), (0, -.1), (h * .55, -.07), (h, 0)], .02, CLOTH2 if k % 2 else CLOTH,
              at=(x, COUNTER_H - .56, CZ + COUNTER_D / 2 + .012))

top = COUNTER_H

# The candle tree at the counter's left end: a brass stem, two curved arms a
# side and a crown socket, a lit taper in each.
tx, tz = -.62, CZ - .04
a.cyl(.09, .1, .03, tx, top + .015, tz, BRASS, sides=10)
a.cyl(.016, .016, .34, tx, top + .2, tz, BRASS, sides=6)
cups = [(tx, top + .4, tz)]
for k, (dx, dy) in enumerate([(-.17, .27), (-.09, .32), (.09, .32), (.17, .27)]):
    a.span((tx, top + .18 + dy * .25, tz), (tx + dx, top + dy, tz), .014, .014, BRASS)
    cups.append((tx + dx, top + dy + .01, tz))
for (x, y, z) in cups:
    a.cyl(.026, .02, .03, x, y, z, BRASS, sides=6)
    a.cyl(.011, .012, .2, x, y + .115, z, WAX[0], sides=6)
    flame(a, x, y + .215, z)

# Two lit pillar candles, fat and slumped, on a saucer at the right end.
for (x, z, h, rr) in [(.66, CZ + .08, .2, .05), (.52, CZ + .14, .13, .042)]:
    a.cyl(.075, .075, .015, x, top + .008, z, BRASS, sides=10)
    a.cyl(rr, rr * 1.04, h, x, top + .015 + h / 2, z, WAX[1], sides=10)
    a.cyl(rr * .7, rr * .9, .012, x, top + .015 + h, z, WAX[3], sides=10)
    flame(a, x, top + .02 + h, z, 1.3)

# Bundles of tapers lying on the counter, six to a bundle, tied with twine.
for b, (x, z, ry, col) in enumerate([(-.2, CZ + .13, .12, WAX[0]), (.04, CZ + .02, -.08, WAX[2]), (-.12, CZ - .14, .05, WAX[1])]):
    for k in range(6):
        ox = (k % 3 - 1) * .022
        oy = (k // 3) * .02
        a.cyl(.011, .011, .32, x - ox * math.sin(ry), top + .013 + oy, z + ox * math.cos(ry), col, sides=6, rz=math.pi / 2, ry=ry)
    a.cyl(.042, .042, .025, x, top + .024, z, TWINE, sides=8, rz=math.pi / 2, ry=ry)

# Beeswax in blocks, stacked, and one broken.
for k, (x, z, y) in enumerate([(.3, CZ - .14, 0), (.3, CZ - .14, .075), (.44, CZ - .16, 0)]):
    a.box(.13, .07, .09, x, top + .035 + y, z, WAX[1], ry=r.uniform(-.2, .2))

# A shallow basket of rushlights at the front edge.
a.cyl(.14, .11, .07, .28, top + .035, CZ + .15, WICKER, sides=10)
for k in range(9):
    ang = k / 9 * math.tau
    a.cyl(.006, .006, .2, .28 + math.cos(ang) * .045, top + .1, CZ + .15 + math.sin(ang) * .035, WAX[3], sides=4,
          rx=.22, ry=ang)

# The drying frame at the keeper's left: two uprights on feet, two bars, and
# tapers hung in pairs over the bars by their joined wicks.
FX0, FX1, FZ = 1.25, 1.9, .2
for x in (FX0, FX1):
    a.box(.06, 1.75, .06, x, .875, FZ, TIMBER)
    a.box(.08, .06, .5, x, .03, FZ, TIMBER2)
    a.span((x, .5, FZ), (x, .03, FZ + .22), .04, .04, TIMBER2)
    a.span((x, .5, FZ), (x, .03, FZ - .22), .04, .04, TIMBER2)
for y in (1.72, 1.32):
    a.box(FX1 - FX0 + .1, .04, .04, (FX0 + FX1) / 2, y, FZ, TIMBER2)
    n = 7
    for k in range(n):
        x = FX0 + .07 + k * (FX1 - FX0 - .14) / (n - 1)
        col = WAX[(k + (y > 1.5)) % 3]
        L = r.uniform(.28, .34)
        for sz in (-1, 1):
            a.cyl(.0105, .0125, L, x, y - .03 - L / 2, FZ + sz * .022, col, sides=6)

# The dipping pot behind the frame: an iron tripod over a ring of stones and
# embers, the pot of melted wax on it.
PX, PZ = 1.55, -.48
for k in range(7):
    ang = k / 7 * math.tau
    a.rock(.11, .08, .11, PX + math.cos(ang) * .2, .04, PZ + math.sin(ang) * .2, (.30, .29, .30), jag=.15, sides=5)
for k in range(5):
    ang = k / 5 * math.tau + .3
    a.rock(.07, .03, .07, PX + math.cos(ang) * .07, .02, PZ + math.sin(ang) * .07, EMBER, jag=.2, sides=5)
for k in range(3):
    ang = k / 3 * math.tau
    a.span((PX + math.cos(ang) * .3, 0, PZ + math.sin(ang) * .3), (PX, .62, PZ), .025, .025, IRON)
a.span((PX, .62, PZ), (PX, .5, PZ), .012, .012, IRON)
a.cyl(.15, .12, .17, PX, .4, PZ, IRON, sides=10)
a.cyl(.13, .13, .01, PX, .485, PZ, WAX[1], sides=10)

# A crate of boxed candles under the counter's right end, its lid off.
a.box(.42, .26, .3, .55, .13, CZ - .02, TIMBER2, ry=.06)
for k in range(4):
    a.box(.08, .05, .26, .41 + k * .095, .27, CZ - .02, WAX[3 if k % 2 else 0], ry=.06)

a.finish(cam_at=(1.6, 1.7, 3.2), cam_look=(.4, .85, .3), res=(800, 600), lens=35, sun=(55, 0, 150),
         extra_views=[('front', (0, 1.4, 3.0), (.3, .9, .4)), ('side', (3.2, 1.6, .4), (.6, .8, .2))])
