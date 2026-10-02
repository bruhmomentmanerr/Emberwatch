# The two other archive halls fitted out (r155), after the Moon Archive
# (r154). Both were the same 20 x 16 m room with a rug, a table or two and
# whatever the storeroom filler scattered round the walls.
#
#   scriptorium        the Eastwall Scriptorium — "ink-stained desks, tall
#                      ledgers, and the eastern wall's records": ledger cases
#                      on the back wall, pigeonholes of rolled records down
#                      the sides, two rows of slanted scribes' desks with
#                      inkwells, quills, pages and candles, one page
#                      unfinished; lamps over the rows (warm glow)
#   cold-assay         the Cold Assay — "they weigh things here that nobody
#                      will name": a great beam balance on a stone counter, a
#                      cabinet of small drawers, shelves of stoppered jars, a
#                      long table with something under a sheet, a strongbox,
#                      cold lamps (cool glow)
#   cold-assay-fire    its assay furnace and the crucibles by it (fire glow)
#
# Local frame as moon-archive.py: the room's middle at the origin, the door
# at +z (inner face z = 7.79), side walls' inner faces x = +-9.79, the back
# wall's z = -7.79, the floor y = 0. The game lays each at its room's middle
# (placeScriptorium, placeColdAssay) with colliders from the same numbers.
#
#   python tools/assets/archives.py [scriptorium|assay ...]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

WOOD = (.30, .19, .11)
WOOD2 = (.22, .14, .08)
WOOD3 = (.38, .25, .14)
IRON = (.12, .12, .14)
BRASS = (.62, .48, .22)
STONE = (.42, .40, .44)
STONE2 = (.33, .31, .35)
BRICK = (.38, .18, .12)
PAGE = (.86, .81, .68)
PAGE2 = (.78, .72, .58)
INK = (.05, .05, .08)
WAX = (.88, .84, .72)
CLOTH = (.62, .60, .56)
FLAME = (1.0, .76, .38, .06)
LAMP = (1.0, .80, .48, .1)
COLD = (.70, .86, 1.0, .1)
GLASS = (.45, .62, .70, .55)
FIRE = (1.0, .45, .15, .05)
EMBER = (.95, .30, .08, .25)
SOOT = (.13, .11, .10)
LEDGERS = [(.30, .16, .10), (.20, .13, .09), (.12, .10, .09), (.36, .26, .16), (.24, .20, .14), (.40, .12, .10)]

BACK = -7.79
SIDE = 9.79


def books(a, cx, cz, along, width, y, axis, palette, hmin, hmax, runs):
    # A shelf of books in runs of one binding, as moon-archive.py lays them.
    rng = a.rng
    pos = -width / 2 + .04
    while pos < width / 2 - .1:
        run = rng.choice(runs)
        w = rng.uniform(.07, .12) * run
        if pos + w > width / 2 - .04:
            break
        if rng.random() < .06:
            pos += rng.uniform(.08, .2)
            continue
        h, d, c = rng.uniform(hmin, hmax), rng.uniform(.28, .38), rng.choice(palette)
        mid = pos + w / 2
        x, z = cx + along[0] * mid, cz + along[1] * mid
        if axis == 'x':
            a.box(w, h, d, x, y + h / 2, z, c)
        else:
            a.box(d, h, w, x, y + h / 2, z, c)
        pos += w + rng.uniform(0, .015)


def ledger_case(a, cx, cz, bay=2.4, height=4.6, depth=.5):
    # A bay of tall ledgers against the back wall, spines toward +z.
    a.box(bay, height, .05, cx, height / 2, cz - depth / 2 + .025, WOOD2)
    for s in (-1, 1):
        a.box(.08, height, depth, cx + s * (bay / 2 - .04), height / 2, cz, WOOD)
    a.box(bay + .12, .16, depth + .08, cx, height + .08, cz + .02, WOOD3)
    for y in (.18, 1.08, 1.98, 2.88, 3.78):
        a.box(bay - .12, .05, depth - .04, cx, y - .025, cz, WOOD)
        if y < height - .5:
            books(a, cx, cz + .04, (1, 0), bay - .2, y, 'x', LEDGERS, .5, .72, (3, 4, 5))


