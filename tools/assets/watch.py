# The two guild halls fitted out (r156), after the archives (r154, r155).
# Both were the same 20 x 16 m room: a rug, a table or a bench, a shelf, a
# banner, and the storeroom filler's chests and barrels round the walls.
#
#   northwatch       the Northwatch Guild — "a planning table, spare gear,
#                    and a room for the watch": the planning table under a
#                    map of the city, racks of spears and shields on the back
#                    wall, three armour stands, bunks for the watch with a
#                    stove between them, a notice board by the door, a
#                    ladder to the tower's hatch, a lamp over the table
#                    (warm glow)
#   westwall-refuge  the Westwall Refuge — "a workbench, ward maps, and a
#                    watchful repair corner": a long workbench under a tool
#                    board, the ward maps on their boards, a repair corner
#                    with an anvil, a grindstone and the broken gear waiting
#                    for it, cots for whoever needs the refuge, a brazier
#                    (warm glow)
#
# Local frame as moon-archive.py: the room's middle at the origin, the door
# at +z (inner face z = 7.79), side walls' inner faces x = +-9.79, the back
# wall's z = -7.79, the floor y = 0. The game lays each at its room's middle
# (placeNorthwatch, placeWestwallRefuge) with colliders from these numbers.
#
#   python tools/assets/watch.py [northwatch|refuge ...]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

WOOD = (.30, .19, .11)
WOOD2 = (.22, .14, .08)
WOOD3 = (.38, .25, .14)
IRON = (.12, .12, .14)
STEEL = (.34, .35, .38)
BRASS = (.62, .48, .22)
STONE = (.42, .40, .44)
PAGE = (.80, .74, .58)
INK = (.10, .09, .10)
WAX = (.88, .84, .72)
WOOL = (.30, .28, .34)
WOOL2 = (.42, .16, .14)
LEATHER = (.36, .20, .10)
WATCH = (.16, .22, .42)                 # the watch's blue
FLAME = (1.0, .76, .38, .06)
LAMP = (1.0, .80, .48, .1)
COALS = (1.0, .42, .14, .45)

BACK = -7.79
SIDE = 9.79


def hanging_lamp(a, x, z):
    a.box(.03, 2.6, .03, x, 5.7, z, IRON)
    a.cyl(.42, .42, .04, x, 4.38, z, IRON, sides=8)
    for k in range(4):
        ang = k / 4 * math.tau
        a.span((x, 5.0, z), (x + math.cos(ang) * .38, 4.4, z + math.sin(ang) * .38), .02, .02, IRON)
        a.cyl(.05, .05, .14, x + math.cos(ang) * .3, 4.47, z + math.sin(ang) * .3, WAX, sides=4)
        a.cyl(.035, 0, .1, x + math.cos(ang) * .3, 4.59, z + math.sin(ang) * .3, FLAME, sides=4)
    a.box(.22, .22, .22, x, 4.27, z, LAMP)


def sconce(a, x, z, facing):
    # A candle in an iron sconce on a side wall (facing +1: the wall at -x).
    a.box(.04, .3, .14, x, 2.4, z, IRON)
    a.span((x, 2.3, z), (x + facing * .25, 2.45, z), .03, .03, IRON)
    a.cyl(.07, .05, .05, x + facing * .27, 2.47, z, IRON, sides=6)
    a.cyl(.035, .035, .16, x + facing * .27, 2.58, z, WAX, sides=5)
    a.cyl(.03, 0, .1, x + facing * .27, 2.71, z, FLAME, sides=4)


def map_board(a, x, z, facing, w=1.7, h=1.3):
    # A ward map on a board, hung on a side wall.
    rng = a.rng
    a.box(.06, h, w, x, 2.2, z, WOOD)
    a.box(.02, h - .2, w - .2, x + facing * .04, 2.2, z, PAGE)
    for j in range(6):
        a.box(.01, .015, rng.uniform(.3, 1.2), x + facing * .05, 2.2 + rng.uniform(-.45, .45), z + rng.uniform(-.4, .4), INK, rx=rng.uniform(-.8, .8))


