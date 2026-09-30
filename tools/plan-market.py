# Bake the Cinder Market's fixture table (r144).
#
#   python3 tools/plan-market.py > /tmp/market-table.js
#
# The market is authored, not generated at runtime (docs/AUTHORED-CITY-
# DRESSING.md): this script only does the arithmetic of laying stalls in rows
# along the avenue and prints every record with its exact transform, so the
# table in index.html says in plain numbers what will be drawn. The game
# tests each record's footprint and skips (and logs) any that does not fit;
# it never moves one.
#
# The square: paving r 31 round (0, 108). The north avenue crosses it, 10 m
# wide, centre line (-0.8, 54) -> (-6, 120). A crooked lane cuts its north
# edge, (-43.2, 125.9) -> (43.2, 140.1), 7 m wide. The Cinder and Keg's west
# wall is x 27 (z 105.5..122.5); a brick house's east wall is x -31.5
# (z 106.5..117.5).
#
# Rows run parallel to the avenue. Offsets are across it, east negative in
# the frame's t (t points west):
#   E1a  faces the avenue           W1a  faces the avenue
#   E1b  back to E1a, faces east    W1b  back to W1a, faces west
#   E3   faces E1b across an aisle  W3   faces W1b across an aisle
# The hearth court breaks the east rows round the fire; the west rows break
# once for a cross-aisle to the square's west side.
import math

CX, CZ = -5.05, 108.0                      # the avenue's centre line at z 108
UX, UZ = -0.0786, 0.9969                   # along the avenue, north
TX, TZ = -UZ, UX                           # across it; +t is west


def at(s, t):
    return (CX + UX * s + TX * t, CZ + UZ * s + TZ * t)


def facing(dx, dz):
    return math.atan2(dx, dz)


RY_WEST = facing(TX, TZ)                   # a stall whose front looks west
RY_EAST = facing(-TX, -TZ)

ROAD_HALF, VERGE = 5.0, 1.5
DEPTH_FRONT, DEPTH_BACK = 1.65, 1.55       # stall footprint from its centre
HALF_W = 2.35
PITCH = 5.5                                # one stall and a 0.8 m gap
AISLE = 6.5

off_1a = ROAD_HALF + VERGE + DEPTH_FRONT                  # 8.15
off_1b = off_1a + DEPTH_BACK + .3 + DEPTH_BACK            # back to back
off_3 = off_1b + DEPTH_FRONT + AISLE + DEPTH_FRONT


def on_paving(x, z, margin=.4):
    return math.hypot(x, z - 108) <= 31 - margin


def clear_of_lane(x, z, margin=1.0):
    ax, az, bx, bz, w = -43.2, 125.9, 43.2, 140.1, 7
    dx, dz = bx - ax, bz - az
    L = math.hypot(dx, dz)
    ux, uz = dx / L, dz / L
    t = max(0, min(L, (x - ax) * ux + (z - az) * uz))
    return math.hypot(x - (ax + ux * t), z - (az + uz * t)) > w / 2 + margin


def clear_of_buildings(x, z):
    if 26.3 < x and 104.8 < z < 123.2:
        return False
    if x < -30.8 and 105.8 < z < 118.2:
        return False
    return True


def corners(x, z, ry):
    co, si = math.cos(ry), math.sin(ry)
    out = []
    for lx, lz in ((-HALF_W, -DEPTH_BACK), (HALF_W, -DEPTH_BACK), (HALF_W, DEPTH_FRONT), (-HALF_W, DEPTH_FRONT), (0, 0)):
        out.append((x + lx * co + lz * si, z - lx * si + lz * co))
    return out


TRADES = ['produce', 'cloth', 'pots']
TRADE_WORDS = {'produce': 'a grocer', 'cloth': 'a draper', 'pots': 'a potter'}
ROW_WORDS = {'e1a': 'facing the avenue, east side', 'e1b': 'on the east aisle, avenue side',
             'e3': 'on the east aisle, far side', 'w1a': 'facing the avenue, west side',
             'w1b': 'on the west aisle, avenue side', 'w3': 'on the west aisle, far side'}

