# Bake the avenues' new frontage and festoons (r146).
#
#   python3 tools/plan-avenues.py avdump.json > avenues.js
#
# avdump.json is dumped from the running game by
# tools/probes/probe-avenue-dump.js: the street plan (roads, rings), every
# recorded house front, every collider within 26 m of an avenue, the interior
# doors and the interactions.
#
# The two avenues through the centre are the city's main streets, and from
# the street they read as a wide empty road: of the houses beside them, most
# turn a side or a back to the avenue, and between them lie gaps. This walks
# both verges of every avenue segment and packs houses facing the avenue into
# the gaps, their fronts 2.6 m back from the kerb as the avenue's own fronts
# stand (measured: 2.3 to 3.7 m). It never touches a crossing, the citadel
# ring, the gates or the Cinder Market, keeps every doorway and interaction
# clear, and leaves an alley after at most four houses so no yard behind is
# walled in. It only does the arithmetic and prints a table of exact
# records; the game tests each against what stands there when it is built
# and leaves out (and logs) any that does not fit — it never moves one.
#
# Then the festoons: a string of lanterns across the avenue every 22 m or so,
# hung between two iron poles 0.75 m back from either kerb, clear of the
# crossings (which have their lamps), the market (which has its strings),
# every doorway — the new houses' too — and every interaction. A pole that
# does not fit may slide up to 3 m along the verge with its partner; a span
# that still does not fit is dropped.
import json, math, sys

data = json.load(open(sys.argv[1]))
roads = [dict(x1=r[0], z1=r[1], ux=r[2], uz=r[3], len=r[4], w=r[5]) for r in data['roads']]
rings = [dict(r=g[0], w=g[1]) for g in data['rings']]
cols = data['cols']
doors = [tuple(d) for d in data['doors']]
inter = data['inter']
fronts = data['fronts']

SET = 2.6              # front face back from the kerb
RUN = 4                # houses in a row before an alley
ALLEY = 2.8            # the alley's width
GAP = .5               # between neighbours in a row (a jetty is 3% proud of each side)
WIDTHS = [9.0, 8.2, 7.4, 6.6]
DEPTHS = [8.0, 7.2, 6.4]
CROSS_PAD = 1.5        # a house may make the corner of a crossing street
POLE_PAD = 5.0         # a festoon pole stands well clear of a crossing
MARKET = (-28.0, 84.0, 18.0, 126.0)    # the Cinder Market's stalls, poles and strings


def road_dist(x, z, r):
    t = max(0, min(r['len'], (x - r['x1']) * r['ux'] + (z - r['z1']) * r['uz']))
    return math.hypot(x - (r['x1'] + r['ux'] * t), z - (r['z1'] + r['uz'] * t)) - r['w'] / 2


def on_paving(x, z, pad):
    if any(road_dist(x, z, r) < pad for r in roads):
        return True
    rad = math.hypot(x, z)
    return any(abs(rad - g['r']) < g['w'] / 2 + pad for g in rings)


def in_collider(x, z, extra):
    for (cx, cz, a, b, co, si, box) in cols:
        dx, dz = x - cx, z - cz
        if box:
            lx, lz = dx * co - dz * si, dx * si + dz * co
            if abs(lx) < a + extra and abs(lz) < b + extra:
                return True
        elif dx * dx + dz * dz < (a + extra) ** 2:
            return True
    return False


# Every doorway: the recorded fronts' (worked out as wardHouse does) and the
# interiors'. Nothing may stand within 3 m of one, or in the 4.5 m in front.
door_zones = []
for (x, z, w, d, ry, st, acc) in fronts:
    fx, fz = math.sin(ry), math.cos(ry)
    door_zones.append((x + fx * (d * .5 + .05), z + fz * (d * .5 + .05), fx, fz))
for (x, z) in doors:
    door_zones.append((x, z, 0.0, 0.0))


def blocks_door(x, z):
    for (dx0, dz0, fx, fz) in door_zones:
        ddx, ddz = x - dx0, z - dz0
        if ddx * ddx + ddz * ddz < 9.0:
            return True
        if fx or fz:
            along = ddx * fx + ddz * fz
            across = abs(ddx * fz - ddz * fx)
            if 0 <= along <= 4.5 and across < 1.6:
                return True
    return False


def near_interaction(x, z):
    return any(math.hypot(x - ix, z - iz) < ir + 1.2 for (ix, iz, ir, _id) in inter)


