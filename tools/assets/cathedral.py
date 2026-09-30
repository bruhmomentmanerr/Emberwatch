# The Cathedral of Hours (r144): Vaneth's cathedral, whose bells turn the
# watches. Until r144 it was a 12 x 22 box with a pyramid on it and two
# cylinders for spires — the only tall thing in the city that was not a wall
# tower, and it read as a shed. This is a gothic church you walk into:
#
#   cathedral            the stone: nave and clerestory on an arcade of
#                        piers, two aisles, flying buttresses, the west front
#                        between two towers with belfries and spires, the apse,
#                        a flèche on the ridge, the roofs (slate-dark colour)
#   cathedral-glass      every window: aisle and clerestory lancets, the apse
#                        lancets, the rose over the door, the belfry louvres'
#                        glow (vertex-alpha glow mask, warm in the game)
#   cathedral-furnishing the inside: pews, the altar on its dais, candles,
#                        three hanging candle rings (untextured, glow mask)
#
# Local frame (game axes): the nave runs along Z; the west front with the
# door faces +Z; y=0 is the floor. The footprint is x -10..10, z -15.6..15.6.
# Colliders are traced from these numbers in index.html (placeCathedral).
#
# The east tower (r149) is hollow and climbable: a door from the east aisle,
# a square newel stair of stone steps winding up its inside walls — ten
# flights of eight, 19 m — to a timber belfry floor under open pointed arches,
# with two bells in a frame. Its plan is the BELL_* numbers below, which the
# game reads again to lay the steps it walks on (placeCathedral).
#
#   python tools/assets/cathedral.py
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import Asset, pointed_arch_curve

STONE = (0.80, 0.79, 0.86)
STONE2 = (0.66, 0.65, 0.73)
DARK = (0.36, 0.35, 0.42)
SLATE = (0.30, 0.31, 0.40)
SLATE2 = (0.24, 0.25, 0.33)
LEAD = (0.40, 0.42, 0.50)

# Plan (metres).
FRONT, BACK = 15.5, -9.0          # nave from the west front to where the apse begins
NAVE_X, NAVE_T = 5.0, 0.8         # the arcade/clerestory line and its wall thickness
AISLE_X, AISLE_T = 9.5, 1.0       # the aisles' outer walls
TOWER_Z0 = 9.5                    # the towers stand from here to FRONT
TOWER_X0, TOWER_X1 = 4.0, 10.0
PIERS = [7.5, 4.0, 0.5, -3.0, -6.5]           # arcade piers along each side (z)
BAYS = [(PIERS[i] + PIERS[i + 1]) / 2 for i in range(len(PIERS) - 1)]   # window bays between them
ARCADE_TOP, CLER_TOP = 8.0, 16.0
AISLE_H = 8.0
RIDGE = 23.0
APSE_R = 5.6

# The climbable (east, +x) tower, in the tower's own offsets from its middle.
BELL_IN = 2.2                     # the shaft's inner half-width
BELL_W = 1.0                      # a flight's width, and a corner landing's
BELL_RISE, BELL_STEPS, BELL_FLIGHTS = 1.9, 8, 10
BELL_FLOOR = BELL_RISE * BELL_FLIGHTS          # 19.0
BELL_DOOR = (-1.6, -.1, 2.4)      # the door in its south wall: x from, x to, height (a body's width either side of the middle)


# ---- the stone ------------------------------------------------------------------
s = Asset('cathedral', seed=1444)
g = Asset('cathedral-glass', seed=1445)
GLASS = (0.55, 0.48, 0.62, .18)
GLASS2 = (0.62, 0.40, 0.36, .2)

# Floor, and the apse's.
s.box(2 * AISLE_X, .15, FRONT - BACK, 0, .075, (FRONT + BACK) / 2, STONE2)
s.cyl(APSE_R, APSE_R, .15, 0, .075, BACK, STONE2, sides=10)

