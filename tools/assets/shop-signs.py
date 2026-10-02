# Hanging shop signs (r147): a wrought-iron bracket out from the wall with the
# trade hung from it as a thing, not a painted board — the pretzel, the
# cask, the candles, the shears, the key, the horseshoe, the book, the
# bottle. Until r147 every shop's sign was a plain board in the house's
# accent colour on a wooden arm: from the street, a coloured card.
#
#   shop-sign-baker       a pretzel
#   shop-sign-grocer      a cask
#   shop-sign-chandler    three candles on a shelf, lit
#   shop-sign-draper      open shears
#   shop-sign-ironmonger  a gilded key
#   shop-sign-saddler     a horseshoe
#   shop-sign-bookseller  an open book
#   shop-sign-apothecary  a bottle of green glass, lit
#
# Local frame (game axes): the wall is the plane z=0, the bracket runs out
# along +z at y=0 (the game hangs it at 3.1 m), and the emblem hangs below
# it on rods, broadside to +-x so it is read by someone walking along the
# street. Lit parts carry alpha < 1 (placeLandmark glow).
#
#   python tools/assets/shop-signs.py [trade ...]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

IRON = (.14, .14, .16)
GILT = (.78, .60, .24)
BREAD = (.70, .43, .17)
WOOD = (.44, .29, .15)
WAX = (.90, .86, .74)
FLAME = (1.0, .78, .40, .08)
STEEL = (.58, .60, .65)
LEATHER = (.45, .19, .12)
PAGE = (.88, .84, .72)
GLASS = (.35, .85, .55, .3)
CORK = (.52, .38, .22)
CZ = .76                     # the emblem's centre, out from the wall


def ring(a, cy, cz, r, rad, color, n=10, sides=4):
    pts = [(0, cy + r * math.sin(k / n * math.tau), cz + r * math.cos(k / n * math.tau)) for k in range(n + 1)]
    a.tube(pts, [rad] * (n + 1), color, sides=sides, ref=(1, 0, 0), cap0=False, cap1=False)


def bracket(a):
    a.box(.07, .52, .04, 0, -.17, .02, IRON)                           # wall plate
    a.span((0, 0, .03), (0, 0, 1.18), .05, .05, IRON)                  # the bar
    a.span((0, -.42, .04), (0, -.03, .66), .035, .035, IRON)           # the brace
    ring(a, -.13, .3, .11, .018, IRON)                                 # a scroll between them
    a.cyl(.035, 0, .1, 0, 0, 1.23, IRON, sides=6, rx=math.pi / 2)     # a spike at the end


# Each emblem is built round (cy, CZ) and returns where it hangs from: the
# height its rods reach down to, and the points along the bar they hang at.
def pretzel(a, cy):
    # A trefoil with its lower lobe opened: the two lobes above, the arms
    # twisting across the middle and their ends resting on the belly. The
    # strand rides over and under itself at each crossing (the x wobble).
    pts = []
    t0, t1, n = math.pi + .75, 3 * math.pi - .75, 32
    for k in range(n + 1):
        t = t0 + (t1 - t0) * k / n
        z = math.sin(t) + 2 * math.sin(2 * t)
        y = math.cos(t) - 2 * math.cos(2 * t)
        pts.append((.035 * math.sin(3 * t), cy + .1 + .105 * y, CZ + .105 * z))
    a.tube(pts, [.045] * len(pts), BREAD, sides=5, ref=(1, 0, 0))
    return cy + .22, [CZ - .2, CZ + .2]


def cask(a, cy):
    a.cyl(.2, .2, .5, 0, cy, CZ, WOOD, sides=10, rx=math.pi / 2)
    a.cyl(.23, .23, .26, 0, cy, CZ, WOOD, sides=10, rx=math.pi / 2)     # the belly
    for dz, r in ((-.2, .212), (0.0, .238), (.2, .212)):
        a.cyl(r, r, .035, 0, cy, CZ + dz, IRON, sides=10, rx=math.pi / 2, cap=False)
    return cy + .19, [CZ - .2, CZ + .2]


