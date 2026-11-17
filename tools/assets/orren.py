# Orren of the Broken Hall (r176), second sculpt: one smooth, textured figure.
#
# The owner, on the first sculpt (fused clay under kit-built blades of hair and
# a faceted hat, flat-shaded): "far too low quality and high poly. I could let
# everything else slide if the wizard looked cohesive." It read as shards. The
# reference's wizard is a PlayStation 2-era figure: few polygons, but every
# surface smooth-shaded and painted. So this one is built the way those were:
#
#   - clean lofted surfaces (rings along a path), no fused clay: a broad robe
#     with pipe folds deepening to the hem, a bell sleeve hanging from the arm
#     that holds the staff, a floppy hat whose crown bends over to his left, a
#     brim that droops and waves, hair as one sheet lying on his back that
#     splits into locks only at its hem, a long beard, a gnarled staff forked
#     round a crystal; the head alone is a fused sculpt (nose, brow, cheeks);
#   - smooth normals everywhere but the crystal, and on the hair normals that
#     point out from the body, so it shades as one soft mass;
#   - a texture: each surface's procedural paint (cloth mottled and streaked
#     down its folds, hair in fine strands, bark) baked with Cycles into one
#     atlas, darkened by two bakes of ambient occlusion (broad and fine).
#
# Proportions are measured off the reference (tools/video-frames/reference/
# wizard-vista.jpg) at 327 px to the metre: 0.6 m across the shoulders, 0.73
# at the hem, a brim 0.68 m wide, the hat's tip half a metre up and 0.37 m to
# his left, the staff 2.5 m, his hand on it at 1.22 m.
#
# Local frame (game axes): he faces +Z, his right hand is on -X, y=0 is his
# feet. Writes assets/orren.glb (two materials: the atlas, and the crystal's
# emission), tools/assets/_bake-orren.jpg and the previews.
#
# (r177) After the reference again, close up: the hair a part of its own on
# the same atlas, each lock fading out over its lower half by its vertices'
# alpha (its points had ended in a row of teeth), and whiter; the staff's
# fork a thick knotted branch round the crystal, not two thin horns; the
# crystal deeper violet and glowing a third as hard. Three materials now:
# the atlas, the hair (the atlas, blended), the crystal.
#
#   python tools/assets/orren.py            the whole build
#   ORREN_FAST=1 python tools/assets/orren.py   previews of the forms only (no bake, no export)
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy, bmesh
import numpy as np
from mathutils import Vector, Matrix
from _kit import g2b, HERE, ROOT

FAST = bool(os.environ.get('ORREN_FAST'))
SEED = 1760
rng = random.Random(SEED)
SIZE = 1024                      # the atlas
MATS = ['robe', 'hat', 'hair', 'skin', 'wood', 'band', 'shoe', 'eye', 'iris', 'crystal']


def M(name):
    return MATS.index(name)


class Buf:
    def __init__(self):
        # A: (r177) an alpha for a vertex, where it is not 1 (the hair's tips)
        self.V, self.F, self.FM, self.N, self.A = [], [], [], {}, {}


main, head = Buf(), Buf()
cur = main


# ---- curves ---------------------------------------------------------------------
def catmull(P, s):
    n = len(P)
    i = min(int(s), n - 2)
    t = s - i
    p0, p1, p2, p3 = P[max(i - 1, 0)], P[i], P[i + 1], P[min(i + 2, n - 1)]
    return tuple(.5 * (2 * b + (c - a) * t + (2 * a - 5 * b + 4 * c - d) * t * t + (3 * b - a - 3 * c + d) * t * t * t)
                 for a, b, c, d in zip(p0, p1, p2, p3))


def resample(P, k):
    return [catmull(P, i / k) for i in range((len(P) - 1) * k)] + [tuple(P[-1])]


def smoothstep(a, b, x):
    t = min(1.0, max(0.0, (x - a) / (b - a)))
    return t * t * (3 - 2 * t)


