# The Oathfield's small pieces (r143), one script for the set:
#   oath-blade          a longsword planted point-down, the fuller glowing
#   oath-ribbon         a strip of cloth knotted at a blade's cross, hanging
#   oath-cairn          the stones heaped round a blade's foot, and its name-stone
#   oathfield-lychgate  the roofed timber gate the field is entered by
#
#   python tools/assets/oathfield-pieces.py      (pip bpy, or blender --background --python)
#
# Each writes assets/<name>.glb and tools/assets/_preview-<name>.png. Origins
# are on the ground: a blade's where it enters the earth, the lychgate's in
# the middle of its passage. +Z is the front: the flat of a blade faces +Z
# with its cross along X; the lychgate's passage runs along Z.
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset
from mathutils import Vector

STEEL = (.60, .63, .70)
FULLER = (.42, .52, .95, .25)       # alpha < 1 glows (cobalt, in the blade's material)
BRONZE = (.52, .43, .30)
LEATHER = (.16, .11, .09)
CLOTH = (.30, .38, .62)
CLOTH_DARK = (.22, .27, .46)
STONE = (.46, .45, .50)
STONE_DARK = (.34, .33, .38)
MOSS = (.27, .35, .25)
OAK = (.34, .25, .17)
OAK_DARK = (.22, .16, .11)
SHINGLE = (.30, .26, .24)
SHINGLE_DARK = (.21, .18, .17)
IRON = (.16, .16, .18)
LAMP = (1.0, .78, .45, .15)          # alpha < 1 glows (amber, in the lychgate's material)

GUARD_Y = 1.13

# ---- the blade ------------------------------------------------------------------
b = Asset('oath-blade', seed=3)
b.tube([(0, -.06, 0), (0, .55, 0), (0, GUARD_Y, 0)], [(.036, .010), (.041, .011), (.046, .012)], STEEL, sides=4, ref=(0, 0, 1))
for face in (-1, 1):
    b.box(.014, .84, .003, 0, .60, face * .0125, FULLER)
# The cross: a shallow inverted V, its quillons bending toward the blade.
b.span((-.25, GUARD_Y - .03, 0), (0, GUARD_Y + .015, 0), .045, .05, BRONZE)
b.span((0, GUARD_Y + .015, 0), (.25, GUARD_Y - .03, 0), .045, .05, BRONZE)
b.box(.07, .06, .06, 0, GUARD_Y + .02, 0, BRONZE)
b.tube([(0, GUARD_Y + .05, 0), (0, GUARD_Y + .31, 0)], [.021, .019], LEATHER, sides=8)
for y in (.10, .19, .28):
    b.tube([(0, GUARD_Y + y - .012, 0), (0, GUARD_Y + y + .012, 0)], [.025, .025], BRONZE, sides=8)
b.cyl(.036, .044, .05, 0, GUARD_Y + .345, 0, BRONZE, sides=8)
b.cyl(.044, .0, .05, 0, GUARD_Y + .395, 0, BRONZE, sides=8)
b.finish(cam_at=(.9, 1.2, 2.2), cam_look=(0, .8, 0), res=(500, 700), lens=40, sun=(55, 0, 150))

# ---- a ribbon knotted at the cross ------------------------------------------------
r = Asset('oath-ribbon', seed=4)
r.tube([(-.05, GUARD_Y - .02, .0), (.05, GUARD_Y - .02, .0)], [(.035, .03), (.035, .03)], CLOTH_DARK, sides=8, ref=(0, 1, 0))
# Two tails from the knot, each one flat strip (a tube squashed to 8 mm)
# hanging down the front of the blade in a gentle S, cut square at the end.
for (sx, L, tw) in [(-1, .62, .05), (1, .50, .045)]:
    pts = [(sx * .03, GUARD_Y - .03, .045), (sx * .06, GUARD_Y - .03 - L * .3, .07), (sx * .05, GUARD_Y - .03 - L * .62, .085),
           (sx * .085, GUARD_Y - .03 - L, .11)]
    r.tube(pts, [(tw / 2, .004), (tw / 2, .004), (tw * .46, .004), (tw * .42, .004)], CLOTH, sides=4, ref=(0, 0, 1))
r.finish(cam_at=(.8, 1.0, 1.6), cam_look=(0, .85, 0), res=(400, 500), lens=40, sun=(55, 0, 150))

# ---- the cairn and name-stone ---------------------------------------------------------
c = Asset('oath-cairn', seed=5)
for k in range(6):
    a = k / 6 * math.tau + .3
    rr = .17 + .05 * (k % 2)
    size = .20 + .06 * ((k * 7) % 3) / 2
    c.rock(size, size * .62, size * .85, math.cos(a) * rr, size * .22, math.sin(a) * rr, STONE, jag=.25, ry=a, top_color=MOSS if k % 3 == 0 else STONE)