# The arcade: piers with a moulded base and capital, pointed arches between.
for side in (-1, 1):
    x = side * NAVE_X
    for zp in PIERS:
        s.box(1.0, ARCADE_TOP, 1.0, x, ARCADE_TOP / 2, zp, STONE)
        s.box(1.3, .4, 1.3, x, .2, zp, STONE2)
        s.box(1.25, .3, 1.25, x, 5.4, zp, STONE2)
    for zc in BAYS:
        half = (PIERS[0] - PIERS[1]) / 2 - .5
        s.arch_wall(half, 5.5, 1.6, ARCADE_TOP, NAVE_T, STONE, at=(x, 0, zc), ry=math.pi / 2, side_color=STONE2)
    # the first bay, from the front pier to the towers
    s.box(NAVE_T, ARCADE_TOP, TOWER_Z0 - PIERS[0] - .5, x, ARCADE_TOP / 2, (TOWER_Z0 + PIERS[0] + .5) / 2, STONE)
    # the last, from the rear pier to the apse
    s.box(NAVE_T, ARCADE_TOP, PIERS[-1] - .5 - BACK, x, ARCADE_TOP / 2, (PIERS[-1] - .5 + BACK) / 2, STONE)
    # A string course, then the clerestory: solid between tall lancets.
    s.box(NAVE_T + .3, .35, FRONT - BACK, x, ARCADE_TOP + .17, (FRONT + BACK) / 2, STONE2)
    WIN_SILL, WIN_SPRING, WIN_RISE, WIN_HALF = 9.6, 13.2, 1.4, .8
    edges = [TOWER_Z0] + [(PIERS[i]) for i in range(len(PIERS))] + [BACK]
    for zc in BAYS + [(TOWER_Z0 + PIERS[0]) / 2, (PIERS[-1] + BACK) / 2]:
        s.box(NAVE_T, WIN_SILL - ARCADE_TOP - .35, 2 * WIN_HALF, x, (WIN_SILL + ARCADE_TOP + .35) / 2, zc, STONE)
        s.arch_wall(WIN_HALF, WIN_SPRING, WIN_RISE, CLER_TOP, NAVE_T, STONE, at=(x, 0, zc), ry=math.pi / 2, side_color=DARK)
        g.box(.08, WIN_SPRING - WIN_SILL, 2 * WIN_HALF - .1, x, (WIN_SPRING + WIN_SILL) / 2, zc, GLASS)
        curve = pointed_arch_curve(WIN_HALF - .05, WIN_SPRING, WIN_RISE - .05)
        g.extrude([(p[0], p[1]) for p in curve], .08, GLASS, at=(x, 0, zc), ry=math.pi / 2)
    # the solid wall between the windows (from each window's edge to the next)
    stops = sorted([z + d for z in BAYS + [(TOWER_Z0 + PIERS[0]) / 2, (PIERS[-1] + BACK) / 2] for d in (-WIN_HALF, WIN_HALF)] + [TOWER_Z0, BACK])
    for i in range(0, len(stops) - 1, 2):
        z0, z1 = stops[i], stops[i + 1]
        if z1 - z0 > .05:
            s.box(NAVE_T, CLER_TOP - ARCADE_TOP - .35, z1 - z0, x, (CLER_TOP + ARCADE_TOP + .35) / 2, (z0 + z1) / 2, STONE)
    # the cornice
    s.box(NAVE_T + .5, .4, FRONT - BACK + .4, x, CLER_TOP + .2, (FRONT + BACK) / 2 - .2, STONE2)

