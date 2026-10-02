# The street lamp (r147). Every lamp in Vaneth's streets was a tapered wooden
# pole with a glowing cube on top and a stick across it. This is a lamp post:
# a cast-iron foot and shaft, the lamplighter's ladder-bar, and a four-paned
# lantern under a pyramid hood with a finial.
#
#   street-lamp       glass lit (alpha < 1: placeLandmark glow)
#   street-lamp-dark  the same, glass dark, for the lamps the city leaves unlit
#
# Local frame (game axes): the foot at y=0; the lantern's middle at 3.85 m,
# where the lamp's light is.
#
#   python tools/assets/street-lamp.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

IRON = (.14, .14, .16)
IRON2 = (.21, .20, .22)
LIT = (1.0, .80, .48, .08)
DARK = (.10, .11, .15)


def lamp(a, glass):
    a.cyl(.24, .19, .34, 0, .17, 0, IRON, sides=8)                        # the foot
    a.cyl(.2, .2, .06, 0, .37, 0, IRON2, sides=8)
    a.cyl(.085, .065, 3.2, 0, .4 + 1.6, 0, IRON, sides=8, cap=False)       # the shaft
    a.cyl(.1, .1, .08, 0, 1.2, 0, IRON2, sides=8)                          # collars
    a.cyl(.09, .09, .06, 0, 3.3, 0, IRON2, sides=8)
    a.span((-.36, 3.36, 0), (.36, 3.36, 0), .045, .045, IRON)             # the ladder-bar
    for s in (-1, 1):
        a.cyl(.03, .03, .05, s * .36, 3.36, 0, IRON2, sides=6)             # its knobs
    a.cyl(.07, .15, .1, 0, 3.58, 0, IRON, sides=4, ry=math.pi / 4)        # the lantern's seat
    a.box(.26, .34, .26, 0, 3.82, 0, glass)                                # the glass
    for sx in (-1, 1):                                                     # corner bars
        for sz in (-1, 1):
            a.box(.035, .38, .035, sx * .135, 3.82, sz * .135, IRON)
    a.box(.3, .03, .3, 0, 4.0, 0, IRON2)                                   # the hood's rim
    a.cyl(.23, 0, .24, 0, 4.13, 0, IRON, sides=4, ry=math.pi / 4)         # the hood
    a.cyl(.035, 0, .16, 0, 4.32, 0, IRON2, sides=6)                        # finial


for name, glass in (('street-lamp', LIT), ('street-lamp-dark', DARK)):
    s = Asset(name, seed=1480)
    lamp(s, glass)
    s.finish(cam_at=(2.4, 3.2, 3.4), cam_look=(0, 2.6, 0), res=(400, 600), lens=35, sun=(50, 0, 140),
             extra_views=[('head', (.9, 4.1, 1.2), (0, 3.85, 0))])
