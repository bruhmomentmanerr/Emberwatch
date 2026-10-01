# The last five halls fitted out (r158), after the archives (r154, r155), the
# guild halls (r156) and the taverns (r157). Each still had the generic
# furniture for its kind: a stone slab and a drum for a guild hall, a bar
# slab and two blocks for a tavern, a cone on a plinth for the shrine, a rug
# and a table for the chapel, and the storeroom filler round the walls.
#
#   drovers-rest        the Drovers' Rest (22 x 17) — "straw on the floor and
#                       the south road at the door": straw underfoot, a joint
#                       turning on the spit, a drover's dog asleep by the
#                       hearth, saddles, bridles and crooks on the tack wall,
#                       a plank-and-barrel bar, the tally board, hams hung
#                       from the beam, two long tables (warm glow)
#   lamplighters-hall   the Lamplighters' Hall (20 x 16) — "where the oil is
#                       measured out and the rounds are set": the oil casks
#                       and the measures, rows of oil cans, the board of the
#                       rounds, the poles, a ladder, the wick bench, a table
#                       of lanterns, the clerk's desk, the guild's banner
#                       (warm glow)
#   ferriers-yard       Ferrier's Yard (20 x 16) — "iron, hooves and an
#                       argument, most watches": the forge with its hood and
#                       bellows, the anvil, the quench tub, a wall of shoes
#                       with the horses' names over them, the shoeing stall,
#                       the argument's table by the door (fire glow)
#   pilgrim-shrine      the Pilgrim Shrine (18 x 15) — "an offering table and
#   pilgrim-shrine-violet   a little violet quiet": the offering table and what
#                       is left on it, votive racks, kneelers either side of
#                       the aisle, prayer ribbons, staffs, the stoup; the
#                       violet lamps are a second asset with their own glow
#   new-chapel          the New Chapel (19 x 16) — "newer than the city it
#                       stands in, and it shows": pale new pews, the altar
#                       under the sign of the hours, a pulpit, the font, and
#                       the scaffolding still up before a half-painted mural,
#                       pews not yet set, sawhorses (warm glow)
#
# Local frame as the other halls: the room's middle at the origin, the door at
# +z, the inner faces of the side walls at x = +-(w/2 - .21) and of the back
# wall at z = -(d/2 - .21), the floor y = 0, the ceiling's underside y = 6.82.
#
#   python tools/assets/halls.py [drovers|lamplighters|ferriers|shrine|chapel ...]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset
from taverns import (Wall, WOOD, WOOD2, WOOD3, DARK, IRON, BRASS, GILT, PEWTER, STONE, STONE2, SOOT, PAGE,
                     INK, SLATE, WAX, WOOL, WINE, WINE2, PLUM, OCHRE, MOSS, LEATHER, STRAW, BREAD, GLASS,
                     FLAME, LAMP, COALS, FIRE, CEIL, TAU, tankard, bottle, candle, bowl, loaf, crate, sack,
                     cask, barrel, round_table, stool, bench, lantern, wheel, sconce, fireplace, framed,
                     curtain, rug)

STRAW2 = (.52, .44, .24)
MEAT = (.46, .22, .12)
DOG = (.40, .29, .17)
FLEECE = (.78, .74, .66)
CHALK = (.80, .78, .72)
COPPER = (.56, .30, .16)
OIL = (.16, .12, .05)
CLEAR = (.62, .66, .64)
BRICK = (.44, .21, .14)
COAL = (.07, .07, .08)
VIOLET = (.30, .17, .44)
VIOLET2 = (.22, .12, .32)
VLAMP = (.86, .70, 1.0, .1)
PALE = (.58, .44, .27)
PALE2 = (.50, .37, .22)
PLASTER = (.80, .76, .68)
LINEN = (.86, .84, .80)


def ring(a, x, y, z, r, rad, color, n=12, axis='y'):
    # A hoop: a rope coil, a bridle, a crown of candles.
    pts = []
    for k in range(n + 1):
        t = k / n * TAU
        if axis == 'y':
            pts.append((x + math.cos(t) * r, y, z + math.sin(t) * r))
        elif axis == 'x':
            pts.append((x, y + math.sin(t) * r, z + math.cos(t) * r))
        else:
            pts.append((x + math.cos(t) * r, y + math.sin(t) * r, z))
    a.tube(pts, [rad] * (n + 1), color, sides=3, cap0=False, cap1=False)


def long_table(a, x, z0, z1, top=WOOD3, legs=WOOD, benches=True, bench_c=WOOD):
    zc, L = (z0 + z1) / 2, z1 - z0
    a.box(1.0, .1, L, x, .82, zc, top)
    for zz in (z0 + .4, zc, z1 - .4) if L > 4 else (z0 + .4, z1 - .4):
        a.box(.9, .1, .12, x, .2, zz, legs)
        for e in (-1, 1):
            a.box(.1, .78, .1, x + e * .35, .39, zz, legs)
    if benches:
        for s in (-1, 1):
            bench(a, x + s * .85, zc, L - .2, along='z', c=bench_c)