# The aisles: outer walls with lancets, buttresses and flying buttresses.
for side in (-1, 1):
    x = side * AISLE_X
    A_SILL, A_SPRING, A_RISE, A_HALF = 1.6, 5.0, 1.2, .75
    for zc in BAYS + [(TOWER_Z0 + PIERS[0]) / 2, (PIERS[-1] + BACK) / 2]:
        s.box(AISLE_T, A_SILL, 2 * A_HALF, x, A_SILL / 2, zc, STONE)
        s.arch_wall(A_HALF, A_SPRING, A_RISE, AISLE_H, AISLE_T, STONE, at=(x, 0, zc), ry=math.pi / 2, side_color=DARK)
        g.box(.08, A_SPRING - A_SILL, 2 * A_HALF - .1, x, (A_SPRING + A_SILL) / 2, zc, GLASS2)
        curve = pointed_arch_curve(A_HALF - .05, A_SPRING, A_RISE - .05)
        g.extrude([(p[0], p[1]) for p in curve], .08, GLASS2, at=(x, 0, zc), ry=math.pi / 2)
    stops = sorted([z + d for z in BAYS + [(TOWER_Z0 + PIERS[0]) / 2, (PIERS[-1] + BACK) / 2] for d in (-A_HALF, A_HALF)] + [TOWER_Z0, BACK])
    for i in range(0, len(stops) - 1, 2):
        z0, z1 = stops[i], stops[i + 1]
        if z1 - z0 > .05:
            s.box(AISLE_T, AISLE_H, z1 - z0, x, AISLE_H / 2, (z0 + z1) / 2, STONE)
    s.box(AISLE_T + .3, .3, TOWER_Z0 - BACK + .3, x, AISLE_H + .15, (TOWER_Z0 + BACK) / 2, STONE2)
    # the aisle's end wall where the apse begins
    s.box(AISLE_X - NAVE_X, AISLE_H, AISLE_T, side * (AISLE_X + NAVE_X) / 2, AISLE_H / 2, BACK, STONE)
    # lean-to roof from the clerestory's foot down over the aisle wall
    y0, y1, x0, x1 = ARCADE_TOP + 1.5, AISLE_H + .25, side * (NAVE_X + NAVE_T / 2), side * (AISLE_X + AISLE_T / 2 + .3)
    for k in range(10):
        z0 = BACK - .2 + k * (TOWER_Z0 - BACK + .4) / 10
        z1 = z0 + (TOWER_Z0 - BACK + .4) / 10
        s.span((x0, y0, (z0 + z1) / 2), (x1, y1, (z0 + z1) / 2), .18, z1 - z0 + .01, SLATE if k % 2 else SLATE2, up=(0, 0, 1))
    # buttresses at every pier, and the flying arches from them to the nave
    for zp in PIERS:
        bx = side * (AISLE_X + AISLE_T / 2 + .7)
        s.box(1.4, 11.0, 1.1, bx, 5.5, zp, STONE, taper=.85)
        s.box(1.6, .5, 1.3, bx, .25, zp, STONE2)
        s.cyl(.55, .0, 2.4, bx, 12.2, zp, STONE2, sides=4, ry=math.pi / 4)        # pinnacle
        # the flier: a sloping rib from the buttress to the clerestory, and a
        # thinner one under it that reads as its arch
        s.span((bx - side * .4, 10.4, zp), (side * (NAVE_X + NAVE_T / 2), 14.2, zp), .55, .7, STONE, up=(0, 0, 1))
        s.span((bx - side * .6, 9.2, zp), (side * (NAVE_X + NAVE_T / 2), 12.6, zp), .3, .6, STONE2, up=(0, 0, 1))

# The nave roof: two steep slopes, courses, a lead ridge.
run = NAVE_X + NAVE_T / 2 + .4
slope = math.atan2(RIDGE - CLER_TOP - .4, run)
for side in (-1, 1):
    for k in range(14):
        z0 = BACK - .3 + k * (TOWER_Z0 - BACK + .6) / 14
        z1 = z0 + (TOWER_Z0 - BACK + .6) / 14
        s.span((side * run, CLER_TOP + .4, (z0 + z1) / 2), (0, RIDGE, (z0 + z1) / 2), .22, z1 - z0 + .01, SLATE if k % 2 else SLATE2, up=(0, 0, 1))
s.box(.5, .4, TOWER_Z0 - BACK + .6, 0, RIDGE + .1, (TOWER_Z0 + BACK) / 2, LEAD)

# The flèche: a slender lead spire on the ridge over the crossing.
FZ = -1.2
s.cyl(1.1, 1.1, 2.4, 0, RIDGE + 1.2, FZ, LEAD, sides=8)
for k in range(8):
    ang = k / 8 * math.tau
    s.box(.12, 2.0, .12, math.cos(ang) * 1.1, RIDGE + 1.2, FZ + math.sin(ang) * 1.1, SLATE2)
g.cyl(.9, .9, 1.6, 0, RIDGE + 1.2, FZ, (0.9, 0.7, 0.5, .3), sides=8)       # the lantern stage, lit
s.cyl(1.2, .02, 11.0, 0, RIDGE + 2.4 + 5.5, FZ, LEAD, sides=8)