# ---- surfaces -------------------------------------------------------------------
def loft(rings, mat, cap0=None, cap1=None, closed=True, face=None):
    """Quads between successive rings of points. cap0/cap1: True closes an end
    flat at its centre, a point closes it to that apex. The surface faces out
    from the rings' centres, or toward `face` (a direction) for discs and
    sheets, whichever way the rings happen to run."""
    b = cur
    n = len(rings[0])
    base = len(b.V)
    for ring in rings:
        assert len(ring) == n
        b.V.extend(Vector(p) for p in ring)
    span = n if closed else n - 1
    quads = []
    for i in range(len(rings) - 1):
        for j in range(span):
            jj = (j + 1) % n
            quads.append((base + i * n + j, base + i * n + jj, base + (i + 1) * n + jj, base + (i + 1) * n + j))
    i = (len(rings) - 1) // 2
    q = quads[min(len(quads) - 1, i * span + span // 4)]
    a, bb, c, d = (b.V[k] for k in q)
    nrm = (bb - a).cross(d - a)
    if face is not None:
        flip = nrm.dot(Vector(face)) < 0
    else:
        cen = sum((Vector(p) for p in rings[i]), Vector()) / n
        flip = nrm.dot((a + bb + c + d) / 4 - cen) < 0
    for q in quads:
        b.F.append(tuple(reversed(q)) if flip else q)
        b.FM.append(M(mat))
    for cap, idx, start in ((cap0, 0, True), (cap1, len(rings) - 1, False)):
        if cap is None or cap is False:
            continue
        apex = sum((Vector(p) for p in rings[idx]), Vector()) / n if cap is True else Vector(cap)
        ci = len(b.V)
        b.V.append(apex)
        for j in range(span):
            jj = (j + 1) % n
            tri = (base + idx * n + j, base + idx * n + jj, ci)
            if start != flip:
                tri = (tri[1], tri[0], tri[2])
            b.F.append(tri)
            b.FM.append(M(mat))
    return base


def frames(path, ref=None):
    P = [Vector(p) for p in path]
    n = len(P)
    T = [(P[min(i + 1, n - 1)] - P[max(i - 1, 0)]).normalized() for i in range(n)]
    r = Vector(ref) if ref is not None else (Vector((0, 0, 1)) if abs(T[0].z) < .9 else Vector((1, 0, 0)))
    u = (r - T[0] * r.dot(T[0])).normalized()
    U = [u]
    for i in range(1, n):
        u = U[-1] - T[i] * U[-1].dot(T[i])
        u.normalize()
        U.append(u)
    W = [T[i].cross(U[i]) for i in range(n)]
    return P, T, U, W


def tube(path, radii, n=10, mat='robe', cap0=True, cap1=True, mod=None, ref=None):
    P, T, U, W = frames(path, ref)
    rings = []
    for i in range(len(P)):
        r = radii[i]
        ru, rw = (r if isinstance(r, (tuple, list)) else (r, r))[:2]
        ring = []
        for j in range(n):
            th = j / n * math.tau
            k = mod(i, th, P, T, U, W) if mod else 1.0
            ring.append(P[i] + U[i] * (math.cos(th) * ru * k) + W[i] * (math.sin(th) * rw * k))
        rings.append(ring)
    return loft(rings, mat, cap0, cap1)


def ellipsoid(c, r, mat, n=12, m=8):
    c = Vector(c)
    rings = []
    for i in range(1, m):
        lat = -math.pi / 2 + math.pi * i / m
        cl, sl = math.cos(lat), math.sin(lat)
        rings.append([c + Vector((r[0] * cl * math.sin(j / n * math.tau), r[1] * sl, r[2] * cl * math.cos(j / n * math.tau)))
                      for j in range(n)])
    return loft(rings, mat, cap0=c - Vector((0, r[1], 0)), cap1=c + Vector((0, r[1], 0)))


def flat_face(pts, mat, centre):
    """One face with corners of its own and its own normal: the crystal's facets."""
    pts = [Vector(p) for p in pts]
    nrm = (pts[1] - pts[0]).cross(pts[2] - pts[0]).normalized()
    if nrm.dot(sum(pts, Vector()) / len(pts) - Vector(centre)) < 0:
        pts.reverse()
        nrm = -nrm
    i = len(cur.V)
    cur.V.extend(pts)
    cur.F.append(tuple(range(i, i + len(pts))))
    cur.FM.append(M(mat))
    for k in range(len(pts)):
        cur.N[i + k] = nrm


# ---- the robe ---------------------------------------------------------------------
# Rings from the hem to the collar: (height, half width, half depth, centre z,
# fold depth). Broad and nearly straight-sided, as the reference's is from
# behind; the back rounded at the shoulder blades, the head carried forward.
ROBE = [
    (0.015, .385, .355, .012, .120),
    (0.14, .372, .338, .008, .112),
    (0.34, .352, .312, .004, .096),
    (0.56, .332, .286, .000, .078),
    (0.78, .314, .262, .000, .058),
    (0.98, .302, .244, -.002, .040),
    (1.14, .298, .232, -.008, .026),
    (1.27, .300, .226, -.016, .014),
    (1.37, .302, .220, -.024, .006),
    (1.44, .294, .206, -.024, .0),
    (1.495, .262, .180, -.014, .0),
    (1.530, .196, .146, .004, .0),
    (1.555, .128, .116, .022, .0),
    (1.580, .086, .090, .038, .0),
    (1.610, .072, .076, .048, .0),
]
NR = 40


def robe_fold(th, y):
    # Nine pipe folds, uneven in width and depth, wandering a little as they fall.
    w = th + .16 * math.sin(2 * th + 1.3) + .07 * math.sin(5 * th + .5) + .05 * math.sin(2.3 * y + th)
    depth = .62 + .38 * math.sin(3 * th + 2.0 + .6 * y)
    f = math.cos(9 * w + .4) + .45 * math.cos(17 * w + 2.1) + .30 * math.cos(4 * w + 4.0)
    return depth * f / 1.75


def robe_at(y):
    """The robe's ellipse at a height: half width, half depth, centre z."""
    ys = [r[0] for r in ROBE]
    return tuple(float(np.interp(y, ys, [r[k] for r in ROBE])) for k in (1, 2, 3))


def build_robe():
    rings = []
    for (y, rx, rz, cz, amp) in resample(ROBE, 2):
        ring = []
        for j in range(NR):
            th = j / NR * math.tau
            f = robe_fold(th, y) if amp > 0 else 0.0
            k = 1 + amp * f
            lift = .018 * max(0.0, 1 - y / .2) * (f + .4)          # the hem rides up over each fold
            ring.append(Vector((rx * math.sin(th) * k, max(.004, y + lift), cz + rz * math.cos(th) * k)))
        rings.append(ring)
    loft(rings, 'robe', cap0=True, cap1=True)


# ---- the sleeves --------------------------------------------------------------------
def sleeve(ctrl, prof, n=16, k=3, mat='robe', cuff=True):
    """A sleeve along the arm: prof is (half width, radius up, radius down,
    lag) at each control point. The underside hangs (radius down) and trails
    back toward the elbow (lag), which is the bell of a wizard's sleeve. The
    cuff turns in on itself, so its opening shows dark."""
    P = [Vector(p) for p in resample(ctrl, k)]
    R = resample(prof, k)
    up = Vector((0, 1, 0))
    rings = []
    for i, p in enumerate(P):
        T = (P[min(i + 1, len(P) - 1)] - P[max(i - 1, 0)]).normalized()
        U = up - T * up.dot(T)
        if U.length < .2:
            U = Vector((0, 0, 1)) - T * T.z
        U.normalize()
        W = T.cross(U)
        a, bu, bd, lag = R[i]
        t = i / (len(P) - 1)
        ring = []
        for j in range(n):
            th = j / n * math.tau
            c, s = math.cos(th), math.sin(th)
            wr = 1 + .045 * math.sin(i * 2.4 + 3 * th) * (1 - abs(2 * t - 1))      # creases where the arm bends
            hang = 1 + (.07 * math.cos(5 * th + i * .3) if s < 0 else 0.0) * t      # drape in what hangs
            q = p + W * (c * a * wr) + U * (s * (bu if s >= 0 else bd * hang) * wr)
            if s < 0:
                q -= T * (-s * bd * lag)
            ring.append(q)
        rings.append(ring)
    if cuff:
        last = rings[-1]
        cen = sum(last, Vector()) / n
        T = (P[-1] - P[-2]).normalized()
        rings.append([cen + (q - cen) * .86 - T * .035 for q in last])
        rings.append([cen + (q - cen) * .60 - T * .12 for q in last])
    loft(rings, mat, cap0=True, cap1=True)
    return P


def build_sleeves():
    # his right arm: out from the shoulder, bent, the forearm forward and out
    # to the staff; the sleeve's bell hangs 0.4 m under the wrist
    sleeve([(-.205, 1.455, -.012), (-.300, 1.385, -.004), (-.392, 1.215, .040), (-.452, 1.190, .155), (-.498, 1.218, .262), (-.505, 1.228, .300)],
           [(.082, .082, .090, .0), (.108, .100, .120, .0), (.120, .108, .170, .10), (.118, .104, .260, .26), (.112, .096, .345, .36), (.106, .090, .385, .40)])
    # his left arm hangs, a little forward; the hand just out of the cuff
    sleeve([(.205, 1.455, -.012), (.298, 1.380, -.006), (.345, 1.150, .020), (.338, .985, .075), (.318, .860, .130), (.312, .815, .148)],
           [(.082, .082, .090, .0), (.106, .100, .112, .0), (.116, .110, .118, .0), (.118, .112, .124, .04), (.122, .114, .134, .08), (.124, .114, .140, .10)], n=14)


# ---- the hat --------------------------------------------------------------------------
HAT_AT = Vector((0.0, 1.795, .062))
HAT_ROT = Matrix.Rotation(math.radians(-5), 3, 'Z') @ Matrix.Rotation(math.radians(-3), 3, 'X')
BRIM_IN, BRIM_OUT, BRIM_N = .150, .345, 32


def hat_pt(p):
    return HAT_AT + HAT_ROT @ Vector(p)


def brim_y(r, th):
    t = (r - BRIM_IN) / (BRIM_OUT - BRIM_IN)
    t = max(0.0, t)
    droop = -.070 * t ** 1.7
    droop -= .035 * t * t * max(0.0, math.cos(th - math.radians(140)))          # lower behind his left shoulder
    wave = .026 * t * t * math.sin(2 * th + .7) + .012 * t * t * math.sin(5 * th + 2.0)
    return droop + wave


def build_hat():
    radii = [BRIM_IN, .195, .245, .295, .330, BRIM_OUT]
    top = [[hat_pt((r * math.sin(j / BRIM_N * math.tau), brim_y(r, j / BRIM_N * math.tau), r * math.cos(j / BRIM_N * math.tau)))
            for j in range(BRIM_N)] for r in radii]
    loft(top, 'hat', face=(0, 1, 0))
    under_r = [BRIM_OUT, .330, .295, .245, .195, .150, .100]
    under = [[hat_pt((r * math.sin(j / BRIM_N * math.tau), brim_y(r, j / BRIM_N * math.tau) - (.006 if r == BRIM_OUT else .014), r * math.cos(j / BRIM_N * math.tau)))
              for j in range(BRIM_N)] for r in under_r]
    loft([top[-1], under[0]], 'hat')                                                # the rim
    loft(under, 'hat', face=(0, -1, 0))
    # The crown: a wide cone that leans over to his left and a little back,
    # its tip flopping; soft folds round it, and a buckle of cloth on the
    # inside of the bend.
    ctrl = [(0, 0, 0), (.004, .075, -.003), (.022, .155, -.010), (.060, .245, -.024), (.120, .330, -.044),
            (.200, .402, -.066), (.282, .456, -.088), (.350, .492, -.106), (.398, .508, -.118)]
    rad = [.160, .152, .134, .112, .088, .064, .041, .022, .007]
    P = [hat_pt(p) for p in resample(ctrl, 2)]
    R = [r[0] for r in resample([(r,) for r in rad], 2)]
    nP = len(P)

    def crumple(i, th, P_, T, U, W):
        t = i / (nP - 1)
        inner = (T[min(i + 1, nP - 1)] - T[max(i - 1, 0)])
        k = 1 + .045 * math.sin(3 * th + t * 5.0) * math.sin(math.pi * t)
        if inner.length > 1e-4:
            inner.normalize()
            d = math.cos(th) * U[i].dot(inner) + math.sin(th) * W[i].dot(inner)
            k -= .16 * max(0.0, d) ** 2 * math.sin(math.pi * min(1.0, t * 1.25)) ** 2
            k += .05 * math.sin(t * 19.0) * max(0.0, d)                               # the buckles themselves
        return k
    tube(P, R, n=20, mat='hat', cap0=False, cap1=True, mod=crumple)
    # the band
    band = [[hat_pt((r * math.sin(j / 28 * math.tau), y, r * math.cos(j / 28 * math.tau))) for j in range(28)]
            for (y, r) in ((.004, .168), (.018, .171), (.040, .166), (.052, .160))]
    loft(band, 'band')


# ---- the hair ---------------------------------------------------------------------------
# One sheet from under the brim, round the back of the head, out over the
# shoulders and down the back: (height, half width, half depth, centre z, how
# far round it reaches, degrees each side of straight behind).
HAIR = [
    (0.90, .312, .268, .000, 50),
    (1.08, .307, .256, -.004, 54),
    (1.18, .310, .252, -.008, 57),
    (1.28, .314, .246, -.016, 60),
    (1.38, .320, .240, -.024, 64),
    (1.46, .316, .230, -.022, 76),
    (1.52, .240, .194, .004, 98),
    (1.58, .156, .154, .040, 112),
    (1.66, .124, .137, .060, 118),
    (1.74, .117, .129, .068, 118),
    (1.80, .109, .119, .070, 118),
]


def hair_at(y):
    ys = [r[0] for r in HAIR]
    return tuple(float(np.interp(y, ys, [r[k] for r in HAIR])) for k in (1, 2, 3, 4))


def hair_lock(f0, wf, y_top, y_tip, offset, seed, ncol=4, nrow=18, fade_from=.45):
    """One lock lying on the hair's shell: f0 is where it hangs, from -1 (his
    right) to 1 (his left), a fraction of how far round the shell reaches at
    each height, so locks that start round the sides of the head close in
    over the back as they fall; wf its width in those fractions. It narrows
    to a soft point over its last third and sways a little as it falls. Its
    normals point out from the body, so the locks shade as one mass."""
    lr = random.Random(seed)
    drift, sway, ph = lr.uniform(-.05, .05), lr.uniform(.008, .022), lr.uniform(0, math.tau)
    grid = []
    for i in range(nrow):
        s = i / (nrow - 1)
        y = y_top - (y_top - y_tip) * s ** .95
        rx, rz, cz, reach = hair_at(y)
        taper = 1 - .94 * smoothstep(.42, 1.0, s)
        row = []
        for j in range(ncol):
            u = -1 + 2 * j / (ncol - 1)
            f = f0 + drift * s + u * wf / 2 * taper
            phi = math.radians(reach) * f
            off = offset + .005 * (1 - u * u) + sway * math.sin(s * 5.5 + ph) * s
            p = Vector(((rx + off) * math.sin(phi), y, cz - (rz + off) * math.cos(phi)))
            nrm = Vector((math.sin(phi) / rx, .28, -math.cos(phi) / rz)).normalized()
            row.append((p, nrm))
        grid.append(row)
    phi0 = math.radians(hair_at((y_top + y_tip) / 2)[3]) * f0
    base = loft([[p for p, _ in row] for row in grid], 'hair', closed=False, face=(math.sin(phi0), 0, -math.cos(phi0)))
    # (r177) and it fades out over its lower half, so the locks' points do
    # not end in a row of teeth: lit by the glow on his back they read as
    # icicles. The reference's hair thins into wisps.
    for i, row in enumerate(grid):
        s = i / (nrow - 1)
        a = 1 - smoothstep(fade_from, 1.0, s)
        for j, (_, nrm) in enumerate(row):
            cur.N[base + i * ncol + j] = nrm
            if a < 1:
                cur.A[base + i * ncol + j] = a


def hair_layer(n, offset, tip_mid, tip_side, jitter, width, seed, shift=0.0):
    """A layer of locks side by side, overlapping, longest down the middle of
    his back and shorter toward his shoulders, each its own length."""
    lr = random.Random(seed)
    for k in range(n):
        f0 = -1 + 2 * (k + .5 + shift) / n
        f0 = max(-1.0, min(1.0, f0 + lr.uniform(-.25, .25) / n))
        tip = tip_mid + (tip_side - tip_mid) * abs(f0) ** 1.4 + lr.uniform(-jitter, jitter)
        hair_lock(f0, width * lr.uniform(.8, 1.25) * 2 / n, 1.80, tip, offset, seed * 100 + k)


def build_hair():
    # The mass, to the middle of his back; a shorter layer over it, between
    # its locks; a few long ones over the top, astray.
    hair_layer(22, .020, 1.04, 1.36, .11, 1.55, SEED + 1)
    hair_layer(16, .032, 1.20, 1.42, .13, 1.45, SEED + 2, shift=.5)
    lr = random.Random(SEED + 3)
    for k in range(6):
        hair_lock(lr.uniform(-.75, .75), .07, 1.80, lr.uniform(1.00, 1.18), .042, SEED * 7 + k, ncol=3)
    # The beard: full under the cheeks, long to the breastbone, lying on the chest.
    BEARD = [(1.668, .086, .030, .128), (1.630, .099, .052, .138), (1.585, .100, .064, .149), (1.525, .090, .061, .167),
             (1.450, .074, .053, .190), (1.370, .058, .044, .209), (1.295, .042, .034, .224), (1.225, .025, .023, .234)]
    rows = resample(BEARD, 2)
    rings = []
    for i, (y, rx, rz, cz) in enumerate(rows):
        ring = []
        for j in range(14):
            th = j / 14 * math.tau
            k = 1 + .075 * math.sin(7 * th + i * .9) + .04 * math.sin(3 * th - i * .5)
            ring.append(Vector((rx * math.sin(th) * k, y + .010 * math.sin(4 * th + i), cz + rz * math.cos(th) * k)))
        rings.append(ring)
    loft(rings, 'hair', cap0=True, cap1=(0.006, 1.165, .240))
    for sx in (-1, 1):
        # the moustache, drooping into the beard; the brows, bushy
        tube(resample([(sx * .010, 1.653, .160), (sx * .048, 1.634, .153), (sx * .084, 1.588, .134), (sx * .100, 1.538, .122)], 2),
             [r[0] for r in resample([(.017,), (.016,), (.011,), (.003,)], 2)], n=8, mat='hair')
        tube(resample([(sx * .020, 1.731, .156), (sx * .050, 1.742, .150), (sx * .083, 1.730, .124)], 2),
             [r[0] for r in resample([(.008,), (.012,), (.005,)], 2)], n=6, mat='hair')


# ---- the head (a fused sculpt, built apart) -------------------------------------------------
HEAD = Vector((0, 1.695, .075))


def build_head():
    global cur
    cur = head
    C = HEAD
    ellipsoid(C, (.098, .115, .112), 'skin', n=20, m=14)                               # the cranium
    ellipsoid(C + Vector((0, -.070, .030)), (.072, .062, .075), 'skin', n=16, m=10)    # the jaw
    tube([C + Vector((0, -.09, -.02)), Vector((0, 1.56, .045)), Vector((0, 1.50, .03))], [.054, .052, .056], n=12, mat='skin')
    # a hooked nose, its nostrils; the brow's ridge; the cheekbones; the mouth's mound
    tube(resample([C + Vector(p) for p in ((0, .034, .100), (0, .004, .126), (0, -.028, .152), (0, -.046, .134))], 2),
         [r[0] for r in resample([(.013,), (.017,), (.024,), (.013,)], 2)], n=10, mat='skin')
    for sx in (-1, 1):
        ellipsoid(C + Vector((sx * .017, -.040, .128)), (.013, .011, .013), 'skin', n=8, m=6)
        ellipsoid(C + Vector((sx * .060, -.012, .078)), (.030, .024, .030), 'skin', n=10, m=8)
    tube(resample([C + Vector(p) for p in ((-.078, .034, .066), (-.042, .046, .097), (0, .041, .108), (.042, .046, .097), (.078, .034, .066))], 2),
         [.017] * 9, n=8, mat='skin')
    ellipsoid(C + Vector((0, -.070, .098)), (.036, .020, .020), 'skin', n=10, m=6)
    cur = main
    for sx in (-1, 1):                                                                  # the eyes, set in after
        ellipsoid(C + Vector((sx * .036, .012, .0925)), (.0135, .0135, .0135), 'eye', n=10, m=8)
        ellipsoid(C + Vector((sx * .036, .011, .1010)), (.0072, .0072, .006), 'iris', n=8, m=6)


# ---- the staff, the crystal, the hands, the shoes ----------------------------------------------
STAFF = [(-.530, 0.00, .330), (-.522, .26, .337), (-.512, .52, .326), (-.519, .78, .339), (-.507, 1.02, .330),
         (-.512, 1.23, .338), (-.501, 1.46, .330), (-.509, 1.70, .340), (-.495, 1.90, .332), (-.488, 2.02, .330)]
STAFF_R = [.031, .032, .029, .031, .028, .027, .028, .030, .033, .038]
CRYSTAL = Vector((-.522, 2.325, .331))


def build_staff():
    def gnarl(i, th, P, T, U, W):
        return 1 + .075 * math.sin(3 * th + i * 1.3) + .045 * math.sin(5 * th - i * .7)
    tube(resample(STAFF, 2), [r[0] for r in resample([(r,) for r in STAFF_R], 2)], n=9, mat='wood', mod=gnarl)
    # the fork: the main limb leans away to his left, then hooks back over the
    # crystal; a shorter prong comes up under it from the other side
    # (r177) Both thick to the end and knotted, as the reference's are: a
    # branch, not two horns. Thin and tapering to points they drew a smooth
    # crescent round the crystal, and its light caught their inner faces pink.
    def knotty(i, th, P, T, U, W):
        return 1 + .12 * math.sin(3 * th + i * 1.3) + .07 * math.sin(5 * th - i * .7) + .05 * math.sin(2 * th + i * 2.1)
    hook = [(-.488, 1.99, .330), (-.462, 2.09, .328), (-.444, 2.19, .326), (-.440, 2.29, .326), (-.452, 2.38, .328),
            (-.478, 2.47, .330), (-.512, 2.525, .332), (-.548, 2.540, .334)]
    tube(resample(hook, 2), [r[0] for r in resample([(.041,), (.039,), (.036,), (.034,), (.031,), (.027,), (.021,), (.013,)], 2)], n=9, mat='wood', mod=knotty)
    for (t, d, s) in ((1.4, (.024, .006, 0), 1.0), (3.6, (.022, 0, .010), .9), (5.2, (.010, .018, 0), .8)):    # its knots
        p = Vector(catmull(hook, t)) + Vector(d)
        ellipsoid(p, (.024 * s, .030 * s, .024 * s), 'wood', n=8, m=6)
    prong = [(-.500, 1.990, .332), (-.530, 2.060, .334), (-.560, 2.120, .336), (-.578, 2.170, .337)]
    tube(resample(prong, 2), [r[0] for r in resample([(.031,), (.027,), (.020,), (.011,)], 2)], n=8, mat='wood', mod=knotty)
    for (t, s) in ((.9, 1.5), (2.3, 1.4), (4.6, 1.6), (6.4, 1.5), (7.7, 1.45)):          # knots
        p = Vector(catmull(STAFF, t))
        a = rng.uniform(0, math.tau)
        ellipsoid(p + Vector((math.cos(a) * .018, 0, math.sin(a) * .018)), (.026 * s / 1.5, .034, .026 * s / 1.5), 'wood', n=8, m=6)
    # The crystal: a long six-sided point, its facets flat.
    # (r177) Its upper point longer than its lower, as the reference's is,
    # and a touch wider.
    c = CRYSTAL
    top, bot = c + Vector((.008, .150, 0)), c + Vector((-.008, -.120, 0))
    ra = [c + Vector((.032 * math.cos(k / 6 * math.tau), -.050, .032 * math.sin(k / 6 * math.tau))) for k in range(6)]
    rb = [c + Vector((.036 * math.cos(k / 6 * math.tau + .2), .040, .036 * math.sin(k / 6 * math.tau + .2))) for k in range(6)]
    for k in range(6):
        kk = (k + 1) % 6
        flat_face([ra[k], ra[kk], bot], 'crystal', c)
        flat_face([ra[k], ra[kk], rb[kk], rb[k]], 'crystal', c)
        flat_face([rb[k], rb[kk], top], 'crystal', c)


def build_hands():
    # his right hand round the staff: the back of the hand from the wrist, four
    # fingers round the far side, the thumb up the near side
    sx, sy, sz = -.512, 1.232, .338
    tube([(-.503, 1.226, .272), (-.507, 1.230, .300), (-.510, 1.232, .318)], [(.026, .030), (.031, .040), (.030, .042)], n=10, mat='skin', ref=(0, 1, 0))
    for k in range(4):
        y = sy + .033 - k * .0215
        arc = [(sx + .038 * math.cos(math.radians(a)), y - .004 * (a < 60), sz + .038 * math.sin(math.radians(a))) for a in (232, 196, 160, 124, 88, 52, 20)]
        tube(arc, [.0125, .0125, .012, .0118, .0112, .0105, .0085], n=6, mat='skin', ref=(0, 1, 0))
    tube([(sx + .020, sy + .010, sz - .034), (sx + .036, sy + .030, sz - .012), (sx + .034, sy + .052, sz + .012), (sx + .020, sy + .066, sz + .028)],
         [.014, .0135, .012, .009], n=6, mat='skin', ref=(0, 0, 1))
    # his left, hanging just out of its cuff
    hx, hy, hz = .312, .775, .168
    ellipsoid((hx, hy, hz), (.027, .046, .017), 'skin', n=10, m=8)
    for k in range(4):
        x = hx - .020 + k * .0135
        tube([(x, hy - .036, hz + .002), (x, hy - .068, hz + .010), (x + .001, hy - .092, hz + .022)], [.0095, .009, .0072], n=6, mat='skin', ref=(1, 0, 0))
    tube([(hx - .026, hy - .004, hz + .004), (hx - .036, hy - .034, hz + .016), (hx - .034, hy - .058, hz + .028)], [.011, .0105, .008], n=6, mat='skin', ref=(1, 0, 0))
    for s in (-1, 1):                                                                    # the toes of his shoes
        ellipsoid((s * .105, .036, .345), (.058, .040, .100), 'shoe', n=10, m=6)


# ---- Blender objects ----------------------------------------------------------------------------
def make_object(buf, name, materials):
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bv = [bm.verts.new(g2b(v)) for v in buf.V]
    skipped = 0
    for idx, mi in zip(buf.F, buf.FM):
        try:
            f = bm.faces.new([bv[i] for i in idx])
        except ValueError:
            skipped += 1
            continue
        f.material_index = mi
        f.smooth = True
    bm.to_mesh(mesh)
    bm.free()
    if skipped:
        print('WARN %s: %d faces skipped' % (name, skipped))
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    for m in materials:
        mesh.materials.append(m)
    return obj


def only(obj):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def tris_of(obj):
    return sum(len(p.vertices) - 2 for p in obj.data.polygons)


# ---- the paint: one procedural material a surface ---------------------------------------------------
def paint(name, stops, scale, stretch, detail=6.0, rough=.62, distort=0.0, fine=None, blotch=None, emission=None, fade=None):
    """Colour from a noise through a ramp (stops: position, linear rgb), in
    the object's own space so it runs down what hangs (Blender's z is up:
    a stretch of (1, 1, .2) draws features five times as tall as wide);
    fine: a second noise (scale, stretch, low, high) multiplied over it for
    strands, weave and grain; blotch: a third, broad; fade: (low, high,
    dark) darkens it toward the bottom, from 1 at height high to dark at low."""
    m = bpy.data.materials.new('orren-' + name)
    m.use_nodes = True
    nt = m.node_tree
    bsdf = nt.nodes['Principled BSDF']
    tc = nt.nodes.new('ShaderNodeTexCoord')

    def noise(scale, stretch, detail, rough, distort=0.0):
        mp = nt.nodes.new('ShaderNodeMapping')
        mp.inputs['Scale'].default_value = stretch
        nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])
        nz = nt.nodes.new('ShaderNodeTexNoise')
        nz.inputs['Scale'].default_value = scale
        nz.inputs['Detail'].default_value = detail
        nz.inputs['Roughness'].default_value = rough
        nz.inputs['Distortion'].default_value = distort
        nt.links.new(mp.outputs['Vector'], nz.inputs['Vector'])
        return nz.outputs[0]

    def ramp(src, stops):
        r = nt.nodes.new('ShaderNodeValToRGB')
        els = r.color_ramp.elements
        for i, (pos, col) in enumerate(stops):
            e = els[i] if i < 2 else els.new(pos)
            e.position = pos
            e.color = (col[0], col[1], col[2], 1) if isinstance(col, tuple) else (col, col, col, 1)
        nt.links.new(src, r.inputs[0])
        return r.outputs[0]

    def times(a, b):
        mx = nt.nodes.new('ShaderNodeMix')
        mx.data_type = 'RGBA'
        mx.blend_type = 'MULTIPLY'
        mx.inputs[0].default_value = 1.0
        nt.links.new(a, mx.inputs[6])
        nt.links.new(b, mx.inputs[7])
        return mx.outputs[2]
    out = ramp(noise(scale, stretch, detail, rough, distort), stops)
    if fine:
        out = times(out, ramp(noise(fine[0], fine[1], 3.0, .55), [(.34, fine[2]), (.66, fine[3])]))
    if blotch:
        out = times(out, ramp(noise(blotch[0], (1, 1, 1), 4.0, .6), [(.3, blotch[1]), (.7, blotch[2])]))
    if fade:
        sep = nt.nodes.new('ShaderNodeSeparateXYZ')
        nt.links.new(tc.outputs['Object'], sep.inputs['Vector'])
        mr = nt.nodes.new('ShaderNodeMapRange')
        mr.inputs['From Min'].default_value, mr.inputs['From Max'].default_value = fade[0], fade[1]
        mr.inputs['To Min'].default_value, mr.inputs['To Max'].default_value = fade[2], 1.0
        nt.links.new(sep.outputs['Z'], mr.inputs['Value'])
        out = times(out, mr.outputs['Result'])
    nt.links.new(out, bsdf.inputs['Base Color'])
    bsdf.inputs['Roughness'].default_value = .86
    if emission:
        bsdf.inputs['Emission Color'].default_value = (*emission[0], 1)
        bsdf.inputs['Emission Strength'].default_value = emission[1]
    return m