def footprint_ok(cx, cz, w, d, ry, avenue):
    co, si = math.cos(ry), math.sin(ry)
    pts = []
    nx, nz = max(2, int(w / 1.0) + 1), max(2, int(d / 1.0) + 1)
    for i in range(nx):
        for j in range(nz):
            lx, lz = -w / 2 + w * i / (nx - 1), -d / 2 + d * j / (nz - 1)
            pts.append((cx + lx * co + lz * si, cz - lx * si + lz * co))
    for (x, z) in pts:
        if MARKET[0] - 1 < x < MARKET[2] + 1 and MARKET[1] - 1 < z < MARKET[3] + 1:
            return False
        # the avenue itself is 2.6 m off by construction; every other street,
        # lane and ring keeps a body's width of verge
        for r in roads:
            if r is avenue:
                if road_dist(x, z, r) < SET - .05:
                    return False
            elif road_dist(x, z, r) < .9:
                return False
        rad = math.hypot(x, z)
        if any(abs(rad - g['r']) < g['w'] / 2 + .9 for g in rings):
            return False
        if in_collider(x, z, .3) or blocks_door(x, z) or near_interaction(x, z):
            return False
    return True


def crossings(a, pad=CROSS_PAD):
    # Parameters along a where another street meets or crosses it, with the
    # half-width to keep clear either side.
    out = []
    for b in roads:
        if b is a:
            continue
        det = a['ux'] * (-b['uz']) - a['uz'] * (-b['ux'])
        if abs(det) > .2:
            dx, dz = b['x1'] - a['x1'], b['z1'] - a['z1']
            ta = (dx * (-b['uz']) - dz * (-b['ux'])) / det
            tb = (a['ux'] * dz - a['uz'] * dx) / det
            if -b['w'] <= tb <= b['len'] + b['w'] and -20 <= ta <= a['len'] + 20:
                out.append((ta, b['w'] / 2 / abs(det) + pad))
        # a street that ends on the avenue's verge without crossing it
        for (ex, ez) in [(b['x1'], b['z1']), (b['x1'] + b['ux'] * b['len'], b['z1'] + b['uz'] * b['len'])]:
            if road_dist(ex, ez, a) < 6:
                t = (ex - a['x1']) * a['ux'] + (ez - a['z1']) * a['uz']
                out.append((t, b['w'] / 2 + pad))
    return out


def storeys_hash(i):
    return (i * 2654435761 % 2 ** 32) / 2 ** 32


# The avenues: the 10 m roads whose line runs through the centre.
avenues = [r for r in roads if r['w'] >= 9.5 and abs(r['x1'] * r['uz'] - r['z1'] * r['ux']) < 20
           and min(math.hypot(r['x1'], r['z1']), math.hypot(r['x1'] + r['ux'] * r['len'], r['z1'] + r['uz'] * r['len'])) < 150]
names = {}
records, n = [], 0
for a in avenues:
    # name by compass arm and inner/outer: n1 is the inner north segment
    mx, mz = a['x1'] + a['ux'] * a['len'] / 2, a['z1'] + a['uz'] * a['len'] / 2
    arm = 'n' if mz < -abs(mx) else 's' if mz > abs(mx) else 'w' if mx < 0 else 'e'
    arm += '1' if math.hypot(mx, mz) < 120 else '2'
    blocked = crossings(a)
    nx0, nz0 = -a['uz'], a['ux']
    for side, sname in [(1, 'l'), (-1, 'r')]:
        t, row, k = 3.0, 0, 0
        while t < a['len'] - 3:
            placed = False
            for w in WIDTHS:
                lo, hi = t, t + w
                if hi > a['len'] - 3:
                    continue
                if any(lo - pad < tc < hi + pad for (tc, pad) in blocked):
                    continue
                for d in DEPTHS:
                    off = side * (a['w'] / 2 + SET + d / 2)
                    tm = (lo + hi) / 2
                    cx = a['x1'] + a['ux'] * tm + nx0 * off
                    cz = a['z1'] + a['uz'] * tm + nz0 * off
                    ry = math.atan2(-nx0 * side, -nz0 * side)       # the front faces the avenue
                    if math.hypot(cx, cz) > 222 or math.hypot(cx, cz) < 66:
                        continue
                    if footprint_ok(cx, cz, w, d, ry, a):
                        k += 1
                        rid = 'avenue-front-%s-%s-%d' % (arm, sname, k)
                        h = storeys_hash(len(records) + 17)
                        key = 'brick' if h < .22 else 'wall2' if h < .55 else 'wall'
                        accent = 'arcane' if storeys_hash(len(records) + 911) < .2 else 'amber'
                        records.append(dict(id=rid, x=round(cx, 2), z=round(cz, 2), w=w, d=d, ry=round(ry, 4), key=key, accent=accent))
                        # a placed house is a collider for the next one
                        cols.append([cx, cz, w / 2, d / 2, math.cos(ry), math.sin(ry), 1])
                        row += 1
                        t = hi + (ALLEY if row % RUN == 0 else GAP)
                        placed = True
                        break
                if placed:
                    break
            if not placed:
                t += .5
                row = 0

