# How close is a render to a reference image? (r176)
#
#   python tools/match-score.py <reference> <render> [<render> ...] [--mask x0,y0,x1,y1 ...]
#
# Matching a frame by eye drifts: each side-by-side is judged against the last
# one, not against the reference. This scores a render against the reference
# on four things a viewer reads before detail, each 0 to 100:
#
#   colour    the two images' colour statistics in CIELAB: the mean colour,
#             the spread of lightness, and how the hue is spread over the
#             frame (a chroma-weighted hue histogram)
#   regions   the mean colour of each cell of a 9 x 16 grid, compared cell by
#             cell (does the violet sit in the sky and the green in the
#             valley, where the reference has them)
#   light     the lightness of each cell of that grid, correlated (where the
#             bright and the dark masses are: the moon, the figure, the rock)
#   shapes    the strength of edges in an 18 x 32 grid, correlated (where the
#             detail and the silhouettes are)
#
# and an overall score, their mean. Both images are scaled to 135 x 240 (a
# phone frame upright) before scoring. --mask takes rectangles in fractions of
# the frame to leave out of every measure: a watermark, a caption. The scores
# compare a render with the reference, and one render with another; they are
# not a measure of anything else.
#
# Needs Pillow and NumPy.
import sys
import numpy as np
from PIL import Image

W, H = 135, 240


def load(path):
    im = Image.open(path).convert('RGB').resize((W, H), Image.LANCZOS)
    return np.asarray(im, dtype=np.float64) / 255.0


def lab(rgb):
    c = np.where(rgb > .04045, ((rgb + .055) / 1.055) ** 2.4, rgb / 12.92)
    m = np.array([[.4124, .3576, .1805], [.2126, .7152, .0722], [.0193, .1192, .9505]])
    xyz = c @ m.T / np.array([.95047, 1.0, 1.08883])
    f = np.where(xyz > .008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    L = 116 * f[..., 1] - 16
    a = 500 * (f[..., 0] - f[..., 1])
    b = 200 * (f[..., 1] - f[..., 2])
    return np.stack([L, a, b], -1)


def grid(values, keep, gx, gy):
    h, w = values.shape[:2]
    out, ok = [], []
    for j in range(gy):
        for i in range(gx):
            ys, ye, xs, xe = j * h // gy, (j + 1) * h // gy, i * w // gx, (i + 1) * w // gx
            k = keep[ys:ye, xs:xe]
            v = values[ys:ye, xs:xe]
            if k.mean() < .5:
                ok.append(False); out.append(np.zeros(values.shape[2:]) if values.ndim > 2 else 0.0); continue
            ok.append(True); out.append(v[k].mean(axis=0))
    return np.array(out), np.array(ok)


def corr(a, b):
    a, b = a - a.mean(), b - b.mean()
    d = np.sqrt((a * a).sum() * (b * b).sum())
    return float((a * b).sum() / d) if d > 1e-9 else 0.0


def hue_hist(lb, keep, bins=18):
    a, b = lb[..., 1][keep], lb[..., 2][keep]
    chroma = np.hypot(a, b)
    hue = (np.degrees(np.arctan2(b, a)) + 360) % 360
    h, _ = np.histogram(hue, bins=bins, range=(0, 360), weights=chroma)
    return h / max(h.sum(), 1e-9), float(chroma.mean())


def edges(rgb):
    g = rgb.mean(-1)
    gx = np.zeros_like(g); gy = np.zeros_like(g)
    gx[:, 1:-1] = g[:, 2:] - g[:, :-2]
    gy[1:-1, :] = g[2:, :] - g[:-2, :]
    return np.hypot(gx, gy)


def score(ref, img, keep):
    lr, li = lab(ref), lab(img)
    # colour
    dmean = np.linalg.norm(lr[keep].mean(0) - li[keep].mean(0))
    dspread = abs(lr[..., 0][keep].std() - li[..., 0][keep].std())
    hr, cr = hue_hist(lr, keep); hi, ci = hue_hist(li, keep)
    hue_overlap = np.minimum(hr, hi).sum()
    colour = 100 * (.4 * max(0, 1 - dmean / 40) + .2 * max(0, 1 - dspread / 20) + .25 * hue_overlap + .15 * max(0, 1 - abs(cr - ci) / 30))
    # regions and light
    gr, ok = grid(lr, keep, 9, 16); gi, _ = grid(li, keep, 9, 16)
    de = np.linalg.norm(gr[ok] - gi[ok], axis=1).mean()
    regions = 100 * max(0, 1 - de / 45)
    light = 100 * max(0, corr(gr[ok][:, 0], gi[ok][:, 0]))
    # shapes
    er, ok2 = grid(edges(ref)[..., None], keep, 18, 32); ei, _ = grid(edges(img)[..., None], keep, 18, 32)
    shapes = 100 * max(0, corr(er[ok2][:, 0], ei[ok2][:, 0]))
    parts = {'colour': colour, 'regions': regions, 'light': light, 'shapes': shapes}
    parts['overall'] = sum(parts.values()) / 4
    return parts


def main(argv):
    masks, files, i = [], [], 0
    while i < len(argv):
        if argv[i] == '--mask':
            masks.append([float(v) for v in argv[i + 1].split(',')]); i += 2
        else:
            files.append(argv[i]); i += 1
    if len(files) < 2:
        print(__doc__ if __doc__ else 'usage: match-score.py <reference> <render> ...'); return 2
    keep = np.ones((H, W), bool)
    for x0, y0, x1, y1 in masks:
        keep[int(y0 * H):int(y1 * H), int(x0 * W):int(x1 * W)] = False
    ref = load(files[0])
    print('%-44s %7s %7s %7s %7s %7s' % ('render', 'overall', 'colour', 'regions', 'light', 'shapes'))
    for f in files[1:]:
        s = score(ref, load(f), keep)
        print('%-44s %7.1f %7.1f %7.1f %7.1f %7.1f' % (f.split('/')[-1][-44:], s['overall'], s['colour'], s['regions'], s['light'], s['shapes']))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