def crate(a, x, z, s, ry=0.0, y=0.0):
    a.box(s, s, s, x, y + s / 2, z, WOOD3, ry=ry)
    a.box(s + .02, .06, s + .02, x, y + s * .8, z, WOOD2, ry=ry)
    a.box(s + .02, .06, s + .02, x, y + s * .2, z, WOOD2, ry=ry)


def sack(a, x, z, ry=0.0):
    a.rock(.5, .55, .4, x, .27, z, (.52, .44, .30), jag=.15, sides=6, ry=ry)
    a.cyl(.07, .04, .12, x, .58, z, (.40, .33, .22), sides=5)


def table(a, x, z, w, d, top=WOOD3):
    a.box(w, .1, d, x, .86, z, top)
    for lx in (-1, 1):
        for lz in (-1, 1):
            a.box(.12, .82, .12, x + lx * (w / 2 - .15), .41, z + lz * (d / 2 - .15), WOOD)


def city_map(a, x, z, w, d, y):
    # The map on the planning table: parchment, the walls as rings, the four
    # avenues out to the gates, the river, a few wards blocked in, markers.
    rng = a.rng
    a.box(w, .012, d, x, y, z, PAGE)
    r0 = min(w, d) * .44
    for frac in (1.0, .66):
        n = 24
        pts = [(x + math.cos(k / n * math.tau) * r0 * frac, y + .012, z + math.sin(k / n * math.tau) * r0 * frac * d / w * 1.0) for k in range(n + 1)]
        a.tube(pts, [.012] * (n + 1), INK, sides=3, cap0=False, cap1=False)
    for ang in (0, math.pi / 2, math.pi, 3 * math.pi / 2):
        a.span((x, y + .012, z), (x + math.cos(ang) * r0 * 1.05, y + .012, z + math.sin(ang) * r0 * 1.05 * d / w), .02, .004, INK)
    for k in range(14):
        ang, rr = rng.uniform(0, math.tau), rng.uniform(.2, .9) * r0
        a.box(rng.uniform(.06, .14), .006, rng.uniform(.05, .12), x + math.cos(ang) * rr, y + .01, z + math.sin(ang) * rr * d / w, (.55, .47, .34))
    for k in range(7):                                              # the markers
        ang, rr = rng.uniform(0, math.tau), rng.uniform(.3, 1.0) * r0
        c = WATCH if k % 3 else WOOL2
        a.cyl(.03, .045, .09, x + math.cos(ang) * rr, y + .05, z + math.sin(ang) * rr * d / w, c, sides=5)


def spear_rack(a, cx, cz, n=7, length=2.4):
    # Against the back wall, spears standing in a rail, points up.
    a.box(length, .1, .3, cx, .15, cz, WOOD)
    a.box(length, .08, .1, cx, 1.5, cz - .08, WOOD)
    for s in (-1, 1):
        a.box(.1, 1.6, .3, cx + s * (length / 2 - .05), .8, cz, WOOD2)
    for k in range(n):
        x = cx - length / 2 + .2 + k * (length - .4) / (n - 1)
        a.cyl(.025, .025, 2.6, x, 1.4, cz - .02, WOOD3, sides=4)
        a.cyl(.05, 0, .28, x, 2.84, cz - .02, STEEL, sides=4)


def shield(a, x, y, z, facing, r=.38, color=WATCH):
    # A round shield hung on a wall; facing is the wall's outward axis.
    if facing == 'z':
        a.cyl(r, r, .05, x, y, z, color, sides=12, rx=math.pi / 2)
        a.cyl(r * .3, r * .2, .08, x, y, z + .05, STEEL, sides=8, rx=math.pi / 2)
        a.cyl(r + .03, r + .03, .03, x, y, z - .005, IRON, sides=12, rx=math.pi / 2)
    else:
        sgn = 1 if facing == 'x+' else -1
        a.cyl(r, r, .05, x, y, z, color, sides=12, rz=math.pi / 2)
        a.cyl(r * .3, r * .2, .08, x + sgn * .05, y, z, STEEL, sides=8, rz=-sgn * math.pi / 2)