# The apse: a half-octagon of tall lancets, its roof a faceted half-cone.
facets = 5
for k in range(facets):
    a0 = math.pi + k * math.pi / facets
    a1 = a0 + math.pi / facets
    p0 = (math.cos(a0) * APSE_R, BACK + math.sin(a0) * APSE_R)
    p1 = (math.cos(a1) * APSE_R, BACK + math.sin(a1) * APSE_R)
    mid = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    L = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
    ry = math.atan2(p1[0] - p0[0], p1[1] - p0[1]) + math.pi / 2
    W_HALF = .8
    # the wall either side of the window, and the window
    for sgn in (-1, 1):
        cx = mid[0] + (p1[0] - p0[0]) / L * sgn * (L / 4 + W_HALF / 2)
        cz = mid[1] + (p1[1] - p0[1]) / L * sgn * (L / 4 + W_HALF / 2)
        s.box(L / 2 - W_HALF + .15, CLER_TOP, NAVE_T, cx, CLER_TOP / 2, cz, STONE, ry=ry)
    s.box(2 * W_HALF, 3.0, NAVE_T, mid[0], 1.5, mid[1], STONE, ry=ry)
    s.arch_wall(W_HALF, 12.0, 1.6, CLER_TOP, NAVE_T, STONE, at=(mid[0], 0, mid[1]), ry=ry, side_color=DARK)
    g.box(2 * W_HALF - .1, 9.0, .08, mid[0], 7.5, mid[1], GLASS, ry=ry)
    curve = pointed_arch_curve(W_HALF - .05, 12.0, 1.55)
    g.extrude([(p[0], p[1]) for p in curve], .08, GLASS, at=(mid[0], 0, mid[1]), ry=ry)
    # a buttress at each angle
    bxz = (math.cos(a1) * (APSE_R + 1.0), BACK + math.sin(a1) * (APSE_R + 1.0))
    if k < facets - 1:
        s.box(1.1, 13.0, 1.4, bxz[0], 6.5, bxz[1], STONE, ry=a1 + math.pi / 2, taper=.8)
        s.cyl(.5, .0, 2.2, bxz[0], 14.1, bxz[1], STONE2, sides=4, ry=math.pi / 4)
    # the roof facet: a triangle from the eaves to the apex over the apse centre
    apex = (0, RIDGE - 1.0, BACK)
    e0 = (p0[0] * 1.08, CLER_TOP + .4, BACK + (p0[1] - BACK) * 1.08)
    e1 = (p1[0] * 1.08, CLER_TOP + .4, BACK + (p1[1] - BACK) * 1.08)
    s.mesh([e0, e1, apex], [(0, 2, 1), (0, 1, 2)], SLATE)

# The climbable tower's shell. Each stage is four walls round the same shaft
# (BELL_IN), thinner as the stage steps in; the ground stage has the door, the
# belfry stage a pair of pointed openings on each face.
def climbable_stage(tx, tz, half, y0, y1, stage):
    t = half - BELL_IN
    for sz in (-1, 1):                                  # south and north walls, full width
        zc = tz + sz * (BELL_IN + t / 2)
        if stage == 0 and sz == -1:
            d0, d1, dh = BELL_DOOR
            s.box(d0 + half, y1 - y0, t, tx + (-half + d0) / 2, (y0 + y1) / 2, zc, STONE)
            s.box(half - d1, y1 - y0, t, tx + (d1 + half) / 2, (y0 + y1) / 2, zc, STONE)
            s.box(d1 - d0, y1 - dh, t, tx + (d0 + d1) / 2, (dh + y1) / 2, zc, STONE)
            s.box(d1 - d0 + .3, .25, t + .1, tx + (d0 + d1) / 2, dh + .12, zc, STONE2)      # its lintel
            continue
        if stage == 2:
            belfry_face(tx, zc, half, t, y0, y1, 'z')
            continue
        s.box(2 * half, y1 - y0, t, tx, (y0 + y1) / 2, zc, STONE)
    for sx in (-1, 1):                                  # east and west walls, between them
        xc = tx + sx * (BELL_IN + t / 2)
        if stage == 2:
            belfry_face(xc, tz, BELL_IN, t, y0, y1, 'x')
            continue
        s.box(t, y1 - y0, 2 * BELL_IN, xc, (y0 + y1) / 2, tz, STONE)


