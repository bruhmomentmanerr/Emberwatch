# The four taverns fitted out (r157), after the archives (r154, r155) and the
# guild halls (r156). Each was the same room: a bar slab across the middle,
# two blocks for tables, a stone drum, a hearth, a rug and the storeroom
# filler's chests and barrels round the walls. The Gilded Finch's centrepiece
# was a glowing violet block on a counter by the door.
#
#   cinder-keg       the Cinder and Keg (22 x 17) — "a warm hearth, a small
#                    stage, and tables meant for lingering": the bar with
#                    Barkeep Varn behind it (he stands at the room's 0, -3),
#                    the keg rack and the back-bar shelves, a hearth nook
#                    with two armchairs, a stage with a curtain, a lute and a
#                    drum, round tables, the regulars' long table, barrel
#                    tables, a dartboard, wheel chandeliers
#   southgate-rest   the Southgate Rest (20 x 16) — "a travel-worn hearth and
#                    a quiet place to set down a pack": a big hearth with
#                    boots drying before it between two settles, the pack
#                    rail and its bench, a map of the south road, pallets,
#                    the keeper's desk with the ledger and the keys, stairs
#                    up to the rooms, a long table
#   gilded-finch     the Gilded Finch (20 x 16) — "soft booths, a musician's
#                    nook, and a late-night room": six booths, the
#                    musician's nook on a dais under a gilt arch with a harp
#                    and a viol, the late-night room behind a curtain, a
#                    small polished bar, the finch in its gilt cage, a
#                    chandelier, panelled walls
#   wayhouse         the Wayhouse (22 x 17) — "first roof inside the new
#                    wall, and it knows it": the hearth with the stew pot,
#                    the datestone over it, the serving table with the
#                    baker's bread, two long tables, pallets down the wall,
#                    a rack of cloaks to take, the alms box by the door
#
# Local frame as the other halls: the room's middle at the origin, the door at
# +z, the side walls' inner faces at x = +-(w/2 - .21), the back wall's at
# z = -(d/2 - .21), the floor y = 0, the ceiling's underside y = 6.82. The
# game lays each at its room's middle (placeCinderKeg, placeSouthgateRest,
# placeGildedFinch, placeWayhouse) with colliders from these numbers.
#
#   python tools/assets/taverns.py [cinder|southgate|finch|wayhouse ...]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset, pointed_arch_curve

WOOD = (.30, .19, .11)
WOOD2 = (.22, .14, .08)
WOOD3 = (.38, .25, .14)
DARK = (.13, .08, .05)
IRON = (.12, .12, .14)
BRASS = (.62, .48, .22)
GILT = (.80, .62, .26)
PEWTER = (.46, .47, .50)
SILVER = (.62, .64, .68)
STONE = (.42, .40, .44)
STONE2 = (.32, .30, .33)
SOOT = (.06, .05, .05)
PAGE = (.80, .74, .58)
INK = (.10, .09, .10)
SLATE = (.10, .11, .12)
WAX = (.88, .84, .72)
WOOL = (.30, .28, .34)
WINE = (.40, .09, .11)
WINE2 = (.30, .06, .08)
PLUM = (.30, .11, .27)
OCHRE = (.58, .40, .14)
MOSS = (.20, .27, .17)
LEATHER = (.36, .20, .10)
STRAW = (.62, .52, .28)
BREAD = (.60, .40, .18)
APPLE = (.56, .14, .09)
GLASS = [(.16, .30, .18), (.34, .19, .10), (.18, .20, .34), (.40, .34, .16), (.22, .12, .10)]
FLAME = (1.0, .76, .38, .06)
LAMP = (1.0, .80, .48, .1)
COALS = (1.0, .42, .14, .45)
FIRE = (1.0, .58, .22, .12)
CEIL = 6.82
TAU = math.tau


class Wall:
    # Pieces against one wall: u runs along it, left to right as you face it
    # from the room, v comes out of it into the room. For the back wall u is
    # x; for the left wall u is -z; for the right wall u is z.
    def __init__(self, a, side, S, B):
        self.a, self.side, self.S, self.B = a, side, S, B
        self.ry = {'back': 0.0, 'left': math.pi / 2, 'right': -math.pi / 2}[side]

    def p(self, u, v):
        if self.side == 'back':
            return (u, self.B + v)
        if self.side == 'left':
            return (-self.S + v, -u)
        return (self.S - v, u)

    def box(self, w, h, d, u, y, v, c, ry=0.0, rx=0.0, rz=0.0):
        x, z = self.p(u, v)
        self.a.box(w, h, d, x, y, z, c, rx=rx, ry=self.ry + ry, rz=rz)

    def cyl(self, r0, r1, h, u, y, v, c, sides=8, rx=0.0, rz=0.0, cap=True):
        x, z = self.p(u, v)
        self.a.cyl(r0, r1, h, x, y, z, c, sides=sides, rx=rx, ry=self.ry, rz=rz, cap=cap)

    def span(self, p, q, t, d, c):
        (x0, z0), (x1, z1) = self.p(p[0], p[2]), self.p(q[0], q[2])
        self.a.span((x0, p[1], z0), (x1, q[1], z1), t, d, c)


# -- small things -------------------------------------------------------------
def tankard(a, x, y, z, c=PEWTER):
    a.cyl(.05, .045, .13, x, y + .065, z, c, sides=6)
    a.box(.02, .08, .03, x + .065, y + .07, z, c)


def bottle(a, x, y, z, c, tall=1.0):
    a.cyl(.042, .042, .2 * tall, x, y + .1 * tall, z, c, sides=5)
    a.cyl(.016, .016, .09, x, y + .2 * tall + .045, z, c, sides=4)


def glass(a, x, y, z, c=(.70, .66, .58)):
    a.cyl(.032, .032, .01, x, y + .005, z, c, sides=5)
    a.cyl(.008, .008, .08, x, y + .05, z, c, sides=3)
    a.cyl(.01, .04, .07, x, y + .125, z, c, sides=6)


def candle(a, x, y, z, holder=BRASS, h=.14):
    a.cyl(.05, .06, .03, x, y + .015, z, holder, sides=6)
    a.cyl(.028, .028, h, x, y + .03 + h / 2, z, WAX, sides=5)
    a.cyl(.024, 0, .08, x, y + .03 + h + .04, z, FLAME, sides=4)


def bowl(a, x, y, z, c=WOOD3, r=.12):
    a.cyl(r * .6, r, r * .55, x, y + r * .27, z, c, sides=7)


def loaf(a, x, y, z, ry=0.0, s=1.0):
    a.rock(.26 * s, .13 * s, .16 * s, x, y + .06 * s, z, BREAD, jag=.08, sides=6, ry=ry)


def crate(a, x, z, s, ry=0.0, y=0.0):
    a.box(s, s, s, x, y + s / 2, z, WOOD3, ry=ry)
    a.box(s + .02, .06, s + .02, x, y + s * .8, z, WOOD2, ry=ry)
    a.box(s + .02, .06, s + .02, x, y + s * .2, z, WOOD2, ry=ry)


def sack(a, x, z, ry=0.0, c=(.52, .44, .30)):
    a.rock(.5, .55, .4, x, .27, z, c, jag=.15, sides=6, ry=ry)
    a.cyl(.07, .04, .12, x, .58, z, (.40, .33, .22), sides=5)


def cask(a, x, y, z, r, L, axis='z', tap=0):
    # A cask on its side, its length along x or z; tap = +1/-1 puts a brass
    # tap on that end.
    rr = dict(rx=math.pi / 2) if axis == 'z' else dict(rz=-math.pi / 2)

    def at(t):
        return (x, y, z + t) if axis == 'z' else (x + t, y, z)
    a.cyl(r * .84, r, L / 2, *at(-L / 4), WOOD, sides=10, **rr)
    a.cyl(r, r * .84, L / 2, *at(L / 4), WOOD, sides=10, **rr)
    for t in (-.36, .36):
        a.cyl(r * .92 + .015, r * .92 + .015, .05, *at(t * L), IRON, sides=10, cap=False, **rr)
    for s in (-1, 1):
        a.cyl(r * .78, r * .78, .02, *at(s * L / 2), WOOD3, sides=10, **rr)
    if tap:
        tx, ty, tz = at(tap * (L / 2 + .05))
        a.box(.05, .05, .05, tx, ty - r * .45, tz, BRASS)
        a.box(.03, .1, .03, tx + (.04 * tap if axis == 'x' else 0), ty - r * .45 - .06, tz + (.04 * tap if axis == 'z' else 0), BRASS)