def armour_stand(a, x, z, ry=0.0):
    a.cyl(.28, .3, .08, x, .04, z, WOOD, sides=6)
    a.cyl(.04, .04, 1.5, x, .8, z, WOOD2, sides=4)
    a.box(.7, .06, .06, x, 1.48, z, WOOD2, ry=ry)                         # the shoulders' bar
    a.box(.52, .62, .3, x, 1.2, z, STEEL, ry=ry)                          # the cuirass
    a.box(.56, .14, .32, x, .86, z, LEATHER, ry=ry)                       # the belt and tassets
    a.cyl(.15, .13, .26, x, 1.68, z, STEEL, sides=8)                      # the helm
    a.cyl(.21, .21, .03, x, 1.56, z, STEEL, sides=10)


def bunk(a, x, z, sgn):
    # A two-tier bunk against a side wall (sgn: which way it faces), its
    # long side along z.
    for lx in (0, 1):
        for lz in (-1, 1):
            a.box(.08, 1.9, .08, x - sgn * lx * .82, .95, z + lz * 1.0, WOOD)
    for y in (.45, 1.35):
        a.box(.86, .08, 2.1, x - sgn * .41, y, z, WOOD3)
        a.box(.8, .12, 1.95, x - sgn * .41, y + .1, z, WOOL)                # the blanket
        a.box(.5, .1, .3, x - sgn * .41, y + .2, z - .78, PAGE)              # the bolster
    a.box(.04, .04, 2.1, x - sgn * .82, 1.62, z, WOOD)                        # the top rail


def stove(a, x, z):
    a.box(.7, .8, .7, x, .4, z, IRON)
    a.box(.62, .22, .04, x, .45, z + .36, COALS)                              # its door ajar
    a.cyl(.08, .08, 5.9, x, .8 + 2.95, z - .2, IRON, sides=6)                 # the pipe to the roof
    a.cyl(.13, .11, .2, x + .15, .9, z, IRON, sides=6)                        # the kettle


def notice_board(a, x, z, facing_sign):
    rng = a.rng
    a.box(.06, 1.2, 1.6, x, 1.6, z, WOOD)
    for k in range(7):
        a.box(.02, rng.uniform(.18, .32), rng.uniform(.16, .26), x + facing_sign * .04, 1.25 + rng.uniform(0, .7), z + rng.uniform(-.6, .6), PAGE if k % 3 else (.70, .62, .46), rx=rng.uniform(-.1, .1))


