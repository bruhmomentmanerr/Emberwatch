# The Moon Archive's fit-out (r154). The hall was a 20 x 16 m room holding a
# rug, two plain shelves, a table and a stone block with a glowing top. This
# is a library: walls of bookcases full to the cornice, a rolling ladder, two
# long reading tables with their benches, candles and open books, hanging
# lamps over them, a lectern and a celestial globe either side of the
# archive's instrument, and on the back wall a round window of moon-glass.
#
#   moon-archive        the furniture, candles and lamps (warm glow)
#   moon-archive-moon   the rose window and the instrument: a moon of pale
#                       glass in brass rings on a stone plinth (cool glow)
#
# Local frame (game axes): the room's middle at the origin, the door at
# +z (the front wall's inner face at z = 7.79), the side walls' inner faces
# at x = +-9.79, the back wall's at z = -7.79; y = 0 the floor. Both models
# are laid at the room's middle by the game (placeMoonArchive), which also
# lays the colliders from the same numbers (MOON_ARCHIVE in the game).
#
#   python tools/assets/moon-archive.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

WOOD = (.30, .19, .11)
WOOD2 = (.22, .14, .08)
WOOD3 = (.38, .25, .14)
IRON = (.12, .12, .14)
BRASS = (.62, .48, .22)
STONE = (.42, .40, .44)
PAGE = (.86, .81, .68)
WAX = (.88, .84, .72)
FLAME = (1.0, .76, .38, .06)
LAMP = (1.0, .80, .48, .1)
MOONGLASS = (.78, .82, 1.0, .12)
MOONGLASS2 = (.62, .66, .95, .2)
SPINES = [(.42, .12, .10), (.14, .28, .17), (.13, .19, .36), (.36, .22, .11), (.52, .38, .14),
          (.09, .08, .08), (.70, .63, .48), (.30, .10, .22), (.20, .30, .30)]

BACK = -7.79
SIDE = 9.79
SHELF_D = .5
SHELF_H = 4.6
BAY = 2.4
SHELVES = [.18, .9, 1.6, 2.3, 3.0, 3.7]          # shelf tops; the books stand on them

a = Asset('moon-archive', seed=1540)
m = Asset('moon-archive-moon', seed=1541)
rng = a.rng


def books(cx, cz, along, width, y, ry_axis):
    # A shelf of books: runs of two to four volumes of one binding, a gap now
    # and then, the odd one leaning. `along` is the unit vector the shelf runs
    # along (x or z), the books' spines face out from the wall.
    pos = -width / 2 + .04
    while pos < width / 2 - .1:
        run = rng.choice((2, 2, 3, 3, 4))
        w = rng.uniform(.06, .12) * run
        if pos + w > width / 2 - .04:
            break
        if rng.random() < .07:                    # a gap
            pos += rng.uniform(.08, .22)
            continue
        h = rng.uniform(.24, .46)
        d = rng.uniform(.26, .36)
        c = rng.choice(SPINES)
        mid = pos + w / 2
        x = cx + along[0] * mid
        z = cz + along[1] * mid
        lean = rng.uniform(-.12, .12) if rng.random() < .1 else 0
        if ry_axis == 'x':
            a.box(w, h, d, x, y + h / 2, z, c, rz=lean)
        else:
            a.box(d, h, w, x, y + h / 2, z, c, rx=lean)
        pos += w + rng.uniform(0, .015)


def bookcase(cx, cz, facing):
    # One bay, 2.4 m wide, its back to the wall. facing: 'z' for the back wall
    # (spines toward +z), 'x+' / 'x-' for the side walls (spines toward the
    # room's middle).
    if facing == 'z':
        along = (1, 0)
        a.box(BAY, SHELF_H, .05, cx, SHELF_H / 2, cz - SHELF_D / 2 + .025, WOOD2)          # back board
        for s in (-1, 1):
            a.box(.08, SHELF_H, SHELF_D, cx + s * (BAY / 2 - .04), SHELF_H / 2, cz, WOOD)   # sides
        a.box(BAY + .12, .16, SHELF_D + .08, cx, SHELF_H + .08, cz + .02, WOOD3)            # cornice
        for y in SHELVES:
            a.box(BAY - .12, .05, SHELF_D - .04, cx, y - .025, cz, WOOD)
            if y < SHELF_H - .3:
                books(cx, cz + .04, along, BAY - .2, y, 'x')
    else:
        sgn = 1 if facing == 'x+' else -1
        along = (0, 1)
        a.box(.05, SHELF_H, BAY, cx - sgn * (SHELF_D / 2 - .025), SHELF_H / 2, cz, WOOD2)
        for s in (-1, 1):
            a.box(SHELF_D, SHELF_H, .08, cx, SHELF_H / 2, cz + s * (BAY / 2 - .04), WOOD)
        a.box(SHELF_D + .08, .16, BAY + .12, cx + sgn * .02, SHELF_H + .08, cz, WOOD3)
        for y in SHELVES:
            a.box(SHELF_D - .04, .05, BAY - .12, cx, y - .025, cz, WOOD)
            if y < SHELF_H - .3:
                books(cx + sgn * .04, cz, along, BAY - .2, y, 'z')