c.rock(.16, .12, .14, .05, .17, -.06, STONE_DARK, jag=.2)
# The name-stone leans back a little in front of the cairn.
c.box(.40, .34, .08, 0, .15, .40, STONE, rx=-.30)
c.box(.28, .12, .01, 0, .192, .434, STONE_DARK, rx=-.30)      # its face: local (0, .03, .045) turned by rx
c.finish(cam_at=(.7, .9, 1.6), cam_look=(0, .12, .1), res=(500, 400), lens=40, sun=(55, 0, 150))

# ---- the lychgate ------------------------------------------------------------------------
g = Asset('oathfield-lychgate', seed=6)
HALF_W, POST_Z, SILL, PLATE, EAVE, RIDGE, ROOF_Z = 1.55, 1.2, .5, 2.62, 2.42, 4.2, 1.85
for sx in (-1, 1):
    x = sx * HALF_W
    for z in (-POST_Z, 0, POST_Z):
        w = .22 if z else .18
        g.box(w, PLATE - SILL, w, x, (PLATE + SILL) / 2, z, OAK)
    g.box(.26, .16, POST_Z * 2 + .5, x, PLATE + .06, 0, OAK_DARK)               # wall plate
    g.box(.30, .10, POST_Z * 2 + .4, x, SILL + .05, 0, OAK_DARK)                # sole plate on the sill
    for z in (-POST_Z, POST_Z):                                                  # knee braces
        g.span((x, PLATE - .62, z), (x - sx * .55, PLATE - .02, z), .10, .10, OAK)
        g.span((x, PLATE - .62, z), (x, PLATE - .02, z - math.copysign(.55, z)), .10, .10, OAK)
for z in (-POST_Z, POST_Z):
    g.box(HALF_W * 2 + .45, .20, .20, 0, PLATE + .08, z, OAK_DARK)                    # tie beam
    g.box(.16, RIDGE - PLATE - .18, .16, 0, (PLATE + .18 + RIDGE) / 2, z, OAK)         # king post
    for sx in (-1, 1):                                                                # struts to the rafters
        g.span((sx * .08, PLATE + .35, z), (sx * .95, 3.30, z), .09, .09, OAK)
# The roof: two steep slopes shingled in courses, a ridge, barge boards. A
# slope's slab turns about Z by -sx*slope, which sends its length (local +X)
# down toward its own eave and its top face out along (sx sin, cos).
run, rise = HALF_W + .6, RIDGE - EAVE
slope = math.atan2(rise, run)
L = math.hypot(run, rise) + .08
for sx in (-1, 1):
    rz = -sx * slope
    nx, ny = sx * math.sin(slope), math.cos(slope)
    g.box(L, .10, ROOF_Z * 2, sx * run / 2, EAVE + rise / 2, 0, SHINGLE, rz=rz)
    for k in range(7):
        f = (k + .5) / 7
        px, py = sx * run * (1 - f), EAVE + rise * f
        g.box(.44, .05, ROOF_Z * 2 + .02, px + nx * .075, py + ny * .075, 0, SHINGLE_DARK if k % 2 else SHINGLE, rz=rz)
    for z in (-ROOF_Z - .03, ROOF_Z + .03):
        g.span((sx * (run + .05), EAVE - .08, z), (0, RIDGE + .06, z), .26, .07, OAK_DARK, up=(0, 0, 1))
g.box(.24, .18, ROOF_Z * 2 + .1, 0, RIDGE + .06, 0, SHINGLE_DARK)
# A lantern under the ridge on the front gable, on a short iron hanger.
g.box(.03, .65, .03, 0, RIDGE - .375, POST_Z + .15, IRON)
g.box(.26, .05, .26, 0, RIDGE - .84, POST_Z + .15, IRON)
g.box(.22, .30, .22, 0, RIDGE - 1.02, POST_Z + .15, LAMP)
g.box(.26, .05, .26, 0, RIDGE - 1.19, POST_Z + .15, IRON)
g.cyl(.17, .0, .12, 0, RIDGE - .76, POST_Z + .15, IRON, sides=4, ry=math.pi / 4)
g.finish(cam_at=(4.2, 2.2, 6.5), cam_look=(0, 2.1, 0), res=(800, 700), lens=35, sun=(55, 0, 150),
         extra_views=[('front', (0, 1.7, 7.0), (0, 2.3, 0))])
