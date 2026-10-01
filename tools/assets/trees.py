# The forest's trees (r152). Until now every one of the 4,200 trees outside
# the walls was a five-sided cylinder under two six-sided cones: from the
# city's walls and the belfry the forest read as rows of Christmas trees.
# These are instanced in thousands, so each is a few dozen triangles, drawn
# to read at a distance and at night: the silhouette is what matters.
#
#   tree-pine       four tiers of drooping, star-edged skirts on a bare
#                   trunk; the commonest tree
#   tree-fir        taller and narrower, five tiers to a spire
#   tree-broadleaf  a forked trunk under a crown of three lumpy masses
#   tree-snag       a dead pine: a bare grey trunk and a few broken limbs
#   shrub           undergrowth for the forest's edge: two low masses
#
# Local frame (game axes): the trunk's foot at the origin, the reference tree
# 6 m tall with its lowest branches about 1.7 m out. The game scales each
# instance by (width, height / 6, width) and tints it per instance, so the
# colours here are near the middle of the range and the tint does the rest.
#
#   python tools/assets/trees.py [pine|fir|broadleaf ...]
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

BARK = (.27, .19, .13)
BARK2 = (.34, .25, .17)
NEEDLE = (.12, .32, .19)
NEEDLE2 = (.17, .40, .23)
NEEDLE_UNDER = (.06, .16, .11)
LEAF = (.17, .36, .17)
LEAF2 = (.24, .45, .21)
DEAD = (.36, .33, .31)
DEAD2 = (.30, .27, .25)


def skirt(a, yt, yb, r, n, phase, side, side2, under, droop=.32, inner=.66):
    # One tier: a cone from (0, yt) out to a star-shaped rim at yb, its
    # points the branch tips, the notches between them higher and further in;
    # a dished underside, darker, so it reads as a canopy seen from below.
    rng, ring = a.rng, []
    for i in range(n):
        ang = (i + phase) / n * math.tau
        tip = i % 2 == 0
        rr = r * (1 if tip else inner) * (1 + rng.uniform(-.09, .09))
        yy = yb + (0 if tip else droop) + rng.uniform(-.06, .06)
        ring.append((math.cos(ang) * rr, yy, math.sin(ang) * rr))
    verts = [(rng.uniform(-.04, .04), yt, rng.uniform(-.04, .04))] + ring + [(0, yb + droop * 1.7, 0)]
    faces, cols = [], []
    for i in range(n):                      # outward: apex, next, this (CCW from outside)
        faces.append((0, 1 + (i + 1) % n, 1 + i)); cols.append(side if i % 2 else side2)
    for i in range(n):                      # underside, facing down
        faces.append((n + 1, 1 + i, 1 + (i + 1) % n)); cols.append(under)
    a.mesh(verts, faces, cols)


def pine():
    a = Asset('tree-pine', seed=1520)
    a.cyl(.17, .07, 5.0, 0, 2.5, 0, BARK, sides=5, cap=False)
    for k, (yt, yb, r) in enumerate([(3.0, 1.15, 1.75), (4.05, 2.35, 1.42), (5.05, 3.45, 1.05), (6.0, 4.45, .62)]):
        skirt(a, yt, yb, r, 8, k * .5, NEEDLE, NEEDLE2, NEEDLE_UNDER)
    return a


def fir():
    a = Asset('tree-fir', seed=1521)
    a.cyl(.14, .05, 5.6, 0, 2.8, 0, BARK, sides=5, cap=False)
    tiers = [(2.2, .75, 1.25), (3.1, 1.75, 1.06), (4.0, 2.7, .84), (4.95, 3.65, .6), (6.15, 4.6, .38)]
    for k, (yt, yb, r) in enumerate(tiers):
        skirt(a, yt, yb, r, 8, k * .5, NEEDLE, NEEDLE2, NEEDLE_UNDER, droop=.26, inner=.6)
    return a


def broadleaf():
    a = Asset('tree-broadleaf', seed=1522)
    # the trunk, and three limbs out of its fork into the crown
    a.tube([(0, 0, 0), (.05, 1.4, 0), (.02, 2.5, .03)], [.24, .17, .13], BARK, sides=5, cap0=False, cap1=False)
    for ang, out, up in ((.3, .95, 1.5), (2.4, .85, 1.3), (4.4, .9, 1.6)):
        a.tube([(.02, 2.4, .03), (math.cos(ang) * out, 2.4 + up, math.sin(ang) * out)], [.12, .05], BARK2, sides=4, cap0=False, cap1=False)
    # the crown: three masses, the top one highest and lightest
    for (x, y, z, w, h) in ((.75, 3.9, .2, 2.3, 1.9), (-.6, 3.75, .55, 2.1, 1.8), (.05, 4.75, -.45, 2.2, 2.0)):
        a.rock(w, h, w * .95, x, y, z, LEAF, jag=.2, sides=5, top_color=LEAF2)
    return a


def snag():
    a = Asset('tree-snag', seed=1523)
    a.cyl(.19, .05, 5.4, 0, 2.7, 0, DEAD, sides=5, cap=False)
    for ang, y, out, up in ((.4, 2.4, .9, .35), (2.5, 3.1, .75, .5), (4.3, 3.7, .6, .3), (1.5, 4.3, .5, .45)):
        a.tube([(0, y, 0), (math.cos(ang) * out, y + up, math.sin(ang) * out)], [.07, .02], DEAD2, sides=4, cap0=False, cap1=False)
    return a


def shrub():
    a = Asset('shrub', seed=1524)
    for (x, z, w, h) in ((.25, .05, 1.3, .9), (-.4, -.1, 1.05, .72)):
        a.rock(w, h, w * .9, x, h * .42, z, LEAF, jag=.24, sides=5, top_color=LEAF2)
    return a


MAKERS = {'pine': pine, 'fir': fir, 'broadleaf': broadleaf, 'snag': snag, 'shrub': shrub}
for name in (sys.argv[1:] or list(MAKERS)):
    t = MAKERS[name]()
    t.finish(cam_at=(7.0, 3.2, 9.0), cam_look=(0, 3.0, 0), res=(360, 420), lens=35, sun=(40, 0, 60),
             extra_views=[('below', (2.4, 1.0, 3.2), (0, 3.4, 0))])