def paints():
    return {
        # dark cloth, mottled, its wrinkles running down it
        'robe': paint('robe', [(.30, (.006, .006, .020)), (.48, (.016, .016, .046)), (.64, (.034, .032, .084)), (.80, (.066, .060, .140))],
                      7.0, (1, 1, .30), detail=7.0, rough=.68, distort=1.2, fine=(46.0, (1, 1, .12), .78, 1.18), blotch=(1.6, .80, 1.15)),
        'hat': paint('hat', [(.32, (.008, .008, .024)), (.52, (.020, .020, .054)), (.74, (.046, .044, .108))],
                     9.0, (1, 1, 1), detail=6.0, rough=.6, fine=(90.0, (1, 1, 1), .86, 1.12)),
        # white hair in fine strands, a lavender shade in it
        # (r177) whiter: in the game under the night grade it came out
        # lavender and dim, where the reference's is silver-white; and darkened
        # less toward its ends, which fade out now instead
        'hair': paint('hair', [(.30, (.50, .50, .57)), (.50, (.76, .76, .81)), (.70, (.95, .95, .96))],
                      1.0, (70, 70, 1.3), detail=3.0, rough=.5, fine=(1.0, (190, 190, 2.5), .78, 1.08), fade=(1.0, 1.48, .62)),
        'skin': paint('skin', [(.35, (.40, .23, .16)), (.65, (.58, .36, .26))], 14.0, (1, 1, 1), detail=4.0, rough=.5),
        # bark, grained along the staff
        'wood': paint('wood', [(.30, (.016, .010, .006)), (.50, (.042, .026, .015)), (.72, (.098, .062, .036))],
                      1.0, (46, 46, 2.2), detail=5.0, rough=.6, distort=.6, fine=(1.0, (120, 120, 6.0), .78, 1.15)),
        'band': paint('band', [(.35, (.050, .040, .090)), (.65, (.105, .085, .175))], 30.0, (1, 1, 1)),
        'shoe': paint('shoe', [(.35, (.012, .008, .006)), (.65, (.032, .021, .014))], 20.0, (1, 1, 1)),
        'eye': paint('eye', [(.0, (.70, .70, .72)), (1.0, (.78, .78, .80))], 5.0, (1, 1, 1)),
        'iris': paint('iris', [(.0, (.02, .05, .10)), (1.0, (.03, .07, .14))], 5.0, (1, 1, 1)),
        # (r177) a deeper violet, and a glow a third as strong: at 6 it burned
        # white in the game, a blank lens; the reference's crystal is violet
        # glass with a bright core, its facets showing
        'crystal': paint('crystal', [(.0, (.36, .16, .92)), (1.0, (.62, .40, 1.0))], 5.0, (1, 1, 1), emission=((.56, .28, 1.0), 2.0)),
    }


