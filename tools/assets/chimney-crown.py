# Chimney crowns (r146) for Vaneth's houses. Until r146 a chimney was a plain
# brick box on a third of the houses, and seen against the moonlit sky, which
# is where a chimney is seen from a night street, it was a block. The shaft is
# still a box, laid by the game in the city's brick batch at whatever height
# the roof needs, so it costs no draw call and its bricks are never stretched;
# what is modelled here is the top of it: a stone string course, two courses
# corbelled out, a mortared cap with soot at the flue, and clay pots.
#
#   chimney-crown         one flue, two pots      (0.76 x 0.76 shaft)
#   chimney-crown-double  a wide stack, three pots (1.30 x 0.70 shaft)
#
# Local frame (game axes): y=0 is the top of the shaft; the string course
# hangs half a metre below it, on the shaft. Untextured in the game (tex
# 'none'), so the brick here is the colour of the city's brick texture.
#
#   python tools/assets/chimney-crown.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset, box_verts, BOX_FACES

CORBEL = (.40, .23, .19)
STONE = (.56, .54, .56)
CAP = (.47, .45, .46)
SOOT = (.09, .08, .08)
POT = (.68, .40, .26)
POT2 = (.57, .33, .22)


def disc(a, r, x, y, z, color, sides=6):
    # One flat polygon facing up (the reversed ring faces +y; see _kit.cyl).
    v = [(math.cos(i / sides * math.tau) * r, 0, math.sin(i / sides * math.tau) * r) for i in range(sides)]
    a.mesh(v, [tuple(reversed(range(sides)))], color, at=(x, y, z))


def crown(a, w, d, pots):
    # A thousand of these stand in the city, so no face that cannot be seen:
    # the cap sits on the second corbel course and has no underside, and the
    # soot is only a top.
    a.box(w + .08, .12, d + .08, 0, -.56, 0, STONE)               # string course
    a.box(w + .10, .13, d + .10, 0, .065, 0, CORBEL)             # corbelled out twice
    a.box(w + .22, .14, d + .22, 0, .20, 0, CORBEL)
    a.mesh(box_verts(w + .16, .06, d + .16, 1.0), BOX_FACES[1:], CAP, at=(0, .30, 0))   # the mortared cap
    a.mesh([(-(w - .1) / 2, 0, -(d - .1) / 2), ((w - .1) / 2, 0, -(d - .1) / 2), ((w - .1) / 2, 0, (d - .1) / 2), (-(w - .1) / 2, 0, (d - .1) / 2)],
           [(3, 2, 1, 0)], SOOT, at=(0, .334, 0))                   # soot round the flues
    for k, (px, pz, h) in enumerate(pots):
        col = POT if k % 2 == 0 else POT2
        # The pot's foot is in the cap and the flue is a black top. (A rolled
        # rim was two pixels from the street and 12 triangles a pot, times
        # three thousand pots: left off.)
        a.cyl(.14, .115, h, px, .33 + h / 2, pz, col, sides=5, cap=False)
        disc(a, .115, px, .33 + h, pz, SOOT, sides=5)


s = Asset('chimney-crown', seed=1461)
crown(s, .76, .76, [(-.17, .0, .46), (.18, .03, .36)])
s.finish(cam_at=(1.7, 1.1, 2.1), cam_look=(0, .05, 0), res=(500, 500), lens=35, sun=(50, 0, 140))

t = Asset('chimney-crown-double', seed=1462)
crown(t, 1.30, .70, [(-.42, .0, .40), (0, .03, .52), (.42, -.02, .36)])
t.finish(cam_at=(2.1, 1.2, 2.5), cam_look=(0, .05, 0), res=(500, 500), lens=35, sun=(50, 0, 140))