def candles(a, cy):
    a.box(.16, .05, .68, 0, cy, CZ, WOOD)                              # the shelf
    for k, dz in enumerate((-.21, 0.0, .21)):
        h = .44 if k == 1 else .34
        a.cyl(.062, .062, h, 0, cy + .025 + h / 2, CZ + dz, WAX, sides=6)
        a.cyl(.035, 0, .13, 0, cy + .025 + h + .07, CZ + dz, FLAME, sides=5)
    return cy, [CZ - .32, CZ + .32]


def shears(a, cy):
    for s in (1, -1):
        ang = s * .3
        a.span((0, cy + .04, CZ), (0, cy - .56 * math.cos(ang), CZ + .56 * math.sin(ang)), .07, .02, STEEL)
        bz, by = CZ - .2 * math.sin(ang), cy + .25 * math.cos(ang)
        ring(a, by, bz, .085, .02, IRON)
        a.span((0, cy + .02, CZ), (0, by - .08, bz), .035, .03, IRON)
    a.cyl(.03, .03, .06, 0, cy, CZ, IRON, sides=6, rz=math.pi / 2)
    return cy + .32, [CZ]


def key(a, cy):
    ring(a, cy, CZ - .3, .15, .035, GILT, n=12, sides=5)               # the bow
    a.box(.05, .065, .6, 0, cy, CZ + .14, GILT)                        # the shank
    a.box(.05, .22, .065, 0, cy - .11, CZ + .4, GILT)                  # the bit
    a.box(.05, .13, .065, 0, cy - .065, CZ + .29, GILT)
    return cy + .03, [CZ - .3, CZ + .3]


def horseshoe(a, cy):
    pts = [(0, cy + .2 * math.cos(t) - .02, CZ + .2 * math.sin(t)) for t in [math.pi * (.2 + 1.6 * k / 14) for k in range(15)]]
    a.tube(pts, [.045] * 15, IRON, sides=5, ref=(1, 0, 0))
    return cy - .2, [CZ]            # hung by its crown, heels up, to keep the luck in


def book(a, cy):
    # open, pages out on both faces: the boards edge them and show at the spine
    a.box(.05, .46, .62, 0, cy, CZ, LEATHER)
    a.box(.07, .42, .27, 0, cy, CZ - .145, PAGE)
    a.box(.07, .42, .27, 0, cy, CZ + .145, PAGE)
    return cy + .23, [CZ - .2, CZ + .2]


def bottle(a, cy):
    a.cyl(.05, .05, .1, 0, cy - .02, CZ, CORK, sides=6)                  # the stopper
    a.cyl(.05, .06, .14, 0, cy - .13, CZ, GLASS, sides=6)                # the neck
    a.cyl(.18, .07, .1, 0, cy - .25, CZ, GLASS, sides=8)                 # the shoulder
    a.cyl(.18, .18, .3, 0, cy - .45, CZ, GLASS, sides=8)                 # the body
    return cy + .03, [CZ]


EMBLEMS = {
    'baker': (pretzel, -.55), 'grocer': (cask, -.5), 'chandler': (candles, -.62), 'draper': (shears, -.52),
    'ironmonger': (key, -.42), 'saddler': (horseshoe, -.42), 'bookseller': (book, -.5), 'apothecary': (bottle, -.2),
}

for trade in (sys.argv[1:] or list(EMBLEMS)):
    make, cy = EMBLEMS[trade]
    s = Asset('shop-sign-' + trade, seed=1470 + list(EMBLEMS).index(trade))
    bracket(s)
    hang_y, at = make(s, cy)
    for z in at:                                                          # the rods it hangs on
        s.box(.018, -.02 - hang_y, .018, 0, (hang_y - .02) / 2, z, IRON)
    s.finish(cam_at=(2.2, -.25, .95), cam_look=(0, -.32, .66), res=(460, 420), lens=35, sun=(40, 0, 60))