# ---- build ------------------------------------------------------------------------------------------
bpy.ops.wm.read_factory_settings(use_empty=True)
build_robe()
build_sleeves()
build_hat()
build_hair()
build_head()
build_staff()
build_hands()

mats = paints()
slots = [mats[n] for n in MATS]
obj = make_object(main, 'orren', slots)
skull = make_object(head, 'orren-head', [mats['skin']])
for p in skull.data.polygons:
    p.material_index = 0
only(skull)
skull.data.remesh_voxel_size = .0055
bpy.ops.object.voxel_remesh()
sm = skull.modifiers.new('polish', 'SMOOTH')
sm.factor, sm.iterations = .5, 4
bpy.ops.object.modifier_apply(modifier=sm.name)
dec = skull.modifiers.new('dec', 'DECIMATE')
dec.ratio = min(1.0, 760 / max(1, tris_of(skull)))
bpy.ops.object.modifier_apply(modifier=dec.name)
print('ORREN head tris=%d' % tris_of(skull))
main_verts = len(obj.data.vertices)
bpy.ops.object.select_all(action='DESELECT')
skull.select_set(True)
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
bpy.ops.object.join()
me = obj.data
assert len(main.V) == main_verts
crystal_slot = M('crystal')
for p in me.polygons:
    p.use_smooth = True
