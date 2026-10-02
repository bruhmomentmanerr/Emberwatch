# The Skywatch's armillary (r143): an old bronze sphere of rings on a stone
# column, at the centre of the knoll's crown where the companions come to
# watch the sky. Three great rings — the horizon, the meridian and a tilted
# ecliptic band — round a small glowing orb, a polar rod through it, all on a
# fluted column over a stepped base.
#
# Local frame (game axes): y=0 is the ground; the meridian ring lies in the
# YZ plane, so the polar rod leans toward +Z.
#
#   python tools/assets/skywatch-armillary.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset, rot
from mathutils import Vector

STONE = (.58, .58, .64)
STONE2 = (.48, .48, .55)
BRONZE = (.60, .47, .28)
BRONZE_DARK = (.40, .31, .19)
ORB = (.75, .82, 1.0, .1)          # alpha < 1 glows (cobalt)

a = Asset('skywatch-armillary', seed=8)

# Stepped base and a fluted column.
a.cyl(1.25, 1.35, .22, 0, .11, 0, STONE2, sides=12)
a.cyl(.95, 1.02, .2, 0, .32, 0, STONE, sides=12)
a.cyl(.36, .42, 1.25, 0, 1.04, 0, STONE, sides=12)
for k in range(12):
    ang = k / 12 * math.tau
    a.box(.05, 1.1, .05, math.cos(ang) * .37, 1.04, math.sin(ang) * .37, STONE2, ry=-ang)
a.cyl(.52, .40, .18, 0, 1.75, 0, STONE2, sides=12)
a.cyl(.12, .16, .5, 0, 2.05, 0, BRONZE_DARK, sides=8)

C = Vector((0, 2.95, 0))
R = .78


def ring(radius, thick, width, rot_m, color, segs=28):
    # A flat band: a tube along a circle, squashed across its plane.
    pts, radii = [], []
    for i in range(segs + 1):
        th = i / segs * math.tau
        p = rot_m @ Vector((math.cos(th) * radius, 0, math.sin(th) * radius))
        pts.append(tuple(C + p))
        radii.append((width / 2, thick / 2))
    a.tube(pts, radii, color, sides=4, ref=tuple(rot_m @ Vector((0, 1, 0))), cap0=False, cap1=False)


tilt = math.radians(33)                        # the pole's lean
pole = rot(tilt, 0, 0)                         # tilts +Y toward +Z
ring(R, .03, .07, pole, BRONZE)                                       # equator (square to the pole)
ring(R * 1.04, .03, .07, rot(0, 0, math.pi / 2), BRONZE_DARK)         # meridian (in the YZ plane)
ring(R * .98, .03, .16, pole @ rot(math.radians(23.5), 0, 0), BRONZE)  # the ecliptic band
ring(R * 1.1, .035, .06, rot(0, 0, 0), BRONZE_DARK)                   # horizon (level)
# The polar rod through the centre, the orb on it.
axis = pole @ Vector((0, 1, 0))
a.tube([tuple(C - axis * (R * 1.15)), tuple(C + axis * (R * 1.15))], [.022, .022], BRONZE_DARK, sides=6)
a.cyl(.13, .13, .26, C.x, C.y, C.z, ORB, sides=10)
a.cyl(.1, .0, .1, C.x, C.y + .18, C.z, ORB, sides=10)
a.cyl(.1, .0, .1, C.x, C.y - .18, C.z, ORB, sides=10, rx=math.pi)
# The horizon ring's supports down to the column head.
for k in range(4):
    ang = k / 4 * math.tau + math.pi / 4
    top = C + Vector((math.cos(ang) * R * 1.1, 0, math.sin(ang) * R * 1.1))
    a.span((math.cos(ang) * .1, 2.25, math.sin(ang) * .1), tuple(top), .04, .04, BRONZE_DARK)

a.finish(cam_at=(2.6, 2.6, 4.2), cam_look=(0, 2.1, 0), res=(600, 800), lens=40, sun=(55, 0, 150))
