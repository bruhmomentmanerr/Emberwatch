# The Fallen Hall — the great hall of the city that stood out here before
# Vaneth drew in behind its walls (PROJECT.md §4, "Places beyond the wall").
# Until r143 it was ten random wall stubs and seven drums from ruins(): a
# scatter that read as rubble, not as a hall anyone had ever stood in. This
# is the building itself, broken: a nave with lancet windows down both sides,
# its roof gone but for two charred beams, the west door still standing, and a
# great pointed window at the east end — which frames the Veilscar falls and,
# from the doorway, the moon.
#
# Local frame (game axes): the nave runs along +Z from the west door (z=-15)
# to the great window (z=+15.6); the hall's centre, where the ash lies, is the
# origin. The game turns it so +Z points outward from the city, at the cliff.
#
#   python tools/assets/fallen-hall.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

STONE = (0.84, 0.82, 0.88)
WORN = (0.70, 0.68, 0.76)
DARK = (0.38, 0.36, 0.44)
MOSS = (0.46, 0.64, 0.44)
ASH = (0.20, 0.19, 0.23)
CHAR = (0.30, 0.25, 0.24)

a = Asset('fallen-hall', seed=1143)
WALL_X = 6.6          # inner face of each side wall is at 6.0
T = 1.2               # wall thickness
BAYS = [-12, -6, 0, 6, 12]
TOPS = [9.2, 7.6, 10.2, 3.2, 8.4]      # broken height of each bay's wall; bay 3 has fallen
SILL, SPRING, RISE, HALF = 1.7, 5.3, 2.2, 1.15

for side in (-1, 1):
    x = side * WALL_X
    for b, zc in enumerate(BAYS):
        top = TOPS[b] if side < 0 else TOPS[(b + 2) % 5]
        if top < SPRING + RISE:
            # a fallen bay: the sill course and a heap of its own stones
            a.box(T, 1.1, 6.0, x, .55, zc, WORN)
            for k in range(5):
                a.rock(1.5, .9, 1.3, x + side * a.rng.uniform(-.2, 2.4), .35, zc + a.rng.uniform(-2.6, 2.6), WORN, ry=a.rng.uniform(0, 3))
            continue
        a.box(T, SILL, 2 * HALF, x, SILL / 2, zc, STONE)                     # sill wall under the window
        a.arch_wall(HALF, SPRING, RISE, top, T, STONE, at=(x, 0, zc), ry=math.pi / 2, side_color=DARK)
        # the jambs of the opening up to the springing line
        for s in (-1, 1):
            a.box(T, SPRING - SILL, .01, x, (SPRING + SILL) / 2, zc + s * HALF, DARK)
    # piers between the bays, each a little taller or shorter where it broke
    for k, zp in enumerate([-15, -9, -3, 3, 9, 15]):
        h = [10.8, 9.6, 11.4, 6.2, 9.8, 12.2][k] - (1.4 if side > 0 and k in (2, 3) else 0)
        a.box(T + .1, h, 3.6 if abs(zp) < 15 else 1.8, x, h / 2, zp if abs(zp) < 15 else zp - math.copysign(.9, zp), STONE)
        # a battered buttress on the outside of every pier
        a.box(1.5, h * .78, 1.3, x + side * 1.25, h * .39, zp if abs(zp) < 15 else zp - math.copysign(.9, zp), WORN, taper=.72)
        a.box(1.6, .4, 1.4, x + side * 1.25, .2, zp if abs(zp) < 15 else zp - math.copysign(.9, zp), DARK)
        # moss where rain sits on the broken top
        a.box(T + .16, .12, 1.4, x, h + .06, zp if abs(zp) < 15 else zp - math.copysign(.9, zp), MOSS)