# Normals: Blender's own, smooth; the hair's point out from the body, so its
# sheets and locks shade as one mass; the crystal's are its facets'.
normals = [v.normal.copy() for v in me.vertices]
for i, nrm in main.N.items():
    normals[i] = g2b(nrm).normalized()
me.normals_split_custom_set_from_vertices([tuple(nrm) for nrm in normals])
print('ORREN tris=%d verts=%d' % (tris_of(obj), len(me.vertices)))

scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.view_settings.view_transform = 'Standard'
world = bpy.data.worlds.new('w')
scene.world = world
world.use_nodes = True
BG = world.node_tree.nodes['Background']


def bake():
    only(obj)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.003)
    bpy.ops.object.mode_set(mode='OBJECT')
    # (r177) ORREN_REUSE_BAKE=1: keep the last atlas, for a change that does
    # not touch the geometry or the paint (the unwrap of the same mesh is the
    # same, so the old atlas still fits). It saves the Cycles bakes.
    if os.environ.get('ORREN_REUSE_BAKE') and os.path.exists(os.path.join(HERE, '_bake-orren.jpg')):
        print('ORREN reusing the last bake')
        return os.path.join(HERE, '_bake-orren.jpg')

    def target(name):
        img = bpy.data.images.new(name, SIZE, SIZE, alpha=False, float_buffer=True)
        for m in mats.values():
            nt = m.node_tree
            node = nt.nodes.get('bake-target') or nt.nodes.new('ShaderNodeTexImage')
            node.name = 'bake-target'
            node.image = img
            for nd in nt.nodes:
                nd.select = False
            node.select = True
            nt.nodes.active = node
        return img

    def read(img):
        buf = np.empty(SIZE * SIZE * 4, dtype=np.float32)
        img.pixels.foreach_get(buf)
        return buf.reshape(SIZE, SIZE, 4)[..., :3].astype(np.float64)
    scene.render.bake.margin = 8
    scene.render.bake.use_clear = True
    scene.cycles.samples = 2
    col = target('orren-colour')
    bpy.ops.object.bake(type='DIFFUSE', pass_filter={'COLOR'})
    # the ground under him, for the occlusion at his hem
    bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 0, -.002))
    floor = bpy.context.active_object
    only(obj)
    scene.cycles.samples = 64
    world.light_settings.distance = 1.2
    ao = target('orren-ao')
    bpy.ops.object.bake(type='AO')
    world.light_settings.distance = .07
    fine = target('orren-ao-fine')
    bpy.ops.object.bake(type='AO')
    bpy.data.objects.remove(floor, do_unlink=True)
    a = read(col) * (read(ao).mean(-1, keepdims=True) ** .95) * (read(fine).mean(-1, keepdims=True) ** .55)
    a = np.clip(a, 0, 1)
    srgb = np.where(a > .0031308, 1.055 * a ** (1 / 2.4) - .055, a * 12.92)
    from PIL import Image
    path = os.path.join(HERE, '_bake-orren.jpg')
    Image.fromarray((srgb[::-1] * 255 + .5).astype(np.uint8)).save(path, quality=84)
    return path