# -- the Drovers' Rest ---------------------------------------------------------
def drovers():
    a = Asset('drovers-rest', seed=1580)
    rng = a.rng
    S, B, F = 10.79, -8.29, 8.29
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    # straw underfoot, thickest by the door
    for k in range(90):
        x = rng.uniform(-S + .4, S - .4)
        z = rng.uniform(B + 1.4, F - .3) if k % 3 else rng.uniform(2.0, F - .3)
        a.box(rng.uniform(.3, .9), .012, rng.uniform(.12, .4), x, .066 + (k % 4) * .002, z, STRAW if k % 2 else STRAW2, ry=rng.uniform(0, math.pi))
    # the hearth, a joint turning on the spit
    fireplace(back, 0, 3.8, pot=False)
    for s in (-1, 1):
        a.box(.08, 1.0, .08, s * 1.25, .5, B + .75, IRON)
        a.box(.3, .06, .3, s * 1.25, .03, B + .75, IRON)
    a.cyl(.02, .02, 2.8, 0, .98, B + .75, IRON, sides=4, rz=math.pi / 2)
    a.rock(.62, .34, .36, 0, .98, B + .75, MEAT, jag=.12, sides=7)
    a.span((1.4, .98, B + .75), (1.5, .78, B + .75), .03, .03, IRON)
    a.box(1.1, .05, .4, 0, .2, B + 1.1, IRON)                               # the dripping pan
    # the dog, asleep on a fleece by the fire
    dx, dz = 2.7, B + 1.75
    a.rock(1.0, .1, .8, dx, .1, dz, FLEECE, jag=.12, sides=8)
    a.rock(.72, .3, .44, dx, .3, dz, DOG, jag=.08, sides=7, ry=.3)
    a.rock(.28, .22, .24, dx - .38, .3, dz + .2, DOG, jag=.06, sides=6)
    a.rock(.14, .1, .12, dx - .52, .26, dz + .27, (.30, .22, .14), jag=.05, sides=5)      # the muzzle
    for e in (-1, 1):
        a.box(.06, .12, .1, dx - .36 + e * .07, .44, dz + .17, (.30, .21, .12), rz=e * .5)
    a.span((dx + .34, .22, dz - .1), (dx + .1, .16, dz + .32), .07, .05, DOG)            # the tail, tucked
    bowl(a, dx + .7, .07, dz + .5, (.40, .34, .28), r=.14)
    # two long tables, the drovers' dinner on them
    for tx in (-3.6, 3.6):
        long_table(a, tx, -4.4, 3.4)
        for k in range(5):
            z = -3.9 + k * 1.6
            tankard(a, tx + rng.choice((-.3, .3)), .87, z + rng.uniform(-.2, .2))
            if k % 2 == 0:
                a.cyl(.26, .26, .03, tx, .885, z + .7, WOOD2, sides=10)
                a.rock(.34, .2, .24, tx, .99, z + .7, MEAT, jag=.1, sides=6, ry=rng.uniform(0, 3))
            else:
                loaf(a, tx + rng.uniform(-.1, .1), .87, z + .6, ry=rng.uniform(0, 3))
        a.box(.04, .01, .3, tx + .2, .875, -1.0, (.60, .62, .66), ry=.4)
        candle(a, tx, .87, -.4)
    # the tack wall, left: saddles on their brackets, bridles and halters,
    # rope, crooks and goads
    for z in (-5.4, -3.6, -1.8):
        a.span((-S, 1.25, z), (-S + .75, 1.25, z), .08, .12, WOOD2)
        a.box(.7, .1, .5, -S + .45, 1.38, z, LEATHER, rz=.08)
        for e in (-1, 1):
            a.box(.62, .44, .05, -S + .45, 1.18, z + e * .27, LEATHER, rx=e * .35)
            a.box(.02, .42, .02, -S + .5, .98, z + e * .32, (.24, .14, .08))
            a.box(.12, .08, .06, -S + .5, .76, z + e * .32, IRON)
        a.box(.14, .14, .44, -S + .12, 1.48, z, (.30, .16, .08))
    for k in range(4):
        z = .2 + k * .7
        a.box(.18, .04, .04, -S + .1, 2.0, z, WOOD3)
        ring(a, -S + .16, 1.78, z, .2, .022, (.28, .16, .08), axis='x')          # a bridle, its reins hanging
        a.span((-S + .16, 1.6, z - .08), (-S + .2, .9, z - .12), .02, .012, (.28, .16, .08))
        a.span((-S + .16, 1.6, z + .08), (-S + .2, .95, z + .1), .02, .012, (.28, .16, .08))
    ring(a, -S + .3, .12, 3.6, .32, .05, (.52, .42, .26))
    ring(a, -S + .3, .22, 3.6, .26, .05, (.52, .42, .26))
    for k in range(3):
        z = 4.6 + k * .4
        a.span((-S + .5, 0, z), (-S + .12, 2.2, z + .05), .045, .045, WOOD3)
        if k != 1:
            a.tube([(-S + .12, 2.2, z + .05), (-S + .14, 2.42, z + .2), (-S + .16, 2.42, z + .38), (-S + .17, 2.3, z + .42)], [.03] * 4, WOOD3, sides=4)
    # the bar, right: planks on barrels, casks on a rack behind
    for z in (-4.4, -1.2):
        barrel(a, 7.9, z, .38, .95)
    a.box(.8, .08, 4.2, 7.9, 1.0, -2.8, WOOD3)
    for k in range(3):
        tankard(a, 7.8 + rng.uniform(-.1, .1), 1.04, -4.2 + k * 1.3)
    for z in (-5.0, -3.6, -2.2):
        cask(a, S - .55, .55, z, .42, .9, axis='x', tap=-1)
    a.box(.9, .14, 4.0, S - .55, .1, -3.6, DARK)
    # the tally board, right: head counted in, head counted out
    right.box(2.6, 1.5, .05, 2.4, 2.1, .025, WOOD2)
    right.box(2.44, 1.34, .02, 2.4, 2.1, .06, SLATE)
    for row in range(5):
        for grp in range(rng.randint(2, 4)):
            u0 = 1.3 + grp * .42
            y = 2.6 - row * .25
            for j in range(4):
                right.box(.012, .14, .01, u0 + j * .06, y, .075, CHALK)
            right.box(.012, .2, .01, u0 + .09, y, .076, CHALK, rz=1.1)
    # hams hung from the beam
    a.box(5.0, .06, .06, 0, 5.95, 4.08, WOOD2)
    for k in range(6):
        x = -2.2 + k * .88
        a.box(.015, .5, .015, x, 5.68, 4.08, (.40, .34, .24))
        a.rock(.26, .5, .22, x, 5.2, 4.08, (.40, .20, .12) if k % 2 else (.48, .30, .16), jag=.08, sides=6)
    # by the door: muddy boots, sheepskins on a bench
    for k in range(4):
        for s in (-.09, .09):
            x = 4.2 + k * .55 + s
            a.box(.12, .3, .14, x, .17, F - .45, (.26, .18, .10))
            a.box(.12, .1, .28, x, .05, F - .38, (.26, .18, .10))
    bench(a, -4.2, F - .5, 2.4, along='x')
    for k in range(3):
        a.rock(.8, .08, .6, -4.6 + k * .5, .53 + k * .05, F - .5, FLEECE, jag=.15, sides=8, ry=k)
    lantern(a, -3.6, 3.6, -.5)
    lantern(a, 3.6, 3.6, -.5)
    for (W, u) in ((left, -6.0), (right, 5.6), (right, -6.5)):
        sconce(W, u)
    a.finish(cam_at=(0, 2.4, 7.6), cam_look=(0, 1.2, -4), res=(640, 420), lens=22,
             extra_views=[('hearth', (1.0, 1.6, -3.0), (1.6, .6, -7.6)), ('tack', (-4.0, 2.0, 1.0), (-10.4, 1.2, -2.0))])