def belfry_face(cx, cz, half, t, y0, y1, axis):
    # sill to 19.6, piers either side of two openings (1.2 wide at +-1.3), the
    # pointed heads from 23.2, solid again above
    SILL, SPRING, RISE = BELL_FLOOR + .6, 23.2, .6
    along = (lambda a, w, h, y: s.box(w, h, t, cx + a, y, cz, STONE)) if axis == 'z' else \
            (lambda a, w, h, y: s.box(t, h, w, cx, y, cz + a, STONE))
    along(0, 2 * half, SILL - y0, (y0 + SILL) / 2)
    for a0, a1 in ((-half, -1.9), (-.7, .7), (1.9, half)):
        along((a0 + a1) / 2, a1 - a0, SPRING + RISE - SILL, (SILL + SPRING + RISE) / 2)
    along(0, 2 * half, y1 - (SPRING + RISE), (SPRING + RISE + y1) / 2)
    for a in (-1.3, 1.3):
        if axis == 'z':
            s.arch_wall(.6, SPRING, RISE, SPRING + RISE, t, STONE, at=(cx + a, 0, cz))
        else:
            s.arch_wall(.6, SPRING, RISE, SPRING + RISE, t, STONE, at=(cx, 0, cz + a), ry=math.pi / 2)


def ring_course(tx, tz, half, y):
    for sz in (-1, 1):
        s.box(2 * half + .3, .35, .5, tx, y, tz + sz * (half - .1), STONE2)
    for sx in (-1, 1):
        s.box(.5, .35, 2 * half + .3, tx + sx * (half - .1), y, tz, STONE2)


# The stair: flight k runs along a wall (south, east, north, west, round and
# up), eight steps of 0.24 over 2.4 m, between corner landings; the tenth
# arrives at the belfry floor. Stone blocks 0.3 deep under each tread.
def bell_stair(tx, tz):
    c, L = BELL_IN - BELL_W / 2, 2 * BELL_IN - 2 * BELL_W
    run, rise = L / BELL_STEPS, BELL_RISE / BELL_STEPS
    dirs = [((1, 0), (0, -1)), ((0, 1), (1, 0)), ((-1, 0), (0, 1)), ((0, -1), (-1, 0))]   # travel, which wall
    corners = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    for k in range(BELL_FLIGHTS):
        (ux, uz), (wx, wz) = dirs[k % 4]
        h0 = k * BELL_RISE
        for j in range(BELL_STEPS):
            a = -L / 2 + (j + .5) * run
            top = h0 + (j + 1) * rise
            x, z = tx + ux * a + wx * c, tz + uz * a + wz * c
            s.box(run + .02 if ux else BELL_W, .3, BELL_W if ux else run + .02, x, top - .15, z, STONE2)
        cx, cz = corners[k % 4]
        if k < BELL_FLIGHTS - 1:
            s.box(BELL_W, .3, BELL_W, tx + cx * c, h0 + BELL_RISE - .15, tz + cz * c, STONE2)
    # The belfry floor, boards over the shaft but for the stair's last two
    # flights (south and east) and the landing between them.
    f0, f1 = BELL_IN - BELL_W, BELL_IN
    s.box(BELL_IN + f0, .25, BELL_IN + f0, tx + (f0 - BELL_IN) / 2, BELL_FLOOR - .125, tz + (BELL_IN - f0) / 2, (0.40, 0.28, 0.18))
    s.box(BELL_W, .25, BELL_W, tx + c, BELL_FLOOR - .125, tz + c, (0.40, 0.28, 0.18))