def baked_material(path, name='orren-baked', alpha=False):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    tex = nt.nodes.new('ShaderNodeTexImage')
    tex.image = bpy.data.images.load(path, check_existing=True)
    bsdf = nt.nodes['Principled BSDF']
    nt.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    bsdf.inputs['Roughness'].default_value = .86
    if alpha:
        # the colours multiply the atlas (they are white) as well as giving
        # the alpha: so the exporter writes them once, as COLOR_0, which the
        # game reads. Used for the alpha alone they went out as COLOR_1, with
        # an all-white COLOR_0 in front of them.
        vc = nt.nodes.new('ShaderNodeVertexColor')
        vc.layer_name = 'Col'
        mx = nt.nodes.new('ShaderNodeMix')
        mx.data_type = 'RGBA'
        mx.blend_type = 'MULTIPLY'
        mx.inputs[0].default_value = 1.0
        nt.links.new(tex.outputs['Color'], mx.inputs[6])
        nt.links.new(vc.outputs['Color'], mx.inputs[7])
        nt.links.new(mx.outputs[2], bsdf.inputs['Base Color'])
        nt.links.new(vc.outputs['Alpha'], bsdf.inputs['Alpha'])
        m.surface_render_method = 'BLENDED'
    return m


hair_slot = M('hair')
atlas = None
hair = None
if not FAST:
    atlas = bake()
    flat = baked_material(atlas)
    # (r177) The hair on a material of its own over the same atlas, blended
    # by its vertices' alpha: its locks fade out toward their points.
    strands = baked_material(atlas, 'orren-strands', alpha=True)
    glow = mats['crystal']
    if glow.node_tree.nodes.get('bake-target'):          # (none when the last bake is reused)
        glow.node_tree.nodes.remove(glow.node_tree.nodes['bake-target'])
    kind = [2 if p.material_index == hair_slot else 1 if p.material_index == crystal_slot else 0 for p in me.polygons]
    me.materials.clear()
    for m in (flat, glow, strands):
        me.materials.append(m)
    for p, k in zip(me.polygons, kind):
        p.material_index = k
    # The alpha by vertex: white, and the hair's tips toward clear. The main
    # buffer's vertices come first in the joined mesh, so its indices hold.
    col = me.color_attributes.new('Col', 'FLOAT_COLOR', 'POINT')
    rgba = np.ones(len(me.vertices) * 4, dtype=np.float32)
    for i, a in main.A.items():
        rgba[i * 4 + 3] = a
    col.data.foreach_set('color', rgba)
    me.color_attributes.active_color = col
    # And the hair its own object, so that only it carries the colours.
    only(obj)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    obj.active_material_index = 2
    bpy.ops.object.material_slot_select()
    bpy.ops.mesh.separate(type='SELECTED')
    bpy.ops.object.mode_set(mode='OBJECT')
    hair = next(o for o in bpy.context.selected_objects if o is not obj)
    hair.name = 'orren-hair'
    # Only the hair's alpha, and only on the hair. Something else in the
    # joined mesh is a colour attribute too (all white); exported first as
    # COLOR_0 it was the one the game read, and the hair never faded.
    for o in (obj, hair):
        cas = o.data.color_attributes
        for name in [c.name for c in cas]:
            if o is obj or name != 'Col':
                cas.remove(cas[name])
    hair.data.color_attributes.active_color = hair.data.color_attributes['Col']
    hair.data.color_attributes.render_color_index = 0
    print('ORREN colours: body %s, hair %s' % ([c.name for c in obj.data.color_attributes], [(c.name, c.data_type, c.domain) for c in hair.data.color_attributes]))
    print('ORREN hair tris=%d faded verts=%d' % (tris_of(hair), len(main.A)))