def pigeonholes(a, cx, cz, sgn, bay=2.4, height=2.7, depth=.45, cols=6, rows=6):
    # A cabinet of pigeonholes against a side wall (sgn: which way it faces,
    # +1 toward +x), each hole with a rolled record or two showing their ends.
    rng = a.rng
    a.box(.05, height, bay, cx - sgn * (depth / 2 - .025), height / 2, cz, WOOD2)
    a.box(depth, .1, bay + .06, cx, height + .05, cz, WOOD3)
    a.box(depth, .3, bay, cx, .15, cz, WOOD)
    ch, cw = (height - .4) / rows, bay / cols
    for r in range(rows + 1):
        a.box(depth, .03, bay, cx, .3 + r * ch, cz, WOOD)
    for c in range(cols + 1):
        a.box(depth, height - .3, .03, cx, .3 + (height - .3) / 2, cz - bay / 2 + c * cw, WOOD)
    for r in range(rows):
        for c in range(cols):
            if rng.random() < .12:
                continue
            y0, z0 = .3 + r * ch, cz - bay / 2 + (c + .5) * cw
            for k in range(rng.choice((1, 2, 2, 3))):
                rr = rng.uniform(.045, .07)
                a.cyl(rr, rr, depth * .9, cx + sgn * .02, y0 + rr + .01 + (k % 2) * .09, z0 + (k - 1) * .1,
                      PAGE if rng.random() < .6 else PAGE2, sides=5, rz=math.pi / 2)


def hanging_lamp(a, x, z, glow, flame=FLAME):
    a.box(.03, 2.6, .03, x, 5.7, z, IRON)
    a.cyl(.42, .42, .04, x, 4.38, z, IRON, sides=8)
    for k in range(4):
        ang = k / 4 * math.tau
        a.span((x, 5.0, z), (x + math.cos(ang) * .38, 4.4, z + math.sin(ang) * .38), .02, .02, IRON)
        a.cyl(.05, .05, .14, x + math.cos(ang) * .3, 4.47, z + math.sin(ang) * .3, WAX, sides=4)
        a.cyl(.035, 0, .1, x + math.cos(ang) * .3, 4.59, z + math.sin(ang) * .3, flame, sides=4)
    a.box(.22, .22, .22, x, 4.27, z, glow)


# ---- the Eastwall Scriptorium ----------------------------------------------
DESKS = [(sx * 2.7, z) for sx in (-1, 1) for z in (-3.6, -.8, 2.0)]     # the desks' middles
PAGE_DESK = (-2.7, -.8)                                                 # the unfinished page


def scriptorium():
    a = Asset('scriptorium', seed=1550)
    for x in (-8.4, -6.0, -3.6, 3.6, 6.0, 8.4):
        ledger_case(a, x, BACK + .25)
    # the records cabinet between them: wider pigeonholes, the city's walls
    a.box(3.9, .1, .5, 0, 3.25, BACK + .27, WOOD3)
    rng = a.rng
    a.box(3.8, 3.2, .05, 0, 1.6, BACK + .03, WOOD2)
    for r in range(8):
        a.box(3.8, .03, .45, 0, .2 + r * .42, BACK + .25, WOOD)
    for c in range(9):
        a.box(.03, 3.0, .45, -1.9 + c * .475, 1.7, BACK + .25, WOOD)
    for r in range(7):
        for c in range(8):
            if rng.random() < .15:
                continue
            rr = rng.uniform(.05, .08)
            a.cyl(rr, rr, .4, -1.9 + (c + .5) * .475, .2 + r * .42 + rr + .02, BACK + .27, PAGE if rng.random() < .6 else PAGE2, sides=5, rx=math.pi / 2)
    for s in (-1, 1):
        for z in (-5.2, -2.8, -.4):
            pigeonholes(a, s * (SIDE - .23), z, -s)
    # the desks: a slanted top on a frame, a ledge for the ink, a stool
    for (x, z) in DESKS:
        for lx in (-1, 1):
            for lz in (-1, 1):
                a.box(.07, .9 + (.12 if lz > 0 else 0), .07, x + lx * .55, (.9 + (.12 if lz > 0 else 0)) / 2, z + lz * .3, WOOD)
        a.box(1.3, .05, .8, x, 1.0, z, WOOD3, rx=-.22)                       # the slope, rising away from the scribe
        a.box(1.3, .08, .14, x, 1.12, z - .42, WOOD)                         # the ledge
        a.cyl(.05, .06, .07, x + .4, 1.19, z - .42, INK, sides=6)            # the inkwell
        a.span((x + .4, 1.2, z - .42), (x + .48, 1.42, z - .3), .015, .015, PAGE)   # a quill
        a.box(.36, .01, .5, x - .15, 1.04, z + .02, PAGE, rx=-.22)          # the page
        a.cyl(.05, .07, .04, x - .5, 1.17, z - .42, BRASS, sides=6)          # a candle
        a.cyl(.03, .03, .16, x - .5, 1.27, z - .42, WAX, sides=5)
        a.cyl(.025, 0, .08, x - .5, 1.39, z - .42, FLAME, sides=4)
        a.cyl(.22, .22, .06, x, .58, z + .85, WOOD3, sides=8)                # the stool
        for k in range(3):
            ang = k / 3 * math.tau
            a.span((x + math.cos(ang) * .17, 0, z + .85 + math.sin(ang) * .17), (x + math.cos(ang) * .1, .56, z + .85 + math.sin(ang) * .1), .04, .04, WOOD)
    # the unfinished page: the quill lying across it, a blot
    px, pz = PAGE_DESK
    a.span((px - .25, 1.08, pz + .1), (px + .1, 1.06, pz - .05), .012, .012, PAGE2)
    a.box(.06, .012, .05, px - .05, 1.055, pz + .05, INK, rx=-.22)
    # a great ledger open on its stand by the door end of the aisle
    a.box(.55, 1.05, .45, 0, .525, 4.6, WOOD)
    a.box(.9, .05, .62, 0, 1.12, 4.6, WOOD3, rx=.3)
    a.box(.84, .04, .56, 0, 1.16, 4.62, PAGE, rx=.3)
    for x in (-2.7, 2.7):
        hanging_lamp(a, x, -.8, LAMP)
    a.finish(cam_at=(0, 3.0, 7.2), cam_look=(0, 1.6, -3), res=(640, 420), lens=24,
             extra_views=[('desk', (-1.4, 1.9, .9), (-2.7, 1.0, -.8))])


