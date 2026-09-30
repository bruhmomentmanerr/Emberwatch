# The Veilscar — the cliff behind the Fallen Hall that the falls come over.
# r136-r139 hung two translucent planes in the air here and called them a
# waterfall; there was no cliff for water to fall from. The ground itself is
# raised by a landform in the game (a plateau 15 m up, see placeFallenHall);
# this is the rock face that makes that rise read as a cliff: ribs of
# stratified rock of uneven width and depth, some standing proud as
# buttresses and some set back, a notch where the water comes over, wet stone
# round the notch, moss on the ledges, talus at the foot, and end caps
# wrapping the plateau's sides.
#
# The first cut was clean boxes on an even grid and read as a masonry wall;
# every block is now a jittered box (_kit.jbox) and no two ribs break their
# strata at the same heights.
#
# Local frame (game axes): the face runs along X from -34 to +34, facing -Z
# (toward the hall); the rock body goes back into +Z; y=0 is the ground at
# the foot. The falls come over the notch at x=0, lip at 14.2 m.
#
#   python tools/assets/veilscar-cliff.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

ROCK = (0.74, 0.74, 0.84)
ROCK2 = (0.60, 0.60, 0.72)
ROCK3 = (0.52, 0.53, 0.66)
WET = (0.32, 0.36, 0.50)
MOSS = (0.44, 0.60, 0.42)

a = Asset('veilscar-cliff', seed=31415)
r = a.rng
TOP = 15.0
HALF = 34.0


LEDGE_X = -9.0      # the ruin wizard's shelf (game: t=+9 from the falls)


def rib(x, z, w, top, wet=False, proud=0.0, crown=True):
    # One vertical rib: strata of irregular height, each a jittered block,
    # set back a little more the higher it sits, leaning a hair.
    y = -1.2
    k = 0
    while y < top - .2:
        h = min(top - y, r.uniform(2.2, 5.8))
        if top - (y + h) < 1.4:
            h = top - y
        setback = k * r.uniform(.05, .5) - proud
        d = r.uniform(5.0, 8.0)
        col = WET if wet else (ROCK, ROCK2, ROCK3)[(k + int(x)) % 3]
        a.jbox(w * r.uniform(.9, 1.1), h + .15, d, x + r.uniform(-.25, .25), y + h / 2, z + setback + d / 2, col,
               jit=.10, ry=r.uniform(-.08, .08), rz=r.uniform(-.04, .04), taper=r.uniform(.84, .98),
               top_color=MOSS if (not wet and r.random() < .55) else None)
        y += h
        k += 1
    if crown:
        a.rock(w * .95, r.uniform(.9, 2.4), 3.2, x + r.uniform(-.3, .3), top + .35, z + 2.2 - proud * .5,
               ROCK2, jag=.34, top_color=MOSS)


x = -HALF
i = 0
while x < HALF:
    w = r.uniform(2.2, 5.0)
    cx = x + w / 2
    near = abs(cx) < 3.0
    ledge = abs(cx - LEDGE_X) < 2.6
    edge = max(0.0, abs(cx) - 27)
    top = (TOP - .9) if near else (TOP - .5) if ledge else TOP + r.uniform(-.8, 1.4) - edge * r.uniform(.1, .45)
    proud = 0.0 if near else .9 if ledge else (r.uniform(.6, 1.8) if i % 3 == 1 else r.uniform(-.8, .3))
    rib(cx, (1.4 if near else 0.0) + r.uniform(-.4, .4), w, top, wet=near, proud=proud, crown=not ledge)
    x += w * r.uniform(.82, .96)          # ribs overlap a little, so no slot shows between them
    i += 1

# the shelf the ruin wizard stands on: flat, mossed, jutting a little past the
# face so he stands clear of the rock and against the sky from the hall
a.jbox(3.6, .9, 5.0, LEDGE_X, TOP - .2, 1.2, ROCK2, jit=.04, top_color=MOSS)

# the lip of the notch the water pours over, worn smooth and dark
a.jbox(5.4, .7, 3.2, 0, TOP - .9, 1.9, WET, jit=.06)

# end caps: the plateau's two sides turn back into the hill, falling away
for side in (-1, 1):
    zc = -1.0
    while zc < 27:
        w = r.uniform(2.6, 4.6)
        # On the +X end the stair's head landing crosses the cap at z 9.5-14.5
        # (placed in the game at 15.05 m): hold the rock under it, no crown.
        saddle = side > 0 and zc + w > 8.5 and zc < 15.0
        h = (13.6 if saddle else TOP - max(0.0, zc - 6) * .28 + r.uniform(-.8, .8))
        a.jbox(7.0, h + 1.2, w * 1.08, side * (HALF + 1.4 + r.uniform(-.8, .8)), h / 2 - .6, zc + w / 2,
               (ROCK, ROCK2, ROCK3)[int(zc) % 3], jit=.11, ry=r.uniform(-.1, .1), taper=r.uniform(.8, .95), top_color=MOSS)
        if not saddle:
            a.rock(5.8, r.uniform(1, 2.2), w, side * (HALF + 1.2), h + .25, zc + w / 2, ROCK2, jag=.34, top_color=MOSS)
        zc += w * .9

# talus: fallen blocks along the foot, none where the pool is
for k in range(36):
    tx = r.uniform(-HALF - 2, HALF + 2)
    if abs(tx) < 7:
        continue
    s = r.uniform(.8, 2.8)
    a.rock(s * 1.3, s, s * 1.1, tx, s * .30, r.uniform(-4.2, -.8), (ROCK2, ROCK3)[k % 2], jag=.3, ry=r.uniform(0, 3),
           top_color=MOSS if k % 4 == 0 else None)
# wet boulders round where the falls land
for k in range(8):
    ang = k / 8 * math.pi + .2
    s = r.uniform(.8, 1.6)
    a.rock(s * 1.4, s, s * 1.2, math.cos(ang) * 6.8, s * .25, -4.0 - math.sin(ang) * 3.2, WET, jag=.25, ry=r.uniform(0, 3))

a.finish(cam_at=(10.0, 6.0, -42.0), cam_look=(0.0, 8.0, 0.0), res=(1000, 600), lens=24,
         extra_views=[('end', (52.0, 10.0, -16.0), (26.0, 8.0, 8.0))])