# ---- previews ------------------------------------------------------------------------------------------
def light(kind, at, energy, color=(1, 1, 1), look=None, size=.1):
    d = bpy.data.lights.new(kind.lower(), type=kind)
    d.energy = energy
    d.color = color
    if kind == 'AREA':
        d.size = size
    if kind == 'POINT':
        d.shadow_soft_size = size
    o = bpy.data.objects.new(kind.lower(), d)
    o.location = g2b(at)
    if look is not None:
        o.rotation_euler = (g2b(look) - g2b(at)).to_track_quat('-Z', 'Y').to_euler()
    bpy.context.collection.objects.link(o)
    return o


cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam'))
cam.data.sensor_fit = 'VERTICAL'
cam.data.sensor_height = 24
bpy.context.collection.objects.link(cam)
scene.camera = cam
scene.render.resolution_x, scene.render.resolution_y = 540, 960
scene.render.image_settings.file_format = 'PNG'
scene.cycles.samples = 40
try:
    scene.cycles.use_denoising = True
except Exception:
    pass
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, -.004))
ground = bpy.context.active_object
gm = bpy.data.materials.new('ground')
gm.use_nodes = True
gm.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (.20, .20, .24, 1)
gm.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = 1
ground.data.materials.append(gm)


def shoot(suffix, at, look, fov=60.0):
    cam.data.lens = 12 / math.tan(math.radians(fov) / 2)
    cam.location = g2b(at)
    cam.rotation_euler = (g2b(look) - g2b(at)).to_track_quat('-Z', 'Y').to_euler()
    path = os.path.join(HERE, '_preview-orren' + suffix + '.png')
    scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    return path