# ---- the Cold Assay ----------------------------------------------------------
JARS_Z = (.6, 3.0)
BALANCE = (0, -6.3)
TABLE = (0, .6)


def assay():
    a = Asset('cold-assay', seed=1551)
    f = Asset('cold-assay-fire', seed=1552)
    rng = a.rng
    # the great balance on its stone counter against the back wall
    bx, bz = BALANCE
    a.box(4.4, 1.0, 1.1, bx, .5, bz, STONE2)
    a.box(4.6, .12, 1.25, bx, 1.06, bz, STONE)
    a.cyl(.1, .14, 1.9, bx, 1.12 + .95, bz, BRASS, sides=8)                 # the pillar
    a.cyl(.18, .18, .1, bx, 1.17, bz, BRASS, sides=8)
    a.box(3.0, .08, .08, bx, 3.05, bz, BRASS, rz=.06)                       # the beam, a little out of true
    a.cyl(.05, 0, .36, bx, 3.32, bz, BRASS, sides=4)                        # the pointer
    for s in (-1, 1):
        ex, ey = bx + s * 1.45, 3.05 + s * .09
        py = ey - 1.05
        for k in range(3):
            ang = k / 3 * math.tau + .5
            a.span((ex, ey, bz), (ex + math.cos(ang) * .32, py, bz + math.sin(ang) * .32), .012, .012, IRON)
        a.cyl(.36, .3, .06, ex, py, bz, BRASS, sides=10)                     # the pans
    a.rock(.3, .22, .26, bx + 1.45, 2.15 - .09 + .05, bz, (.16, .14, .16), jag=.3, sides=5)   # what is being weighed
    y = 2.03                                                                 # the weights, stacked in the other pan
    for r, h in ((.16, .2), (.13, .16), (.1, .13), (.08, .1), (.06, .08)):
        a.cyl(r, r, h, bx - 1.45, y + h / 2, bz, BRASS, sides=8)
        y += h
    for k in range(6):                                                       # spare weights on the counter
        r = .05 + k * .025
        a.cyl(r, r, r * 1.2, bx + 1.2 + k * .15 - .5, 1.12 + r * .6, bz + .35, BRASS, sides=8)
    # a cabinet of small drawers, two bays on the right wall
    for z in (-5.0, -2.6):
        cx = SIDE - .3
        a.box(.58, 3.0, 2.3, cx, 1.5, z, WOOD)
        for r in range(8):
            for c in range(6):
                dy, dz = .25 + r * .34, z - 1.0 + c * .4
                a.box(.04, .3, .36, cx - .3, dy + .15, dz, WOOD3)
                a.box(.04, .04, .08, cx - .33, dy + .17, dz, BRASS)
        a.box(.66, .1, 2.38, cx, 3.05, z, WOOD2)
    # shelves of stoppered jars, two bays further down the right wall
    for z in JARS_Z:
        cx = SIDE - .25
        a.box(.05, 2.8, 2.2, cx + .22, 1.4, z, WOOD2)
        for s in (-1, 1):
            a.box(.48, 2.8, .06, cx, 1.4, z + s * 1.07, WOOD)
        for y in (.3, 1.0, 1.7, 2.4):
            a.box(.46, .04, 2.1, cx, y, z, WOOD)
            zz = z - .95
            while zz < z + .9:
                r = rng.uniform(.07, .12)
                h = rng.uniform(.18, .34)
                if rng.random() < .85:
                    a.cyl(r, r * .9, h, cx, y + h / 2 + .02, zz + r, GLASS if rng.random() < .3 else (.30, .38, .40), sides=6)
                    a.cyl(r * .45, r * .45, .05, cx, y + h + .045, zz + r, (.45, .33, .2), sides=5)
                zz += 2 * r + rng.uniform(.03, .1)
    # the long table, and on it something under a sheet
    tx, tz = TABLE
    a.box(1.5, .08, 4.2, tx, .86, tz, WOOD3)
    for lx in (-1, 1):
        for lz in (-1, 1):
            a.box(.12, .82, .12, tx + lx * .6, .41, tz + lz * 1.9, WOOD)
    a.rock(1.1, .55, 1.6, tx, 1.15, tz - .4, CLOTH, jag=.18, sides=7, top_color=(.70, .68, .64))
    a.box(.5, .05, .38, tx + .3, .925, tz + 1.4, PAGE)                       # the assay book
    a.box(.52, .03, .4, tx + .3, .9, tz + 1.4, LEDGERS[2])
    a.cyl(.04, .05, .06, tx - .35, .93, tz + 1.5, INK, sides=6)
    # a strongbox, iron-bound, against the left wall
    a.box(1.1, .7, .7, -SIDE + .55, .35, 3.4, WOOD2)
    for dz in (-.3, 0, .3):
        a.box(1.14, .74, .05, -SIDE + .55, .35, 3.4 + dz, IRON)
    # cold lamps hung down the room
    for z in (-3.5, 1.5):
        hanging_lamp(a, 0, z, COLD, flame=COLD)
    a.finish(cam_at=(0, 3.0, 7.2), cam_look=(0, 1.6, -3), res=(640, 420), lens=24,
             extra_views=[('balance', (1.8, 2.4, -2.6), (0, 2.2, -6.3))])
    # the furnace on the left wall: brick, a glowing mouth, a flue to the
    # ceiling; a bench by it with crucibles, tongs and a cupel tray
    fx, fz = -SIDE + .85, -4.2
    f.box(1.6, 1.5, 1.7, fx, .75, fz, BRICK)
    f.box(1.7, .12, 1.8, fx, 1.56, fz, STONE)
    f.box(.06, .5, .8, fx + .81, .7, fz, FIRE)                               # the mouth
    f.box(.06, .2, .9, fx + .81, .38, fz, EMBER)
    f.cyl(.32, .26, 5.4, fx - .1, 1.62 + 2.7, fz, SOOT, sides=6)             # the flue, black with soot
    f.box(.6, .9, 2.6, -SIDE + .35, .45, -1.3, WOOD)                         # the bench
    f.box(.7, .06, 2.7, -SIDE + .4, .92, -1.3, STONE)
    for k in range(4):
        f.cyl(.09, .06, .14, -SIDE + .45, 1.02, -2.2 + k * .45, (.55, .52, .5), sides=6)
        if k % 2 == 0:
            f.cyl(.05, .05, .02, -SIDE + .45, 1.1, -2.2 + k * .45, EMBER, sides=6)
    f.span((-SIDE + .3, .96, -.3), (-SIDE + .55, .99, .35), .025, .025, IRON)    # tongs
    f.span((-SIDE + .35, .96, -.25), (-SIDE + .62, .98, .32), .025, .025, IRON)
    f.finish(cam_at=(-4.0, 2.2, 1.5), cam_look=(-8.5, 1.0, -3.0), res=(520, 420), lens=28)


WHICH = {'scriptorium': scriptorium, 'assay': assay}
for name in (sys.argv[1:] or list(WHICH)):
    WHICH[name]()