def barrel(a, x, z, r=.36, h=.9, y=0.0):
    a.cyl(r * .86, r, h / 2, x, y + h / 4, z, WOOD, sides=10)
    a.cyl(r, r * .86, h / 2, x, y + 3 * h / 4, z, WOOD, sides=10)
    for t in (.14, .86):
        a.cyl(r * .93 + .015, r * .93 + .015, .05, x, y + t * h, z, IRON, sides=10, cap=False)
    a.cyl(r * .8, r * .8, .02, x, y + h + .005, z, WOOD3, sides=10)


def round_table(a, x, z, r=.6, h=.78, top=WOOD3):
    a.cyl(r, r, .06, x, h, z, top, sides=12)
    a.cyl(.07, .07, h - .06, x, (h - .06) / 2, z, WOOD, sides=6)
    a.box(r * 1.3, .06, .1, x, .03, z, WOOD)
    a.box(.1, .06, r * 1.3, x, .03, z, WOOD)


def stool(a, x, z, y=0.0, h=.62):
    a.cyl(.19, .19, .06, x, y + h, z, WOOD3, sides=8)
    for k in range(3):
        ang = k / 3 * TAU + .4
        a.span((x + math.cos(ang) * .1, y + h - .02, z + math.sin(ang) * .1),
               (x + math.cos(ang) * .2, y, z + math.sin(ang) * .2), .04, .04, WOOD)


def bench(a, x, z, L, along='x', h=.46, c=WOOD):
    w, d = (L, .36) if along == 'x' else (.36, L)
    a.box(w, .08, d, x, h, z, c)
    for s in (-1, 1):
        lx, lz = ((s * (L / 2 - .2), 0) if along == 'x' else (0, s * (L / 2 - .2)))
        a.box(.3 if along == 'z' else .08, h - .04, .08 if along == 'z' else .3, x + lx, (h - .04) / 2, z + lz, c)


def armchair(a, x, z, ry, cushion, frame=WOOD2):
    # Facing its local +z.
    c, s = math.cos(ry), math.sin(ry)

    def P(lx, lz):
        return (x + lx * c + lz * s, z - lx * s + lz * c)
    px, pz = P(0, 0)
    a.box(.74, .14, .66, px, .42, pz, frame, ry=ry)
    a.box(.64, .12, .6, px, .55, pz, cushion, ry=ry)
    for lx in (-.31, .31):
        for lz in (-.27, .27):
            qx, qz = P(lx, lz)
            a.box(.07, .36, .07, qx, .18, qz, frame, ry=ry)
    qx, qz = P(0, -.32)
    a.box(.74, 1.05, .1, qx, .95, qz, frame, ry=ry, rx=-.12)
    qx, qz = P(0, -.26)
    a.box(.6, .72, .07, qx, .98, qz, cushion, ry=ry, rx=-.12)
    for lx in (-.37, .37):
        qx, qz = P(lx, .02)
        a.box(.1, .1, .64, qx, .78, qz, frame, ry=ry)
        qx, qz = P(lx, .28)
        a.box(.07, .26, .07, qx, .63, qz, frame, ry=ry)


def lantern(a, x, y, z, top=CEIL):
    a.box(.025, top - y - .28, .025, x, (top + y + .28) / 2, z, IRON)
    a.cyl(.17, .03, .14, x, y + .23, z, IRON, sides=4)
    a.box(.2, .28, .2, x, y, z, LAMP)
    for sx in (-1, 1):
        for sz in (-1, 1):
            a.box(.025, .32, .025, x + sx * .105, y, z + sz * .105, IRON)
    a.box(.25, .04, .25, x, y - .16, z, IRON)


def wheel(a, x, z, r=.9, y=4.4, c=WOOD2, n=8):
    # A cartwheel chandelier on three chains, candles round its rim.
    m = 16
    pts = [(x + math.cos(k / m * TAU) * r, y, z + math.sin(k / m * TAU) * r) for k in range(m + 1)]
    a.tube(pts, [.05] * (m + 1), c, sides=4, cap0=False, cap1=False)
    a.cyl(.12, .12, .14, x, y, z, c, sides=6)
    for k in range(6):
        ang = k / 6 * TAU
        a.span((x, y, z), (x + math.cos(ang) * r, y, z + math.sin(ang) * r), .04, .04, c)
    for k in range(n):
        ang = (k + .5) / n * TAU
        cx, cz = x + math.cos(ang) * r, z + math.sin(ang) * r
        a.cyl(.035, .035, .16, cx, y + .12, cz, WAX, sides=5)
        a.cyl(.026, 0, .09, cx, y + .245, cz, FLAME, sides=4)
    for k in range(3):
        ang = k / 3 * TAU + .3
        a.span((x + math.cos(ang) * r * .92, y, z + math.sin(ang) * r * .92), (x, y + 1.3, z), .014, .014, IRON)
    a.box(.03, CEIL - y - 1.3, .03, x, (CEIL + y + 1.3) / 2, z, IRON)


def sconce(W, u, y=2.4, glass_chimney=False, metal=IRON):
    W.box(.14, .32, .04, u, y, .02, metal)
    W.span((u, y - .1, 0), (u, y + .05, .26), .03, .03, metal)
    W.cyl(.07, .05, .05, u, y + .07, .28, metal, sides=6)
    W.cyl(.035, .035, .16, u, y + .18, .28, WAX, sides=5)
    W.cyl(.03, 0, .1, u, y + .31, .28, FLAME, sides=4)
    if glass_chimney:
        W.cyl(.07, .06, .26, u, y + .26, .28, LAMP, sides=6, cap=False)


def fireplace(W, u, width=3.0, pot=False):
    a = W.a
    hw = width / 2
    W.box(width + .6, .12, 1.15, u, .06, .575, STONE2)                 # the hearthstone
    for s in (-1, 1):
        W.box(.55, 1.6, .78, u + s * (hw - .02), .8, .39, STONE)        # the jambs
    W.box(width + .3, .42, .82, u, 1.81, .41, STONE)                   # the lintel
    W.box(width + .7, .1, .52, u, 2.07, .5, WOOD2)                     # the mantel shelf
    W.box(width - .2, CEIL - 2.12, .64, u, (CEIL + 2.12) / 2, .32, STONE)   # the breast, up to the ceiling
    for k in range(int(width * 2)):                                    # coursing on the breast
        W.box(width - .18, .03, .01, u, 2.5 + k * .55, .645, STONE2)
    W.box(width - .5, 1.6, .06, u, .8, .04, SOOT)                      # the back of the fire
    W.box(width - .7, .06, .55, u, .15, .4, COALS)                     # the embers
    for (du, dv, y) in ((-.25, .32, .23), (.25, .32, .23), (0, .44, .37)):
        W.cyl(.09, .09, width * .42, u + du * .3, y, dv, WOOD3, sides=5, rz=math.pi / 2)
    for (du, h, r) in ((-.42, .5, .13), (-.1, .72, .17), (.22, .6, .15), (.5, .42, .11)):
        W.cyl(r, 0, h, u + du * hw * .9, .2 + h / 2, .4, FIRE, sides=5)
    for s in (-1, 1):                                                  # the firedogs
        W.box(.06, .3, .5, u + s * hw * .55, .22, .5, IRON)
        W.box(.08, .1, .08, u + s * hw * .55, .4, .76, IRON)
    if pot:                                                            # a crane and a pot over it
        W.box(.06, 1.3, .06, u - hw + .45, .9, .2, IRON)
        W.span((u - hw + .45, 1.45, .2), (u - .05, 1.45, .45), .04, .04, IRON)
        W.box(.02, .4, .02, u - .05, 1.25, .45, IRON)
        W.cyl(.24, .3, .34, u - .05, .9, .45, IRON, sides=10)
        W.cyl(.27, .27, .02, u - .05, 1.07, .45, IRON, sides=10, cap=False)


def framed(W, u, y, w, h, colors, frame=WOOD3, v=0.0):
    # A picture: a frame, a dark ground and a few blocks of colour on it.
    rng = W.a.rng
    W.box(w, h, .05, u, y, v + .025, frame)
    W.box(w - .14, h - .14, .02, u, y, v + .055, (.12, .11, .10))
    for c in colors:
        W.box(rng.uniform(.2, .5) * w, rng.uniform(.12, .3) * h, .01, u + rng.uniform(-.25, .25) * w, y + rng.uniform(-.25, .25) * h, v + .07, c)


