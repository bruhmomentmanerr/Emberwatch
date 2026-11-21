# Region by region, how far is a render from the reference? (r180)
#
#   python tools/region-audit.py <reference> <render> [--sheet out.png]
#
# tools/match-score.py gives one number a measure; this breaks the frame into
# the parts a viewer names (sky, the mountain, the castle, the cliff and
# falls, the valley, the rock, the wizard) and for each reports, reference
# against render: the mean colour (CIELAB L, a, b), the spread of lightness
# (sd of L), the edge density (detail), and the colour difference between
# the means (delta E, 1976). With --sheet it draws both frames with the
# regions outlined, so a number can be found in the picture.
#
# The regions are fractions of the frame, set for the owner's wizard-vista
# reference in a 540 x 960 frame; a different reference wants its own.
#
# Needs Pillow and NumPy.
import sys
import numpy as np
from PIL import Image, ImageDraw

W, H = 540, 960
REGIONS = {
    'sky':             (.00, .00, .55, .26),
    'moon sky':        (.30, .05, .62, .22),
    'left mountain':   (.00, .30, .12, .62),
    'castle':          (.55, .30, 1.0, .45),
    'cliff and falls': (.50, .45, 1.0, .62),
    'valley':          (.50, .62, 1.0, .82),
    'rock':            (.45, .87, 1.0, 1.0),
    'wizard':          (.10, .45, .40, .85),
}


def load(p):
    return np.asarray(Image.open(p).convert('RGB').resize((W, H), Image.LANCZOS), dtype=np.float64) / 255.0


def lab(rgb):
    c = np.where(rgb > .04045, ((rgb + .055) / 1.055) ** 2.4, rgb / 12.92)
    xyz = c @ np.array([[.4124, .3576, .1805], [.2126, .7152, .0722], [.0193, .1192, .9505]]).T
    xyz /= np.array([.95047, 1.0, 1.08883])
    f = np.where(xyz > .008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def edges(rgb):
    g = rgb.mean(-1)
    return np.hypot(np.diff(g, axis=1)[:-1, :], np.diff(g, axis=0)[:, :-1])


def stats(rgb, box):
    x0, y0, x1, y1 = int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)
    part = rgb[y0:y1, x0:x1]
    lb = lab(part)
    return lb.reshape(-1, 3).mean(0), lb[..., 0].std(), edges(part).mean() * 100


def main(argv):
    sheet = None
    if '--sheet' in argv:
        i = argv.index('--sheet'); sheet = argv[i + 1]; del argv[i:i + 2]
    ref, img = load(argv[0]), load(argv[1])
    print('%-16s %20s %20s %7s %7s %7s' % ('region', 'reference L a b', 'render L a b', 'sd ref', 'sd ren', 'dE'))
    rows = []
    for name, box in REGIONS.items():
        (mr, sr, er), (mi, si, ei) = stats(ref, box), stats(img, box)
        de = float(np.linalg.norm(mr - mi))
        rows.append((name, de))
        print('%-16s %6.1f %6.1f %6.1f  %6.1f %6.1f %6.1f %7.1f %7.1f %7.1f   detail %4.1f / %4.1f' % (
            name, *mr, *mi, sr, si, de, er, ei))
    print('worst first: ' + ', '.join('%s %.1f' % r for r in sorted(rows, key=lambda r: -r[1])))
    if sheet:
        out = Image.new('RGB', (W * 2 + 8, H), (20, 20, 20))
        for k, a in enumerate((ref, img)):
            im = Image.fromarray((a * 255).astype(np.uint8)); d = ImageDraw.Draw(im)
            for name, b in REGIONS.items():
                d.rectangle((b[0] * W, b[1] * H, b[2] * W - 1, b[3] * H - 1), outline=(255, 220, 0)); d.text((b[0] * W + 3, b[1] * H + 2), name, fill=(255, 220, 0))
            out.paste(im, (k * (W + 8), 0))
        out.save(sheet)


if __name__ == '__main__':
    main(sys.argv[1:])
