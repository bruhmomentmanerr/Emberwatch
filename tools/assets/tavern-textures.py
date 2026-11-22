# The taverns' surfaces (r181), painted with the light baked in, after the
# owner's tavern frame (tools/video-frames/reference/hall-02-f00137.png):
#
#   tavern-flag.jpg    pale, worn flagstones: irregular rounded slabs, a dark
#                      grout line, the edges falling away into it, cracks
#   tavern-stone.jpg   the wall: rounded rubble stones in rough courses, a
#                      mossy green-grey, deep mortar
#   tavern-glass.jpg   a round window: green quarries of uneven size between
#                      heavy dark timber bars, a timber ring round it
#   hall-stone.jpg     (r182) the rubble again in plain grey, no moss: the
#                      other halls tint it to their own glass
#   hall-glass.jpg     (r182) the round window in near-white quarries, for
#                      the game to tint (blue, amber, violet, rose)
#
# All three are painted, not photographed: Voronoi cells for the stones and
# the quarries, a height field from each cell's distance to its own edge, and
# that height lit from the upper left so every slab carries its own bevel and
# shadow (STYLE-PLAYBOOK §1: high-contrast ground, detail in the texture).
# The floor and the wall tile seamlessly; the cells are laid in a wrapped
# unit square.
#
#   tools/assets/_venv-python tools/assets/tavern-textures.py [outdir]
# then inline each with tools/assets/inline-tex.js.
import sys, os
import numpy as np
from PIL import Image

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets')
os.makedirs(OUT, exist_ok=True)


def smooth(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)


def value_noise(n, cells, rng, octaves=4):
    # Tileable fractal value noise on an n x n grid.
    out = np.zeros((n, n))
    amp, tot = 1.0, 0.0
    for o in range(octaves):
        c = cells * 2 ** o
        g = rng.random((c, c))
        ys = np.arange(n) * c / n
        y0 = np.floor(ys).astype(int); fy = ys - y0
        fy = fy * fy * (3 - 2 * fy)
        a = g[y0 % c][:, y0 % c]; b = g[y0 % c][:, (y0 + 1) % c]
        cc = g[(y0 + 1) % c][:, y0 % c]; d = g[(y0 + 1) % c][:, (y0 + 1) % c]
        fx = fy[None, :]; fyy = fy[:, None]
        out += amp * ((a * (1 - fx) + b * fx) * (1 - fyy) + (cc * (1 - fx) + d * fx) * fyy)
        tot += amp; amp *= .5
    return out / tot


def voronoi(n, pts, sx=1.0):
    # For every pixel of a wrapped unit square: the nearest cell, and the
    # distance (in pixels) to that cell's own edge — the bisector with the
    # nearest neighbour, which is what makes the bevel follow the slab.
    # sx stretches the metric across, for stones longer than they are tall.
    P = np.concatenate([pts + np.array([dx, dy]) for dx in (-1, 0, 1) for dy in (-1, 0, 1)])
    ids = np.tile(np.arange(len(pts)), 9)
    ys, xs = np.mgrid[0:n, 0:n] / n
    owner = np.zeros((n, n), int); edge = np.full((n, n), 9.0)
    for r0 in range(0, n, 64):
        px = xs[r0:r0 + 64, :, None]; py = ys[r0:r0 + 64, :, None]
        dx = (P[None, None, :, 0] - px) * sx; dy = P[None, None, :, 1] - py
        d2 = dx * dx + dy * dy
        k = np.argmin(d2, axis=2)
        owner[r0:r0 + 64] = ids[k]
        ax = np.take_along_axis(P[None, None, :, 0] * np.ones_like(px), k[..., None], 2)[..., 0]
        ay = np.take_along_axis(P[None, None, :, 1] * np.ones_like(py), k[..., None], 2)[..., 0]
        # distance from p to the bisector of a and b: (|p-b|^2 - |p-a|^2) / 2|a-b|
        bx = (P[None, None, :, 0] - ax[..., None]) * sx; by = P[None, None, :, 1] - ay[..., None]
        ab = np.sqrt(bx * bx + by * by); ab[ab == 0] = 1e9
        da2 = np.take_along_axis(d2, k[..., None], 2)
        e = (d2 - da2) / (2 * ab)
        e[ab > 1e8] = 9
        edge[r0:r0 + 64] = e.min(axis=2) * n
    return owner, edge