# The back wall: three bays either side of the window, a map chest under it.
for x in (-8.4, -6.0, -3.6, 3.6, 6.0, 8.4):
    bookcase(x, BACK + SHELF_D / 2, 'z')
a.box(3.8, .95, .8, 0, .475, BACK + .42, WOOD)                                          # the map chest
for k in range(4):
    a.box(.9, .05, .02, -1.35 + k * .9, .55, BACK + .83, IRON)                           # its drawer pulls
for k in range(5):                                                                       # scrolls on it
    a.cyl(.07, .07, .9, -1.2 + k * .55, 1.02, BACK + .4, PAGE if k % 2 else WAX, sides=6, rz=math.pi / 2)
# The side walls: four bays each, the door end left clear.
for s, facing in ((-1, 'x+'), (1, 'x-')):
    for z in (-5.2, -2.8, -.4, 2.0):
        bookcase(s * (SIDE - SHELF_D / 2), z, facing)
# A rolling ladder on the back wall, on its rail.
a.box(7.2, .05, .05, -6.0, 4.3, BACK + .62, BRASS)
for dx in (-.25, .25):
    a.span((-6.6 + dx, 0, BACK + 1.45), (-6.6 + dx, 4.35, BACK + .66), .06, .06, WOOD3)
for k in range(1, 11):
    f = k / 11
    a.box(.5, .04, .07, -6.6, 4.35 * f, BACK + 1.45 - .79 * f, WOOD3)
# Two long reading tables down the room, benches either side, candles and
# open books on them, a lamp hanging over each.
for s in (-1, 1):
    tx, tz = s * 4.8, .8
    a.box(1.25, .08, 3.7, tx, .82, tz, WOOD3)                                             # the top
    for lx in (-1, 1):
        for lz in (-1, 1):
            a.box(.1, .78, .1, tx + lx * .5, .39, tz + lz * 1.6, WOOD)
    a.box(.9, .06, .06, tx, .25, tz, WOOD)
    for b in (-1, 1):                                                                     # benches
        bx = tx + b * .98
        a.box(.36, .06, 3.4, bx, .46, tz, WOOD)
        for lz in (-1, 1):
            a.box(.3, .43, .08, bx, .215, tz + lz * 1.5, WOOD)
    for cz in (-1.0, 1.1):                                                                # candles
        a.cyl(.07, .09, .05, tx + .2, .885, tz + cz, BRASS, sides=6)
        a.cyl(.035, .035, .2, tx + .2, 1.01, tz + cz, WAX, sides=5)
        a.cyl(.03, 0, .09, tx + .2, 1.155, tz + cz, FLAME, sides=4)
    for bz, ang in ((-.2, .1), (1.6, -.15)):                                              # open books
        a.box(.5, .03, .36, tx - .15, .875, tz + bz, PAGE, ry=ang)
        a.box(.52, .02, .38, tx - .15, .862, tz + bz, rng.choice(SPINES), ry=ang)
    for k in range(3):                                                                    # a stack
        a.box(.34 - k * .03, .07, .26, tx + .28, .895 + k * .07, tz - 1.65, rng.choice(SPINES), ry=k * .2)
    a.box(.03, 2.6, .03, tx, 5.7, tz, IRON)                                               # hanging lamp
    a.cyl(.42, .42, .04, tx, 4.38, tz, IRON, sides=8)
    for k in range(4):
        ang = k / 4 * math.tau
        a.span((tx, 5.0, tz), (tx + math.cos(ang) * .38, 4.4, tz + math.sin(ang) * .38), .02, .02, IRON)
        a.cyl(.05, .05, .14, tx + math.cos(ang) * .3, 4.47, tz + math.sin(ang) * .3, WAX, sides=4)
        a.cyl(.035, 0, .1, tx + math.cos(ang) * .3, 4.59, tz + math.sin(ang) * .3, FLAME, sides=4)
    a.box(.22, .22, .22, tx, 4.27, tz, LAMP)