rows = [
    ('e1a', -off_1a, RY_WEST, [-26, -20.5, -15, -9.5, 9.5, 15]),
    ('e1b', -off_1b, RY_EAST, [-26, -20.5, -15, -9.5, 9.5, 15]),
    ('e3', -off_3, RY_WEST, [-18, -12.5, -7, -1.5, 4, 9.5]),
    ('w1a', off_1a, RY_EAST, [-26, -20.5, -15, -9.5, 1.5, 7, 12.5]),
    ('w1b', off_1b, RY_WEST, [-26, -20.5, -15, -9.5, 1.5, 7, 12.5]),
    ('w3', off_3, RY_EAST, [-18, -12.5, -7, -1.5, 4, 9.5]),
]

stalls, skipped = [], []
k = 0
for row, t, ry, slots in rows:
    for i, s in enumerate(slots):
        x, z = at(s, t)
        pts = corners(x, z, ry)
        ok = all(on_paving(px, pz) and clear_of_lane(px, pz) and clear_of_buildings(px, pz) for px, pz in pts)
        rid = 'cm-%s-%d' % (row, i + 1)
        if not ok:
            skipped.append(rid)
            continue
        trade = TRADES[int((k * 0.6180339887) % 1 * 3)]      # golden-ratio walk: no two rows alike
        k += 1
        stalls.append((rid, trade, x, z, ry, row))

# Lantern poles in the gaps between stalls, on each row's front line, and the
# strings between facing poles: across the avenue (E1a <-> W1a) and across
# each aisle (E1b <-> E3, W1b <-> W3).
poles, lines = [], []


def pole_line(row_a, t_a, row_b, t_b, pairs, tag):
    # Each pole stands in a gap between two stalls (or where its row breaks),
    # so a string may cross at a slant when the two rows' gaps do not line up.
    for j, (sa, sb) in enumerate(pairs):
        pa, pb = at(sa, t_a), at(sb, t_b)
        ida, idb = 'cm-pole-%s-%d' % (row_a, j + 1), 'cm-pole-%s-%d' % (row_b, j + 1)
        poles.append((ida, pa[0], pa[1]))
        poles.append((idb, pb[0], pb[1]))
        lines.append(('cm-lights-%s-%d' % (tag, j + 1), ida, idb))


front_1a = off_1a - DEPTH_FRONT + .25      # just inside the stall's front line
pole_line('e1a', -front_1a, 'w1a', front_1a, [(-23.25, -23.25), (-17.75, -17.75), (-12.25, -12.25), (12.25, 9.75)], 'avenue')
front_1b = off_1b + DEPTH_FRONT - .25
front_3 = off_3 - DEPTH_FRONT + .25
pole_line('e1b', -front_1b, 'e3', -front_3, [(-17.75, -15.25), (-4.25, -4.25), (6.75, 6.75)], 'east')
pole_line('w1b', front_1b, 'w3', front_3, [(-17.75, -15.25), (-4.0, -4.25), (9.75, 6.75)], 'west')

print('// %d stalls, %d skipped (%s)' % (len(stalls), len(skipped), ', '.join(skipped) or 'none'))
print('const CINDER_MARKET_STALLS=[')
for rid, trade, x, z, ry, row in stalls:
    print("  {id:'%s',trade:'%s',x:%.2f,z:%.2f,ry:%.4f,purpose:'%s %s'}," % (rid, trade, x, z, ry, TRADE_WORDS[trade], ROW_WORDS[row]))
print('];')
print('const CINDER_MARKET_POLES=[')
for pid, x, z in poles:
    print("  {id:'%s',x:%.2f,z:%.2f}," % (pid, x, z))
print('];')
print('const CINDER_MARKET_LIGHTS=[')
for lid, a, b in lines:
    print("  {id:'%s',from:'%s',to:'%s'}," % (lid, a, b))
print('];')
