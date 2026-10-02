# Cinder Market stalls (r144): the night market's booths, three trades on one
# frame so a row of them reads as a market and not as one booth repeated.
#
#   market-stall-cloth    a draper: bolts of cloth on the counter, lengths
#                         hanging at the back, a madder-and-cream awning
#   market-stall-produce  a grocer: baskets of apples, cabbages and gourds,
#                         crates below, an indigo-and-cream awning
#   market-stall-pots     a potter: jars, jugs and bowls, an ochre-and-green
#                         awning
#
# Each is a timber booth 3.6 m wide and 2.3 m deep: four posts (the back pair
# taller), a striped awning sloping down over the counter and past it, a
# scalloped valance, half-height side cloths, a counter at the front with the
# stock on it, a back rack, crates at its feet, and a lantern hanging under
# the awning's front edge (vertex-alpha glow mask, warm in the game).
#
# Local frame (game axes): the customer side is +Z, the width runs along X,
# y=0 is the ground. Everything stands inside x -2.35..2.35, z -1.55..1.65
# (the awning overhangs the front by .55; crates and jars stand at the sides),
# which is the footprint the game checks.
#
#   python tools/assets/market-stall.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

TIMBER = (.30, .22, .15)
TIMBER2 = (.24, .17, .12)
WICKER = (.46, .34, .18)
IRON = (.16, .16, .18)
LANTERN = (.16, .15, .14)
GLOW = (1.0, .80, .48, .1)

W, D = 3.6, 2.3
FRONT_Z, BACK_Z = D / 2 - .1, -D / 2 + .1
FRONT_H, BACK_H = 2.35, 2.85
OVER = .55                                  # the awning's reach past the front posts
COUNTER_H, COUNTER_D = .95, .55


def booth(a, stripe_a, stripe_b, side_cloth):
    # Posts.
    for sx in (-1, 1):
        a.box(.13, FRONT_H, .13, sx * (W / 2 - .1), FRONT_H / 2, FRONT_Z, TIMBER)
        a.box(.13, BACK_H, .13, sx * (W / 2 - .1), BACK_H / 2, BACK_Z, TIMBER)
        # the side rail the side cloth hangs from, and a brace
        a.span((sx * (W / 2 - .1), BACK_H - .15, BACK_Z), (sx * (W / 2 - .1), FRONT_H - .15, FRONT_Z), .09, .09, TIMBER2)
        a.span((sx * (W / 2 - .1), 1.2, BACK_Z), (sx * (W / 2 - .1), FRONT_H - .5, FRONT_Z), .07, .07, TIMBER2)
    # The front and back beams.
    # (kept a hand's breadth under the awning, which slopes across them)
    a.box(W, .14, .14, 0, FRONT_H - .13, FRONT_Z, TIMBER)
    a.box(W, .14, .14, 0, BACK_H - .1, BACK_Z, TIMBER)
    # The striped awning: eight strips from the back beam down past the front.
    y0, z0 = BACK_H + .02, BACK_Z - .12
    y1 = FRONT_H - .02 - (BACK_H - FRONT_H) * OVER / (FRONT_Z - BACK_Z)
    z1 = FRONT_Z + OVER
    n = 8
    for k in range(n):
        x = -W / 2 - .12 + (k + .5) * (W + .24) / n
        a.span((x, y0, z0), (x, y1, z1), (W + .24) / n + .004, .04, stripe_a if k % 2 == 0 else stripe_b, up=(0, 1, 0))
    # The valance: a row of scallops hanging from the awning's front edge.
    for k in range(9):
        x = -W / 2 - .12 + (k + .5) * (W + .24) / 9
        half = (W + .24) / 18 - .01
        a.extrude([(-half, 0), (-half * .6, -.2), (0, -.27), (half * .6, -.2), (half, 0)], .03,
                  stripe_b if k % 2 == 0 else stripe_a, at=(x, y1 - .02, z1 + .01))
    # Half-height side cloths under the side rails.
    for sx in (-1, 1):
        x = sx * (W / 2 - .06)
        a.extrude([(BACK_Z, BACK_H - 1.35), (FRONT_Z, FRONT_H - .85), (FRONT_Z, FRONT_H - .2), (BACK_Z, BACK_H - .2)], .03,
                  side_cloth, at=(x, 0, 0), ry=-math.pi / 2)
    # The counter: a plank top on a boarded front, a kick board.
    cz = FRONT_Z - COUNTER_D / 2
    a.box(W - .3, .07, COUNTER_D + .08, 0, COUNTER_H, cz, TIMBER)
    a.box(W - .36, COUNTER_H - .1, .05, 0, (COUNTER_H - .1) / 2 + .02, FRONT_Z - .03, TIMBER2)
    for sx in (-1, 0, 1):
        a.box(.08, COUNTER_H - .1, .08, sx * (W / 2 - .3), (COUNTER_H - .1) / 2, FRONT_Z - .06, TIMBER)
    # The back rack: two shelves between the back posts.
    for y in (.75, 1.45):
        a.box(W - .3, .05, .38, 0, y, BACK_Z + .22, TIMBER2)
    # The lantern on a bracket off the right front post, above head height
    # and clear of anyone at the counter.
    lx, lz = W / 2 - .1, FRONT_Z + .32
    a.box(.05, .05, .36, lx, FRONT_H - .3, FRONT_Z + .16, IRON)
    a.box(.02, .12, .02, lx, FRONT_H - .38, lz, IRON)
    a.cyl(.12, .0, .11, lx, FRONT_H - .5, lz, LANTERN, sides=4, ry=math.pi / 4)
    a.box(.16, .21, .16, lx, FRONT_H - .66, lz, GLOW)
    a.box(.18, .03, .18, lx, FRONT_H - .78, lz, LANTERN)


