# Bake the lamps at the main avenues' crossings (r145).
#
#   python3 tools/plan-crossings.py roads.json > crossings.js
#
# roads.json is the live street plan, dumped from the running game:
#   { "roads": [[x1, z1, ux, uz, len, w], ...], "rings": [[r, w], ...] }
# (EMBER.kit.roads and EMBER.kit.rings; any probe can write it.)
#
# Lamps belong at turns and crossings, not along a street like fence posts
# (docs/MAP-VISUAL-CANON.md). This finds every place a street, lane or the
# citadel ring crosses — or ends on — one of the two 10 m avenues through the
# centre, and puts a lamp on two opposite corners, 1.2 m back from both
# kerbs. It only does the arithmetic and prints a table of exact positions;
# the game tests each record against what stands there and leaves out (and
# logs) any that does not fit — it never moves one.
import json, math, sys

data = json.load(open(sys.argv[1]))
roads = [dict(x1=r[0], z1=r[1], ux=r[2], uz=r[3], len=r[4], w=r[5]) for r in data['roads']]
rings = [dict(r=g[0], w=g[1]) for g in data['rings']]
MARGIN = 1.2


def on_road(x, z, pad=0.0):
    for r in roads:
        t = max(0, min(r['len'], (x - r['x1']) * r['ux'] + (z - r['z1']) * r['uz']))
        if math.hypot(x - (r['x1'] + r['ux'] * t), z - (r['z1'] + r['uz'] * t)) < r['w'] / 2 + pad:
            return True
    rad = math.hypot(x, z)
    return any(abs(rad - g['r']) < g['w'] / 2 + pad for g in rings)


def cross(a, b):
    # Intersection of two centre lines as parameters along each; None if parallel.
    det = a['ux'] * (-b['uz']) - a['uz'] * (-b['ux'])
    if abs(det) < 0.2:                     # nearly parallel: not a crossing
        return None
    dx, dz = b['x1'] - a['x1'], b['z1'] - a['z1']
    ta = (dx * (-b['uz']) - dz * (-b['ux'])) / det
    tb = (a['ux'] * dz - a['uz'] * dx) / det
    return ta, tb


def corner(p, a, sa, oa, b, sb, ob):
    # Where the line offset sa*oa across road a meets the line offset sb*ob
    # across road b.
    na = (-a['uz'], a['ux'])
    nb = (-b['uz'], b['ux'])
    pa = (p[0] + na[0] * sa * oa, p[1] + na[1] * sa * oa)
    pb = (p[0] + nb[0] * sb * ob, p[1] + nb[1] * sb * ob)
    det = a['ux'] * (-b['uz']) - a['uz'] * (-b['ux'])
    dx, dz = pb[0] - pa[0], pb[1] - pa[1]
    ta = (dx * (-b['uz']) - dz * (-b['ux'])) / det
    return (pa[0] + a['ux'] * ta, pa[1] + a['uz'] * ta)


avenues = [r for r in roads if r['w'] >= 9.5]
others = [r for r in roads if r['w'] < 9.5]
found = []
for a in avenues:
    for b in others:
        res = cross(a, b)
        if not res:
            continue
        ta, tb = res
        if not (-1 <= ta <= a['len'] + 1):
            continue
        # a crossing, or a street ending on the avenue (a T): its end within
        # the avenue's width of the centre line
        if not (-a['w'] / 2 - 1 <= tb <= b['len'] + a['w'] / 2 + 1):
            continue
        p = (a['x1'] + a['ux'] * ta, a['z1'] + a['uz'] * ta)
        found.append((p, a, b))
# the citadel ring, where each avenue arm meets it
for a in avenues:
    for g in rings:
        if g['r'] > 100:
            continue
        # solve |x1 + u t| = r
        bq = 2 * (a['x1'] * a['ux'] + a['z1'] * a['uz'])
        cq = a['x1'] ** 2 + a['z1'] ** 2 - g['r'] ** 2
        disc = bq * bq - 4 * cq
        if disc < 0:
            continue
        for sgn in (-1, 1):
            t = (-bq + sgn * math.sqrt(disc)) / 2
            if 0 <= t <= a['len']:
                p = (a['x1'] + a['ux'] * t, a['z1'] + a['uz'] * t)
                rad = math.hypot(*p)
                tang = dict(x1=p[0], z1=p[1], ux=-p[1] / rad, uz=p[0] / rad, len=1, w=g['w'])
                found.append((p, a, tang))

# One record per crossing (segments of one crooked avenue can report the same
# crossing twice), none in the market square or inside the citadel ring.
lamps, seen = [], []
for p, a, b in found:
    if any(math.hypot(p[0] - q[0], p[1] - q[1]) < 8 for q in seen):
        continue
    if math.hypot(p[0], p[1] - 108) < 38 or math.hypot(*p) < 50:
        continue
    # the inner gates already have their authored pair of lamps (±6, ±216)
    if any(math.hypot(p[0] - gx, p[1] - gz) < 14 for gx, gz in ((0, 216), (0, -216), (216, 0), (-216, 0))):
        continue
    seen.append(p)
    placed = 0
    for sa, sb in ((1, 1), (-1, -1), (1, -1), (-1, 1)):
        c = corner(p, a, sa, a['w'] / 2 + MARGIN, b, sb, b['w'] / 2 + MARGIN)
        if on_road(c[0], c[1], .5) or math.hypot(c[0], c[1] - 108) < 38:
            continue
        # the first two clear corners in this order: opposite ones if they can be
        lamps.append((len(seen), c[0], c[1], (sa, sb)))
        placed += 1
        if placed == 2:
            break

print('// %d crossings on the two main avenues, %d lamps' % (len(seen), len(lamps)))
print('const AVENUE_CROSSING_LAMPS=[')
for n, x, z, (sa, sb) in lamps:
    print("  {id:'avenue-crossing-%d-%s%s',x:%.2f,z:%.2f}," % (n, 'a' if sa > 0 else 'b', 'a' if sb > 0 else 'b', x, z))
print('];')