def northwatch():
    a = Asset('northwatch', seed=1560)
    rng = a.rng
    # the planning table, the map on it, its candles and dividers
    table(a, 0, .6, 4.6, 2.5)
    city_map(a, 0, .6, 4.0, 2.1, .92)
    for (cx, cz) in ((-1.9, -.4), (1.9, 1.6)):
        a.cyl(.05, .07, .04, cx, .93, cz, BRASS, sides=6)
        a.cyl(.035, .035, .18, cx, 1.04, cz, WAX, sides=5)
        a.cyl(.025, 0, .08, cx, 1.17, cz, FLAME, sides=4)
    a.span((1.2, .93, -.2), (1.45, .93, .15), .012, .012, BRASS)
    a.span((1.2, .93, -.2), (1.6, .93, -.05), .012, .012, BRASS)
    for s in (-1, 1):                                                         # benches either side
        a.box(4.0, .08, .4, 0, .46, .6 + s * 1.65, WOOD)
        for lx in (-1, 1):
            a.box(.08, .44, .34, lx * 1.8, .22, .6 + s * 1.65, WOOD)
    hanging_lamp(a, 0, .6)
    # the back wall: spear racks either side, shields above, the banner
    for cx in (-6.0, 6.0):
        spear_rack(a, cx, BACK + .2)
        for k in range(3):
            shield(a, cx - 1.0 + k * 1.0, 3.5, BACK + .06, 'z', color=WATCH if k != 1 else WOOL2)
    a.box(1.6, 3.2, .04, 0, 3.6, BACK + .04, WATCH)                          # the watch's banner
    a.box(1.8, .08, .08, 0, 5.25, BACK + .08, WOOD2)
    for k in range(5):                                                        # its eye: a pale ring
        ang = k / 5 * math.tau
        a.box(.18, .18, .02, math.cos(ang) * .38, 3.9 + math.sin(ang) * .38, BACK + .07, PAGE)
    a.cyl(.12, .12, .02, 0, 3.9, BACK + .07, PAGE, sides=8, rx=math.pi / 2)
    a.box(1.4, .9, .55, 0, .45, BACK + .4, WOOD2)                            # a chest of spare gear under it
    for dx in (-.5, 0, .5):
        a.box(.05, .92, .57, dx, .45, BACK + .4, IRON)
    # the left wall: three armour stands, a rack of cloaks
    for z in (-5.0, -3.2, -1.4):
        armour_stand(a, -SIDE + .7, z, ry=math.pi / 2)
    a.box(.1, .1, 2.6, -SIDE + .12, 2.2, 1.6, WOOD2)                          # the peg rail
    for k in range(5):
        z = .5 + k * .55
        a.box(.06, 1.2, .42, -SIDE + .3, 1.55, z, WATCH if k % 2 else WOOL, rz=.05)
    # the right wall: bunks for the watch, a stove between them
    for z in (-5.2, 1.8):
        bunk(a, SIDE - .05, z, -1)
    stove(a, SIDE - .7, -1.7)
    # a notice board by the door; a ladder to the tower's hatch above the
    # front-left corner, where the tower stands on the roof
    notice_board(a, SIDE - .05, 5.4, -1)
    for dx in (-.25, .25):
        a.box(.07, 7.0, .07, -7.6 + dx, 3.5, 6.6, WOOD3)
    for k in range(1, 18):
        a.box(.5, .05, .06, -7.6, k * .4, 6.6, WOOD3)
    a.box(1.2, .08, 1.2, -7.6, 6.96, 6.0, WOOD2)                              # the hatch
    # (more) a ward map on the right wall, a bow rack and an arrow barrel on
    # the left, footlockers under the bunks, sconces down both walls
    map_board(a, SIDE - .05, 3.6, -1, w=2.2, h=1.6)
    a.box(.1, .1, 1.8, -SIDE + .12, 2.4, 4.2, WOOD2)                         # the bow rack's pegs
    for k in range(4):
        z = 3.5 + k * .45
        pts = [(-SIDE + .2, 2.4 + .7 * math.cos(t), z + .18 * math.sin(t)) for t in [math.pi * (-.5 + j / 8) for j in range(9)]]
        a.tube(pts, [.02] * 9, WOOD3, sides=3, cap0=False, cap1=False)
        a.box(.01, 1.4, .01, -SIDE + .2, 2.4, z, PAGE)
    a.cyl(.3, .32, .8, -SIDE + .55, .4, 5.4, WOOD2, sides=8)                 # the arrow barrel
    for k in range(9):
        ang = k / 9 * math.tau
        a.cyl(.012, .012, .7, -SIDE + .55 + math.cos(ang) * .15, 1.05, 5.4 + math.sin(ang) * .15, WOOD3, sides=3, rz=math.cos(ang) * .12, rx=math.sin(ang) * .12)
    for z in (-5.2, 1.8):
        a.box(.6, .4, .9, SIDE - .5, .2, z + .45, WOOD2)                     # footlockers
    for s in (-1, 1):
        for z in (-4.2, -.2, 3.0):
            if s > 0 and z == 3.0:
                continue
            sconce(a, s * (SIDE - .03), z, -s)
    a.finish(cam_at=(0, 3.0, 7.2), cam_look=(0, 1.6, -3), res=(640, 420), lens=24,
             extra_views=[('table', (2.6, 2.4, 3.6), (0, .9, .6))])