# East gable: the great window, 6 m across, its tracery half standing.
GZ, GT = 15.6, 1.4
GH, GS, GR = 3.0, 8.4, 4.6
a.box(2 * GH, GS * .3, GT, 0, GS * .15, GZ, STONE)                              # the wall below the window (only under it: the side pieces run to the ground, and coplanar overlaps z-fight)
a.box((15.8 - 2 * GH) / 2, GS, GT, -(GH + (15.8 - 2 * GH) / 4), GS / 2, GZ, STONE)  # left of the opening
a.box((15.8 - 2 * GH) / 2, GS - 1.5, GT, (GH + (15.8 - 2 * GH) / 4), (GS - 1.5) / 2, GZ, STONE)  # right, lower: it broke
a.arch_wall(GH, GS, GR, 15.2, GT, STONE, at=(0, 0, GZ), segs=9, side_color=DARK)
# the gable's broken peak above the arch, higher on the left
a.extrude([(-7.9, 15.2), (-1.0, 15.2), (-2.6, 17.6), (-5.8, 16.4)], GT, STONE, at=(0, 0, GZ))
a.extrude([(1.4, 15.2), (5.2, 15.2), (3.4, 16.3)], GT, WORN, at=(0, 0, GZ))
# tracery: a central mullion and the two lesser lancets it carries
a.box(.34, GS - GS * .3 + 2.6, .5, 0, GS * .3 + (GS - GS * .3 + 2.6) / 2, GZ, WORN)
for s in (-1, 1):
    a.arch_wall(1.35, GS + .9, 1.7, GS + 3.4, .45, WORN, at=(s * 1.5, 0, GZ), segs=5)
a.box(2 * GH, .5, GT + .2, 0, GS * .3 + .25, GZ - .1, DARK)                      # the window's sill
# corner turrets flanking the gable, one broken low
for s, h in ((-1, 18.6), (1, 11.2)):
    a.cyl(1.6, 1.4, h, s * 7.9, h / 2, GZ, STONE, sides=8)
    for m in range(8):
        if m % 2 == 0 or (s > 0 and m % 4 == 1):
            ang = m / 8 * math.tau
            mh = 1.3 if s < 0 else .6
            a.box(.8, mh, .8, s * 7.9 + math.cos(ang) * 1.35, h + mh / 2, GZ + math.sin(ang) * 1.35, WORN, ry=-ang)

# West front: the door arch stands whole; the wall either side has broken.
WZ = -15.6
a.box(4.0, 7.2, T, -4.5, 3.6, WZ, STONE)
a.box(4.0, 4.4, T, 4.6, 2.2, WZ, WORN)
a.arch_wall(2.0, 4.2, 2.6, 8.4, T, STONE, at=(0, 0, WZ), segs=7, side_color=DARK)
for s in (-1, 1):
    a.box(.5, 4.2, T + .3, s * 2.25, 2.1, WZ, WORN)                             # door jamb shafts
a.box(5.6, .35, 2.6, 0, .17, WZ - .6, WORN)                                     # the worn doorstep

# Inside: two column stumps of the vanished arcade, drums where they fell,
# two charred roof beams, and at the centre the ring round the ash.
for sx, sz, h in ((-3.4, -8.5, 3.6), (3.4, 6.5, 2.2), (3.4, -8.5, .9)):
    a.cyl(.62, .58, h, sx, h / 2, sz, STONE, sides=10)
    a.cyl(.78, .78, .3, sx, .15, sz, DARK, sides=10)
for dx, dz, ry in ((-2.2, -5.2, .4), (-1.0, 9.4, 1.9), (4.4, 1.8, 1.2), (-4.6, 3.6, 2.6)):
    a.cyl(.6, .6, 1.05, dx, .6, dz, WORN, sides=10, rz=math.pi / 2, ry=ry)
a.span((-6.0, 9.6, -2.5), (1.8, 0.2, 2.6), .42, .36, CHAR)
a.span((6.0, 7.0, 10.5), (1.0, 0.25, 13.2), .38, .34, CHAR)
for k in range(14):
    ang = k / 14 * math.tau
    a.rock(.9, .55, .7, math.cos(ang) * 2.55, .2, math.sin(ang) * 2.55, WORN, ry=-ang, jag=.15)
a.cyl(2.2, 2.2, .06, 0, .04, 0, ASH, sides=18)
a.box(11.6, .04, 29.0, 0, .02, 0, DARK)                                         # the old floor, sunk flush

a.finish(cam_at=(-9.0, 7.5, -30.0), cam_look=(0.0, 5.0, 4.0), res=(1000, 640), lens=28,
         extra_views=[('east', (14.0, 9.0, 30.0), (0.0, 5.5, 0.0)), ('nave', (0.0, 1.7, -17.5), (0.0, 7.0, 15.0))])