# -- the Lamplighters' Hall ------------------------------------------------------
def oil_can(a, x, y, z):
    a.cyl(.09, .1, .22, x, y + .11, z, BRASS, sides=6)
    a.cyl(.05, .02, .06, x, y + .25, z, BRASS, sides=6)
    a.span((x + .07, y + .16, z), (x + .2, y + .3, z), .02, .02, BRASS)
    a.box(.02, .14, .08, x - .1, y + .14, z, BRASS)


def lamplighters():
    a = Asset('lamplighters-hall', seed=1581)
    rng = a.rng
    S, B, F = 9.79, -7.79, 7.79
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    # the oil: three casks on a cradle, taps over the drip tray, the measures
    # on a shelf over them
    a.box(4.4, .3, 1.3, -6.1, .15, B + .75, DARK)
    for x in (-7.4, -6.1, -4.8):
        cask(a, x, .86, B + .75, .56, 1.2, axis='z', tap=1)
    a.box(4.2, .05, .45, -6.1, .2, B + 1.6, OIL)
    a.box(4.4, .05, .35, -6.1, 2.3, B + .18, WOOD3)
    for k, r in enumerate((.18, .15, .12, .1, .08, .06)):
        x = -7.9 + k * .6
        a.cyl(r, r * .85, r * 2.2, x, 2.325 + r * 1.1, B + .18, COPPER if k % 2 else BRASS, sides=8)
        a.box(.03, r * 1.4, .04, x + r + .02, 2.33 + r * 1.2, B + .18, COPPER if k % 2 else BRASS)
    for k in range(3):
        x = -4.6 + k * .3
        a.cyl(.13, .015, .2, x, 2.42, B + .18, PEWTER, sides=8)               # funnels
    # the guild's banner: the lamp
    a.box(1.5, 2.6, .04, -.6, 3.8, B + .03, OCHRE)
    a.box(1.7, .08, .08, -.6, 5.15, B + .07, WOOD2)
    a.cyl(.28, .22, .12, -.6, 3.5, B + .07, IRON, sides=8, rx=math.pi / 2)
    a.box(.36, .5, .02, -.6, 3.85, B + .065, (.92, .78, .40))
    a.cyl(.26, 0, .26, -.6, 4.25, B + .065, IRON, sides=4, rx=math.pi / 2)
    # the cans, a row for every lamplighter, each with a name under it
    for y in (1.0, 1.7):
        a.box(5.2, .05, .32, 4.4, y, B + .17, WOOD3)
        for k in range(12):
            x = 2.1 + k * .42
            oil_can(a, x, y + .025, B + .17)
            a.box(.2, .06, .01, x, y - .06, B + .335, PAGE)
    # the board of the rounds, right wall: the city as rings, a pin for every
    # lamp, a coloured thread for every round
    right.box(4.4, 2.6, .06, -.6, 2.6, .03, WOOD2)
    right.box(4.2, 2.4, .02, -.6, 2.6, .07, PAGE)
    for frac in (1.0, .66, .33):
        n = 24
        pts = []
        for k in range(n + 1):
            t = k / n * TAU
            pts.append((-.6 + math.cos(t) * 1.0 * frac * 1.6, 2.6 + math.sin(t) * 1.0 * frac, .085))
        for (p, q) in zip(pts, pts[1:]):
            right.span(p, q, .015, .01, INK)
    threads = [(.70, .20, .14), (.18, .30, .56), (.24, .46, .22), (.70, .56, .14), (.46, .20, .50)]
    for c in threads:
        pins = [(-.6 + rng.uniform(-1.6, 1.6), 2.6 + rng.uniform(-.95, .95)) for _ in range(6)]
        pins.sort()
        for (p, q) in zip(pins, pins[1:]):
            right.span((p[0], p[1], .095), (q[0], q[1], .095), .012, .008, c)
        for (u, y) in pins:
            right.cyl(.03, .03, .04, u, y, .1, c, sides=5, rx=math.pi / 2)
    right.span((1.4, 2.0, .095), (2.1, 1.7, .095), .012, .008, (.86, .82, .70))     # one thread runs off the board
    # the poles, left wall: hooks and wick-lighters up
    a.box(.12, .1, 4.6, -S + .12, .25, -2.6, WOOD2)
    a.box(.12, .1, 4.6, -S + .12, 2.4, -2.6, WOOD2)
    for k in range(9):
        z = -4.6 + k * .5
        a.cyl(.025, .025, 3.4, -S + .22, 1.7, z, WOOD3, sides=4)
        a.tube([(-S + .22, 3.4, z), (-S + .22, 3.6, z), (-S + .3, 3.68, z), (-S + .38, 3.6, z)], [.012] * 4, BRASS, sides=3)
        a.cyl(.02, .02, .06, -S + .22, 3.45, z + .05, WAX, sides=4)
    for dz in (-.25, .25):                                                    # a ladder against the wall
        a.span((-S + .9, 0, 3.6 + dz), (-S + .12, 4.2, 3.6 + dz), .07, .07, WOOD3)
    for k in range(1, 12):
        t = k / 12
        a.box(.05, .05, .5, -S + .9 - t * .78, t * 4.2, 3.6, WOOD3)
    # the wick bench: spools, scissors, glass chimneys, a lantern in pieces
    long_table(a, -3.2, -.4, 2.6, benches=False)
    for k in range(4):
        a.cyl(.07, .07, .12, -3.35 + (k % 2) * .25, .93, -.1 + k * .3, (.86, .84, .76), sides=8, rx=math.pi / 2)
    for k in range(5):
        a.cyl(.06, .05, .22, -2.95, .98, .6 + k * .3, CLEAR, sides=6, cap=False)
    a.box(.24, .02, .05, -3.1, .88, 2.0, (.60, .62, .66), ry=.5)
    a.box(.22, .3, .22, -3.2, 1.02, 2.3, IRON, rz=.4)
    stool(a, -2.1, .8)
    # a table of lanterns, two of them lit
    long_table(a, 3.4, -.4, 2.6, benches=False)
    for k in range(6):
        z = -.1 + k * .5
        lit = k in (1, 4)
        a.box(.18, .26, .18, 3.4, 1.0, z, LAMP if lit else CLEAR)
        a.cyl(.15, .03, .1, 3.4, 1.18, z, IRON, sides=4)
        a.box(.22, .04, .22, 3.4, .89, z, IRON)
    # the clerk's desk by the door, the ledger of the rounds and a bell
    a.box(1.0, 1.1, .7, 6.4, .55, 5.4, WOOD2)
    a.box(1.1, .06, .8, 6.4, 1.16, 5.35, WOOD3, rx=.2)
    a.box(.5, .02, .36, 6.4, 1.22, 5.35, PAGE, rx=.2)
    a.cyl(.06, .08, .08, 6.95, 1.14, 5.6, BRASS, sides=8)
    stool(a, 6.4, 6.2, h=.85)
    for (x, z) in ((-3.2, 4.4), (3.4, 4.4)):
        lantern(a, x, 3.8, z)
    lantern(a, 0, 3.6, 1.0)
    for (W, u) in ((left, 1.4), (left, 6.0), (right, -5.2), (right, 4.6)):
        sconce(W, u)
    a.finish(cam_at=(0, 2.4, 7.0), cam_look=(0, 1.4, -4), res=(640, 420), lens=22,
             extra_views=[('oil', (-2.0, 2.0, -2.0), (-6.4, 1.2, -7.4)), ('rounds', (2.0, 2.2, .6), (9.6, 2.4, -.6))])