def lit(h, n, light=(-.55, -.65, .52), strength=3.0):
    # Lambert on a height field, tileable (np.roll wraps).
    gx = (np.roll(h, -1, 1) - np.roll(h, 1, 1)) * strength
    gy = (np.roll(h, -1, 0) - np.roll(h, 1, 0)) * strength
    nx, ny, nz = -gx, -gy, np.ones_like(h)
    l = np.array(light); l = l / np.linalg.norm(l)
    return (nx * l[0] + ny * l[1] + nz * l[2]) / np.sqrt(nx * nx + ny * ny + nz * nz)


def jittered(nx, ny, rng, jit=.8, row_shift=False):
    pts = []
    for j in range(ny):
        for i in range(nx):
            sh = .5 if (row_shift and j % 2) else 0
            pts.append(((i + sh + .5 + rng.uniform(-jit, jit) * .5) / nx, (j + .5 + rng.uniform(-jit, jit) * .5) / ny))
    return np.array(pts) % 1.0


def relaxed(count, rng, iters=2, n=128):
    # Random points eased apart (Lloyd, on a coarse wrapped grid): stones of
    # uneven size that still do not bunch, where a jittered grid reads as rows.
    pts = rng.random((count, 2))
    ys, xs = np.mgrid[0:n, 0:n] / n
    for _ in range(iters):
        own, _e = voronoi(n, pts)
        new = []
        for i in range(count):
            m = own == i
            if not m.any():
                new.append(pts[i]); continue
            # a circular mean, so a cell across the wrap is not averaged to the middle
            ax = np.angle(np.exp(2j * np.pi * xs[m]).mean()) / (2 * np.pi)
            ay = np.angle(np.exp(2j * np.pi * ys[m]).mean()) / (2 * np.pi)
            new.append((ax % 1, ay % 1))
        pts = np.array(new)
    return pts