previews = []
# In an even light, from four sides: the model itself.
BG.inputs['Color'].default_value = (.34, .36, .46, 1)
BG.inputs['Strength'].default_value = 1.0
studio = [light('SUN', (2, 6, 4), 2.6, look=(0, 1, 0)), light('SUN', (-3, 4, -4), 1.2, color=(.8, .85, 1), look=(0, 1, 0))]
previews.append(shoot('-back', (-1.2, 1.95, -2.97), (-.51, 1.50, .15), fov=50))
previews.append(shoot('-front', (.9, 1.6, 3.4), (-.15, 1.25, 0), fov=50))
previews.append(shoot('-side', (-3.5, 1.5, .5), (-.1, 1.25, .1), fov=50))
previews.append(shoot('-face', (.25, 1.66, 1.05), (0, 1.60, .1), fov=40))
for o in studio:
    bpy.data.objects.remove(o, do_unlink=True)
# As the reference sees him: from behind his right shoulder under a night sky,
# the moon ahead of him, his crystal's light on his hair and shoulder.
BG.inputs['Color'].default_value = (.035, .030, .095, 1)
BG.inputs['Strength'].default_value = 1.0
light('SUN', (1.5, 5, 9), 1.6, color=(.75, .80, 1.0), look=(0, 1.2, 0))
light('POINT', tuple(CRYSTAL), 26, color=(.62, .36, 1.0), size=.04)
light('AREA', (-1.6, 2.6, -2.6), 34, color=(.50, .44, .95), look=(0, 1.3, 0), size=2.5)
previews.insert(0, shoot('', (-1.2, 1.95, -2.97), (-.51, 1.73, .15), fov=60))

if FAST:
    print('ASSET_FAST name=orren triangles=%d previews=%s' % (tris_of(obj), ','.join(previews)))
    sys.exit(0)

# ---- export ---------------------------------------------------------------------------------------------
bpy.data.objects.remove(ground, do_unlink=True)
only(obj)
hair.select_set(True)
out = os.path.join(ROOT, 'assets', 'orren.glb')
# (r177) the colours a material reads go out: the hair's alpha, once (as the
# active colour as well it went out twice)
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', use_selection=True, export_apply=True,
                          export_materials='EXPORT', export_normals=True, export_texcoords=True,
                          export_vertex_color='MATERIAL', export_image_format='AUTO')
print('ASSET_OK name=orren triangles=%d bytes=%d texture=%d out=%s previews=%s' % (
    tris_of(obj) + tris_of(hair), os.path.getsize(out), os.path.getsize(atlas), out, ','.join(previews)))