def refuge():
    a = Asset('westwall-refuge', seed=1561)
    rng = a.rng
    # the workbench along the back wall, the tool board above it
    a.box(7.0, .12, 1.0, -3.0, .9, BACK + .6, WOOD3)
    for lx in (-3.3, -1.1, 1.1, 3.3):
        a.box(.14, .86, .9, -3.0 + lx, .43, BACK + .6, WOOD)
    a.box(6.8, .06, .8, -3.0, .3, BACK + .6, WOOD2)                          # its shelf
    a.box(6.8, 1.6, .05, -3.0, 2.1, BACK + .04, WOOD2)                       # the tool board
    tools = [('hammer', -6.0), ('saw', -5.0), ('tongs', -4.0), ('hammer', -3.1), ('rasp', -2.3), ('saw', -1.4), ('tongs', -.5)]
    for kind, x in tools:
        if kind == 'hammer':
            a.box(.05, .5, .03, x, 2.0, BACK + .09, WOOD3)
            a.box(.18, .07, .06, x, 2.27, BACK + .1, IRON)
        elif kind == 'saw':
            a.box(.5, .14, .01, x, 2.2, BACK + .09, STEEL)
            a.box(.1, .16, .04, x - .3, 2.2, BACK + .1, WOOD3)
        elif kind == 'tongs':
            a.span((x - .06, 1.7, BACK + .09), (x + .02, 2.4, BACK + .09), .03, .02, IRON)
            a.span((x + .06, 1.7, BACK + .09), (x - .02, 2.4, BACK + .09), .03, .02, IRON)
        else:
            a.box(.05, .55, .02, x, 2.0, BACK + .09, STEEL)
    a.box(.24, .3, .24, -.4, 1.11, BACK + .5, IRON)                          # the vise
    for k in range(4):                                                        # work on the bench
        a.box(rng.uniform(.2, .5), .05, rng.uniform(.15, .3), -5.6 + k * 1.3, .985, BACK + .6, (.30, .30, .33) if k % 2 else WOOD3, ry=rng.uniform(-.4, .4))
    hanging_lamp(a, -3.0, BACK + 1.6)
    # the ward maps on boards, on the back wall's other half
    for k, x in enumerate((2.6, 4.6, 6.6)):
        a.box(1.7, 1.3, .06, x, 2.2, BACK + .05, WOOD)
        a.box(1.5, 1.1, .02, x, 2.2, BACK + .09, PAGE)
        for j in range(5):
            a.box(rng.uniform(.3, 1.2), .015, .01, x + rng.uniform(-.4, .4), 2.2 + rng.uniform(-.4, .4), BACK + .1, INK, rz=rng.uniform(-.8, .8))
        a.cyl(.02, .02, .02, x - .6, 2.65, BACK + .1, WOOL2, sides=4, rx=math.pi / 2)
    a.box(1.6, .9, .7, 4.6, .45, BACK + .45, WOOD2)                          # the map chest under them
    # the repair corner, right wall: an anvil on its block, a grindstone,
    # the broken gear waiting, a water butt
    ax, az = SIDE - 1.6, -5.2
    a.cyl(.32, .36, .55, ax, .275, az, WOOD2, sides=8)
    a.box(.8, .22, .32, ax, .66, az, IRON)
    a.box(.32, .3, .26, ax, .45, az, IRON)
    a.cyl(0, .14, .35, ax + .55, .7, az, IRON, sides=4, rz=-math.pi / 2)     # the horn
    gx, gz = SIDE - 1.2, -2.6
    a.box(.9, .5, .5, gx, .25, gz, WOOD)
    a.cyl(.42, .42, .14, gx, .9, gz, STONE, sides=12, rz=math.pi / 2)         # the stone, on edge
    a.span((gx + .45, .4, gz), (gx + .7, .9, gz), .05, .05, WOOD3)
    for k in range(4):                                                        # broken spears leaning
        a.span((SIDE - .2, 0, -.9 + k * .22), (SIDE - .55, 1.8 - k * .2, -.85 + k * .22), .04, .04, WOOD3)
    for k in range(3):                                                        # dented shields stacked
        a.cyl(.36, .36, .05, SIDE - .35, .35 + k * .02, .4 + k * .15, (.20, .26, .44) if k != 1 else (.40, .16, .13), sides=10, rz=math.pi / 2 - .3)
    a.cyl(.36, .4, .9, SIDE - .6, .45, 1.6, WOOD2, sides=10)                  # the water butt
    a.cyl(.38, .38, .03, SIDE - .6, .91, 1.6, (.18, .26, .32), sides=10)
    # cots along the left wall, a blanket on each
    for z in (-5.4, -3.4, -1.4, .6):
        cx = -SIDE + .55
        a.box(.85, .1, 2.0, cx, .45, z + .4, WOOD3)
        for lz in (-1, 1):
            for lx in (-1, 1):
                a.box(.07, .4, .07, cx + lx * .36, .2, z + .4 + lz * .9, WOOD)
        a.box(.78, .1, 1.5, cx, .55, z + .6, rng.choice((WOOL, WOOL2, (.32, .30, .22))))
        a.box(.5, .1, .3, cx, .57, z - .4, PAGE)
    # a table with a lamp by the door, and a brazier in the middle of the room
    table(a, -4.0, 4.4, 1.8, 1.0)
    a.cyl(.06, .08, .3, -4.0, 1.06, 4.4, IRON, sides=6)
    a.box(.14, .16, .14, -4.0, 1.28, 4.4, LAMP)
    a.cyl(.45, .3, .35, 0, .7, .4, IRON, sides=8)
    a.cyl(.42, .42, .06, 0, .86, .4, COALS, sides=8)
    for k in range(3):
        ang = k / 3 * math.tau
        a.span((math.cos(ang) * .3, .55, .4 + math.sin(ang) * .3), (math.cos(ang) * .45, 0, .4 + math.sin(ang) * .45), .05, .05, IRON)
    # (more) benches round the brazier, firewood stacked by it
    for ang in (0, 2.1, 4.2):
        bx, bz = math.cos(ang) * 1.7, .4 + math.sin(ang) * 1.7
        a.box(1.4, .08, .36, bx, .45, bz, WOOD, ry=-ang + math.pi / 2)
        for s in (-1, 1):
            a.box(.3, .43, .08, bx + math.cos(-ang + math.pi / 2) * s * .55, .215, bz - math.sin(-ang + math.pi / 2) * s * .55, WOOD, ry=-ang + math.pi / 2)
    for k in range(9):
        a.cyl(.07, .07, .9, 1.4 + (k % 3) * .15, .08 + (k // 3) * .13, -1.6, WOOD3 if k % 2 else WOOD, sides=5, rx=math.pi / 2)
    # provisions stacked by the door on the right; a shelf of blankets over
    # the cots; herbs hung to dry from the beam; sconces down both walls
    crate(a, SIDE - .6, 4.6, .8, ry=.1)
    crate(a, SIDE - .65, 4.65, .6, ry=.4, y=.8)
    crate(a, SIDE - .6, 5.6, .7, ry=-.2)
    for (sx, sz, r) in ((-1.5, 4.0, .3), (-1.2, 5.2, -.4), (-2.1, 5.9, 1.1)):
        sack(a, SIDE + sx, sz, ry=r)
    a.box(.4, .05, 7.6, -SIDE + .22, 2.2, -2.2, WOOD)
    for k in range(10):
        a.box(.34, .22, .5, -SIDE + .22, 2.34 + (k % 2) * .03, -5.6 + k * .75, rng.choice((WOOL, WOOL2, (.32, .30, .22))))
    a.box(5.0, .04, .04, -3.0, 4.2, -3.0, WOOD2)
    for k in range(9):
        a.box(.02, .4, .02, -5.2 + k * .55, 4.0, -3.0, (.30, .26, .14))
        a.rock(.18, .3, .18, -5.2 + k * .55, 3.72, -3.0, (.30, .40, .22), jag=.3, sides=5)
    for s in (-1, 1):
        for z in (-4.2, -.2, 3.0):
            sconce(a, s * (SIDE - .03), z, -s)
    a.finish(cam_at=(0, 3.0, 7.2), cam_look=(0, 1.6, -3), res=(640, 420), lens=24,
             extra_views=[('corner', (5.0, 2.2, 1.0), (9.0, 1.0, -4.0))])


WHICH = {'northwatch': northwatch, 'refuge': refuge}
for name in (sys.argv[1:] or list(WHICH)):
    WHICH[name]()