def save(img, name, q):
    p = os.path.join(OUT, name)
    Image.fromarray((np.clip(img, 0, 1) * 255 + .5).astype(np.uint8)).save(p, quality=q, subsampling=0, optimize=True)
    print(name, os.path.getsize(p) // 1024, 'KB')


def flagstones(n=512):
    rng = np.random.default_rng(181)
    pts = relaxed(27, rng, 1)
    owner, edge = voronoi(n, pts)
    grout = 1.9                                        # px of dark joint either side
    bevel = 13.0
    h = smooth(grout, grout + bevel, edge) ** .7       # the slab rounds over into the joint
    lump = value_noise(n, 4, rng, 5)
    h = h * (.82 + .3 * lump)
    shade = lit(h, n, strength=2.2)
    # cracks: the edges of a finer Voronoi, kept only inside a third of the slabs
    cpts = rng.random((60, 2))
    cown, cedge = voronoi(n, cpts)
    cracked = rng.random(len(pts)) < .3
    crack = (cedge < .9) & cracked[owner] & (edge > grout + 5) & (value_noise(n, 6, rng, 2) > .5)
    # each slab its own tone: sand, bone, a cooler grey, a little rust
    tones = np.array([(.80, .68, .50), (.74, .64, .50), (.64, .60, .54), (.78, .62, .44), (.70, .66, .58), (.62, .52, .40)])
    base = tones[rng.integers(0, len(tones), len(pts))] * rng.uniform(.78, 1.12, (len(pts), 1))
    col = base[owner]
    mott = value_noise(n, 16, rng, 4)
    col = col * (.72 + .5 * mott[..., None])
    col = col * (.30 + .95 * np.clip(shade, 0, 1))[..., None]
    ao = smooth(0, grout + bevel * 1.4, edge)
    col = col * (.25 + .75 * ao)[..., None]
    col[crack] *= .35
    joint = edge < grout
    col[joint] = np.array([.05, .045, .04]) * (.7 + .6 * mott[joint])[..., None]
    save(col, 'tavern-flag.jpg', 82)


GREEN_STONE = [(.30, .40, .30), (.26, .34, .28), (.34, .40, .32), (.24, .30, .26), (.32, .36, .30)]
GREY_STONE = [(.36, .35, .34), (.30, .30, .31), (.40, .38, .35), (.28, .28, .29), (.34, .33, .31)]


def rubble(name='tavern-stone.jpg', tones=GREEN_STONE, mossy=True, n=512):
    rng = np.random.default_rng(1812)
    pts = jittered(4, 6, rng, .6, row_shift=True)
    owner, edge = voronoi(n, pts, sx=.62)
    mortar = 2.2
    h = smooth(mortar, mortar + 16, edge) ** .55
    lump = value_noise(n, 4, rng, 4)
    h = h * (.8 + .35 * lump)
    shade = lit(h, n, light=(-.4, -.75, .5), strength=2.6)
    tones = np.array(tones)
    base = tones[rng.integers(0, len(tones), len(pts))] * rng.uniform(.8, 1.15, (len(pts), 1))
    col = base[owner]
    moss = value_noise(n, 8, rng, 4)
    col = col * (.75 + .45 * value_noise(n, 20, rng, 3)[..., None])
    if mossy:
        col[..., 1] *= .9 + .3 * moss
    col = col * (.28 + 1.0 * np.clip(shade, 0, 1))[..., None]
    col = col * (.3 + .7 * smooth(0, mortar + 18, edge))[..., None]
    joint = edge < mortar
    col[joint] = np.array([.035, .04, .035])
    save(col, name, 80)


def glass(name='tavern-glass.jpg', neutral=False, n=256):
    rng = np.random.default_rng(18101)
    ys, xs = np.mgrid[0:n, 0:n] / n
    r = np.hypot(xs - .5, ys - .5) * 2                 # 0 at the middle, 1 at the rim
    # quarries: a ring of eight round a middle one, jittered, plus two loose
    pts = [(.5, .5)]
    for k in range(8):
        a = k / 8 * np.pi * 2 + rng.uniform(-.2, .2)
        pts.append((.5 + np.cos(a) * .3, .5 + np.sin(a) * .3))
    for k in range(12):
        a = (k + .5) / 12 * np.pi * 2 + rng.uniform(-.15, .15)
        pts.append((.5 + np.cos(a) * .47, .5 + np.sin(a) * .47))
    pts = np.array(pts)
    d2 = (xs[..., None] - pts[None, None, :, 0]) ** 2 + (ys[..., None] - pts[None, None, :, 1]) ** 2
    srt = np.sort(d2, axis=2)
    owner = np.argmin(d2, axis=2)
    edge = (np.sqrt(srt[..., 1]) - np.sqrt(srt[..., 0])) * n * .5
    bar = 4.2
    greens = np.stack([rng.uniform(.30, .52, len(pts)), rng.uniform(.78, .95, len(pts)), rng.uniform(.26, .42, len(pts))], 1)
    greens[0] = (.46, .70, .92)                        # the middle one a cold pale blue, as the reference's inner pane
    if neutral:                                        # near-white, each quarry its own brightness, the middle brightest
        v = rng.uniform(.70, .92, len(pts))
        greens = np.stack([v * rng.uniform(.96, 1.0, len(pts)), v, v * rng.uniform(.94, 1.0, len(pts))], 1)
        greens[0] = (.98, .98, .98)
    lum = (.62 + .38 * smooth(bar, bar + 22, edge)) * (.85 + .25 * value_noise(n, 6, rng, 3))
    col = greens[owner] * lum[..., None]
    wood = np.array([.22, .13, .07]) * (.6 + .6 * value_noise(n, 24, rng, 3))[..., None]
    woodmask = (edge < bar) | (r > .86)
    # the ring catches a little light along its top
    ringlit = np.where(r > .86, .8 + .5 * np.clip(.5 - ys, 0, 1), 1.0)
    col = np.where(woodmask[..., None], wood * ringlit[..., None], col)
    save(col, name, 85)


flagstones()
rubble()
glass()
rubble('hall-stone.jpg', GREY_STONE, mossy=False)
glass('hall-glass.jpg', neutral=True)
