# The Veilscar castle as a ruin (r178), after the owner's reference frame: a
# gutted keep on the cliff above the falls, its walls standing to ragged
# heights, tall broken piers at its corners, arched openings through which
# the sky shows; a round tower broken off on a slant; the stump of another;
# the curtain wall along the lip fallen to stumps. Until now the game built
# the castle from whole boxes and cylinders: a solid keep with dark slits
# painted on, a round tower whole to its crenels and a curtain wall the
# length of the cliff, which from the wizard's crag read as a fortress, not
# the reference's ruin.
#
# Every wall is a row of slab segments, each with its own top, so its crown
# is ragged; an opening is where segments leave out a span of height, its top
# rounding over as an arch. The joints are paint (the 'masonry' style of
# _bake.py), baked with the occlusion into one texture.
#
# Local frame (game axes), centred on the keep (the game's s=51, t=-4, the
# plateau's top y=0): +Z is +s (back, away from the falls), +X is -t (the
# left as the crag sees it). The footprint is the game's: the keep 9 m square
# (its collider), the round tower at X -16 Z -6, the stump at X 15 Z -5, the
# curtain wall at Z -8.4 in the game's three segments, the side walls.
#
#   python tools/assets/veilscar-ruin.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset
from _bake import finish_baked

# (pale: the reference's stone stands lit grey against its sky; darker, the
# ruin was a silhouette)
STONE = (0.68, 0.69, 0.66)
STONE2 = (0.60, 0.61, 0.59)
STONE3 = (0.52, 0.54, 0.52)

a = Asset('veilscar-ruin', seed=1780)
r = a.rng


def wall(x0, z0, x1, z1, tops, thick, holes=(), seg=1.0, base=-.8, outward=None):
    """A wall from (x0, z0) to (x1, z1): segments about seg wide, each a slab
    from base to tops(u) (u from 0 to 1 along the wall), less any opening.
    holes: (u0, u1, sill, crown) openings; an opening's top rounds over from
    its crown down to its sides, a semicircle on the span."""
    L = math.hypot(x1 - x0, z1 - z0)
    dx, dz = (x1 - x0) / L, (z1 - z0) / L
    ry = math.atan2(-dz, dx)
    n = max(1, round(L / seg))
    w = L / n
    for i in range(n):
        u = (i + .5) / n
        cx, cz = x0 + dx * L * u, z0 + dz * L * u
        top = tops(u)
        spans = [(base, top)]
        for (u0, u1, sill, crown) in holes:
            if not (u0 <= u <= u1):
                continue
            half = (u1 - u0) * L / 2
            off = (u - (u0 + u1) / 2) * L
            spring = crown - half
            lid = spring + math.sqrt(max(0.0, half * half - off * off))
            out = []
            for (y0, y1) in spans:
                if y1 <= sill or y0 >= lid:
                    out.append((y0, y1))
                    continue
                if y0 < sill:
                    out.append((y0, sill))
                if y1 > lid:
                    out.append((lid, y1))
            spans = out
        col = (STONE, STONE2, STONE3)[i % 3]
        for (y0, y1) in spans:
            if y1 - y0 < .25:
                continue
            a.jbox(w * 1.02, y1 - y0, thick * r.uniform(.94, 1.06), cx, (y0 + y1) / 2, cz, col, jit=.03, ry=ry)


def ragged(lo, hi, peaks=(), dips=(), seed=0):
    """A wall's crown: noise between lo and hi, with peaks (u, height, width)
    standing up and dips (u, height, width) broken down."""
    phase = [r.uniform(0, 6.28) for _ in range(3)]

    def f(u):
        # (broad swells, no fine teeth: with them the crowns were rows of
        # spikes, organ pipes, where the reference's broken walls are blunt)
        h = lo + (hi - lo) * (.5 + .32 * math.sin(u * 7.0 + phase[0]) + .12 * math.sin(u * 15.0 + phase[1]))
        for (pu, ph, pw) in peaks:
            k = max(0.0, 1 - abs(u - pu) / pw)
            h = max(h, h + (ph - h) * k * k * (3 - 2 * k))
        for (du, dh, dw) in dips:
            k = max(0.0, 1 - abs(u - du) / dw)
            h = min(h, h + (dh - h) * k * k * (3 - 2 * k))
        return h + r.uniform(-.1, .1)
    return f


def ring(cx, cz, rad, tops, thick, sides=14, holes=(), base=-.8):
    """A round tower as a ring of slabs, tops(u) by the angle (u 0 to 1)."""
    for k in range(sides):
        u0, u1 = k / sides, (k + 1) / sides
        a0, a1 = u0 * math.tau, u1 * math.tau
        x0, z0 = cx + math.cos(a0) * rad, cz + math.sin(a0) * rad
        x1, z1 = cx + math.cos(a1) * rad, cz + math.sin(a1) * rad
        wall(x0, z0, x1, z1, lambda u, k=k: tops((k + u) / sides), thick, seg=99,
             holes=[(0, 1, s, c) for (hk, s, c) in holes if hk == k], base=base)


