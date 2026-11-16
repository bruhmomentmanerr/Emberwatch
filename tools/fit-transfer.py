# Fit a colour transfer from a render onto a reference image (r176).
#
#   python tools/fit-transfer.py <reference> <render> [--mask x0,y0,x1,y1 ...] [--preview out.png] [--mode tone|hist]
#
# Prints three curves, one each for CIELAB lightness and its two colour axes,
# as base64 of 768 bytes (256 for each, in that order), for a place's mood in
# the game (PLACE_MOODS: curves). The game's grade pass applies them last, to
# the finished frame (see the grade shader).
#
# The lightness curve matches the render's histogram to the reference's: the
# darkest tenth of the render's pixels takes the lightness of the
# reference's darkest tenth, and so on up. The two colour axes (green-red,
# blue-yellow) move together: shifted to the reference's mean colour and
# scaled about it by one factor, so the render keeps its own shapes and hues
# and takes the reference's tones and its colour's centre and spread (see
# fit(), and --mode hist for each axis by its own histogram). Fit it on a render made without
# the transfer (the mood's curves left out), from where the place is meant to
# be seen; the curves are only as good as that frame is typical of the place.
#
# --mask leaves rectangles (fractions of the frame) out of both images'
# statistics: a watermark, a caption. --preview writes the render with the
# curves applied, as the game will show it within the 8-bit curves' rounding,
# and the match score of render and preview against the reference is printed.
#
# Needs Pillow and NumPy.
import sys, base64, importlib.util, os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('match_score', os.path.join(HERE, 'match-score.py'))
ms = importlib.util.module_from_spec(spec); spec.loader.exec_module(ms)

DOMAIN = [(0.0, 100.0), (-128.0, 127.0), (-128.0, 127.0)]   # L, a, b


def lab_to_rgb(lab):
    fy = (lab[..., 0] + 16) / 116
    f = np.stack([fy + lab[..., 1] / 500, fy, fy - lab[..., 2] / 200], -1)
    xyz = np.where(f > .206893, f ** 3, (f - 16 / 116) / 7.787) * np.array([.95047, 1.0, 1.08883])
    m = np.array([[3.2406, -1.5372, -.4986], [-.9689, 1.8758, .0415], [.0557, -.2040, 1.0570]])
    lin = np.clip(xyz @ m.T, 0, 1)
    return np.where(lin > .0031308, 1.055 * lin ** (1 / 2.4) - .055, lin * 12.92)


def fit(ref_lab, img_lab, keep_ref, keep_img, mode='tone'):
    # mode 'tone' (the default): lightness by histogram, as above, but the two
    # colour axes moved together, by one shift to the reference's mean colour
    # and one common scale for the spread about it, so hues keep their places
    # relative to each other. Matching each colour axis's histogram on its own
    # ('hist') scores better on the colour statistics and looks worse: it
    # pulls separate hues apart, and the rock came out magenta and the clouds
    # cyan.
    ar, br = img_lab[..., 1][keep_img], img_lab[..., 2][keep_img]
    at, bt = ref_lab[..., 1][keep_ref], ref_lab[..., 2][keep_ref]
    spread = np.sqrt((at.var() + bt.var()) / max(ar.var() + br.var(), 1e-9))
    curves = []
    for ch, (lo, hi) in enumerate(DOMAIN):
        v = np.linspace(lo, hi, 256)
        if mode == 'tone' and ch > 0:
            r_mean = (ar if ch == 1 else br).mean(); t_mean = (at if ch == 1 else bt).mean()
            mapped = (v - r_mean) * spread + t_mean
            curves.append(np.clip(np.round((mapped - lo) / (hi - lo) * 255), 0, 255).astype(np.uint8))
            continue
        r = np.sort(img_lab[..., ch][keep_img].ravel())
        t = np.sort(ref_lab[..., ch][keep_ref].ravel())
        q = np.interp(v, r, np.linspace(0, 1, len(r)))
        mapped = np.interp(q, np.linspace(0, 1, len(t)), t)
        # a light smoothing, so a gap in either histogram does not band
        k = np.array([1, 2, 3, 2, 1], float); k /= k.sum()
        mapped = np.convolve(np.pad(mapped, 2, mode='edge'), k, mode='valid')
        mapped = np.maximum.accumulate(mapped)          # keep it monotonic
        curves.append(np.clip(np.round((mapped - lo) / (hi - lo) * 255), 0, 255).astype(np.uint8))
    return np.concatenate(curves)


def apply(img_lab, raw):
    out = np.empty_like(img_lab)
    for ch, (lo, hi) in enumerate(DOMAIN):
        curve = raw[ch * 256:(ch + 1) * 256].astype(np.float64) / 255 * (hi - lo) + lo
        u = np.clip((img_lab[..., ch] - lo) / (hi - lo), 0, 1) * 255
        out[..., ch] = np.interp(u, np.arange(256), curve)
    return out


def main(argv):
    masks, files, preview, mode, i = [], [], None, 'tone', 0
    while i < len(argv):
        if argv[i] == '--mask':
            masks.append([float(x) for x in argv[i + 1].split(',')]); i += 2
        elif argv[i] == '--preview':
            preview = argv[i + 1]; i += 2
        elif argv[i] == '--mode':
            mode = argv[i + 1]; i += 2
        else:
            files.append(argv[i]); i += 1
    if len(files) != 2:
        print('usage: fit-transfer.py <reference> <render> [--mask x0,y0,x1,y1 ...] [--preview out.png]'); return 2
    ref = np.asarray(Image.open(files[0]).convert('RGB'), dtype=np.float64) / 255
    img_im = Image.open(files[1]).convert('RGB')
    img = np.asarray(img_im, dtype=np.float64) / 255

    def keep_for(a):
        h, w = a.shape[:2]; k = np.ones((h, w), bool)
        for x0, y0, x1, y1 in masks:
            k[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)] = False
        return k
    raw = fit(ms.lab(ref), ms.lab(img), keep_for(ref), keep_for(img), mode)
    print(base64.b64encode(raw.tobytes()).decode())
    if preview:
        out = lab_to_rgb(apply(ms.lab(img), raw))
        Image.fromarray(np.clip(out * 255 + .5, 0, 255).astype(np.uint8)).save(preview)
        keep = np.ones((ms.H, ms.W), bool)
        for x0, y0, x1, y1 in masks:
            keep[int(y0 * ms.H):int(y1 * ms.H), int(x0 * ms.W):int(x1 * ms.W)] = False
        r = ms.load(files[0])
        for name, path in (('render', files[1]), ('preview', preview)):
            s = ms.score(r, ms.load(path), keep)
            print('%-8s overall %5.1f  colour %5.1f  regions %5.1f  light %5.1f  shapes %5.1f' % (
                name, s['overall'], s['colour'], s['regions'], s['light'], s['shapes']), file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
