# The avenues' festoons (r146): an iron pole at each kerb and small lanterns
# hung along a string between a pair of them, across the carriageway, as the
# Cinder Market's strings hang between its stalls.
#
#   festoon-pole     a cast-iron post, 5.1 m, a bracket arm to carry the string
#   festoon-lantern  a hanging lantern, hook at the top, glass lit
#
# Local frames (game axes): the pole's foot is at y=0 and its arm points to
# +z, where the string is hooked at (0, 4.95, 0.44); the game turns the arm to
# face the pole across the avenue. The lantern's hook is at its origin and it
# hangs below. Glass carries alpha < 1: the game lights it (placeLandmark glow).
#
#   python tools/assets/festoon.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

IRON = (.15, .15, .17)
IRON2 = (.22, .21, .23)
GLASS = (1.0, .78, .45, .1)

p = Asset('festoon-pole', seed=1463)
p.cyl(.19, .15, .42, 0, .21, 0, IRON, sides=8)                        # cast foot
p.cyl(.17, .17, .06, 0, .45, 0, IRON2, sides=8)
p.cyl(.075, .06, 4.6, 0, .48 + 2.3, 0, IRON, sides=8, cap=False)       # the shaft
p.cyl(.1, .1, .08, 0, 2.5, 0, IRON2, sides=8)                          # a collar at head height
p.cyl(.09, .09, .07, 0, 5.1, 0, IRON2, sides=8)                        # cap and finial
p.cyl(.07, 0, .3, 0, 5.28, 0, IRON, sides=8)
p.span((0, 4.95, 0), (0, 4.95, .47), .045, .045, IRON)                 # the arm
p.span((0, 4.52, .02), (0, 4.93, .34), .03, .03, IRON)                 # and its brace
p.cyl(.035, .035, .1, 0, 4.9, .44, IRON2, sides=6)                     # the hook
p.finish(cam_at=(3.6, 3.4, 5.6), cam_look=(0, 2.75, 0), res=(400, 600), lens=30, sun=(50, 0, 140),
         extra_views=[('top', (1.1, 5.3, 1.4), (0, 4.95, .2))])

l = Asset('festoon-lantern', seed=1464)
l.box(.014, .1, .014, 0, -.05, 0, IRON)                                # the hanger
l.cyl(.09, 0, .08, 0, -.14, 0, IRON, sides=6)                          # the hood
l.cyl(.095, .095, .02, 0, -.19, 0, IRON2, sides=6)
l.cyl(.066, .066, .17, 0, -.285, 0, GLASS, sides=6)                    # the glass
l.cyl(.075, .045, .045, 0, -.392, 0, IRON, sides=6)                    # the drip plate
l.finish(cam_at=(.7, -.15, .8), cam_look=(0, -.22, 0), res=(400, 400), lens=35, sun=(50, 0, 140))