# ---- festoons ------------------------------------------------------------
POLE_OUT = .75          # pole centre back from the kerb
STEP = 22.0
for r in records:       # the new houses' doorways are doorways too
    fx, fz = math.sin(r['ry']), math.cos(r['ry'])
    door_zones.append((r['x'] + fx * (r['d'] * .5 + .05), r['z'] + fz * (r['d'] * .5 + .05), fx, fz))


def pole_ok(x, z, avenue):
    for r in roads:
        if r is not avenue and road_dist(x, z, r) < .6:
            return False
    rad = math.hypot(x, z)
    if any(abs(rad - g['r']) < g['w'] / 2 + .6 for g in rings):
        return False
    if MARKET[0] - 4 < x < MARKET[2] + 4 and MARKET[1] - 4 < z < MARKET[3] + 4:
        return False
    if in_collider(x, z, .35) or near_interaction(x, z):
        return False
    for (dx0, dz0, fx, fz) in door_zones:
        ddx, ddz = x - dx0, z - dz0
        if ddx * ddx + ddz * ddz < 4.0:
            return False
        if (fx or fz) and 0 <= ddx * fx + ddz * fz <= 4.5 and abs(ddx * fz - ddz * fx) < 1.4:
            return False
    return True


festoons = []
for a in avenues:
    mx, mz = a['x1'] + a['ux'] * a['len'] / 2, a['z1'] + a['uz'] * a['len'] / 2
    arm = 'n' if mz < -abs(mx) else 's' if mz > abs(mx) else 'w' if mx < 0 else 'e'
    arm += '1' if math.hypot(mx, mz) < 120 else '2'
    blocked = crossings(a, POLE_PAD)
    nx0, nz0 = -a['uz'], a['ux']
    off = a['w'] / 2 + POLE_OUT
    count = max(1, int((a['len'] - 16) // STEP) + 1)
    spacing = (a['len'] - 16) / max(1, count - 1) if count > 1 else 0
    k = 0
    for i in range(count):
        t0 = 8 + spacing * i if count > 1 else a['len'] / 2
        for shift in [0, 1, -1, 2, -2, 3, -3]:
            t = t0 + shift
            if t < 6 or t > a['len'] - 6 or any(abs(t - tc) < pad for (tc, pad) in blocked):
                continue
            cx, cz = a['x1'] + a['ux'] * t, a['z1'] + a['uz'] * t
            A = (cx + nx0 * off, cz + nz0 * off)
            B = (cx - nx0 * off, cz - nz0 * off)
            if math.hypot(*A) > 222 or math.hypot(*A) < 66 or math.hypot(*B) > 222 or math.hypot(*B) < 66:
                continue
            if pole_ok(A[0], A[1], a) and pole_ok(B[0], B[1], a):
                k += 1
                festoons.append(dict(id='avenue-festoon-%s-%d' % (arm, k), ax=A[0], az=A[1], bx=B[0], bz=B[1]))
                cols.append([A[0], A[1], .2, 0, 0, 0, 0])
                cols.append([B[0], B[1], .2, 0, 0, 0, 0])
                break

print('// %d houses and %d festoons along %d avenue segments' % (len(records), len(festoons), len(avenues)), file=sys.stderr)
print('const AVENUE_FRONTAGE=[')
for r in records:
    print("  {id:'%s',x:%.2f,z:%.2f,w:%.1f,d:%.1f,ry:%.4f,key:'%s',accent:'%s'}," % (r['id'], r['x'], r['z'], r['w'], r['d'], r['ry'], r['key'], r['accent']))
print('];')
print('const AVENUE_FESTOONS=[')
for f in festoons:
    print("  {id:'%s',a:{x:%.2f,z:%.2f},b:{x:%.2f,z:%.2f}}," % (f['id'], f['ax'], f['az'], f['bx'], f['bz']))
print('];')
