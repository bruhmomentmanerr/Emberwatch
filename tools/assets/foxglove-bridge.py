# The Foxglove bridge (r143): a humpbacked stone arch over the brook where it
# widens above Foxglove Pond. The r140 bridge was a flat deck at ground level
# with a token half-arch hung under it, placed over a painted ribbon of water
# on dry grass; this one crosses the real brook, and its hump is the thing a
# moonlit bridge is recognised by.
#
# One solid: the bridge's side profile — the humped road on top, the arch cut
# out underneath — extruded through the bridge's width. On both faces a ring
# of voussoirs stands a little proud of the spandrel; parapets with a coping
# follow the hump; end posts close each parapet; short wing walls splay into
# the banks. The game walks it on a matching profile (placeFoxglove).
#
# Local frame (game axes): the span runs along Z (-8 to +8), width along X;
# y=0 is the bank at the bridge's ends, the road's crown is at ROAD_CROWN.
#
#   python tools/assets/foxglove-bridge.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

STONE = (0.66, 0.63, 0.60)
STONE2 = (0.56, 0.54, 0.52)
VOUSSOIR = (0.74, 0.72, 0.70)
COPING = (0.60, 0.58, 0.56)
MOSS = (0.40, 0.50, 0.36)

HALF_LEN = 8.0
WIDTH = 3.8
ROAD_CROWN = 2.45
ARCH_R = 4.5
ARCH_CY = -2.9           # the arch's centre: springs at y=-0.2, z=+-3.6; crown 1.6
ARCH_HALF = 3.6
RING = 0.5
BASE = -1.4              # the foot of the solid, below the bed


def road(z):
    # The hump: a parabola from the banks to the crown.
    return ROAD_CROWN * (1 - (z / HALF_LEN) ** 2)


def arch_y(z, r=ARCH_R):
    return ARCH_CY + math.sqrt(max(0.0, r * r - z * z))


a = Asset('foxglove-bridge', seed=77)

# The side profile, counter-clockwise seen from +X: along the foot from one
# end, up over the arch's intrados, on to the other end, then back along the
# road. Extruded along X by the kit (outline in its local XY, depth along its
# local Z), so it is turned a quarter round Y: local X -> -Z, local Z -> +X.
N = 14
outline = [(HALF_LEN, BASE), (ARCH_HALF + .01, BASE)]
for i in range(N + 1):
    z = ARCH_HALF - 2 * ARCH_HALF * i / N
    outline.append((z, arch_y(z)))
outline += [(-ARCH_HALF - .01, BASE), (-HALF_LEN, BASE)]
for i in range(16 + 1):
    z = -HALF_LEN + 2 * HALF_LEN * i / 16
    outline.append((z, road(z)))
# Outline u runs along the span; turned by ry=+90 deg its local X goes to -Z.
# The profile is symmetric, so the mirror does not matter; the winding does:
# the list above runs (+8, foot) -> (+3.6, foot) -> over the arch -> (-8, foot)
# -> up the road from -8 to +8, which is clockwise in (u, v) — reverse it.
outline = list(reversed(outline))
a.extrude(outline, WIDTH, STONE, at=(0, 0, 0), ry=math.pi / 2, side_color=STONE2)

# The voussoir ring on both faces, each stone a short block square to the arch.
for side in (-1, 1):
    x = side * (WIDTH / 2 + .05)
    for i in range(11):
        t0 = math.pi * (.14 + .72 * i / 11)
        t1 = math.pi * (.14 + .72 * (i + 1) / 11)
        tm = (t0 + t1) / 2
        rm = ARCH_R + RING / 2
        z, y = math.cos(tm) * rm, ARCH_CY + math.sin(tm) * rm
        span = (t1 - t0) * rm
        # rx = pi/2 - tm turns the block's local Z onto the arc's tangent at tm
        # (and its local Y onto the radius), so each stone sits square to the curve.
        a.box(.12, RING + (.14 if i % 2 else .02), span * .96, x, y, z, VOUSSOIR if i != 5 else COPING, rx=math.pi / 2 - tm)

# Parapets following the hump, with a coping, from end post to end post.
for side in (-1, 1):
    x = side * (WIDTH / 2 - .16)
    segs = 10
    for i in range(segs):
        z0 = -HALF_LEN + .45 + (2 * HALF_LEN - .9) * i / segs
        z1 = -HALF_LEN + .45 + (2 * HALF_LEN - .9) * (i + 1) / segs
        y0, y1 = road(z0), road(z1)
        # a length of wall standing on the road, turned to its slope
        mz, my = (z0 + z1) / 2, (y0 + y1) / 2
        slope = math.atan2(y1 - y0, z1 - z0)
        L = math.hypot(z1 - z0, y1 - y0) + .04
        a.box(.32, .72, L, x, my + .36, mz, STONE2 if i % 3 == 1 else STONE, rx=-slope)
        a.box(.44, .12, L + .02, x, my + .78, mz, COPING, rx=-slope)
    for zend in (-1, 1):
        z = zend * (HALF_LEN - .25)
        a.box(.56, 1.25, .56, x, road(z) + .5, z, STONE2)
        a.box(.66, .14, .66, x, road(z) + 1.19, z, COPING)
        # wing walls splaying out into the bank
        wz = zend * (HALF_LEN + 1.1)
        a.jbox(.5, 1.0, 2.4, x + side * .5, -.25, wz, STONE2, jit=.05, ry=side * zend * .35, top_color=MOSS)

a.finish(cam_at=(11.0, 2.2, 9.0), cam_look=(0, .8, 0), res=(900, 560), lens=30,
         extra_views=[('side', (15.0, 1.0, 0.0), (0, .8, 0)), ('deck', (0, 4.5, -12.0), (0, 1.5, 0))])
