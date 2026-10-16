# Dunna Wex, the chandler of Lowmere — reference NPC role design preview.
#
# A merchant of the lower town: a human woman in an artisan's apron over an
# amber dress, hair in a practical bun, leaning over her stall counter with a
# bundle of tapers in one hand and the other arranging the wares. Gameplay
# flavour: a vendor figure — the kind of role a playable Emberwatch would buy
# from and hear gossip from.
#
# Built on _kit's tube() so every limb tapers PS2-meshy: upper arm wider than
# forearm, calves narrowing to the ankle, hands tapering past the wrist. No
# constant-cross-section box limbs anywhere on the figure.
#
#   ~/workspace/blender/blender-4.5.14-linux-x64/blender --background \
#     --python tools/assets/dunna-wex.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset

SKIN   = (.90, .72, .58)
SKIN_D = (.80, .60, .47)
HAIR   = (.24, .15, .09)
DRESS  = (.56, .37, .19)
DRESS_D= (.43, .27, .13)
APRON  = (.79, .72, .59)
APRON_D= (.64, .57, .45)
WAX    = (.90, .82, .60)
STOCK  = (.62, .52, .40)
SHOE   = (.20, .14, .10)
TIMBER = (.33, .24, .15)
TIMBER_D=(.26, .18, .11)
CREAM  = (.93, .86, .68)
AMBER  = (.86, .64, .32)
MADDER = (.62, .22, .14)

a = Asset('dunna-wex', seed=20261015)

# ---- legs & shoes (mostly under the dress hem) ------------------------------
for sx in (-1, 1):
    x = sx * .095
    a.box(.11, .09, .24, x, .045, .03, SHOE, taper=1.1)          # shoe
    a.tube([(x, .09, 0), (x, .25, .005), (x, .42, .01)],        # calf, tapering
           [.052, .045, .038], STOCK, sides=8)

# ---- dress: flared, pleated skirt --------------------------------------------
a.tube([(0, .98, 0), (0, .76, .008), (0, .54, .014), (0, .34, .02)],
       [.185, .225, .265, .30], [DRESS, DRESS, DRESS_D],
       sides=10, folds=7, amps=[0, .05, .07, .09])

# ---- torso, leaning a touch over the counter ---------------------------------
a.tube([(0, .98, 0), (0, 1.20, .02), (0, 1.40, .05)],
       [.180, .172, .158], DRESS, sides=10)

# ---- apron: bib panel, waistband, a wax stain --------------------------------
a.box(.34, .82, .028, 0, .90, .205, APRON, rx=-.07, taper=.82)
a.box(.40, .055, .035, 0, 1.29, .175, APRON_D, rx=-.05)
a.box(.10, .15, .006, .07, .72, .222, WAX, rx=-.07)              # wax splash
a.box(.07, .05, .006, -.08, 1.05, .215, WAX, rx=-.07)

# ---- neck & head --------------------------------------------------------------
a.cyl(.045, .050, .10, 0, 1.47, .05, SKIN_D, sides=8)
a.tube([(0, 1.50, .05), (0, 1.58, .058), (0, 1.66, .052),
        (0, 1.73, .042), (0, 1.775, .035)],
       [.052, .098, .104, .078, .028], SKIN, sides=10)

# ---- hair: mass over the back of the head + a bun -----------------------------
a.tube([(0, 1.70, .05), (0, 1.755, .015), (0, 1.71, -.035), (0, 1.63, -.055)],
       [.104, .092, .096, .062], HAIR, sides=8)
a.tube([(0, 1.695, -.055), (0, 1.69, -.115), (0, 1.685, -.155)],
       [.052, .058, .030], HAIR, sides=8)

# ---- arms, tend-wares: forward over the counter --------------------------------
# right arm ends holding the taper bundle; left hand stays open, arranging.
a.tube([(.205, 1.40, .05), (.255, 1.20, .20), (.185, 1.045, .40)],
       [.058, .046, .036], [DRESS, SKIN], sides=8)
a.tube([(-.205, 1.40, .05), (-.265, 1.22, .17), (-.145, 1.06, .35)],
       [.058, .046, .036], [DRESS, SKIN], sides=8)
# hands taper past the wrist
a.tube([(.185, 1.045, .40), (.185, 1.03, .52)], [.034, .020], SKIN, sides=7)
a.tube([(-.145, 1.06, .35), (-.105, 1.045, .47)], [.034, .020], SKIN, sides=7)

# ---- the taper bundle in her right hand ----------------------------------------
for k, (dx, dz, col, tilt) in enumerate([
        (0, 0, CREAM, .06), (.028, .012, AMBER, -.05),
        (-.028, .010, CREAM, .10), (.012, -.026, MADDER, -.09),
        (-.014, -.024, AMBER, .04)]):
    a.cyl(.011, .013, .34, .185 + dx, 1.20, .52 + dz, col,
          sides=6, rx=tilt, rz=tilt * .7)

# ---- her stall counter ----------------------------------------------------------
a.box(1.30, .07, .55, 0, .865, .78, TIMBER)                       # counter top
for sx in (-1, 1):
    for sz in (0, 1):
        a.box(.08, .83, .08, sx * .58, .415, .55 + sz * .46, TIMBER_D)
a.box(1.16, .05, .44, 0, .18, .78, TIMBER_D)                      # low shelf
# a rack of finished tapers on the counter
a.box(.34, .05, .12, -.38, .925, .72, TIMBER_D)
for k, col in enumerate([CREAM, AMBER, CREAM, MADDER, AMBER, CREAM]):
    a.cyl(.011, .013, .30, -.50 + k * .048, 1.10, .72, col, sides=6,
          rx=.05 * (1 if k % 2 else -1))
# a crate of tallow blocks under the counter
a.box(.34, .26, .30, .42, .31, .78, TIMBER_D)
a.box(.30, .05, .26, .42, .465, .78, WAX)

a.finish(cam_at=(1.5, 1.45, 2.7), cam_look=(0, 1.0, 0.3), res=(700, 900),
         lens=35, sun=(35, 0, 35),
         extra_views=(('back', (-1.5, 1.45, -2.7), (0, 1.0, 0.1)),))
