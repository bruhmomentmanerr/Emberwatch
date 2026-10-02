# The Rain Oath's island (r143): the ring the kneeling knight keeps his vow
# in. Nine standing stones round the rim, leaning a little inward, a gap where
# the causeway arrives; paving in two rings of radial slabs; a two-tier round
# plinth at the centre for the knight. Everything is stone the rain can wet
# (the game registers its material with the rain's wet pass).
#
# Local frame (game axes): the causeway arrives from -Z; y=0 is the island's
# top; the plinth is at the origin.
#
#   python tools/assets/rain-oath-ring.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

STONE = (.50, .52, .60)
STONE2 = (.42, .44, .52)
SLAB = (.46, .47, .54)
SLAB2 = (.38, .39, .46)
MOSS = (.34, .44, .34)
RUNE = (.45, .55, 1.0, .35)       # the plinth's inlaid ring glows faintly

a = Asset('rain-oath-ring', seed=404)
r = a.rng

# Paving: two rings of radial slabs, a little uneven.
for (r0, r1, n, col) in [(1.9, 3.3, 14, SLAB), (3.4, 4.9, 22, SLAB2)]:
    for k in range(n):
        ang = (k + .5) / n * math.tau
        if abs(math.atan2(math.sin(ang + math.pi / 2), math.cos(ang + math.pi / 2))) < .01:
            pass
        rm = (r0 + r1) / 2
        w = 2 * math.pi * rm / n * .9
        a.jbox(w, .16, (r1 - r0) * .92, math.cos(ang) * rm, -.05 + r.uniform(-.02, .02), math.sin(ang) * rm, col,
               jit=.05, ry=math.pi / 2 - ang)

# The plinth: two tiers, a ring inlaid in its top that glows under rain-light.
a.cyl(1.55, 1.65, .28, 0, .14, 0, STONE2, sides=16)
a.cyl(1.15, 1.25, .26, 0, .41, 0, STONE, sides=16)
a.tube([(0, .545, 0), (0, .56, 0)], [(.95, .95), (.95, .95)], RUNE, sides=24, cap0=False, cap1=True)
a.cyl(.85, .85, .02, 0, .555, 0, STONE, sides=24)

# Nine stones round the rim; the gap faces the causeway (-Z).
for k in range(10):
    ang = -math.pi / 2 + k / 10 * math.tau
    if k == 0:
        continue                      # the causeway's way in
    rr = 5.6 + r.uniform(-.15, .2)
    h = r.uniform(2.3, 3.4)
    w = r.uniform(.9, 1.3)
    x, z = math.cos(ang) * rr, math.sin(ang) * rr
    lean = r.uniform(.03, .09)
    # rx leans a stone's top in toward the centre: its local +Z is turned to
    # face outward by ry, so a positive tilt about local X brings the top in.
    a.jbox(w, h, w * .62, x, h / 2 - .35, z, STONE if k % 2 else STONE2, jit=.12,
           ry=math.pi / 2 - ang, rx=-lean, taper=r.uniform(.62, .8), top_color=MOSS)
    a.rock(w * 1.3, .5, w * .9, x * 1.02, .0, z * 1.02, STONE2, jag=.3, ry=r.uniform(0, 3))

# The two stones either side of the way in stand taller: a threshold.
for side in (-1, 1):
    ang = -math.pi / 2 + side * .5
    x, z = math.cos(ang) * 5.9, math.sin(ang) * 5.9
    a.jbox(1.2, 3.9, .8, x, 1.6, z, STONE, jit=.08, ry=math.pi / 2 - ang, taper=.7, top_color=MOSS)

a.finish(cam_at=(0, 3.5, -16.0), cam_look=(0, 1.0, 0), res=(900, 600), lens=35,
         extra_views=[('high', (9.0, 10.0, 9.0), (0, 0, 0))])