H = 4.5   # half the keep's side, outer face
T = 1.4   # its walls' thickness
# (its heights a third over the first cut's: beside the reference's castle
# it stood small in the frame; taller, not wider, so it keeps to its collider)
S = 1.33


def kwall(x0, z0, x1, z1, tops, thick, holes=()):
    # (segments half as wide again: a metre each, the broken crowns read as
    # a comb of sticks; the reference's walls break in broad fragments)
    wall(x0, z0, x1, z1, lambda u: tops(u) * S, thick, holes=[(u0, u1, s * S, c * S) for (u0, u1, s, c) in holes], seg=1.5)


# The keep. Its front, toward the falls and the crag: broken down in the
# middle to a great arch, two windows high on either side, a tall pier at
# each end, the left one the tallest thing on the cliff.
kwall(H, -H + T / 2, -H, -H + T / 2,
     ragged(11.0, 14.5, peaks=((.08, 19.0, .22), (.92, 16.5, .20)), dips=((.52, 8.6, .26),)), T,
     holes=((.40, .64, 1.0, 6.4), (.13, .27, 9.0, 12.2), (.74, .86, 9.4, 12.0)))
# its back: higher, one window, a broken notch
kwall(-H, H - T / 2, H, H - T / 2,
     ragged(12.5, 15.5, peaks=((.12, 17.5, .24),), dips=((.68, 9.5, .20),)), T,
     holes=((.30, .44, 8.0, 11.0),))
# its sides: falling away toward the front, a window each
kwall(H - T / 2, H, H - T / 2, -H,
     ragged(10.5, 14.0, peaks=((.92, 19.0, .20),), dips=((.45, 7.5, .24),)), T,
     holes=((.20, .34, 9.0, 11.6), (.62, .74, 3.0, 5.6)))
kwall(-H + T / 2, -H, -H + T / 2, H,
     ragged(9.0, 13.0, peaks=((.08, 16.5, .20),), dips=((.60, 6.0, .24),)), T,
     holes=((.70, .82, 8.6, 11.2),))
# the floor inside, deep in rubble
for k in range(9):
    a.rock(r.uniform(1.0, 2.2), r.uniform(.5, 1.2), r.uniform(1.0, 2.0), r.uniform(-2.6, 2.6), .2, r.uniform(-2.6, 2.6), STONE3, jag=.3,
           ry=r.uniform(0, 3))

# The round tower, broken off on a slant: whole to 12 m on its far side, down
# to 6 on the side toward the falls, a slit or two.
ring(-16, -6, 3.15, lambda u: 11.5 + 4.6 * math.cos((u - .25) * math.tau) + r.uniform(-.4, .4), 1.0, sides=16,
     holes=((4, 3.4, 5.2), (9, 8.0, 9.8)))
# the stump of the other, gutted
ring(15, -5, 2.75, lambda u: 4.0 + 2.6 * math.cos((u - .6) * math.tau) + r.uniform(-.5, .5), 1.0, sides=14)

# The curtain wall along the lip, the game's three segments (its colliders),
# fallen to stumps between merlon-high fragments.
# (the middle one standing high, an arch through it, as the reference's
# central range does: low, the ruin was a thin keep and two towers)
for (xa, xb, lo, hi) in ((13.2, 5.4, 2.4, 5.6), (-10.8, -13.4, 1.8, 4.6)):
    wall(xa, -8.4, xb, -8.4, ragged(lo, hi, dips=((r.uniform(.3, .7), lo * .6, .2),)), 1.6, seg=1.1)
wall(2.2, -8.4, -7.0, -8.4, ragged(7.5, 10.5, peaks=((.12, 12.0, .14),), dips=((.82, 4.5, .16),)), 1.6, seg=1.1,
     holes=((.36, .62, 1.4, 6.8),))
# the side walls, lower, back from the lip
for (xa, za, xb, zb, lo, hi) in ((-13.4, -8.4, -17.5, 4.5, 1.6, 4.2), (13.2, -8.4, 16.5, 4.0, 1.4, 3.4), (-17.5, 4.5, -6.0, 6.0, 1.0, 2.6)):
    wall(xa, za, xb, zb, ragged(lo, hi), 1.3, seg=1.0)
# fallen blocks along the foot of the walls
for k in range(18):
    x, z = r.uniform(-18, 17), r.uniform(-11, 7)
    if abs(x) < 4.8 and abs(z) < 4.8:
        continue
    s = r.uniform(.5, 1.2)
    a.rock(s * 1.4, s * .8, s * 1.1, x, s * .2, z, (STONE2, STONE3)[k % 2], jag=.25, ry=r.uniform(0, 3))

finish_baked(a, cam_at=(10.0, 16.0, -70.0), cam_look=(0.0, 8.0, 0.0), res=(1000, 600), lens=40,
             extra_views=[('close', (-6.0, 9.0, -24.0), (0.0, 9.0, 0.0))],
             size=1024, style='masonry', jpeg_quality=72, ao_power=.9,
             style_args=dict(block=(1.1, .55), moss=(.20, .28, .16), moss_cover=(.48, .60)))
