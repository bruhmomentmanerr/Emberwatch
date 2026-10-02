# Foxglove Mill (r143), upstream of the Foxglove bridge: a mill house on the
# brook's bank — stone below, a jettied timber-framed storey above, a steep
# shingled roof — and an overshot wheel on its stream side, fed by a flume on
# trestles from upstream. Two models, because the wheel turns:
#   foxglove-mill   the house, the flume and its trestles (static)
#   mill-wheel      the wheel, drawn about its own hub, axle along X
#
# Local frame (game axes) for the house: long axis along Z, the stream along
# the +X side, upstream toward -Z, the door on the +Z gable (downstream); y=0
# is the ground at the stream-side foot. The wheel's hub sits at WHEEL.
#
#   python tools/assets/foxglove-mill.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset, rot
from mathutils import Vector

STONE = (.52, .50, .52)
STONE2 = (.42, .41, .44)
PLASTER = (.52, .47, .40)       # untextured in the game (tex 'none'), so darker than the city's limewash
TIMBER = (.26, .19, .13)
SHINGLE = (.30, .25, .23)
SHINGLE2 = (.22, .18, .17)
WOOD = (.36, .27, .18)
WET = (.22, .19, .16)
IRON = (.18, .18, .20)
LIT = (1.0, .80, .48, .12)
DARKWIN = (.08, .08, .10)

W, L = 6.5, 9.0          # house width (x) and length (z)
BASE, GROUND, UPPER = .5, 3.0, 2.6
WHEEL = (4.6, 2.4, 0.0)  # hub (x, y, z)
WHEEL_R = 2.6

h = Asset('foxglove-mill', seed=55)
# Plinth, stone ground storey, jettied timber-framed upper storey.
h.box(W + .5, BASE + .6, L + .5, 0, (BASE - .6) / 2, 0, STONE2)
h.box(W, GROUND, L, 0, BASE + GROUND / 2, 0, STONE)
y1 = BASE + GROUND
h.box(W + .4, .25, L + .4, 0, y1 + .12, 0, TIMBER)                      # the jetty beam
h.box(W + .4, UPPER, L + .4, 0, y1 + .25 + UPPER / 2, 0, PLASTER)
y2 = y1 + .25 + UPPER
h.box(W + .5, .2, L + .5, 0, y2 - .1, 0, TIMBER)                        # wall plate
# Timber framing on the upper storey: posts, a mid rail, and braces.
for side in (-1, 1):
    x = side * (W / 2 + .21)
    for k in range(7):
        z = -L / 2 - .1 + k * (L + .2) / 6
        h.box(.1, UPPER, .18, x, y1 + .25 + UPPER / 2, z, TIMBER)
    h.box(.1, .14, L + .4, x, y1 + .25 + UPPER * .5, 0, TIMBER)
    for k in range(3):
        z0 = -L / 2 + .6 + k * 3.0
        h.span((x, y1 + .35, z0), (x, y2 - .25, z0 + 1.3), .1, .12, TIMBER, up=(1, 0, 0))
for zf in (-1, 1):
    z = zf * (L / 2 + .21)
    for k in range(5):
        x = -W / 2 - .1 + k * (W + .2) / 4
        h.box(.18, UPPER, .1, x, y1 + .25 + UPPER / 2, z, TIMBER)
# Gable ends: a triangle of plaster framed in timber.
RISE = 3.3
for zf in (-1, 1):
    z = zf * (L / 2 + .2)
    h.extrude([(-(W / 2 + .2), y2), (W / 2 + .2, y2), (0, y2 + RISE)], .2, PLASTER, at=(0, 0, z))
    h.span((-(W / 2 + .2), y2, z + zf * .12), (0, y2 + RISE, z + zf * .12), .16, .1, TIMBER, up=(0, 0, 1))
    h.span((0, y2 + RISE, z + zf * .12), (W / 2 + .2, y2, z + zf * .12), .16, .1, TIMBER, up=(0, 0, 1))
    h.box(.14, RISE * .8, .1, 0, y2 + RISE * .4, z + zf * .12, TIMBER)
# Roof: two steep shingled slopes, a ridge, courses.
run = W / 2 + .75
slope = math.atan2(RISE, run - .55)
Lr = math.hypot(run, RISE) + .1
for sx in (-1, 1):
    rz = -sx * slope
    nx, ny = sx * math.sin(slope), math.cos(slope)
    h.box(Lr, .14, L + 1.2, sx * run / 2, y2 + RISE / 2 - .1, 0, SHINGLE, rz=rz)
    for k in range(6):
        f = (k + .5) / 6
        px, py = sx * run * (1 - f), y2 - .2 + (RISE + .1) * f
        h.box(.62, .06, L + 1.22, px + nx * .1, py + ny * .1, 0, SHINGLE2 if k % 2 else SHINGLE, rz=rz)
