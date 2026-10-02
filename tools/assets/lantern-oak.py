# The Lantern Oak (r143): the great bare tree at the centre of the Lantern
# Grove, hung with lanterns people light for someone they have lost or are
# waiting for. A short massive trunk with root flares, four great limbs that
# spread and rise, each forking twice more; lanterns hang on short cords from
# the ends of the lower branches, their panes glowing (vertex-alpha glow
# mask, warm in the game).
#
# Local frame (game axes): y=0 is the ground at the trunk; the tree's widest
# spread is roughly +-9 m.
#
#   python tools/assets/lantern-oak.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset
from mathutils import Vector

BARK = (.30, .26, .24)
BARK2 = (.24, .21, .20)
LANTERN = (.16, .15, .14)
GLOW = (1.0, .78, .45, .1)
CORD = (.20, .17, .15)
RIBBON = (.55, .22, .24)

a = Asset('lantern-oak', seed=1809)
r = a.rng
tips = []


def limb(p0, d, length, r0, r1, depth, color):
    # One bough: a tube along a gently curving path, then its forks.
    pts, radii = [], []
    n = 5 if depth < 2 else 3
    bend = Vector((r.uniform(-.25, .25), r.uniform(-.15, .1), r.uniform(-.25, .25)))
    p = Vector(p0)
    dd = Vector(d).normalized()
    for i in range(n + 1):
        f = i / n
        pts.append(tuple(p))
        radii.append(r0 + (r1 - r0) * f)
        dd = (dd + bend * .35).normalized()
        dd.y += -.025 if depth < 1 else (.05 if depth < 2 else -.02)   # great limbs level off, boughs rise, twigs droop a little
        dd.normalize()
        p = p + dd * (length / n)
    a.tube(pts, radii, color, sides=6 if depth < 2 else 4, ref=(0, 0, 1) if abs(dd.z) < .9 else (1, 0, 0), cap0=depth < 1, cap1=depth >= 3)
    end, dir_end = Vector(pts[-1]), dd
    if depth >= 3:
        tips.append((end, dir_end))
        return
    forks = 2 if depth else 3
    for k in range(forks):
        ang = (k - (forks - 1) / 2) * r.uniform(.5, .8)
        # turn the direction about the vertical and tilt it outward
        c, s = math.cos(ang), math.sin(ang)
        nd = Vector((dir_end.x * c - dir_end.z * s, dir_end.y + r.uniform(-.2, .15), dir_end.x * s + dir_end.z * c))
        limb(end, nd, length * r.uniform(.58, .72), r1, r1 * .55, depth + 1, BARK2 if depth else color)


# Trunk with root flares.
trunk = [(0, -.3, 0), (0, 1.4, .05), (.12, 2.9, 0), (.05, 4.1, -.05)]
a.tube(trunk, [1.25, 1.0, .9, .82], BARK, sides=11)
for k in range(6):
    ang = k / 6 * math.tau + .3
    a.tube([(math.cos(ang) * .5, .9, math.sin(ang) * .5), (math.cos(ang) * 1.4, .15, math.sin(ang) * 1.4),
            (math.cos(ang) * 2.2, -.2, math.sin(ang) * 2.2)], [.42, .3, .12], BARK, sides=6, ref=(0, 1, 0))
# Five great limbs from the crown of the trunk, spreading wide and low the
# way an old oak's do, rather than climbing.
for k in range(5):
    ang = k / 5 * math.tau + r.uniform(-.25, .25)
    d = Vector((math.cos(ang), r.uniform(.42, .68), math.sin(ang)))
    limb((math.cos(ang) * .35, 3.7 + r.uniform(-.3, .3), math.sin(ang) * .35), d, r.uniform(5.2, 6.4), .6, .36, 0, BARK)

# Lanterns on cords from the lowest tips (and a few ribbons tied on).
hung = 0
tips.sort(key=lambda t: t[0].y)
for (end, d) in tips:
    if hung >= 30 or end.y > 11.0:
        continue
    cord = r.uniform(.6, 1.8)
    top = end + Vector((0, -.05, 0))
    cord = min(cord, top.y - 2.6)             # every lantern hangs above head height
    if cord < .35:
        continue
    bottom = top + Vector((0, -cord, 0))
    a.box(.025, cord, .025, top.x, (top.y + bottom.y) / 2, top.z, CORD)
    a.cyl(.13, .0, .12, bottom.x, bottom.y - .02, bottom.z, LANTERN, sides=4, ry=math.pi / 4)
    a.box(.18, .24, .18, bottom.x, bottom.y - .2, bottom.z, GLOW)
    a.box(.2, .03, .2, bottom.x, bottom.y - .33, bottom.z, LANTERN)
    if hung % 3 == 1:
        a.leaf(tuple(end), tuple(end + Vector((.05, -.9, .05))), .09, .01, RIBBON, (0, 0, 1), segs=3, quill=.9, belly=.5, round_tip=.1)
    hung += 1
print('lanterns hung:', hung, 'of', len(tips), 'tips')

a.finish(cam_at=(19.0, 4.0, 17.0), cam_look=(0, 5.0, 0), res=(900, 700), lens=30, sun=(55, 0, 150))

# ---- the sitting stones -----------------------------------------------------------
# One low boulder, placed eight times round the tree (and once, larger, as the
# stone the candles stand on). A rock with a broad flat top to sit on, rather
# than the kit's domed one: four rings of jittered points, the top ring wide.
# y=0 is the ground; the foot is sunk .1 so it never shows a gap on the mesa's
# small roughness. The game textures it as rock.
s = Asset('grove-stone', seed=1810)
rng = s.rng
W2, H2, D2, SIDES = 1.3, .55, .78, 8
rings = [(-.1, .82), (.12, 1.0), (.36, .96), (.45, .78)]
v, f = [], []
for ri, (yy, rr) in enumerate(rings):
    for i in range(SIDES):
        ang = (i + rng.uniform(-.18, .18) + ri * .3) / SIDES * math.tau
        k = rr * (1 + rng.uniform(-.12, .12))
        v.append((math.cos(ang) * k * W2 / 2, yy + (rng.uniform(-.025, .025) if ri == len(rings) - 1 else 0), math.sin(ang) * k * D2 / 2))
for ri in range(len(rings) - 1):
    for i in range(SIDES):
        j = (i + 1) % SIDES
        f.append((ri * SIDES + i, (ri + 1) * SIDES + i, (ri + 1) * SIDES + j, ri * SIDES + j))
f.append(tuple(range(SIDES)))
top = (len(rings) - 1) * SIDES
f.append(tuple(reversed(range(top, top + SIDES))))
s.mesh(v, f, [(.50, .49, .52)] * (len(f) - 1) + [(.56, .55, .56)])
s.finish(cam_at=(1.3, .9, 1.6), cam_look=(0, .2, 0), res=(500, 400), lens=35)
