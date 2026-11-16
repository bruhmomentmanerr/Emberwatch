# The Veilscar peaks (r175): the grey rock mountains that stand to the left
# of the castle in the owner's reference frame, behind the wizard's shoulder:
# pale streaked spires, the tallest about seventy metres, falling in buttresses
# to green lower slopes. The game's ring of peaks is far off and dark; these
# are near enough to read as rock.
#
# Local frame (game axes): x runs along the range, z back from its front
# (toward -Z is the side the wizard sees), y=0 is the valley floor. It stands
# inside x -45..45, z -30..30.
#
#   python tools/assets/veilscar-peaks.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

PALE = (0.74, 0.72, 0.84)
PALE2 = (0.60, 0.58, 0.72)
DARK = (0.40, 0.39, 0.52)
GREEN = (0.34, 0.50, 0.32)

a = Asset('veilscar-peaks', seed=1751)
r = a.rng

# Spires: tall jagged rocks stacked two or three high, the tallest near the
# middle-left, the range falling away to the right.
SPIRES = [(-30, 6, 46), (-18, -2, 72), (-6, 8, 58), (6, -4, 64), (18, 6, 44), (30, -2, 36), (-38, -10, 28), (38, 10, 26)]
for (x, z, h) in SPIRES:
    y = 0
    w = h * .42
    k = 0
    while y < h - 2:
        seg = min(h - y, r.uniform(.28, .42) * h)
        a.rock(w, seg * 1.25, w * r.uniform(.8, 1.1), x + r.uniform(-1.5, 1.5), y + seg * .5, z + r.uniform(-1.5, 1.5),
               (PALE, PALE2, DARK)[(k + int(x)) % 3], jag=.32, sides=7, ry=r.uniform(0, 3),
               top_color=PALE if k > 0 else GREEN)
        y += seg * .85
        w *= r.uniform(.55, .7)
        k += 1
    # a needle on top
    a.rock(w * .9, h * .14, w * .8, x, y + h * .05, z, PALE, jag=.4, sides=5, ry=r.uniform(0, 3))
    # buttresses at the foot
    for b in range(3):
        ang = r.uniform(0, math.tau)
        a.rock(h * .3, h * .22, h * .26, x + math.cos(ang) * h * .22, h * .09, z + math.sin(ang) * h * .2,
               (PALE2, DARK)[b % 2], jag=.3, sides=6, ry=ang, top_color=GREEN)
# Green lower slopes between them, low and broad.
for k in range(10):
    x = -42 + k * 9.3 + r.uniform(-2, 2)
    a.rock(r.uniform(14, 20), r.uniform(6, 11), r.uniform(14, 22), x, 2.5, r.uniform(-6, 10), GREEN, jag=.2, sides=7,
           ry=r.uniform(0, 3), top_color=GREEN)

a.finish(cam_at=(0, 30, -150), cam_look=(0, 30, 0), res=(1000, 600), lens=35, sun=(40, 0, -30))