def crate(a, x, z, s=1.0, ry=0.0, color=TIMBER2):
    a.box(.55 * s, .42 * s, .42 * s, x, .21 * s, z, color, ry=ry)
    a.box(.57 * s, .05 * s, .44 * s, x, .40 * s, z, TIMBER, ry=ry)


# ---- the draper ---------------------------------------------------------------
c = Asset('market-stall-cloth', seed=1440)
r = c.rng
booth(c, (.55, .16, .14), (.72, .64, .50), (.44, .14, .13))
BOLTS = [(.52, .18, .20), (.20, .30, .52), (.62, .52, .30), (.30, .44, .30), (.48, .30, .52), (.70, .66, .58)]
cz = FRONT_Z - COUNTER_D / 2
for k in range(6):                               # bolts lying on the counter, two rows
    x = -1.3 + (k % 3) * .6 + (k // 3) * .3
    c.cyl(.12, .12, .62, x, COUNTER_H + .15 + (k // 3) * .2, cz + (k // 3) * .06 - .05, BOLTS[k], sides=8, rx=math.pi / 2, ry=r.uniform(-.1, .1))
for k in range(3):                               # folded lengths stacked at the other end
    c.box(.55, .08, .38, .95, COUNTER_H + .08 + k * .085, cz, BOLTS[(k + 2) % 6], ry=r.uniform(-.08, .08))
for k in range(5):                               # lengths hanging from the back beam
    x = -1.4 + k * .7
    col = BOLTS[(k * 2) % 6]
    c.box(.5, 1.25, .02, x, BACK_H - .8, BACK_Z + .05, col)
for k in range(4):                               # bolts upright on the rack
    c.cyl(.1, .1, .5, -1.2 + k * .35, 1.45 + .27, BACK_Z + .22, BOLTS[(k + 3) % 6], sides=8)
crate(c, -2.05, .75, .9, .2)
crate(c, 1.45, BACK_Z - .3, 1.0, -.1)
c.finish(cam_at=(3.4, 2.2, 4.6), cam_look=(0, 1.3, 0), res=(700, 560), lens=32, sun=(55, 0, 150))

# ---- the grocer ---------------------------------------------------------------
p = Asset('market-stall-produce', seed=1441)
r = p.rng
booth(p, (.16, .20, .42), (.72, .64, .50), (.14, .17, .34))
FRUIT = [(.58, .12, .10), (.34, .50, .18), (.70, .42, .10), (.50, .40, .16)]
for k in range(4):                               # four baskets heaped with one crop each
    x = -1.25 + k * .83
    p.cyl(.28, .24, .22, x, COUNTER_H + .12, cz, WICKER, sides=10)
    for j in range(6):
        ang = j / 5 * math.tau + r.uniform(0, .5)
        rr = .13 if j else 0
        s = .11 if k != 2 else .14
        p.rock(s * 1.7, s * 1.4, s * 1.7, x + math.cos(ang) * rr, COUNTER_H + .27 + (0 if j else .05), cz + math.sin(ang) * rr, FRUIT[k], jag=.08, sides=5)
for k in range(3):                               # crates of the same under the rack
    x = -1.1 + k * 1.1
    p.box(.62, .34, .34, x, 1.45 + .17 + .02, BACK_Z + .22, WICKER)
    for j in range(3):
        p.rock(.17, .14, .17, x - .18 + j * .18, 1.45 + .38, BACK_Z + .22, FRUIT[(k + j) % 4], jag=.08, sides=5)
for (x, z, s, ry) in [(-2.05, .8, 1.0, .15), (2.05, .75, 1.0, .05), (-1.4, BACK_Z - .3, .85, -.2)]:
    crate(p, x, z, s, ry)
    for j in range(3):
        p.rock(.16, .13, .16, x - .15 + j * .15, .44 * s, z, FRUIT[j % 4], jag=.08, sides=5)
p.finish(cam_at=(3.4, 2.2, 4.6), cam_look=(0, 1.3, 0), res=(700, 560), lens=32, sun=(55, 0, 150))

# ---- the potter -----------------------------------------------------------------
t = Asset('market-stall-pots', seed=1442)
r = t.rng
booth(t, (.62, .44, .12), (.18, .30, .18), (.50, .34, .10))
CLAY = [(.56, .30, .20), (.46, .26, .18), (.62, .52, .40), (.30, .34, .40)]
for k in range(7):                               # jars and jugs along the counter
    x = -1.45 + k * .48
    h = r.uniform(.28, .5)
    col = CLAY[k % 4]
    t.cyl(.12, .17, h * .55, x, COUNTER_H + .04 + h * .275, cz + r.uniform(-.08, .08), col, sides=8)
    t.cyl(.17, .08, h * .45, x, COUNTER_H + .04 + h * .55 + h * .225, cz, col, sides=8)
    t.cyl(.07, .09, .06, x, COUNTER_H + .04 + h + .03, cz, col, sides=8)
for k in range(6):                               # bowls stacked on the rack
    x = -1.3 + k * .52
    for j in range(3):
        t.cyl(.12 + j * .005, .19, .08, x, .75 + .05 + j * .07, BACK_Z + .22, CLAY[(k + 2) % 4], sides=8)
for k in range(5):                               # big jars on the upper shelf
    x = -1.2 + k * .6
    t.cyl(.14, .19, .32, x, 1.45 + .19, BACK_Z + .22, CLAY[(k + 1) % 4], sides=8)
    t.cyl(.19, .09, .2, x, 1.45 + .45, BACK_Z + .22, CLAY[(k + 1) % 4], sides=8)
for (x, z, s) in [(-2.0, .8, 1.0), (2.0, .75, .9)]:
    t.cyl(.2 * s, .28 * s, .45 * s, x, .225 * s, z, CLAY[0], sides=10)     # a big storage jar at each corner
    t.cyl(.28 * s, .14 * s, .25 * s, x, .45 * s + .125 * s, z, CLAY[0], sides=10)
crate(t, 1.45, BACK_Z - .3, 1.0, .1)
t.finish(cam_at=(3.4, 2.2, 4.6), cam_look=(0, 1.3, 0), res=(700, 560), lens=32, sun=(55, 0, 150))
