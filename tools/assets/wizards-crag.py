# The wizard's crag (r175): the rock Orren stands on to watch the Veilscar,
# after the owner's reference frame, where the wizard stands on a pale,
# streaked outcrop high over a green valley. Until r175 he stood on the flat
# crown of a grassy knoll, which the terrain's 6 m grid could not make sharp:
# from behind him it read as a grey slab. This is the rock on top of that
# knoll: a flat-topped crag with a sheer front toward the falls, fractured
# columns down its sides, and rough slabs stepping down its back so a player
# can climb up beside him.
#
# Local frame (game axes): +Z faces the falls, y=0 is the knoll's crown. The
# standing top is at y=TOP, x -2.3..2.3, z -1.6..2.0 (the game puts a deck
# there); the steps run down the back, z -2.2 to -10, x -1.4..1.4 (the game
# puts a stair there). Everything stands inside x -6..6, z -11..5.
#
#   python tools/assets/wizards-crag.py
#
# (r177) Baked, as Orren is: the blocks below are fused into one rock and
# worn round (_bake.sculpt_rock), then painted (grained, streaked, speckled,
# moss on what faces up) and the paint and its occlusion baked into one
# texture. Flat-shaded with the tiled rock texture, the blocks had read as
# stacked lavender paving under him; the reference's rock is one pale grey
# mass, mottled dark. Its colours grey for the same reason.
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset
from _bake import finish_baked

PALE = (0.80, 0.80, 0.82)
PALE2 = (0.68, 0.68, 0.71)
DARK = (0.44, 0.43, 0.47)
MOSS = (0.38, 0.50, 0.32)

TOP = 6.5

a = Asset('wizards-crag', seed=1750)
r = a.rng

# The body: columns of fractured rock round a core, tallest at the front, the
# outer ones lower and leaning out a little, so the silhouette breaks.
a.jbox(5.2, TOP + 1.0, 4.4, 0, (TOP - 1.0) / 2, .2, PALE2, jit=.06)
for k in range(16):
    ang = k / 16 * math.tau
    rad = r.uniform(2.6, 3.6)
    x, z = math.cos(ang) * rad, math.sin(ang) * rad * .9 + .3
    front = z > 1.2
    back = z < -1.6
    h = TOP - (.15 if front else r.uniform(.4, 1.6) if not back else r.uniform(1.8, 3.0))
    w = r.uniform(1.4, 2.4)
    col = (PALE, PALE2, DARK)[k % 3]
    a.jbox(w, h + 1.2, w * r.uniform(.8, 1.2), x, (h - 1.2) / 2, z, col, jit=.12, ry=ang + r.uniform(-.3, .3),
           rz=r.uniform(-.06, .06), taper=r.uniform(.72, .9), top_color=MOSS if r.random() < .3 else None)
# Streaks down the front: thin dark and pale slabs set into the face.
for k in range(7):
    x = -2.4 + k * .8 + r.uniform(-.2, .2)
    h = r.uniform(2.5, TOP - .5)
    a.jbox(.35, h, .3, x, TOP - .3 - h / 2, 3.1 + r.uniform(-.2, .3), DARK if k % 2 else PALE, jit=.08, taper=.7)

# The standing top: two broad slabs, nearly level, the front one a hand
# higher at its lip, worn pale; jagged stones round the lip.
a.jbox(4.8, .6, 2.2, 0, TOP - .3, .95, PALE, jit=.03, top_color=PALE)
a.jbox(4.4, .6, 2.0, .1, TOP - .32, -1.0, PALE2, jit=.03, top_color=PALE2)
# (r177) no stones along the front lip now: from behind him they stood
# between the vista and the drop, a row of blobs. The reference's rock ends
# at its edge, the valley below it. (The stream of random numbers still
# turns over as it did, so everything after is where it was.)
for k in range(6):
    for _ in range(5 + 72):          # its five arguments' draws, and the 72 rock() makes for its facets
        r.random()
for side in (-1, 1):
    for k in range(3):
        a.rock(r.uniform(.6, 1.0), r.uniform(.5, 1.1), r.uniform(.6, 1.0), side * 2.55, TOP + .15, 1.4 - k * 1.2, PALE2,
               jag=.35, ry=r.uniform(0, 3), top_color=MOSS if k == 2 else None)

# The steps down the back: rough slabs, each a little under a metre down from
# the one before, set on rubble.
N = 7
for k in range(N):
    z = -2.2 - (k + .5) * (7.8 / N)
    y = TOP - (k + 1) * (TOP / N)
    a.jbox(3.0 + r.uniform(-.2, .3), .7, 7.8 / N + .25, r.uniform(-.15, .15), y + .35 - .25, z, (PALE2, PALE)[k % 2],
           jit=.05, ry=r.uniform(-.06, .06), top_color=MOSS if k % 3 == 2 else None)
    a.jbox(3.4, max(.4, y), 7.8 / N + .1, 0, max(.4, y) / 2 - .4, z, DARK, jit=.1)
    for side in (-1, 1):
        a.rock(r.uniform(.7, 1.1), r.uniform(.6, 1.2), r.uniform(.7, 1.1), side * r.uniform(1.9, 2.3), y + .3, z, PALE2,
               jag=.3, ry=r.uniform(0, 3))

# Fallen blocks round the foot.
for k in range(14):
    ang = r.uniform(0, math.tau)
    rad = r.uniform(4.2, 5.6)
    s = r.uniform(.7, 1.6)
    x, z = math.cos(ang) * rad, math.sin(ang) * rad * .8
    if z < -2 and abs(x) < 2.4:
        continue
    a.rock(s * 1.3, s, s * 1.1, x, s * .3, z, (PALE2, DARK)[k % 2], jag=.3, ry=r.uniform(0, 3),
           top_color=MOSS if k % 3 == 0 else None)

# (the deck calmed: roughened a quarter as much where he and the player stand)
finish_baked(a, cam_at=(7.0, 6.0, 12.0), cam_look=(0, 3.4, 0), res=(800, 600), lens=30, sun=(50, 0, 30),
             extra_views=[('back', (-7.0, 7.0, -14.0), (0, 3.0, -4.0)), ('deck', (1.2, TOP + 2.0, -3.4), (0, TOP, 1.6))],
             size=1024, style='rock', jpeg_quality=80,
             # light against dark three times as strongly as the paint first had (measured in the game against
             # the reference's rock, which also carries next to no green)
             # and its dark patches are stains, brown-green, on its top
             style_args=dict(moss=(.11, .12, .08), speckle=.9, streaks=.5, mottle=(.30, 1.45), patches=(4.0, .50, 1.30),
                             moss_cover=(.50, .60), spread=.09),
             shape=dict(voxel=.08, smooth=(.5, 3), rough=(.12, .6), tris=10000, calm=(-2.3, 2.3, -1.7, 2.1, TOP - .45)),
             normals=True)