# The west front: the towers, and between them the portal and the rose.
for side in (-1, 1):
    tx = side * (TOWER_X0 + TOWER_X1) / 2
    tz = (TOWER_Z0 + FRONT) / 2
    TW = TOWER_X1 - TOWER_X0
    TD = FRONT - TOWER_Z0
    stages = [(0, 9.0), (9.0, 17.5), (17.5, 26.0)]
    for i, (y0, y1) in enumerate(stages):
        inset = i * .35
        if side == 1:
            climbable_stage(tx, tz, (TW - inset) / 2, y0, y1, i)
            if i < 2:          # the string course round a hollow shaft is a ring, not a floor
                ring_course(tx, tz, (TW - inset) / 2, y1)
            else:
                s.box(TW - inset + .3, .35, TD - inset + .3, tx, y1, tz, STONE2)
            continue
        s.box(TW - inset, y1 - y0, TD - inset, tx, (y0 + y1) / 2, tz, STONE)
        s.box(TW - inset + .3, .35, TD - inset + .3, tx, y1, tz, STONE2)
    if side == 1:
        bell_stair(tx, tz)
    # corner buttresses up the first two stages
    for cx in (-1, 1):
        for cz in (-1, 1):
            s.box(1.0, 17.0, 1.0, tx + cx * (TW / 2 + .2), 8.5, tz + cz * (TD / 2 + .2), STONE2, taper=.8)
    # the belfry: a tall pair of openings on each face, dark louvres, lit within
    # (the climbable tower's are open, and you stand in its belfry instead)
    fz_off, fx_off = (TD - .7) / 2 + .04, (TW - .7) / 2 + .04
    for n in ((-1, 1) if side == -1 else ()):
        for o in (-1, 1):
            g.box(.9, 5.0, .06, tx + o * 1.3, 21.2, tz + n * fz_off, (0.8, 0.6, 0.45, .5))
            g.box(.06, 5.0, .9, tx + n * fx_off, 21.2, tz + o * 1.3, (0.8, 0.6, 0.45, .5))
            for k in range(5):
                s.box(1.0, .1, .12, tx + o * 1.3, 19.2 + k * .95, tz + n * (fz_off + .05), DARK)
                s.box(.12, .1, 1.0, tx + n * (fx_off + .05), 19.2 + k * .95, tz + o * 1.3, DARK)
    # the parapet and four pinnacles, then the spire
    for cx in (-1, 1):
        for cz in (-1, 1):
            s.box(.8, 2.0, .8, tx + cx * (TW / 2 - .6), 27.0, tz + cz * (TD / 2 - .6), STONE2)
            s.cyl(.45, .0, 3.2, tx + cx * (TW / 2 - .6), 29.6, tz + cz * (TD / 2 - .6), STONE, sides=4, ry=math.pi / 4)
    s.cyl(2.7, 2.7, 1.2, tx, 26.6, tz, STONE2, sides=8)
    s.cyl(2.5, .05, 17.0, tx, 27.2 + 8.5, tz, SLATE, sides=8)
    s.cyl(.25, .05, 1.2, tx, 44.4, tz, LEAD, sides=6)
    # the tower's inner face toward the nave, and its back wall
# Between the towers: the front wall with the portal, the rose, the gable.
PH, PS, PR = 1.7, 4.2, 1.8          # the portal's half width, springing, rise
wall_z = FRONT - .5
s.box(TOWER_X0 - PH, PS + PR, 1.0, -(TOWER_X0 + PH) / 2, (PS + PR) / 2, wall_z, STONE)
s.box(TOWER_X0 - PH, PS + PR, 1.0, (TOWER_X0 + PH) / 2, (PS + PR) / 2, wall_z, STONE)
s.arch_wall(PH, PS, PR, 8.0, 1.0, STONE, at=(0, 0, wall_z), side_color=DARK)
# the portal's orders: three receding pointed arches round the door
for k in range(3):
    ph = PH + .45 * (k + 1)
    curve = pointed_arch_curve(ph, PS, PR + .3 * (k + 1))
    for i in range(len(curve) - 1):
        a0, a1 = curve[i], curve[i + 1]
        s.span((a0[0], a0[1], wall_z + .5 + .2 * (3 - k)), (a1[0], a1[1], wall_z + .5 + .2 * (3 - k)), .28, .3, STONE2 if k % 2 else STONE, up=(0, 0, 1))
    for sx in (-1, 1):
        s.box(.3, PS, .3, sx * ph, PS / 2, wall_z + .5 + .2 * (3 - k), STONE2)
s.box(2 * TOWER_X0, CLER_TOP - 8.0, 1.0, 0, (CLER_TOP + 8.0) / 2, wall_z, STONE)
# the rose: a ring of stone round a glowing disc with radiating tracery
RY_, RR = 11.8, 2.4
g.cyl(RR, RR, .1, 0, RY_, wall_z + .52, GLASS, sides=16, rx=math.pi / 2)
g.cyl(RR, RR, .1, 0, RY_, wall_z - .52, GLASS, sides=16, rx=math.pi / 2)      # and seen from within
ring = [(math.cos(i / 20 * math.tau) * (RR + .25), RY_ + math.sin(i / 20 * math.tau) * (RR + .25), wall_z + .55) for i in range(21)]
s.tube(ring, [.22] * 21, STONE2, sides=5, ref=(0, 0, 1), cap0=False, cap1=False)
for k in range(8):
    ang = k / 8 * math.tau
    s.span((0, RY_, wall_z + .6), (math.cos(ang) * RR, RY_ + math.sin(ang) * RR, wall_z + .6), .12, .12, STONE2, up=(0, 0, 1))
