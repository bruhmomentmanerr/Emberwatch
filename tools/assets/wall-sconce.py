# A wall torch in an iron sconce (r148), for the faces of the town walls: a
# back-plate, a bracket out from it, a cup, and the torch burning in it.
# Until r148 the walls between the gates were twelve metres of unlit stone,
# and the ring road along them the darkest street in Vaneth.
#
# Local frame (game axes): the wall is the plane z=0, the bracket comes out
# along +z, y=0 is the torch cup. The flame carries alpha < 1 (placeLandmark
# glow).
#
#   python tools/assets/wall-sconce.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

IRON = (.13, .13, .15)
IRON2 = (.2, .19, .21)
WOOD = (.34, .22, .13)
PITCH = (.08, .06, .05)
FLAME = (1.0, .66, .30, .05)
FLAME2 = (1.0, .85, .5, .05)

a = Asset('wall-sconce', seed=1481)
a.box(.2, .5, .04, 0, -.15, .02, IRON)                                # back-plate
a.span((0, -.32, .04), (0, -.06, .42), .04, .04, IRON)                # the brace
a.span((0, -.02, .03), (0, -.02, .46), .045, .045, IRON)              # the arm
a.cyl(.09, .06, .12, 0, 0, .46, IRON2, sides=6)                        # the cup
a.cyl(.035, .03, .5, 0, .12, .46, WOOD, sides=5)                       # the torch
a.cyl(.05, .055, .14, 0, .4, .46, PITCH, sides=5)                      # its pitch head
a.cyl(.075, 0, .36, 0, .65, .46, FLAME, sides=5)                       # the flame
a.cyl(.045, 0, .24, .015, .6, .47, FLAME2, sides=4)
a.finish(cam_at=(1.2, .3, 1.3), cam_look=(0, .1, .3), res=(400, 460), lens=35, sun=(40, 0, 60))