def curtain(W, u0, u1, y0, y1, v, c1, c2, fold=.42):
    n = max(2, int(round((u1 - u0) / fold)))
    step = (u1 - u0) / n
    for k in range(n):
        W.box(step + .02, y1 - y0, .1, u0 + step * (k + .5), (y0 + y1) / 2, v + (.06 if k % 2 else 0), c1 if k % 2 else c2)


def rug(a, x, z, w, d, c, border, rot=False):
    if rot:
        w, d = d, w
    a.box(w, .02, d, x, .07, z, c)
    for s in (-1, 1):
        a.box(w, .022, .14, x, .071, z + s * (d / 2 - .22), border)
        a.box(.14, .022, d - .3, x + s * (w / 2 - .22), .071, z, border)


def wainscot(a, S, B, F, c=DARK, rail=GILT):
    # Panelling to dado height on all four walls, the door's opening left.
    a.box(2 * S, 1.1, .04, 0, .55, B + .02, c)
    a.box(2 * S, .05, .07, 0, 1.12, B + .035, rail)
    for s in (-1, 1):
        a.box(.04, 1.1, F - B, s * (S - .02), .55, (F + B) / 2, c)
        a.box(.07, .05, F - B, s * (S - .035), 1.12, (F + B) / 2, rail)
        L = S - 1.5
        a.box(L, 1.1, .04, s * (1.5 + L / 2), .55, F - .02, c)
        a.box(L, .05, .07, s * (1.5 + L / 2), 1.12, F - .035, rail)
    for k in range(int(2 * S / 1.3)):
        a.box(.04, .9, .01, -S + .65 + k * 1.3, .55, B + .045, (.20, .13, .08))