# A lectern with the great register open on it, and a celestial globe.
a.box(.5, 1.0, .4, -2.3, .5, 2.6, WOOD, ry=-.25)
a.box(.62, .05, .5, -2.3, 1.12, 2.6, WOOD3, rx=-.35, ry=-.25)
a.box(.56, .03, .42, -2.3, 1.16, 2.62, PAGE, rx=-.35, ry=-.25)
a.cyl(.25, .3, .06, 2.3, .03, 2.6, WOOD, sides=6)
a.cyl(.04, .04, .9, 2.3, .48, 2.6, WOOD3, sides=5)
a.rock(.62, .62, .62, 2.3, 1.2, 2.6, (.20, .24, .40), jag=.02, sides=8, top_color=(.26, .30, .48))
a.tube([(2.3 + .38 * math.cos(t), 1.2 + .38 * math.sin(t), 2.6) for t in [k / 12 * math.tau for k in range(13)]],
       [.018] * 13, BRASS, sides=4, cap0=False, cap1=False)
a.finish(cam_at=(0, 3.2, 7.4), cam_look=(0, 1.8, -3), res=(640, 420), lens=24,
         extra_views=[('side', (7.5, 2.4, 6.5), (-3, 1.8, -4))])

# ---- the moon --------------------------------------------------------------------
# The round window: a disc of moon-glass in a stone ring, with lead tracery.
R, WY = 1.55, 4.5
m.cyl(R + .14, R + .14, .12, 0, WY, BACK + .07, STONE, sides=16, rx=math.pi / 2)
m.cyl(R, R, .04, 0, WY, BACK + .15, MOONGLASS, sides=16, rx=math.pi / 2)
for k in range(8):
    ang = k / 8 * math.tau
    m.span((0, WY, BACK + .19), (math.cos(ang) * R, WY + math.sin(ang) * R, BACK + .19), .04, .03, IRON)
m.tube([(math.cos(t) * R * .5, WY + math.sin(t) * R * .5, BACK + .19) for t in [k / 16 * math.tau for k in range(17)]],
       [.025] * 17, IRON, sides=4, cap0=False, cap1=False)
# The instrument: a plinth, a brass stand, two great rings crossed and one
# tilted about the moon, pale and lit from within.
OX, OZ = 0, 2.6
m.cyl(.62, .74, .25, OX, .125, OZ, STONE, sides=8)
m.cyl(.42, .5, .8, OX, .65, OZ, STONE, sides=8)
m.cyl(.55, .48, .12, OX, 1.11, OZ, STONE, sides=8)
m.cyl(.06, .09, .55, OX, 1.44, OZ, BRASS, sides=6)
m.rock(.82, .82, .82, OX, 2.12, OZ, MOONGLASS, jag=.03, sides=10, top_color=MOONGLASS2)


def ring(cx, cy, cz, r, tilt, spin, rad=.03):
    pts = []
    for k in range(25):
        t = k / 24 * math.tau
        x, y = math.cos(t) * r, math.sin(t) * r
        # turn the ring about x (tilt) and then about y (spin)
        y, z = y * math.cos(tilt), y * math.sin(tilt)
        x, z = x * math.cos(spin) + z * math.sin(spin), -x * math.sin(spin) + z * math.cos(spin)
        pts.append((cx + x, cy + y, cz + z))
    m.tube(pts, [rad] * 25, BRASS, sides=4, cap0=False, cap1=False)


ring(OX, 2.12, OZ, .66, 0, 0)
ring(OX, 2.12, OZ, .66, 0, math.pi / 2)
ring(OX, 2.12, OZ, .74, 1.1, .5, rad=.022)
m.finish(cam_at=(2.2, 2.6, 5.8), cam_look=(0, 2.4, -1.5), res=(520, 420), lens=28,
         extra_views=[('window', (0, 3.0, 1.0), (0, 4.3, BACK))])