s.cyl(.45, .45, .2, 0, RY_, wall_z + .62, STONE2, sides=10, rx=math.pi / 2)
# the gable over the nave's front, and a statue niche at its peak
s.extrude([(-TOWER_X0, CLER_TOP), (TOWER_X0, CLER_TOP), (0, RIDGE)], 1.0, STONE, at=(0, 0, wall_z))
s.cyl(.3, .0, 2.0, 0, RIDGE + 1.0, wall_z, STONE2, sides=4, ry=math.pi / 4)
# The nave roof's east end, under the apse roof's apex.
s.extrude([(-run, CLER_TOP + .4), (run, CLER_TOP + .4), (0, RIDGE)], .6, STONE, at=(0, 0, BACK - .3))

s.finish(cam_at=(30.0, 18.0, 46.0), cam_look=(0, 14.0, 0), res=(900, 900), lens=30, sun=(50, 0, 140),
         extra_views=[('side', (46.0, 10.0, -4.0), (0, 12.0, -2.0)), ('inside', (1.5, 2.0, 13.0), (0, 5.0, -12.0)),
                      ('belfry', (16.0, 21.0, 22.0), (7.0, 20.0, 12.5))])
g.finish(cam_at=(30.0, 18.0, 46.0), cam_look=(0, 14.0, 0), res=(600, 600), lens=30)

# ---- the furnishing -----------------------------------------------------------------
f = Asset('cathedral-furnishing', seed=1446)
WOOD = (0.34, 0.24, 0.16)
WOOD2 = (0.26, 0.18, 0.12)
IRON = (0.16, 0.16, 0.18)
CLOTH = (0.46, 0.12, 0.14)
CANDLE = (1.0, 0.86, 0.6, .12)
WAX = (0.86, 0.82, 0.70)
# Pews: two blocks either side of the middle aisle.
for side in (-1, 1):
    for r in range(9):
        z = 8.6 - r * 1.35
        x = side * 2.55
        f.box(3.1, .08, .42, x, .48, z, WOOD)              # seat
        f.box(3.1, .5, .06, x, .78, z - .2, WOOD2)          # back
        f.box(3.1, .1, .1, x, 1.05, z - .2, WOOD)           # top rail
        for e in (-1, 1):
            f.box(.08, 1.0, .5, x + e * 1.52, .5, z - .03, WOOD2)
# The dais and the altar, candles, a cloth.
f.box(8.0, .2, 4.0, 0, .1, BACK - .6, (0.62, 0.61, 0.68))
f.box(6.0, .2, 3.0, 0, .3, BACK - 1.0, (0.70, 0.69, 0.76))
f.box(3.0, 1.0, 1.1, 0, .9, BACK - 1.6, (0.78, 0.77, 0.83))
f.box(3.1, .05, 1.2, 0, 1.42, BACK - 1.6, (0.84, 0.84, 0.88))
f.box(.8, .9, 1.22, 0, .95, BACK - 1.6, CLOTH)
for k in range(7):
    x = -1.3 + k * .43
    h = .25 + (k % 3) * .08
    f.cyl(.035, .035, h, x, 1.45 + h / 2, BACK - 1.9, WAX, sides=6)
    f.box(.04, .07, .04, x, 1.45 + h + .04, BACK - 1.9, CANDLE)
for sx in (-1, 1):                                 # two tall candle stands
    f.cyl(.05, .07, 1.8, sx * 2.1, 1.3, BACK - 1.6, IRON, sides=6)
    f.cyl(.2, .1, .08, sx * 2.1, 2.24, BACK - 1.6, IRON, sides=8)
    f.cyl(.06, .06, .35, sx * 2.1, 2.45, BACK - 1.6, WAX, sides=6)
    f.box(.06, .1, .06, sx * 2.1, 2.68, BACK - 1.6, CANDLE)