# -- the Cinder and Keg -------------------------------------------------------
def cinder():
    a = Asset('cinder-keg', seed=1570)
    rng = a.rng
    S, B, F = 10.79, -8.29, 8.29
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    # the bar: Varn stands behind it at (0, -3)
    bz = -1.9
    a.box(9.6, .98, .7, 0, .49, bz, WOOD2)
    for k in range(25):
        a.box(.05, .84, .03, -4.7 + k * 9.4 / 24, .5, bz + .36, WOOD)
    a.box(9.9, .08, .95, 0, 1.02, bz, WOOD3)
    a.box(9.6, .1, .04, 0, .92, bz + .37, DARK)
    a.cyl(.025, .025, 9.3, 0, .2, bz + .62, BRASS, sides=5, rz=math.pi / 2)
    for k in range(5):
        a.box(.04, .04, .28, -4.4 + k * 2.2, .2, bz + .5, BRASS)
    for s in (-1, 1):
        a.box(.7, .98, 1.5, s * 4.45, .49, bz - 1.1, WOOD2)
        a.box(.95, .08, 1.6, s * 4.45, 1.02, bz - 1.12, WOOD3)
    for k in range(7):
        tankard(a, -3.9 + k * 1.25 + rng.uniform(-.3, .3), 1.06, bz + rng.uniform(-.25, .25))
    a.cyl(.09, .07, .2, -2.2, 1.16, bz - .1, (.50, .32, .20), sides=8)          # a jug
    a.cyl(.05, .07, .08, -2.2, 1.3, bz - .1, (.50, .32, .20), sides=8)
    candle(a, -3.3, 1.06, bz)
    candle(a, 2.0, 1.06, bz - .05)
    a.cyl(.2, .13, .1, -.8, 1.11, bz + .1, WOOD3, sides=8)                       # apples
    for k in range(6):
        ang = k / 6 * TAU
        a.rock(.08, .08, .08, -.8 + math.cos(ang) * .09, 1.19 + (k % 2) * .03, bz + .1 + math.sin(ang) * .09, APPLE, jag=.1, sides=5)
    a.box(.55, .01, .38, .9, 1.065, bz, PAGE)
    a.box(.5, .1, .4, 3.6, 1.11, bz - .05, DARK)                                 # a small cask on the bar
    cask(a, 3.6, 1.38, bz - .05, .22, .5, axis='z', tap=1)
    # behind the bar: the keg rack, the back-bar shelves, the emblem
    kz = B + .65
    for y in (.3, 1.42):
        for zz in (B + .25, B + 1.05):
            a.box(8.8, .14, .14, 0, y, zz, DARK)
    for x in (-4.35, 0, 4.35):
        for zz in (B + .25, B + 1.05):
            a.box(.14, 1.5, .14, x, .75, zz, DARK)
    for x in (-3.3, -1.1, 1.1, 3.3):
        cask(a, x, .82, kz, .5, 1.1, axis='z', tap=1)
        cask(a, x, 1.83, kz, .38, .9, axis='z')
    for y in (2.6, 3.1, 3.6):
        a.box(8.4, .05, .32, 0, y, B + .16, WOOD3)
        for x in (-4.0, 0, 4.0):
            a.box(.05, .2, .3, x, y - .12, B + .15, DARK)
        x = -4.0
        while x < 4.0:
            if rng.random() < .8:
                bottle(a, x, y + .025, B + .16 + rng.uniform(-.05, .05), rng.choice(GLASS), tall=rng.uniform(.8, 1.2))
            else:
                tankard(a, x, y + .025, B + .16)
            x += rng.uniform(.18, .32)
    a.cyl(.78, .78, .06, 0, 4.55, B + .04, WOOD3, sides=16, rx=math.pi / 2)     # the keg's end, carved
    a.cyl(.82, .82, .06, 0, 4.55, B + .03, IRON, sides=16, rx=math.pi / 2)
    for (dx, h, r) in ((-.2, .55, .16), (.05, .8, .22), (.28, .5, .14)):
        a.cyl(r, 0, h, dx, 4.3 + h / 2, B + .1, (.62, .22, .08), sides=4)        # a flame, carved and painted
    for s in (-1, 1):                                                           # chalkboards
        a.box(1.9, 1.1, .05, s * 2.7, 4.45, B + .03, WOOD2)
        a.box(1.74, .94, .02, s * 2.7, 4.45, B + .06, SLATE)
        for j in range(5):
            a.box(rng.uniform(.6, 1.4), .025, .01, s * 2.7 + rng.uniform(-.15, .15), 4.75 - j * .16, B + .075, (.78, .76, .70))
    crate(a, -3.4, -4.6, .75, ry=.2)
    crate(a, -3.35, -4.6, .55, ry=.5, y=.75)
    barrel(a, 3.5, -4.8, .38, .95)
    a.box(1.2, .03, 1.0, 1.6, .075, -5.6, DARK)                                  # the cellar's trapdoor
    a.cyl(.1, .1, .02, 1.6, .095, -5.3, IRON, sides=8, cap=False)
    for k in range(3):
        lantern(a, -3.0 + k * 3.0, 3.3, bz)
    # the hearth nook, back left: the fire, two armchairs, a low table, a rug
    fireplace(back, -7.9, 3.0, pot=False)
    rug(a, -7.9, -5.6, 3.4, 2.6, WINE2, OCHRE)
    armchair(a, -9.4, -5.3, 2.52, WINE)
    armchair(a, -6.4, -5.3, -2.52, (.36, .26, .14))
    round_table(a, -7.9, -5.0, .38, .48, WOOD3)
    tankard(a, -7.8, .51, -5.0)
    tankard(a, -8.05, .51, -4.9)
    a.cyl(.4, .36, .55, -10.25, .275, -7.7, (.42, .30, .16), sides=10, cap=False)   # the log basket
    for k in range(5):
        a.cyl(.07, .07, .7, -10.4 + (k % 3) * .14, .45 + (k // 3) * .12, -7.7, WOOD3 if k % 2 else WOOD, sides=5, rx=math.pi / 2)
    for s in (-1, 1):
        candle(a, -7.9 + s * 1.55, 2.12, B + .5)
    for k in range(3):
        back.cyl(.15, .15, .02, -8.6 + k * .7, 2.28, .35, PEWTER, sides=10, rx=math.pi / 2 - .25)
    framed(back, -7.9, 3.4, 1.6, 1.0, [(.50, .20, .10), (.20, .16, .26), (.62, .40, .16)], v=.64)
    # the stage, back right: platform, curtain, a stool and a lute, a drum,
    # a music stand, footlights
    sx0, sz1 = 6.2, -4.0
    cx, cz = (sx0 + S) / 2, (B + sz1) / 2
    a.box(S - sx0, .45, sz1 - B, cx, .225, cz, WOOD3)
    a.box(S - sx0, .1, .06, cx, .4, sz1, DARK)
    a.box(.06, .1, sz1 - B, sx0, .4, cz, DARK)
    for k in range(8):
        a.box(.02, .005, sz1 - B - .1, sx0 + .3 + k * .55, .452, cz, DARK)
    a.box(1.2, .2, .45, 7.2, .1, sz1 + .22, WOOD2)
    curtain(back, sx0 + .05, S - .05, .45, 4.8, .06, WINE, WINE2)
    curtain(right, B + .05, sz1 - .3, .45, 4.8, .06, WINE, WINE2)
    a.box(S - sx0, .45, .16, cx, 4.95, B + .2, OCHRE)
    a.box(S - sx0, .06, .17, cx, 4.7, B + .2, BRASS)
    a.box(.16, .45, sz1 - B, S - .2, 4.95, cz, OCHRE)
    stool(a, 8.7, -6.6, y=.45)
    a.cyl(.22, .22, .1, 8.75, 1.15, -6.62, (.52, .32, .14), sides=10)           # the lute, on the stool
    a.cyl(.15, .15, .1, 8.95, 1.15, -6.4, (.52, .32, .14), sides=8)
    a.cyl(.04, .04, .1, 8.75, 1.21, -6.62, DARK, sides=6)
    a.span((8.95, 1.15, -6.4), (9.35, 1.17, -5.95), .06, .03, DARK)
    a.span((9.35, 1.17, -5.95), (9.45, 1.13, -5.78), .07, .04, DARK)
    a.cyl(.3, .3, .42, 9.9, .45 + .21, -7.3, WINE2, sides=10)                   # the drum
    a.cyl(.29, .29, .01, 9.9, .88, -7.3, PAGE, sides=10)
    a.span((9.7, .92, -7.0), (9.4, 1.05, -6.7), .02, .02, WOOD3)
    a.cyl(.02, .02, 1.2, 7.8, 1.05, -5.9, IRON, sides=4)                        # the music stand
    a.box(.5, .36, .03, 7.8, 1.7, -5.85, IRON, rx=-.5)
    a.box(.44, .3, .01, 7.8, 1.71, -5.83, PAGE, rx=-.5)
    for k in range(3):
        a.cyl(.13, .16, .04, 7.9 + k * .02, .47, -7.6 + k * .3, (.40, .26, .12), sides=6)
    a.box(3.0, .08, .36, 8.6, .9, B + .45, WOOD)                                 # a bench for the players
    for x in (7.3, 9.9):
        a.box(.08, .44, .3, x, .67, B + .45, WOOD)
    for k in range(4):                                                          # footlights
        a.cyl(.07, .05, .06, 6.8 + k * 1.15, .48, sz1 + .12, IRON, sides=6)
        a.cyl(.03, .03, .1, 6.8 + k * 1.15, .56, sz1 + .12, WAX, sides=5)
        a.cyl(.025, 0, .07, 6.8 + k * 1.15, .645, sz1 + .12, FLAME, sides=4)
    lantern(a, cx, 3.6, -5.6)
    # the floor: round tables with their stools
    for (tx, tz) in ((-4.4, 1.0), (4.4, 1.0), (-4.8, 5.0), (4.8, 5.0)):
        round_table(a, tx, tz, .6)
        n = 4 if tz > 3 else 3
        for k in range(n):
            ang = k / n * TAU + rng.uniform(-.3, .3) + tx
            stool(a, tx + math.cos(ang) * 1.0, tz + math.sin(ang) * 1.0)
        for k in range(rng.randint(1, 3)):
            tankard(a, tx + rng.uniform(-.35, .35), .81, tz + rng.uniform(-.35, .35))
        candle(a, tx, .81, tz)
    # the regulars' long table on the left wall, a settle against the wall,
    # a bench on the room side, a game left half-played
    lx, lz0, lz1 = -9.3, .3, 4.9
    lzc, lL = (lz0 + lz1) / 2, lz1 - lz0
    a.box(1.0, .1, lL, lx, .82, lzc, WOOD3)
    for s in (-1, 1):
        a.box(.12, .78, .12, lx, .39, lzc + s * (lL / 2 - .3), WOOD)
        a.box(.9, .1, .1, lx, .2, lzc + s * (lL / 2 - .3), WOOD)
    a.box(.5, .1, lL, -10.48, .46, lzc, WOOD)
    a.box(.08, 1.3, lL, -10.72, 1.05, lzc, WOOD2)
    a.box(.45, .42, lL, -10.48, .21, lzc, WOOD2)
    bench(a, -8.32, lzc, lL - .2, along='z')
    for k in range(4):
        tankard(a, lx + rng.uniform(-.25, .25), .87, lz0 + .5 + k * 1.1 + rng.uniform(-.2, .2))
    candle(a, lx, .87, lzc + .6)
    a.box(.42, .03, .42, lx, .885, lzc - 1.0, PAGE)                               # the game
    for i in range(4):
        for j in range(4):
            if (i + j) % 2:
                a.box(.1, .01, .1, lx - .15 + i * .1, .905, lzc - 1.15 + j * .1, INK)
    for k in range(5):
        a.cyl(.025, .025, .02, lx - .12 + rng.uniform(0, .25), .915, lzc - 1.12 + rng.uniform(0, .25), (WINE if k % 2 else PAGE), sides=6)
    a.box(.3, .05, lL, -10.6, 2.35, lzc, WOOD)                                   # a shelf of plates over it
    for k in range(7):
        a.cyl(.16, .16, .02, -10.62, 2.53, lz0 + .4 + k * .62, PEWTER if k % 2 else (.62, .52, .40), sides=10, rz=math.pi / 2 - .2)
    # barrel tables along the right wall, a dartboard
    for z in (-2.0, 1.0, 4.0):
        barrel(a, 9.9, z, .38, 1.0)
        a.cyl(.5, .5, .05, 9.9, 1.04, z, WOOD3, sides=10)
        tankard(a, 9.8, 1.065, z + .15)
    for (r, c) in ((.24, (.70, .62, .46)), (.17, INK), (.11, (.70, .62, .46)), (.05, WINE)):
        right.cyl(r, r, .04, 6.6, 1.8, .03 + (.24 - r) * .2, c, sides=14, rx=math.pi / 2)
    for k in range(3):
        right.span((6.6 + rng.uniform(-.1, .1), 1.8 + rng.uniform(-.1, .1), .1), (6.6, 1.8, .3), .01, .01, (.60, .20, .10))
    # the front wall: pegs with cloaks and hats; the night's board by the door
    a.box(4.0, .1, .1, -5.0, 1.9, F - .1, WOOD2)
    for k in range(6):
        x = -6.6 + k * .65
        a.box(.04, .04, .16, x, 1.9, F - .2, WOOD3)
        if k % 2 == 0:
            a.box(.45, 1.1, .08, x, 1.35, F - .24, rng.choice((WOOL, MOSS, WINE2, (.36, .30, .22))), rz=rng.uniform(-.05, .05))
        else:
            a.cyl(.2, .14, .14, x, 2.05, F - .24, (.24, .18, .12), sides=8)
    a.box(1.2, 1.5, .06, 4.2, 1.7, F - .05, WOOD2)
    a.box(1.06, 1.36, .02, 4.2, 1.7, F - .09, SLATE)
    for j in range(6):
        a.box(rng.uniform(.4, .9), .025, .01, 4.2 + rng.uniform(-.1, .1), 2.2 - j * .18, F - .1, (.78, .76, .70))
    # light: two wheels over the floor, sconces on the walls
    wheel(a, -4.6, 3.0)
    wheel(a, 4.6, 3.0)
    for (W, u) in ((left, 2.6), (left, -6.4), (right, -2.8), (right, 2.6)):
        sconce(W, u)
    a.finish(cam_at=(0, 2.4, 7.6), cam_look=(0, 1.5, -4), res=(640, 420), lens=22,
             extra_views=[('nook', (-3.6, 2.0, -1.0), (-8.6, 1.0, -6.6)), ('stage', (3.2, 2.0, -.4), (8.6, 1.2, -6.4))])


# -- the Southgate Rest -------------------------------------------------------
def southgate():
    a = Asset('southgate-rest', seed=1571)
    rng = a.rng
    S, B, F = 9.79, -7.79, 7.79
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    # the hearth, big and blackened, a pot on its crane, boots drying before it
    fireplace(back, 0, 3.6, pot=True)
    rug(a, 0, -4.9, 3.4, 2.4, (.36, .22, .14), (.24, .16, .10))
    for k, du in enumerate((-1.0, -.1, .8)):
        for s in (-.09, .09):
            x, z = du + s, B + 1.42 + (k % 2) * .1
            a.box(.12, .32, .14, x, .28, z - .04, LEATHER if k != 1 else (.24, .16, .10))
            a.box(.12, .1, .3, x, .05, z + .02, LEATHER if k != 1 else (.24, .16, .10))
    a.span((-1.6, 1.42, B + .86), (1.6, 1.42, B + .86), .01, .01, (.40, .34, .24))   # a line under the mantel
    for k in range(4):
        a.box(.14, .32, .02, -1.1 + k * .7, 1.24, B + .86, rng.choice((WOOL, (.52, .44, .30), MOSS)), rz=rng.uniform(-.1, .1))
    for s in (-1, 1):                                                           # two settles facing in
        x = s * 2.5
        a.box(.5, .1, 2.4, x, .46, -5.0, WOOD)
        a.box(.46, .42, 2.4, x, .21, -5.0, WOOD2)
        a.box(.08, 1.5, 2.4, x + s * .27, .95, -5.0, WOOD2)
        for e in (-1, 1):
            a.box(.56, .5, .06, x + s * .03, .75, -5.0 + e * 1.2, WOOD2)
    a.box(.4, .12, 1.4, 2.5, .57, -5.3, (.42, .16, .14))                         # a blanket left folded
    a.box(.5, .9, .1, -2.79, 1.2, -4.4, MOSS, rz=-.05)                          # a cloak over the settle's back
    # the left wall: the pack rail, packs and staffs, a bench under it, the
    # map of the south road above
    a.box(.1, .1, 6.0, -S + .08, 1.95, .6, WOOD2)
    for k in range(9):
        z = -2.2 + k * .7
        a.box(.18, .04, .04, -S + .17, 1.95, z, WOOD3)
        if k % 2 == 0:
            c = rng.choice((LEATHER, (.42, .36, .24), MOSS, (.30, .24, .20)))
            a.rock(.4, .6, .5, -S + .32, 1.55, z, c, jag=.12, sides=6)
            a.cyl(.11, .11, .55, -S + .34, 1.92, z, rng.choice((WOOL, (.52, .44, .30), WINE2)), sides=6, rx=math.pi / 2)
        elif k != 3:
            a.cyl(.2, .14, .12, -S + .25, 2.12, z, (.26, .20, .14), sides=8)
    for k in range(3):
        a.span((-S + .45, 0, 3.7 + k * .3), (-S + .1, 1.75, 3.6 + k * .3), .05, .05, WOOD3)
    bench(a, -S + .3, -.4, 3.6, along='z')
    a.rock(.45, .5, .55, -S + .35, .76, -1.2, LEATHER, jag=.12)
    a.rock(.4, .45, .5, -S + .5, .25, .9, (.42, .36, .24), jag=.12)
    a.cyl(.1, .1, .5, -S + .5, .55, .9, WOOL, sides=6, rx=math.pi / 2)
    for s in (-.1, .1):
        a.box(.12, .3, .14, -S + .9, .15, 1.5 + s, LEATHER)
    left.box(3.0, 1.4, .05, -.6, 3.25, .025, WOOD)                              # the south road, painted
    left.box(2.84, 1.24, .02, -.6, 3.25, .06, PAGE)
    road = [(-1.9, 2.75), (-1.3, 3.0), (-.8, 2.9), (-.2, 3.35), (.3, 3.3), (.8, 3.6), (.6, 3.75)]
    for (p, q) in zip(road, road[1:]):
        left.span((p[0], p[1], .075), (q[0], q[1], .075), .04, .01, (.42, .30, .18))
    for (u, y) in road[::2]:
        left.box(.08, .08, .01, u, y + .1, .08, INK)
    left.box(.4, .3, .01, .6, 3.65, .08, STONE2)                                 # the city at the top
    # pallets in the back left corner
    for z in (-6.9, -5.7):
        a.box(1.9, .16, .9, -8.7, .08, z, STRAW)
        a.box(1.4, .08, .8, -8.5, .2, z, rng.choice((WOOL, (.42, .16, .14), (.32, .30, .22))))
        a.rock(.35, .25, .5, -9.4, .27, z, LEATHER, jag=.1)
    barrel(a, -4.6, -7.2, .38, .9)                                               # water, with a dipper
    a.cyl(.36, .36, .02, -4.6, .905, -7.2, (.16, .24, .30), sides=10)
    a.span((-4.5, .92, -7.1), (-4.2, 1.2, -6.9), .02, .02, WOOD3)
    a.box(.6, .8, .45, -6.0, .4, -7.4, WOOD2)                                    # a washstand
    a.cyl(.22, .15, .12, -6.0, .86, -7.4, (.55, .50, .44), sides=10)
    back.box(.5, .7, .03, -6.0, 1.7, .02, (.55, .58, .62))
    # the keeper's desk on the right: the ledger, a bell, the keys behind it
    a.box(.8, 1.0, 2.6, 7.6, .5, -4.6, WOOD2)
    a.box(.95, .07, 2.8, 7.6, 1.03, -4.6, WOOD3)
    a.box(.45, .03, .6, 7.55, 1.08, -4.7, PAGE, ry=.1)
    a.box(.47, .015, .02, 7.55, 1.095, -4.7, INK, ry=.1)
    for j in range(6):
        a.box(.16, .005, .008, 7.45 + (j % 2) * .22, 1.1, -4.9 + (j // 2) * .14, INK, ry=.1)
    a.cyl(.06, .08, .08, 7.5, 1.1, -5.6, BRASS, sides=8)
    a.cyl(.012, .012, .06, 7.5, 1.17, -5.6, BRASS, sides=4)
    candle(a, 7.5, 1.065, -3.6)
    stool(a, 8.9, -4.6)
    right.box(2.0, 1.0, .05, -4.6, 2.05, .025, WOOD)
    for k in range(10):
        u = -5.4 + (k % 5) * .4
        y = 2.3 - (k // 5) * .45
        right.box(.03, .03, .1, u, y, .08, IRON)
        if k not in (3, 7):
            right.box(.02, .14, .01, u, y - .1, .1, BRASS)
            right.box(.06, .05, .01, u, y - .2, .1, PAGE)
    # the stairs up to the rooms along the right wall, and the door at the top
    n, rise, run = 12, .28, .34
    z0 = 6.9
    for k in range(1, n + 1):
        a.box(1.2, rise * k, run, S - .6, rise * k / 2, z0 - run * (k - .5), WOOD2)
        a.box(1.24, .04, run + .03, S - .6, rise * k, z0 - run * (k - .5), WOOD3)
    zl = z0 - run * n
    a.box(1.2, rise * n, 1.6, S - .6, rise * n / 2, zl - .8, WOOD2)
    a.box(1.24, .05, 1.64, S - .6, rise * n, zl - .8, WOOD3)
    hx = S - 1.18
    for k in range(0, n + 1, 2):
        y = rise * k
        a.box(.07, .95, .07, hx, y + .47, z0 - run * k, WOOD)
    a.span((hx, .95, z0), (hx, .95 + rise * n, zl), .07, .07, WOOD3)
    a.span((hx, .95 + rise * n, zl), (hx, .95 + rise * n, zl - 1.6), .07, .07, WOOD3)
    for zz in (zl - .8, zl - 1.6):
        a.box(.07, .95, .07, hx, rise * n + .47, zz, WOOD)
    right.box(1.2, 2.2, .06, zl - .8, rise * n + 1.1, .03, DARK)
    right.box(1.0, 2.05, .04, zl - .8, rise * n + 1.06, .07, WOOD)
    for j in range(3):
        right.box(1.0, .06, .02, zl - .8, rise * n + .5 + j * .7, .1, IRON)
    right.cyl(.05, .05, .03, zl - .45, rise * n + 1.0, .11, IRON, sides=6, rx=math.pi / 2)
    sconce(right, zl + .1, y=rise * n + 1.9)
    barrel(a, S - .5, -.1, .34, .8)
    # the long table, benches either side; small tables on the right
    tx, tz0, tz1 = -4.0, .2, 4.6
    tzc, tL = (tz0 + tz1) / 2, tz1 - tz0
    a.box(1.0, .1, tL, tx, .82, tzc, WOOD3)
    for s in (-1, 1):
        a.box(.9, .1, .12, tx, .2, tzc + s * (tL / 2 - .4), WOOD)
        for e in (-1, 1):
            a.box(.1, .78, .1, tx + e * .35, .39, tzc + s * (tL / 2 - .4), WOOD)
        bench(a, tx + s * .85, tzc, tL - .2, along='z')
    for k in range(5):
        z = tz0 + .5 + k * .85
        bowl(a, tx + (.25 if k % 2 else -.25), .87, z)
    for k in range(3):
        loaf(a, tx + rng.uniform(-.2, .2), .87, tz0 + 1.0 + k * 1.3, ry=rng.uniform(0, 3))
    candle(a, tx, .87, tzc)
    for (sx, sz) in ((4.4, 4.2), (4.4, .6)):
        a.box(.95, .08, .95, sx, .8, sz, WOOD3)
        for e in (-1, 1):
            for f in (-1, 1):
                a.box(.08, .76, .08, sx + e * .38, .38, sz + f * .38, WOOD)
        for k in range(3):
            ang = k / 3 * TAU + sz
            stool(a, sx + math.cos(ang) * .85, sz + math.sin(ang) * .85)
        tankard(a, sx + .15, .84, sz - .1)
        candle(a, sx - .2, .84, sz + .15)
    # by the door: lanterns for the road on hooks, a mat
    a.box(1.4, .08, .08, -4.0, 2.0, F - .1, WOOD2)
    for k in range(3):
        lx = -4.5 + k * .5
        a.box(.02, .2, .02, lx, 1.88, F - .16, IRON)
        a.box(.16, .22, .16, lx, 1.66, F - .2, (.80, .62, .36))
        a.cyl(.12, .02, .08, lx, 1.81, F - .2, IRON, sides=4)
    a.box(2.2, .02, 1.0, 0, .07, F - .7, STRAW)
    # light: two lanterns, sconces
    lantern(a, tx, 3.4, tzc)
    lantern(a, 4.4, 3.6, 2.4)
    for (W, u) in ((left, 4.5), (left, -5.5), (right, -1.6)):
        sconce(W, u)
    a.finish(cam_at=(0, 2.4, 7.0), cam_look=(0, 1.4, -4), res=(640, 420), lens=22,
             extra_views=[('stairs', (-2.0, 2.4, 0.0), (8.6, 2.0, 3.0)), ('fire', (0, 1.6, -1.6), (0, .8, -7.4))])


# -- the Gilded Finch ---------------------------------------------------------
def booth(W, u, cushion):
    # Two high-backed benches standing out from the wall with a table between.
    for s in (-1, 1):
        W.box(.62, .42, 2.0, u + s * .95, .21, 1.05, DARK)
        W.box(.58, .12, 1.96, u + s * .95, .47, 1.05, cushion)
        W.box(.12, 1.65, 2.04, u + s * 1.3, .825, 1.05, DARK)
        W.box(.07, .72, 1.9, u + s * 1.22, .98, 1.05, cushion, rz=s * .06)
        W.box(.16, .05, 2.08, u + s * 1.3, 1.67, 1.05, GILT)
    W.box(1.0, .07, 1.5, u, .76, 1.0, DARK)
    W.box(.1, .7, .1, u, .37, 1.0, DARK)
    W.box(.6, .05, .6, u, .03, 1.0, DARK)


def finch():
    a = Asset('gilded-finch', seed=1572)
    rng = a.rng
    S, B, F = 9.79, -7.79, 7.79
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    wainscot(a, S, B, F)
    rug(a, 0, 1.4, 6.6, 8.4, WINE2, OCHRE)
    a.box(2.2, .023, 2.2, 0, .072, 1.4, PLUM, ry=math.pi / 4)
    # the musician's nook: a half-round dais under a gilt arch, the curtain
    # behind, a harp, a viol on its stand, a stool, the music stand
    r = 2.3
    outline = [(r * math.cos(t), -r * math.sin(t)) for t in [math.pi - k * math.pi / 14 for k in range(15)]]
    a.extrude(outline, .32, DARK, at=(0, .16, B), rx=-math.pi / 2)
    edge = [(math.cos(math.pi - k * math.pi / 14) * (r + .01), .3, B + math.sin(math.pi - k * math.pi / 14) * (r + .01)) for k in range(15)]
    a.tube(edge, [.03] * 15, GILT, sides=4, cap0=False, cap1=False)
    curtain(back, -1.9, 1.9, .32, 4.6, .03, PLUM, (.22, .08, .20), fold=.38)
    arch = pointed_arch_curve(2.05, 3.4, 1.7, segs=8)
    a.tube([(x, y, B + .14) for (x, y) in arch], [.07] * len(arch), GILT, sides=4)
    for s in (-1, 1):
        a.box(.24, 3.4, .16, s * 2.05, 1.7, B + .1, GILT)
        a.box(.36, .2, .22, s * 2.05, .1, B + .12, GILT)
    hx, hz = -.95, B + 1.05                                                     # the harp
    a.box(.5, .1, .3, hx, .37, hz, DARK)
    a.span((hx - .2, .4, hz), (hx - .2, 1.85, hz), .07, .07, GILT)
    a.span((hx + .2, .42, hz), (hx - .05, 1.45, hz), .14, .09, (.42, .26, .12))
    neck = [(hx - .2, 1.85, hz), (hx - .05, 1.8, hz), (hx + .05, 1.62, hz), (hx - .02, 1.5, hz)]
    a.tube(neck, [.04] * 4, GILT, sides=4)
    for k in range(7):
        t = (k + .5) / 7
        a.span((hx + .2 - t * .25, .45 + t * 1.0, hz), (hx - .2 + .02, .55 + t * 1.25, hz), .006, .006, PAGE)
    stool(a, 0, B + 1.25, y=.32, h=.55)
    vx, vz = 1.0, B + .95                                                       # the viol on its stand
    a.cyl(.03, .03, .7, vx, .67, vz - .2, DARK, sides=4)
    a.box(.36, .5, .12, vx, 1.0, vz, (.46, .24, .10))
    a.box(.28, .34, .12, vx, 1.4, vz, (.46, .24, .10))
    a.box(.05, .5, .04, vx, 1.8, vz + .02, DARK)
    a.box(.07, .12, .06, vx, 2.1, vz + .02, DARK, rx=-.4)
    a.cyl(.02, .02, .9, .2, .77, B + 1.9, BRASS, sides=4)
    a.box(.46, .34, .03, .2, 1.32, B + 1.92, BRASS, rx=-.5)
    a.box(.4, .28, .01, .2, 1.33, B + 1.94, PAGE, rx=-.5)
    for s in (-1, 1):                                                           # tall candle stands
        x, z = s * 2.65, B + .6
        a.cyl(.18, .14, .06, x, .03, z, GILT, sides=8)
        a.cyl(.03, .03, 1.7, x, .9, z, GILT, sides=5)
        a.box(.56, .04, .04, x, 1.75, z, GILT)
        for d in (-.26, 0, .26):
            candle(a, x + d, 1.77 + (.08 if d == 0 else 0), z, holder=GILT, h=.18)
    # the late-night room, back left, behind a partition and a curtain
    pz, px = -3.6, -5.6
    dx = -6.7                                                                # the doorway's middle, clear of the booths
    for (x0, x1) in ((-S, dx - .7), (dx + .7, px)):
        a.box(x1 - x0, 3.3, .14, (x0 + x1) / 2, 1.65, pz, DARK)
        a.box(x1 - x0 + .02, .06, .18, (x0 + x1) / 2, 3.33, pz, GILT)
        for k in range(int((x1 - x0) / .4)):
            a.box(.03, 2.9, .02, x0 + .2 + k * .4, 1.6, pz + .08, (.20, .13, .08))
    a.box(1.4, .7, .14, dx, 2.95, pz, DARK)
    a.box(.14, 3.3, pz - B, px, 1.65, (pz + B) / 2, DARK)
    a.box(.18, .06, pz - B + .02, px, 3.33, (pz + B) / 2, GILT)
    a.cyl(.025, .025, 1.6, dx, 2.55, pz + .12, GILT, sides=4, rz=math.pi / 2)
    for s in (-1, 1):                                                           # the drapes, drawn back
        for k in range(3):
            a.box(.18, 2.45, .1, dx + s * (.62 - k * .14), 1.3, pz + .14 + (k % 2) * .04, WINE if k % 2 else WINE2, rz=s * .04 * (k + 1))
        a.cyl(.05, .05, .2, dx + s * .5, 1.2, pz + .2, GILT, sides=4, rz=math.pi / 2)
    round_table(a, -7.7, -5.9, .45, .42, DARK)
    for (x, z, c) in ((-8.6, -5.5, PLUM), (-7.0, -6.8, WINE), (-8.3, -6.9, OCHRE), (-6.7, -5.4, PLUM)):
        a.cyl(.34, .3, .24, x, .12, z, c, sides=10)                          # floor cushions
        a.cyl(.3, .3, .02, x, .245, z, GILT, sides=10, cap=False)
    a.box(.2, .26, .2, -7.7, .58, -5.9, LAMP)
    a.cyl(.12, .02, .06, -7.7, .74, -5.9, BRASS, sides=4)
    bottle(a, -7.5, .45, -6.1, GLASS[1])
    glass(a, -7.9, .45, -5.7)
    glass(a, -7.4, .45, -5.65)
    a.box(2.4, .05, .3, -7.7, 1.6, B + .16, DARK)
    for k in range(6):
        bottle(a, -8.7 + k * .38, 1.625, B + .16, rng.choice(GLASS))
    framed(back, -7.7, 2.5, 1.0, .7, [(.30, .12, .24), (.60, .44, .20)], frame=GILT)
    # the bar, back right: a polished counter, shelves of good bottles, a
    # mirror, decanters and glasses, a small cask behind
    cz = -4.6
    a.box(4.39, 1.0, .7, 7.595, .5, cz, DARK)
    for k in range(6):
        a.box(.6, .7, .02, 5.85 + k * .72, .5, cz + .36, (.20, .12, .07))
        a.box(.62, .03, .03, 5.85 + k * .72, .87, cz + .37, GILT)
    a.box(4.6, .07, .88, 7.5, 1.035, cz, (.24, .12, .08))
    a.box(4.6, .03, .05, 7.5, 1.0, cz + .45, GILT)
    for y in (2.1, 2.6, 3.1):
        a.box(3.8, .05, .3, 7.6, y, B + .16, DARK)
        a.box(3.8, .02, .02, 7.6, y + .03, B + .31, GILT)
        x = 5.85
        while x < 9.4:
            bottle(a, x, y + .025, B + .16, rng.choice(GLASS), tall=rng.uniform(.9, 1.3))
            x += rng.uniform(.2, .3)
    a.box(2.0, 1.1, .03, 7.6, 4.1, B + .03, SILVER)
    a.box(2.2, 1.3, .02, 7.6, 4.1, B + .01, GILT)
    for (x, c) in ((6.0, GLASS[3]), (6.4, GLASS[1])):
        a.cyl(.11, .11, .2, x, 1.17, cz - .1, c, sides=8)
        a.cyl(.03, .05, .14, x, 1.34, cz - .1, c, sides=6)
        a.cyl(.04, .04, .05, x, 1.43, cz - .1, GILT, sides=6)
    for k in range(5):
        glass(a, 7.0 + k * .35, 1.07, cz + rng.uniform(-.15, .15))
    candle(a, 9.0, 1.07, cz, holder=GILT)
    a.box(.5, .4, .5, 8.8, .2, -7.0, DARK)
    cask(a, 8.8, .66, -7.0, .25, .55, axis='x', tap=-1)
    # six booths down the walls
    for (W, u, c) in ((left, .8, WINE), (left, -1.9, PLUM), (left, -4.6, WINE),
                      (right, -2.6, PLUM), (right, .1, WINE), (right, 2.8, PLUM)):
        booth(W, u, c)
        x, z = W.p(u, 1.0)
        candle(a, x, .795, z, holder=GILT)
        a.cyl(.06, .05, .16, x, .92, z, LAMP, sides=6, cap=False)
        for k in range(2):
            gx, gz = W.p(u + (k - .5) * .5, 1.25 + k * .2)
            glass(a, gx, .795, gz)
        framed(W, u, 2.75, 1.3, .9, [rng.choice(((.24, .20, .34), (.40, .30, .16), (.20, .28, .22))), (.62, .48, .24)], frame=GILT)
        sconce(W, u + 1.34, y=2.0, glass_chimney=True, metal=GILT)
    # the floor: small tables with armchairs facing
    for (tx, tz) in ((-3.4, .4), (3.4, .4), (-3.4, 4.2), (3.4, 4.2)):
        round_table(a, tx, tz, .45, .72, DARK)
        a.cyl(.46, .46, .01, tx, .755, tz, GILT, sides=12, cap=False)
        armchair(a, tx, tz - .9, 0.0, PLUM if tz < 2 else WINE, frame=DARK)
        armchair(a, tx, tz + .9, math.pi, PLUM if tz < 2 else WINE, frame=DARK)
        candle(a, tx, .75, tz, holder=GILT)
        glass(a, tx + .2, .75, tz - .15)
    # the finch, in its gilt cage over the middle of the room
    fx, fy, fz = 0, 3.3, 1.6
    for k in range(12):
        ang = k / 12 * TAU
        bar =[(fx + math.cos(ang) * rr, fy + yy, fz + math.sin(ang) * rr) for (rr, yy) in ((.36, 0), (.36, .55), (.3, .78), (.16, .92), (.02, .98))]
        a.tube(bar, [.01] * 5, GILT, sides=3, cap0=False, cap1=False)
    for yy in (0, .3, .55):
        ring = [(fx + math.cos(k / 16 * TAU) * .36, fy + yy, fz + math.sin(k / 16 * TAU) * .36) for k in range(17)]
        a.tube(ring, [.014] * 17, GILT, sides=3, cap0=False, cap1=False)
    a.cyl(.37, .37, .03, fx, fy - .01, fz, GILT, sides=16)
    a.span((fx - .3, fy + .32, fz), (fx + .3, fy + .32, fz), .02, .02, WOOD3)
    a.rock(.13, .1, .09, fx + .02, fy + .4, fz, (.86, .66, .16), jag=.06, sides=6)        # the finch
    a.rock(.08, .08, .08, fx + .09, fy + .47, fz, (.86, .66, .16), jag=.05, sides=5)
    a.cyl(.015, 0, .04, fx + .14, fy + .47, fz, (.80, .48, .20), sides=3, rz=-math.pi / 2)
    a.box(.1, .03, .07, fx - .08, fy + .4, fz, (.20, .16, .12), rz=.3)
    a.box(.03, CEIL - fy - 1.0, .03, fx, (CEIL + fy + 1.0) / 2, fz, GILT)
    a.cyl(.05, .05, .04, fx, fy + 1.0, fz, GILT, sides=6)
    # the chandelier: a gilt ring of candles
    wheel(a, 0, -2.4, r=1.1, y=4.5, c=GILT, n=12)
    for k in range(12):
        ang = k / 12 * TAU
        a.box(.04, .12, .04, math.cos(ang) * 1.1, 4.38, -2.4 + math.sin(ang) * 1.1, (.86, .84, .80))
    # by the door: a coat stand, a fern in a pot
    a.cyl(.25, .2, .06, -8.4, .03, 6.4, DARK, sides=6)
    a.cyl(.04, .04, 1.8, -8.4, .9, 6.4, DARK, sides=5)
    for k in range(4):
        ang = k / 4 * TAU
        a.span((-8.4, 1.7, 6.4), (-8.4 + math.cos(ang) * .25, 1.8, 6.4 + math.sin(ang) * .25), .03, .03, DARK)
    a.box(.5, 1.0, .12, -8.15, 1.25, 6.4, PLUM, rz=.08)
    a.cyl(.3, .24, .5, 8.4, .25, 6.4, (.46, .26, .16), sides=10)
    for k in range(9):
        ang = k / 9 * TAU
        a.span((8.4, .5, 6.4), (8.4 + math.cos(ang) * .6, 1.0 + (k % 3) * .2, 6.4 + math.sin(ang) * .6), .08, .02, MOSS)
    a.finish(cam_at=(0, 2.2, 7.0), cam_look=(0, 1.6, -4), res=(640, 420), lens=22,
             extra_views=[('nook', (0, 1.8, -1.2), (0, 1.6, -7.6)), ('booths', (3.0, 2.0, 6.0), (-8.0, 1.0, -1.0)), ('bar', (2.6, 2.0, -1.0), (8.0, 1.6, -6.8))])


# -- the Wayhouse -------------------------------------------------------------
def wayhouse():
    a = Asset('wayhouse', seed=1573)
    rng = a.rng
    S, B, F = 10.79, -8.29, 8.29
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    # the hearth, the stew pot on its crane, bowls stacked by it
    fireplace(back, 0, 3.8, pot=True)
    for k in range(5):
        bowl(a, 1.6, .12 + k * .06, B + 1.0, (.50, .40, .30), r=.13)
    a.box(.05, .04, .5, -.3, 1.12, B + .7, WOOD3)                                 # the ladle, on the pot
    # the datestone over it: the new wall's line cut in it, a year
    back.box(1.8, .7, .08, 0, 3.4, .66, (.58, .55, .52))
    for k in range(6):
        back.box(.2, .1 if k % 2 else .18, .02, -.6 + k * .24, 3.55, .71, INK)
    back.box(1.3, .02, .02, 0, 3.47, .71, INK)
    for k in range(4):
        back.box(.08, .16, .02, -.4 + k * .27, 3.22, .71, INK)
    # the logs, stacked to the right of the hearth
    for row in range(5):
        for k in range(5 - row // 2):
            a.cyl(.11, .11, .9, 3.2 + k * .23 + (row % 2) * .11, .11 + row * .2, B + .5, WOOD3 if (k + row) % 2 else WOOD, sides=6, rx=math.pi / 2)
    # the serving table along the back wall, left: the baker's bread, the
    # soup, the bowls, a cask of small beer
    sx0, sx1 = -9.9, -4.3
    sxc, sL = (sx0 + sx1) / 2, sx1 - sx0
    a.box(sL, .1, .85, sxc, .86, B + .5, WOOD3)
    for x in (sx0 + .2, sxc, sx1 - .2):
        for s in (-1, 1):
            a.box(.1, .82, .1, x, .41, B + .5 + s * .32, WOOD)
    a.box(sL - .2, .06, .7, sxc, .25, B + .5, WOOD2)
    for (bx, n) in ((-9.2, 6), (-8.1, 5)):
        a.cyl(.35, .28, .22, bx, 1.02, B + .5, (.48, .36, .20), sides=10, cap=False)
        a.cyl(.28, .28, .02, bx, .92, B + .5, (.48, .36, .20), sides=10)
        for k in range(n):
            loaf(a, bx + rng.uniform(-.15, .15), 1.0 + (k // 3) * .08, B + .5 + rng.uniform(-.15, .15), ry=rng.uniform(0, 3))
    a.cyl(.28, .32, .36, -6.9, 1.09, B + .5, IRON, sides=10)
    a.cyl(.27, .27, .01, -6.9, 1.27, B + .5, (.42, .26, .12), sides=10)
    for k in range(6):
        bowl(a, -5.9, .91 + k * .05, B + .5, (.50, .40, .30), r=.13)
    cask(a, -4.9, 1.17, B + .5, .25, .55, axis='z', tap=1)
    a.box(.45, .08, .45, -4.9, .95, B + .5, DARK)
    for k in range(4):
        tankard(a, -9.6 + k * .3, .25 + .03, B + .5, (.48, .40, .32))
    a.box(sL, .05, .3, sxc, 2.4, B + .16, WOOD)                                  # a shelf of bowls over it
    for k in range(12):
        bowl(a, sx0 + .3 + k * .45, 2.425, B + .16, (.50, .40, .30), r=.12)
    # two long tables, benches both sides, places laid
    for tx in (-3.4, 3.4):
        tz0, tz1 = -4.0, 3.6
        tzc, tL = (tz0 + tz1) / 2, tz1 - tz0
        a.box(1.0, .1, tL, tx, .82, tzc, WOOD3)
        for zz in (tz0 + .4, tzc, tz1 - .4):
            a.box(.9, .1, .12, tx, .2, zz, WOOD)
            for e in (-1, 1):
                a.box(.1, .78, .1, tx + e * .35, .39, zz, WOOD)
        for s in (-1, 1):
            bench(a, tx + s * .85, tzc, tL - .2, along='z')
        for k in range(7):
            z = tz0 + .55 + k * 1.05
            for s in (-1, 1):
                if rng.random() < .6:
                    bowl(a, tx + s * .28, .87, z + rng.uniform(-.1, .1), (.50, .40, .30))
                    a.box(.02, .015, .16, tx + s * .28 + .12, .88, z, WOOD3, ry=rng.uniform(-.3, .3))
            if k % 2 == 0:
                loaf(a, tx + rng.uniform(-.08, .08), .87, z + .5, ry=rng.uniform(0, 3), s=.8)
        candle(a, tx, .87, tzc - 1.6)
        candle(a, tx, .87, tzc + 1.6)
        lantern(a, tx, 3.5, tzc)
    # pallets down the right wall, blankets, a shelf of folded ones
    for k, z in enumerate((-7.0, -5.7, -4.4, -3.1, -1.8)):
        a.box(2.0, .16, .95, S - 1.05, .08, z, STRAW)
        if k != 2:
            a.box(1.5, .08, .85, S - 1.25, .2, z, rng.choice((WOOL, (.42, .16, .14), (.32, .30, .22), MOSS)))
            a.rock(.32, .2, .55, S - .32, .26, z, PAGE, jag=.1)
        else:
            a.cyl(.14, .14, .85, S - .6, .3, z, WOOL, sides=6, rx=math.pi / 2)
    a.box(.4, .05, 5.6, S - .22, 2.1, -4.4, WOOD)
    for k in range(8):
        a.box(.34, .2 + (k % 3) * .04, .6, S - .22, 2.24, -6.8 + k * .68, rng.choice((WOOL, (.42, .16, .14), (.32, .30, .22), MOSS)))
    barrel(a, S - .5, 1.0, .38, .9)
    a.cyl(.36, .36, .02, S - .5, .905, 1.0, (.16, .24, .30), sides=10)
    a.box(.6, .8, .45, S - .35, .4, 2.2, WOOD2)                                  # a washstand
    a.cyl(.22, .15, .12, S - .35, .86, 2.2, (.55, .50, .44), sides=10)
    # the left wall: cloaks to take, sacks of meal under a shelf
    a.box(.1, .1, 4.0, -S + .08, 1.95, 1.5, WOOD2)
    for k in range(6):
        z = -.2 + k * .66
        a.box(.18, .04, .04, -S + .17, 1.95, z, WOOD3)
        a.box(.1, 1.2, .5, -S + .25, 1.35, z, rng.choice((WOOL, MOSS, (.36, .30, .22), (.30, .24, .20))), rz=rng.uniform(-.04, .04))
    left.box(2.6, .3, .03, -1.5, 2.55, .02, WOOD3)                               # TAKE ONE, carved
    for k in range(7):
        left.box(.14, .14, .02, -2.55 + k * .3 + (.08 if k > 3 else 0), 2.55, .045, INK if k != 4 else WOOD3)
    for (z, ry) in ((-2.6, .3), (-3.2, -.4), (-3.8, .9)):
        sack(a, -S + .45, z, ry=ry)
    a.box(.4, .05, 2.4, -S + .22, 1.5, -3.2, WOOD)
    for k in range(5):
        a.cyl(.1, .1, .16, -S + .22, 1.605, -4.1 + k * .45, (.50, .40, .30), sides=7)
    # by the door: the alms box on its post, a notice of work wanted
    ax, az = -2.6, 7.5
    a.box(.16, 1.0, .16, ax, .5, az, WOOD)
    a.box(.42, .32, .32, ax, 1.16, az, WOOD2)
    for s in (-1, 1):
        a.box(.44, .04, .34, ax, 1.16 + s * .12, az, IRON)
    a.box(.2, .015, .03, ax, 1.325, az, INK)
    a.box(1.4, 1.1, .05, 4.4, 1.8, F - .05, WOOD)
    for k in range(5):
        a.box(rng.uniform(.25, .4), rng.uniform(.25, .35), .01, 4.0 + (k % 3) * .4, 1.6 + (k // 3) * .45, F - .085, PAGE if k % 2 else (.70, .62, .46))
    # light: sconces, a lantern by the door
    lantern(a, 0, 3.8, 4.4)
    for (W, u) in ((left, -6.0), (left, 2.6), (right, 1.8), (right, 6.0)):
        sconce(W, u)
    a.finish(cam_at=(0, 2.4, 7.6), cam_look=(0, 1.4, -4), res=(640, 420), lens=22,
             extra_views=[('serving', (-2.0, 2.0, -1.0), (-7.6, 1.0, -7.6)), ('pallets', (2.0, 2.2, 1.0), (9.6, .6, -5.0))])


WHICH = {'cinder': cinder, 'southgate': southgate, 'finch': finch, 'wayhouse': wayhouse}
# (r158) tools/assets/halls.py imports the helpers above, so build only when run.
if __name__ == '__main__':
    for name in (sys.argv[1:] or list(WHICH)):
        WHICH[name]()