# -- Ferrier's Yard ------------------------------------------------------------
def shoe(a, x, y, z, facing, c=IRON):
    # A horseshoe hung on a wall, open end down.
    pts = []
    for k in range(7):
        t = math.pi * (1.05 + k / 6 * -1.1)
        u, v = math.cos(t) * .07, math.sin(t) * -.08
        pts.append((x, y + v, z + u) if facing == 'x' else (x + u, y + v, z))
    a.tube(pts, [.012] * 7, c, sides=3)


def ferriers():
    a = Asset('ferriers-yard', seed=1582)
    rng = a.rng
    S, B, F = 9.79, -7.79, 7.79
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    # the forge, back left: the hearth, its hood and chimney, the bellows,
    # the quench tub, the coal
    fx, fz = -5.4, B + .8
    a.box(2.4, .9, 1.5, fx, .45, fz, BRICK)
    a.box(2.5, .08, 1.6, fx, .93, fz, STONE2)
    a.box(1.3, .08, .9, fx, .98, fz + .05, COALS)
    for k in range(6):
        a.rock(.18, .1, .16, fx - .5 + k * .2, 1.02, fz + rng.uniform(-.2, .3), (1.0, .5, .18, .3), jag=.15, sides=5)
    a.box(2.6, 1.0, 1.6, fx, 2.5, fz - .05, BRICK, taper=.55)
    a.box(1.0, CEIL - 3.0, .9, fx, (CEIL + 3.0) / 2, fz - .3, BRICK)
    a.box(2.6, .1, 1.62, fx, 2.0, fz - .05, SOOT)
    bx, bz = fx - 1.9, fz + .1                                                # the bellows
    a.box(.7, .06, 1.2, bx, 1.1, bz, WOOD2, rx=.1)
    a.box(.7, .06, 1.2, bx, .8, bz, WOOD2, rx=-.06)
    a.box(.66, .26, 1.0, bx, .95, bz + .05, LEATHER, taper=.7)
    a.span((bx, 1.15, bz + .55), (bx, 2.2, bz + 1.4), .05, .05, WOOD3)
    a.span((bx, .95, bz - .6), (fx - 1.0, .95, fz), .06, .06, IRON)
    a.box(.12, .8, .12, bx - .25, .4, bz + .4, WOOD)
    a.box(.12, .8, .12, bx + .25, .4, bz + .4, WOOD)
    a.cyl(.42, .45, .7, fx + 1.9, .35, fz + .7, WOOD2, sides=10)                # the quench tub
    a.cyl(.4, .4, .02, fx + 1.9, .69, fz + .7, (.14, .20, .24), sides=10)
    a.box(1.0, .6, .8, fx + 2.0, .3, B + .45, WOOD2)                            # the coal bin
    for k in range(10):
        a.rock(.2, .12, .18, fx + 1.65 + (k % 4) * .2, .62 + (k // 4) * .04, B + .3 + (k % 3) * .18, COAL, jag=.2, sides=5)
    # the anvil on its stump, and the tool rack on the back wall
    ax, az = -4.6, -3.6
    a.cyl(.36, .4, .6, ax, .3, az, WOOD2, sides=8)
    a.box(.84, .22, .32, ax, .71, az, IRON)
    a.box(.34, .3, .26, ax, .5, az, IRON)
    a.cyl(0, .14, .36, ax + .58, .76, az, IRON, sides=4, rz=-math.pi / 2)
    a.box(.3, .05, .1, ax - .1, .845, az + .05, IRON, ry=.4)                    # a shoe on it, cooling
    a.box(2.4, 1.4, .05, -1.4, 2.0, B + .03, WOOD2)
    for k in range(9):
        x = -2.4 + k * .25
        if k % 3 == 0:
            a.span((x - .04, 1.5, B + .08), (x + .02, 2.3, B + .08), .025, .02, IRON)
            a.span((x + .04, 1.5, B + .08), (x - .02, 2.3, B + .08), .025, .02, IRON)
        elif k % 3 == 1:
            a.box(.04, .45, .03, x, 1.95, B + .08, WOOD3)
            a.box(.16, .07, .06, x, 2.2, B + .09, IRON)
        else:
            a.box(.04, .5, .02, x, 1.95, B + .07, (.40, .40, .44))
    # a wall of shoes, right: rows of them, the horse's name chalked over each
    for row in range(6):
        y = 1.2 + row * .42
        a.box(.06, .04, 8.4, S - .03, y + .1, -.6, WOOD2)
        for k in range(18):
            z = -4.6 + k * .46
            if rng.random() < .9:
                shoe(a, S - .07, y, z, 'x', IRON if (row + k) % 5 else (.40, .30, .22))
            if rng.random() < .5:
                right.box(rng.uniform(.14, .28), .02, .01, z, y + .17, .03, CHALK)
    # the shoeing stall, the hoof stand, the horse's blanket on a rail
    sx, sz = 3.0, -2.0
    for (dx, dz) in ((-.6, -1.4), (.6, -1.4), (-.6, 1.4), (.6, 1.4)):
        a.box(.16, 2.0, .16, sx + dx, 1.0, sz + dz, WOOD)
    for s in (-1, 1):
        a.box(.1, .12, 2.9, sx + s * .6, 1.15, sz, WOOD3)
        a.box(.1, .12, 2.9, sx + s * .6, 1.95, sz, WOOD3)
    a.box(1.3, .12, .1, sx, 1.95, sz - 1.4, WOOD3)
    a.box(1.3, .12, .1, sx, 1.95, sz + 1.4, WOOD3)
    for k in range(14):
        a.box(rng.uniform(.3, .7), .012, rng.uniform(.12, .3), sx + rng.uniform(-.7, .7), .066, sz + rng.uniform(-1.4, 1.4), STRAW if k % 2 else STRAW2, ry=rng.uniform(0, 3))
    hx, hz = sx + 1.3, sz + 1.1                                               # the hoof stand
    for k in range(3):
        ang = k / 3 * TAU
        a.span((hx, .5, hz), (hx + math.cos(ang) * .25, 0, hz + math.sin(ang) * .25), .04, .04, IRON)
    a.cyl(.1, .12, .06, hx, .53, hz, IRON, sides=6)
    a.box(.1, 1.0, 1.6, sx + .66, 1.45, sz - .3, (.30, .22, .36), rz=-.06)        # the blanket over the rail
    # the back corner: a barrel of shoes, nail sacks, a cart wheel
    barrel(a, 2.0, B + .5, .38, .9)
    for k in range(7):
        shoe(a, 2.0 + rng.uniform(-.2, .2), .95 + rng.uniform(0, .1), B + .5 + rng.uniform(-.15, .15), 'z')
    sack(a, 3.1, B + .5, ry=.3)
    sack(a, 3.7, B + .7, ry=-.5)
    wx, wz = 6.4, B + .2
    ring(a, wx, 1.0, wz, .95, .06, WOOD2, n=16, axis='z')
    for k in range(6):
        ang = k / 6 * math.pi
        a.span((wx - math.cos(ang) * .92, 1.0 - math.sin(ang) * .92, wz), (wx + math.cos(ang) * .92, 1.0 + math.sin(ang) * .92, wz), .04, .04, WOOD3)
    a.cyl(.14, .14, .2, wx, 1.0, wz, WOOD2, sides=8, rx=math.pi / 2)
    # the argument: a table by the door, two stools set square to each other,
    # two tankards, a slate with a price on it struck out and written again
    round_table(a, -5.6, 4.8, .5, .76)
    stool(a, -6.5, 4.6)
    stool(a, -4.7, 5.1)
    tankard(a, -5.75, .79, 4.7)
    tankard(a, -5.4, .79, 5.0)
    a.box(.3, .02, .22, -5.6, .8, 4.95, SLATE, ry=.2)
    a.box(.18, .01, .01, -5.6, .815, 4.92, CHALK, ry=.2)
    a.box(.2, .01, .01, -5.58, .815, 4.98, CHALK, ry=-.3)
    lantern(a, sx, 3.6, sz)
    lantern(a, -2.0, 3.8, 2.4)
    for (W, u) in ((left, -2.6), (left, 2.4), (right, 5.6)):
        sconce(W, u)
    a.finish(cam_at=(0, 2.4, 7.0), cam_look=(0, 1.4, -4), res=(640, 420), lens=22,
             extra_views=[('forge', (-1.6, 1.8, -1.8), (-5.4, 1.0, -7.0)), ('shoes', (2.0, 2.0, 2.6), (9.6, 2.0, -2.0))])


# -- the Pilgrim Shrine ----------------------------------------------------------
def votive(a, x, z):
    for t in range(3):
        y, w = .7 + t * .3, .9 - t * .2
        a.box(w, .04, .3 - t * .06, x, y, z - t * .06, IRON)
        n = 6 - t
        for k in range(n):
            cx = x - w / 2 + .08 + k * (w - .16) / max(1, n - 1)
            a.cyl(.025, .025, .08, cx, y + .06, z - t * .06, WAX, sides=4)
            a.cyl(.02, 0, .06, cx, y + .13, z - t * .06, FLAME, sides=3)
    for e in (-1, 1):
        a.box(.04, 1.4, .04, x + e * .42, .7, z, IRON)


def shrine():
    S, B, F = 8.79, -7.29, 7.29
    a = Asset('pilgrim-shrine', seed=1583)
    rng = a.rng
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    rug(a, 0, -.6, 1.6, 11.0, VIOLET2, (.42, .34, .52))
    # the offering table: two stone steps, a violet cloth, and what people
    # have left on it
    a.box(3.6, .4, 1.5, 0, .2, B + .78, STONE)
    a.box(3.0, .55, 1.05, 0, .67, B + .6, STONE)
    a.box(3.1, .02, 1.12, 0, .955, B + .6, VIOLET)
    a.box(1.2, .6, .02, 0, .66, B + 1.14, VIOLET)
    for e in (-1, 1):
        a.box(.04, .03, 1.1, e * .6, .97, B + .6, GILT)
    for k in range(22):
        x = rng.uniform(-1.35, 1.35)
        z = B + .6 + rng.uniform(-.38, .38)
        kind = k % 6
        if kind == 0:
            candle(a, x, .965, z, holder=PEWTER, h=rng.uniform(.06, .2))
        elif kind == 1:
            a.box(.1, .015, .07, x, .975, z, PAGE, ry=rng.uniform(0, 3))       # a folded note
        elif kind == 2:
            a.cyl(.025, .025, .006, x, .97, z, BRASS, sides=6)                 # a coin
        elif kind == 3:
            bowl(a, x, .965, z, (.52, .46, .40), r=.08)
        elif kind == 4:
            a.span((x, .975, z), (x + .14, .985, z + .05), .02, .02, MOSS)      # a sprig
        else:
            a.rock(.07, .12, .07, x, 1.02, z, rng.choice(((.50, .40, .28), (.40, .34, .30))), jag=.1, sides=5)
    a.box(.12, .08, .2, .9, 1.0, B + .45, (.40, .24, .20))                     # a child's shoe
    # the roundel over it: a pale moon on violet
    a.cyl(1.25, 1.25, .04, 0, 3.4, B + .03, VIOLET2, sides=24, rx=math.pi / 2)
    a.cyl(1.3, 1.3, .03, 0, 3.4, B + .02, GILT, sides=24, rx=math.pi / 2)
    a.cyl(.62, .62, .02, -.15, 3.5, B + .06, (.84, .82, .90), sides=18, rx=math.pi / 2)
    a.cyl(.55, .55, .02, .12, 3.6, B + .07, VIOLET2, sides=18, rx=math.pi / 2)
    for k in range(8):
        ang = k / 8 * TAU
        a.box(.05, .3, .01, math.cos(ang) * 1.05, 3.4 + math.sin(ang) * 1.05, B + .06, GILT, rz=ang - math.pi / 2)
    # votive racks either side
    for s in (-1, 1):
        votive(a, s * 2.9, B + 1.0)
    # kneelers either side of the aisle, the aisle clear for Pilgrim Sorell
    for s in (-1, 1):
        for z in (-2.2, -.6, 1.0):
            x = s * 2.3
            a.box(2.2, .16, .3, x, .08, z + .25, WOOD2)
            a.box(2.2, .06, .22, x, .2, z + .25, VIOLET)
            a.box(2.2, .06, .2, x, .72, z - .2, WOOD)
            for e in (-1, 1):
                a.box(.06, .72, .5, x + e * 1.05, .36, z, WOOD2)
    # prayer ribbons, left wall: tied to a rail, every colour
    a.box(.08, .08, 7.6, -S + .1, 2.3, -1.4, WOOD2)
    ribbon_c = [(.62, .18, .16), (.20, .30, .56), (.70, .60, .22), (.26, .46, .28), VIOLET, PAGE, (.56, .30, .50)]
    for k in range(46):
        z = -5.1 + k * .162
        L = rng.uniform(.4, 1.1)
        a.box(.01, L, .045, -S + .14, 2.28 - L / 2, z, rng.choice(ribbon_c), rx=rng.uniform(-.06, .06))
    bench(a, -S + .45, -1.4, 3.6, along='z')
    # staffs and gourds, right wall; tokens on a shelf; the stoup by the door
    a.box(.12, .1, 2.4, S - .12, .25, -2.0, WOOD2)
    a.box(.12, .1, 2.4, S - .12, 1.6, -2.0, WOOD2)
    for k in range(6):
        z = -3.0 + k * .4
        a.cyl(.03, .035, 1.9, S - .25, .95, z, WOOD3, sides=5)
        if k % 2 == 0:
            a.rock(.14, .2, .14, S - .3, 1.45, z + .12, (.62, .48, .24), jag=.06, sides=6)
    a.box(.3, .05, 2.0, S - .16, 1.9, 2.4, WOOD3)
    for k in range(9):
        a.cyl(.04, .04, .01, S - .18, 1.94, 1.6 + k * .2, BRASS if k % 2 else PEWTER, sides=8, rz=math.pi / 2 - .3)
    a.cyl(.12, .18, .8, 2.6, .4, 6.2, STONE, sides=8)
    a.cyl(.36, .2, .24, 2.6, .92, 6.2, STONE, sides=10)
    a.cyl(.32, .32, .01, 2.6, 1.03, 6.2, (.18, .22, .30), sides=10)
    for (W, u) in ((left, 4.0), (right, -5.4), (right, 4.6)):
        sconce(W, u)
    a.finish(cam_at=(0, 2.0, 6.0), cam_look=(0, 1.4, -4), res=(640, 420), lens=22,
             extra_views=[('altar', (0, 1.5, -3.4), (0, 1.2, -7.2)), ('ribbons', (2.0, 1.8, 1.0), (-8.6, 1.6, -2.0))])
    # the violet lamps: a second asset, so they glow violet and the candles
    # warm (one glow colour per asset)
    v = Asset('pilgrim-shrine-violet', seed=1584)
    for x in (-1.6, 0, 1.6):
        v.box(.02, CEIL - 3.4 - .2, .02, x, (CEIL + 3.6) / 2, B + 2.4, IRON)
        v.cyl(.16, .1, .3, x, 3.35, B + 2.4, VLAMP, sides=6)
        v.cyl(.18, .03, .1, x, 3.55, B + 2.4, IRON, sides=6)
        v.cyl(.06, .12, .08, x, 3.17, B + 2.4, IRON, sides=6)
    for s in (-1, 1):
        x = s * 1.55
        v.cyl(.03, .03, 1.1, x, .95, B + .45, IRON, sides=4)                 # on the lower step
        v.box(.16, .2, .16, x, 1.6, B + .45, VLAMP)
        v.cyl(.13, .02, .08, x, 1.74, B + .45, IRON, sides=4)
    v.finish(cam_at=(0, 2.0, 2.0), cam_look=(0, 2.2, -6), res=(480, 320), lens=28)


# -- the New Chapel --------------------------------------------------------------
def pew(a, x, z, L, c=PALE):
    a.box(L, .08, .44, x, .46, z, c)
    a.box(L, .5, .06, x, .78, z + .22, c, rx=-.08)
    for e in (-1, 1):
        a.box(.08, .95, .56, x + e * (L / 2 - .04), .47, z + .03, PALE2)
    a.box(L - .1, .06, .3, x, .22, z + .05, PALE2)


def chapel():
    a = Asset('new-chapel', seed=1585)
    rng = a.rng
    S, B, F = 9.29, -7.79, 7.79
    back, left, right = Wall(a, 'back', S, B), Wall(a, 'left', S, B), Wall(a, 'right', S, B)
    # the altar on its step, the sign of the hours over it
    a.box(6.0, .2, 2.4, 0, .1, B + 1.2, PALE2)
    a.box(2.6, .95, .9, 0, .675, B + .8, (.66, .62, .58))
    a.box(2.7, .03, 1.0, 0, 1.165, B + .8, LINEN)
    a.box(2.7, .6, .02, 0, .87, B + 1.31, LINEN)
    for s in (-1, 1):
        a.cyl(.07, .1, .05, s * 1.0, 1.205, B + .8, BRASS, sides=8)
        a.cyl(.025, .025, .5, s * 1.0, 1.48, B + .8, BRASS, sides=5)
        a.cyl(.035, .035, .2, s * 1.0, 1.83, B + .8, WAX, sides=5)
        a.cyl(.03, 0, .1, s * 1.0, 1.98, B + .8, FLAME, sides=4)
    ring(a, 0, 3.7, B + .06, 1.1, .05, BRASS, n=24, axis='z')
    for k in range(12):
        ang = k / 12 * TAU
        L = .26 if k % 3 == 0 else .14
        a.box(.05, L, .02, math.cos(ang) * .93, 3.7 + math.sin(ang) * .93, B + .07, BRASS, rz=ang - math.pi / 2)
    a.span((0, 3.7, B + .08), (0, 4.35, B + .08), .06, .02, BRASS)
    a.span((0, 3.7, B + .08), (.45, 3.45, B + .08), .06, .02, BRASS)
    a.cyl(.07, .07, .03, 0, 3.7, B + .09, BRASS, sides=8, rx=math.pi / 2)
    for s in (-1, 1):                                                         # tall candle stands
        x, z = s * 2.4, B + 1.0
        a.cyl(.2, .16, .06, x, .23, z, IRON, sides=8)
        a.cyl(.03, .03, 1.5, x, .98, z, IRON, sides=5)
        a.cyl(.1, .06, .04, x, 1.74, z, IRON, sides=6)
        a.cyl(.04, .04, .3, x, 1.91, z, WAX, sides=5)
        a.cyl(.035, 0, .12, x, 2.12, z, FLAME, sides=4)
    # the pulpit and the font
    a.cyl(.55, .5, 1.1, -5.6, .55, -5.4, PALE, sides=8)
    a.cyl(.6, .6, .06, -5.6, 1.13, -5.4, PALE2, sides=8)
    a.box(.5, .04, .36, -5.6, 1.25, -5.1, PALE2, rx=.35)
    a.box(.4, .03, .28, -5.6, 1.28, -5.08, PAGE, rx=.35)
    a.box(.4, .3, .4, -5.6, .15, -4.6, PALE2)                                  # its step
    a.cyl(.16, .24, .8, -2.8, .4, 5.6, (.66, .62, .58), sides=8)
    a.cyl(.42, .26, .3, -2.8, .95, 5.6, (.66, .62, .58), sides=10)
    a.cyl(.38, .38, .01, -2.8, 1.09, 5.6, (.18, .22, .30), sides=10)
    # the pews: new wood, two blocks of five, the aisle down the middle
    for s in (-1, 1):
        for k in range(5):
            pew(a, s * 2.75, -3.8 + k * 1.45, 3.3)
    # an iron crown of candles over the nave
    wheel(a, 0, -1.0, r=1.0, y=4.6, c=IRON, n=10)
    # what is not finished: the scaffolding up the left wall before a mural
    # half painted, a ladder, paint pots and brushes
    left.box(4.6, 3.2, .02, 2.0, 3.0, .015, PLASTER)
    figure = [((1.7, 1.6), (1.7, 3.0)), ((1.7, 3.0), (1.4, 3.9)), ((1.7, 3.0), (2.1, 3.9)), ((1.7, 3.0), (1.3, 2.1)), ((1.7, 3.0), (2.2, 2.2)),
              ((1.4, 1.6), (2.0, 1.6)), ((1.4, 1.6), (1.55, 2.6)), ((2.0, 1.6), (1.85, 2.6))]
    for (p, q) in figure:
        left.span((p[0], p[1], .03), (q[0], q[1], .03), .025, .01, INK)
    left.cyl(.18, .18, .02, 1.7, 3.95 + .15, .03, INK, sides=10, rx=math.pi / 2)
    left.cyl(.16, .16, .02, 1.7, 4.1, .035, PLASTER, sides=10, rx=math.pi / 2)
    left.box(.24, .3, .02, 2.15, 4.15, .035, (.92, .78, .40))                  # the lamp it holds up, painted
    for (u, y, w, h, c) in ((3.2, 3.0, 1.2, 1.6, (.34, .40, .58)), (3.4, 2.0, .8, .6, (.30, .44, .30)), (2.6, 4.2, .6, .5, (.34, .40, .58))):
        left.box(w, h, .01, u, y, .035, c)
    for (u0, u1) in ((.0, 3.8),):
        for uu in (u0, u0 + 1.9, u1):
            for vv in (.25, 1.15):
                left.box(.08, 3.6, .08, uu, 1.8, vv, WOOD3)
        for y in (1.8, 3.4):
            left.box(u1 - u0 + .2, .06, 1.1, (u0 + u1) / 2, y, .7, WOOD3)
        for vv in (.25, 1.15):
            left.span((u0, .2, vv), (u0 + 1.9, 1.7, vv), .05, .05, WOOD3)
    for k in range(3):
        x, z = left.p(1.0 + k * .9, .7)
        a.cyl(.1, .09, .16, x, 1.91, z, ((.34, .40, .58), (.30, .44, .30), (.92, .78, .40))[k], sides=7)
    x, z = left.p(3.2, .6)
    a.cyl(.07, .06, .16, x, 1.91, z, (.28, .22, .40), sides=6)
    for k in range(4):
        a.span((x + rng.uniform(-.03, .03), 1.95, z + rng.uniform(-.03, .03)), (x + rng.uniform(-.08, .08), 2.2, z + rng.uniform(-.08, .08)), .015, .015, WOOD3)
    # pews not yet set, sawhorses and a plank, a sheet over something, buckets
    for k in range(3):
        a.box(3.3, .14, .5, S - 1.2, .07 + k * .14, -4.6 + k * .02, PALE, ry=math.pi / 2 + k * .03)
    for z in (1.6, 3.2):
        for e in (-1, 1):
            a.span((S - 1.4 + e * .3, 0, z), (S - 1.4, .8, z), .06, .06, PALE2)
        a.box(.12, .08, .8, S - 1.4, .82, z, PALE2)
    a.box(.4, .06, 2.4, S - 1.4, .9, 2.4, PALE)
    a.box(.5, .01, .1, S - 1.35, .935, 2.6, (.60, .62, .66), ry=.3)
    a.rock(1.4, .9, 1.0, S - .9, .45, -1.6, (.60, .60, .58), jag=.12, sides=8)
    for k in range(3):
        a.cyl(.16, .14, .3, S - .5 - k * .4, .15, 5.2 + (k % 2) * .2, (.74, .72, .68) if k != 1 else PEWTER, sides=8)
    for (W, u) in ((right, -5.4), (right, 3.6), (left, 5.6)):
        sconce(W, u)
    a.finish(cam_at=(0, 2.2, 7.0), cam_look=(0, 1.6, -4), res=(640, 420), lens=22,
             extra_views=[('altar', (0, 1.7, -2.8), (0, 2.0, -7.6)), ('scaffold', (1.0, 2.0, 2.0), (-9.0, 2.4, -2.0))])


WHICH = {'drovers': drovers, 'lamplighters': lamplighters, 'ferriers': ferriers, 'shrine': shrine, 'chapel': chapel}
if __name__ == '__main__':
    for name in (sys.argv[1:] or list(WHICH)):
        WHICH[name]()
