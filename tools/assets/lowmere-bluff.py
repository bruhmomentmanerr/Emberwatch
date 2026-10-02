# The Watcher's Bluff above Lowmere (r143): the rock face of the overlook.
# The ground itself is raised by a landform in the game (a plateau 21 m above
# the hamlet's valley floor, see planAuthoredLandforms); this is the face that
# makes the rise read as a crag: stratified ribs of jittered blocks, pushed
# forward in the middle into a prow, with a flat mossed ledge on the prow's
# crown where the cliff watcher sits, end caps wrapping back into the hill,
# and talus at the foot.
#
# Local frame (game axes): the face runs along X from -17 to +17, facing -Z
# (toward the hamlet); the rock body goes back into +Z; y=0 is the valley
# floor at the foot. The prow's crown is the ledge at x=0, top at 21.0 m.
# On the +X end the stair's head landing crosses the cap at z 9.5-14.5, so
# that cap stops short of it.
#
#   python tools/assets/lowmere-bluff.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

ROCK = (0.72, 0.72, 0.80)
ROCK2 = (0.58, 0.59, 0.69)
ROCK3 = (0.50, 0.51, 0.62)
MOSS = (0.42, 0.56, 0.40)

a = Asset('lowmere-bluff', seed=2718)
r = a.rng
TOP = 21.0
HALF = 17.0
PROW = 2.4


def prow_z(x):
    # The face bulges toward the hamlet in the middle: 2.4 m at the crown,
    # nothing at the ends.
    f = max(0.0, 1 - (x / HALF) ** 2)
    return -PROW * f


def rib(x, z, w, top, proud=0.0, crown=True):
    y = -1.2
    k = 0
    while y < top - .2:
        h = min(top - y, r.uniform(2.2, 5.4))
        if top - (y + h) < 1.2:
            h = top - y
        setback = k * r.uniform(.05, .45) - proud
        d = r.uniform(5.5, 8.5)
        col = (ROCK, ROCK2, ROCK3)[(k + int(x * 3)) % 3]
        a.jbox(w * r.uniform(.9, 1.1), h + .15, d, x + r.uniform(-.2, .2), y + h / 2, z + setback + d / 2, col,
               jit=.10, ry=r.uniform(-.08, .08), rz=r.uniform(-.04, .04), taper=r.uniform(.84, .98),
               top_color=MOSS if r.random() < .5 else None)
        y += h
        k += 1
    if crown:
        a.rock(w * .9, r.uniform(.6, 1.6), 2.8, x + r.uniform(-.3, .3), top + .25, z + 2.4 - proud * .5,
               ROCK2, jag=.34, top_color=MOSS)


x = -HALF
i = 0
while x < HALF:
    w = r.uniform(2.0, 4.2)
    cx = x + w / 2
    crown_zone = abs(cx) < 2.6
    edge = max(0.0, abs(cx) - 12)
    top = TOP if crown_zone else TOP + r.uniform(-.7, .9) - edge * r.uniform(.15, .5)
    proud = 0.0 if crown_zone else (r.uniform(.5, 1.5) if i % 3 == 1 else r.uniform(-.7, .3))
    rib(cx, prow_z(cx) + r.uniform(-.3, .3), w, top, proud=proud, crown=not crown_zone)
    x += w * r.uniform(.82, .95)
    i += 1

# The watcher's ledge: flat, mossed, level with the plateau behind it (the
# game stands a deck at exactly this height), jutting just past the prow.
a.jbox(4.6, .9, 5.4, 0, TOP - .45, 1.2 - PROW * .6, ROCK2, jit=.03, top_color=MOSS)
# A lip of rock either side, so the ledge reads as a seat in the crag.
for side in (-1, 1):
    a.rock(1.6, 1.1, 2.2, side * 2.9, TOP + .35, .2 - PROW * .5, ROCK3, jag=.3, top_color=MOSS)

# End caps: the plateau's sides turn back into the hill.
for side in (-1, 1):
    zc = -.5
    stop = 8.5 if side > 0 else 14.0
    while zc < stop:
        w = r.uniform(2.4, 4.2)
        h = TOP - max(0.0, zc - 5) * .5 + r.uniform(-.8, .6)
        a.jbox(6.0, h + 1.2, w * 1.08, side * (HALF + 1.2 + r.uniform(-.7, .7)), h / 2 - .6, zc + w / 2,
               (ROCK, ROCK2, ROCK3)[int(zc) % 3], jit=.11, ry=r.uniform(-.1, .1), taper=r.uniform(.8, .95), top_color=MOSS)
        a.rock(5.0, r.uniform(.8, 1.8), w, side * (HALF + 1.0), h + .2, zc + w / 2, ROCK2, jag=.34, top_color=MOSS)
        zc += w * .9

# Talus along the foot.
for k in range(26):
    tx = r.uniform(-HALF - 1.5, HALF + 1.5)
    s = r.uniform(.6, 2.2)
    a.rock(s * 1.3, s, s * 1.1, tx, s * .28, prow_z(tx) + r.uniform(-3.6, -.8), (ROCK2, ROCK3)[k % 2], jag=.3, ry=r.uniform(0, 3),
           top_color=MOSS if k % 3 == 0 else None)

a.finish(cam_at=(8.0, 8.0, -40.0), cam_look=(0.0, 10.0, 0.0), res=(1000, 700), lens=28,
         extra_views=[('top', (0.0, 26.0, 14.0), (0.0, 19.0, -6.0))])