h.box(.3, .22, L + 1.3, 0, y2 + RISE + .02, 0, SHINGLE2)
# Chimney on the upstream half.
h.box(.95, 3.4, .95, -1.6, y2 + 1.7, -2.4, STONE2)
h.box(1.15, .25, 1.15, -1.6, y2 + 3.45, -2.4, STONE)
# Door on the downstream gable, in a stone surround; a lamp bracket beside it.
h.box(1.7, 2.6, .25, .9, BASE + 1.3, L / 2 + .06, STONE2)
h.box(1.25, 2.25, .12, .9, BASE + 1.12, L / 2 + .15, WOOD)
h.box(.12, .4, .5, 2.1, BASE + 2.5, L / 2 + .3, IRON)
# Windows: ground floor on the landward side (lit), the upper floor (one lit),
# the gable over the door (lit), a small one on the stream side.
for (x, y, z, lit, face) in [(-W / 2 - .03, BASE + 1.6, -2.2, True, 'x'), (-W / 2 - .03, BASE + 1.6, 2.2, True, 'x'),
                             (-W / 2 - .24, y1 + 1.4, -2.8, False, 'x'), (-W / 2 - .24, y1 + 1.4, 0.2, True, 'x'), (-W / 2 - .24, y1 + 1.4, 3.0, False, 'x'),
                             (0, y2 + 1.1, L / 2 + .33, True, 'z'), (W / 2 + .03, BASE + 1.9, 2.6, False, 'x')]:
    col = LIT if lit else DARKWIN
    if face == 'x':
        h.box(.1, .95, .75, x, y, z, col)
    else:
        h.box(.7, .9, .1, x, y, z, col)
# The wheel's axle housing on the stream wall.
h.box(.7, .9, .9, W / 2 + .35, WHEEL[1], WHEEL[2], TIMBER)
# The flume: a planked channel on trestles from upstream to just past the
# wheel's crown, where the water drops onto the buckets.
fy = WHEEL[1] + WHEEL_R + .35
z0, z1 = -15.0, .45
h.box(.95, .08, z1 - z0, WHEEL[0], fy, (z0 + z1) / 2, WET)
for sx in (-1, 1):
    h.box(.08, .42, z1 - z0, WHEEL[0] + sx * .45, fy + .2, (z0 + z1) / 2, WOOD)
h.box(.7, .02, z1 - z0 - .2, WHEEL[0], fy + .06, (z0 + z1) / 2 - .1, (.45, .55, .85, .45))     # the water in it
for k in range(5):
    z = -13.5 + k * 3.0
    for sx in (-1, 1):
        h.span((WHEEL[0] + sx * .9, -1.0, z), (WHEEL[0] + sx * .4, fy - .05, z), .14, .14, WOOD)
    h.box(1.2, .12, .14, WHEEL[0], fy - .1, z, WOOD)
    h.box(1.5, .1, .12, WHEEL[0], fy * .45, z, WOOD)
h.finish(cam_at=(-9.0, 5.0, 13.0), cam_look=(1.0, 3.5, -2.0), res=(900, 700), lens=32,
         extra_views=[('stream', (13.0, 3.5, 6.0), (3.0, 3.5, -3.0))])

# ---- the wheel ------------------------------------------------------------------
w = Asset('mill-wheel', seed=56)
R, HALF = WHEEL_R, .42
ring_axis = rot(0, 0, math.pi / 2)            # a circle in the YZ plane
for sx in (-1, 1):
    pts = [(sx * HALF, math.sin(i / 32 * math.tau) * R, math.cos(i / 32 * math.tau) * R) for i in range(33)]
    w.tube(pts, [(.07, .09)] * 33, IRON if sx > 0 else WET, sides=4, ref=(1, 0, 0), cap0=False, cap1=False)
    pts2 = [(sx * HALF, math.sin(i / 32 * math.tau) * (R - .55), math.cos(i / 32 * math.tau) * (R - .55)) for i in range(33)]
    w.tube(pts2, [(.05, .06)] * 33, WET, sides=4, ref=(1, 0, 0), cap0=False, cap1=False)
    for k in range(8):
        a = k / 8 * math.tau
        w.span((sx * HALF, 0, 0), (sx * HALF, math.sin(a) * (R - .05), math.cos(a) * (R - .05)), .09, .12, WOOD, up=(1, 0, 0))
for k in range(18):
    a = k / 18 * math.tau
    r0 = R - .28
    y, z = math.sin(a) * r0, math.cos(a) * r0
    # each bucket a board across the rims, leaning back from the radius
    w.box(HALF * 2 + .08, .5, .06, 0, y, z, WET, rx=-(a + .5))
w.cyl(.36, .36, 1.1, 0, 0, 0, TIMBER, sides=10, rz=math.pi / 2)
w.cyl(.12, .12, 2.4, 0, 0, 0, IRON, sides=8, rz=math.pi / 2)
w.finish(cam_at=(5.0, 1.5, 3.0), cam_look=(0, 0, 0), res=(600, 600), lens=35)