# A rack of votive candles inside the door, where people light one on
# their way in.
for side in (-1,):
    f.box(1.8, .9, .5, side * 2.9, .45, 12.4, WOOD2, ry=math.pi / 2)
    for k in range(12):
        x = side * 2.9 - .12 + (k // 6) * .24
        z = 12.4 - .75 + (k % 6) * .3
        f.cyl(.03, .03, .1, x, .95, z, WAX, sides=5)
        f.box(.035, .05, .035, x, 1.02, z, CANDLE)
# Three candle rings hung over the nave on chains.
for zc in (6.0, .5, -5.0):
    ring = [(math.cos(i / 16 * math.tau) * 1.1, 7.0, zc + math.sin(i / 16 * math.tau) * 1.1) for i in range(17)]
    f.tube(ring, [.05] * 17, IRON, sides=4, ref=(0, 1, 0), cap0=False, cap1=False)
    for k in range(8):
        ang = k / 8 * math.tau
        cx, cz = math.cos(ang) * 1.1, zc + math.sin(ang) * 1.1
        f.cyl(.03, .03, .14, cx, 7.12, cz, WAX, sides=5)
        f.box(.04, .07, .04, cx, 7.24, cz, CANDLE)
    for k in range(3):
        ang = k / 3 * math.tau
        f.span((math.cos(ang) * 1.1, 7.0, zc + math.sin(ang) * 1.1), (0, 9.2, zc), .03, .03, IRON)
    f.box(.03, 6.6, .03, 0, 9.2 + 3.3, zc, IRON)
# The bells (r149), in a timber frame on the east tower's belfry floor, and a
# lantern for whoever climbs up to them.
BRONZE = (0.55, 0.40, 0.19)
BRONZE2 = (0.42, 0.30, 0.14)
btx, btz = (TOWER_X0 + TOWER_X1) / 2, (TOWER_Z0 + FRONT) / 2
fz = btz + .8
for px in (btx - 2.0, btx + 1.0):                              # the frame's posts and the beam
    f.box(.22, 4.4, .22, px, BELL_FLOOR + 2.2, fz, WOOD2)
    f.span((px, BELL_FLOOR, fz - .9), (px, BELL_FLOOR + 1.6, fz), .14, .14, WOOD2)
    f.span((px, BELL_FLOOR, fz + .9), (px, BELL_FLOOR + 1.6, fz), .14, .14, WOOD2)
f.box(3.3, .26, .3, btx - .5, BELL_FLOOR + 4.3, fz, WOOD)


# The bells themselves are their own model (cathedral-bell, below): the game
# swings them when the watch turns, so they cannot be merged into this one.
f.box(.03, .5, .03, btx - .5, BELL_FLOOR + 3.9, btz - .6, IRON)                  # the lantern's chain
f.box(.2, .06, .2, btx - .5, BELL_FLOOR + 3.62, btz - .6, IRON)
f.box(.16, .24, .16, btx - .5, BELL_FLOOR + 3.47, btz - .6, CANDLE)
f.finish(cam_at=(6.0, 5.0, 14.0), cam_look=(0, 1.5, -2.0), res=(800, 600), lens=30,
         extra_views=[('bells', (btx + 2.0, BELL_FLOOR + 1.6, btz - 2.0), (btx - .8, BELL_FLOOR + 2.6, fz))])

# ---- the bell ---------------------------------------------------------------------
# One bell, hung from its headstock: the origin is the pivot it swings on,
# under the frame's beam, and the bell hangs below. The game lays two, the
# second at three quarters the size (placeCathedral, cathedralBellTower).
b = Asset('cathedral-bell', seed=1447)
b.box(.9, .2, .22, 0, .02, 0, WOOD2)                                      # the headstock
for s in (-1, 1):
    b.cyl(.05, .05, .14, s * .52, .02, 0, IRON, sides=6, rz=math.pi / 2)    # its gudgeons, the pins it swings on
    b.box(.05, .35, .12, s * .2, -.07, 0, IRON)                            # the straps down to the crown
b.box(.18, .2, .18, 0, -.1, 0, BRONZE2)                                   # the canons
b.cyl(.34, .26, .26, 0, -.33, 0, BRONZE, sides=10)                        # the shoulder
b.cyl(.47, .34, .6, 0, -.76, 0, BRONZE, sides=10, cap=False)              # the waist
b.cyl(.62, .47, .34, 0, -1.23, 0, BRONZE, sides=10, cap=False)            # the sound bow
b.cyl(.64, .62, .07, 0, -1.43, 0, BRONZE2, sides=10, cap=False)
b.cyl(.365, .365, .04, 0, -.47, 0, BRONZE2, sides=10, cap=False)         # the mouldings that band it
b.cyl(.5, .5, .05, 0, -1.07, 0, BRONZE2, sides=10, cap=False)
b.cyl(.03, .03, .9, 0, -.95, 0, IRON, sides=4)                            # the clapper
b.cyl(.09, .09, .16, 0, -1.36, 0, IRON, sides=6)
b.finish(cam_at=(2.2, -.4, 2.6), cam_look=(0, -.7, 0), res=(400, 460), lens=35)
