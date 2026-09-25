// Build Vaneth's lot table by hand instead of by bullseye.
//
// Why this exists. The Blender top-down of r129 showed what a hundred
// screenshots had not: the city was a target. Perfect concentric rings,
// four dead-straight avenues meeting at the exact centre, every block a
// rectangle, every house the same footprint, and a dark empty void inside
// every block. It read as a diagram, not a place, and no amount of prop work
// was ever going to fix that because the problem was the plan.
//
// Since r125 the lots are a plain table rather than a live random walk, so the
// plan is now something that can be authored. This script writes that table:
//
//   node tools/plan-city.js <city-plan.json> <out.js>
//
// It reads the constraints the rest of the city imposes — carriageways, ring
// roads, the compiler's no-build zones, every landmark doorstep and every
// solid collider already standing — and lays buildings against them.
//
// Three things it does that the old walk did not:
//
//   1. Quarters, not quadrants. Character comes from nine hand-placed seed
//      points, and a lot takes its character from whichever seed is nearest.
//      Those seeds are deliberately not symmetric, so the north-east is a
//      different place from the south-west instead of its mirror image.
//   2. Buildings of different sizes. Each quarter has its own mix — a lane of
//      narrow artisan houses reads nothing like a street of merchant halls —
//      and every lot jitters its setback from the road and its angle by a
//      degree or two, so a frontage is a line drawn by hand, not by a ruler.
//   3. Block interiors get built on. The old plan put a ring of houses around
//      a void; this walks the inside of each block and fills it with yards,
//      back-houses and workshops turned off the street grid.
//
// Everything is validated as it is placed: against the roads, the exclusions,
// the doorsteps, every collider already in the world, and every lot already
// accepted. Nothing is trusted to "probably fit".
'use strict';
const fs = require('fs');

const [, , planPath, outPath] = process.argv;
if (!planPath || !outPath) { console.error('usage: node tools/plan-city.js <city-plan.json> <out.js>'); process.exit(2); }
const plan = JSON.parse(fs.readFileSync(planPath, 'utf8'));

// ---- the world's own numbers, copied from index.html ----------------------
const CITY_RADIUS = 240, OUTER_WALL_R = 380, BUILD_EDGE_R = OUTER_WALL_R - 10;
const MARKET_Z = 108;
const EXCLUSIONS = [
  { x: 0, z: 0, r: 67 }, { x: 0, z: MARKET_Z, r: 39 }, { x: 38, z: MARKET_Z + 6, r: 20 },
  { x: -86, z: -44, r: 18 }, { x: 96, z: 52, r: 17 }, { x: -126, z: 88, r: 18 }, { x: 138, z: -18, r: 18 },
  { x: -42, z: -220, r: 20 }, { x: 220, z: 42, r: 19 }, { x: -220, z: -42, r: 19 }, { x: 89, z: -46, r: 22 },
  { x: -158, z: -12, r: 16 }, { x: 156, z: 18, r: 16 }
];
const inBuildableRing = (x, z) => {
  const r = Math.hypot(x, z);
  return (r > 66 && r < CITY_RADIUS - 9) || (r > CITY_RADIUS + 8 && r < BUILD_EDGE_R - 6);
};

// ---- a fixed stream, so this script is reproducible ------------------------
let rngState = 0x1a2b3c4d;
const rnd = () => { let v = rngState += 0x6D2B79F5; v = Math.imul(v ^ v >>> 15, v | 1); v ^= v + Math.imul(v ^ v >>> 7, v | 61); return ((v ^ v >>> 14) >>> 0) / 4294967296; };
const range = (a, b) => a + rnd() * (b - a);
const pick = a => a[(rnd() * a.length) | 0];

// ---- the quarters. Hand-placed, deliberately uneven ------------------------
// A lot belongs to whichever of these it is nearest, so the boundaries between
// them are irregular and none of them is another's mirror image.
const QUARTERS = [
  { id: 'kilns',    x: -150, z: -95,  density: .93, sizes: [[5.4, 7.2], [6.0, 7.8]], storeys: [1, 1, 1, 2], jitter: 1.15, setback: [0.10, 0.68], palette: ['brick', 'wall2', 'brick', 'stone'], accent: 'amber' },
  { id: 'weavers',  x: 120,  z: -140, density: .90, sizes: [[6.0, 8.0], [7.0, 9.0]], storeys: [1, 2, 2, 2], jitter: .85, setback: [0.15, 0.81], palette: ['wall', 'wall2', 'brick'], accent: 'amber' },
  { id: 'highmark', x: 165,  z: 95,   density: .74, sizes: [[9.0, 12.5], [10.0, 14.0]], storeys: [2, 2, 3, 3], jitter: .45, setback: [0.60, 1.53], palette: ['stone', 'wall2', 'stone'], accent: 'arcane' },
  { id: 'lantern',  x: -95,  z: 150,  density: .88, sizes: [[6.4, 8.6], [7.2, 9.4]], storeys: [1, 2, 2, 3], jitter: .95, setback: [0.20, 0.90], palette: ['wall', 'brick', 'wall2'], accent: 'amber' },
  { id: 'shambles', x: -35,  z: -165, density: .97, sizes: [[4.8, 6.4], [5.2, 7.0]], storeys: [1, 1, 2, 2], jitter: 1.6, setback: [0.05, 0.45], palette: ['wall2', 'brick', 'wall2', 'wall'], accent: 'amber' },
  { id: 'quayside', x: 45,   z: 190,  density: .82, sizes: [[7.0, 9.5], [8.0, 11.0]], storeys: [1, 2, 2, 2], jitter: 1.05, setback: [0.25, 1.17], palette: ['wall', 'stone', 'wall2'], accent: 'amber' },
  { id: 'outerN',   x: -20,  z: 300,  density: .94, sizes: [[6.2, 8.4], [7.4, 10.2]], storeys: [1, 1, 2, 2], jitter: 1.25, setback: [0.30, 1.44], palette: ['wall2', 'wall', 'brick'], accent: 'amber' },
  { id: 'outerSE',  x: 250,  z: -190, density: .92, sizes: [[5.8, 8.0], [6.8, 9.6]], storeys: [1, 1, 1, 2], jitter: 1.45, setback: [0.25, 1.60], palette: ['brick', 'wall2', 'wall'], accent: 'amber' },
  { id: 'outerW',   x: -290, z: 40,   density: .90, sizes: [[6.0, 8.2], [7.0, 9.8]], storeys: [1, 1, 2, 2], jitter: 1.35, setback: [0.20, 1.35], palette: ['wall', 'wall2', 'stone'], accent: 'amber' },
];
const quarterAt = (x, z) => {
  let best = QUARTERS[0], bestD = Infinity;
  for (const q of QUARTERS) { const d = (q.x - x) ** 2 + (q.z - z) ** 2; if (d < bestD) { bestD = d; best = q; } }
  return best;
};

// ---- geometry --------------------------------------------------------------
const corners = (l) => {
  const co = Math.cos(l.ry), si = Math.sin(l.ry), hw = l.w / 2, hd = l.d / 2;
  // matches the game's aBox/addBoxCollider convention: local +x across the
  // frontage, local +z out of the front face
  return [[hw, hd], [-hw, hd], [-hw, -hd], [hw, -hd]]
    .map(([ax, az]) => [l.x + ax * co + az * si, l.z - ax * si + az * co]);
};
const axesOf = (l) => { const co = Math.cos(l.ry), si = Math.sin(l.ry); return [[co, -si], [si, co]]; };
// separating axis test for two rotated rectangles, with a gap allowance
function overlaps(a, b, gap) {
  const ca = corners(a), cb = corners(b);
  for (const axes of [axesOf(a), axesOf(b)]) for (const [nx, nz] of axes) {
    let aMin = Infinity, aMax = -Infinity, bMin = Infinity, bMax = -Infinity;
    for (const [x, z] of ca) { const p = x * nx + z * nz; if (p < aMin) aMin = p; if (p > aMax) aMax = p; }
    for (const [x, z] of cb) { const p = x * nx + z * nz; if (p < bMin) bMin = p; if (p > bMax) bMax = p; }
    if (aMax + gap < bMin || bMax + gap < aMin) return false;      // a gap between them on this axis
  }
  return true;
}
const segDist = (px, pz, r) => {
  let t = (px - r.x1) * r.ux + (pz - r.z1) * r.uz;
  t = t < 0 ? 0 : (t > r.len ? r.len : t);
  return Math.hypot(px - (r.x1 + r.ux * t), pz - (r.z1 + r.uz * t));
};

// ---- spatial buckets so this does not run all day --------------------------
const CELL = 14;
const key = (x, z) => ((x / CELL) | 0) + ':' + ((z / CELL) | 0);
const roadGrid = new Map(), solidGrid = new Map(), lotGrid = new Map();
const addTo = (grid, x, z, reach, item) => {
  const n = Math.ceil(reach / CELL) + 1;
  const gx = (x / CELL) | 0, gz = (z / CELL) | 0;
  for (let i = -n; i <= n; i++) for (let j = -n; j <= n; j++) {
    const k = (gx + i) + ':' + (gz + j);
    let list = grid.get(k); if (!list) grid.set(k, list = []);
    list.push(item);
  }
};
for (const r of plan.roads) {
  const steps = Math.max(1, Math.ceil(r.len / CELL));
  for (let i = 0; i <= steps; i++) {
    const t = r.len * (i / steps);
    addTo(roadGrid, r.x1 + r.ux * t, r.z1 + r.uz * t, r.w / 2 + 2, r);
  }
}
for (const c of plan.solid) addTo(solidGrid, c.x, c.z, (c.box ? Math.hypot(c.hw, c.hd) : c.r) + 2, c);
const near = (grid, x, z) => grid.get(key(x, z)) || [];

// ---- can a lot stand here? -------------------------------------------------
const ROAD_CLEAR = 0.9;                 // pavement between a wall and a carriageway
function fits(lot, gap = 0.45) {
  const reach = Math.hypot(lot.w, lot.d) / 2;
  if (!inBuildableRing(lot.x, lot.z)) return false;
  for (const e of EXCLUSIONS) if (Math.hypot(lot.x - e.x, lot.z - e.z) < e.r + reach) return false;
  // every corner and the centre must clear the carriageways
  const pts = corners(lot).concat([[lot.x, lot.z]]);
  const seen = new Set();
  for (const [px, pz] of pts) {
    for (const r of near(roadGrid, px, pz)) {
      if (seen.has(r)) continue;
      if (segDist(px, pz, r) < r.w / 2 + ROAD_CLEAR) return false;
    }
    const rad = Math.hypot(px, pz);
    for (const g of plan.rings) if (Math.abs(rad - g.r) < g.w / 2 + ROAD_CLEAR) return false;
  }
  for (const d of plan.doors) if (Math.hypot(lot.x - d.x, lot.z - d.z) < 6.8 + reach * .35) return false;
  for (const c of near(solidGrid, lot.x, lot.z)) {
    if (c.box) {
      const other = { x: c.x, z: c.z, w: c.hw * 2, d: c.hd * 2, ry: Math.atan2(c.si, c.co) };
      if (overlaps(lot, other, 0.5)) return false;
    } else if (Math.hypot(lot.x - c.x, lot.z - c.z) < c.r + reach + 0.4) return false;
  }
  for (const other of near(lotGrid, lot.x, lot.z)) if (overlaps(lot, other, gap)) return false;
  return true;
}
const accept = (lot) => { lots.push(lot); addTo(lotGrid, lot.x, lot.z, Math.hypot(lot.w, lot.d) / 2 + 1, lot); };
const lots = [];

// ---- pass zero: crooked lanes ---------------------------------------------
// Buildings alone cannot fix a bullseye. The authored grid is four straight
// avenues, a lattice at 0/+-42/+-124/+-210 and a set of concentric rings, and
// every block it makes is a rectangle — which is what the Blender top-down of
// r129 showed so plainly. So before any house goes up, cut lanes through those
// blocks: narrow, wandering, turning a few degrees at every step, some running
// through to another street and some ending in a dead court. They are what
// turns a lattice into an old town, and they give the frontage pass something
// irregular to build against.
const lanes = [];
const laneSegs = [];
function laneClear(x, z, w) {
  if (!inBuildableRing(x, z)) return false;
  for (const e of EXCLUSIONS) if (Math.hypot(x - e.x, z - e.z) < e.r + w) return false;
  for (const c of near(solidGrid, x, z)) {
    const reach = (c.box ? Math.hypot(c.hw, c.hd) : c.r) + w * .5 + .8;
    if (Math.hypot(x - c.x, z - c.z) < reach) return false;
  }
  for (const d of plan.doors) if (Math.hypot(x - d.x, z - d.z) < 7) return false;
  return true;
}
// how close is an existing carriageway? used both to start a lane on one and
// to stop a lane running uselessly alongside one
function roadNear(x, z) {
  let best = Infinity;
  for (const r of near(roadGrid, x, z)) best = Math.min(best, segDist(x, z, r) - r.w / 2);
  const rad = Math.hypot(x, z);
  for (const g of plan.rings) best = Math.min(best, Math.abs(rad - g.r) - g.w / 2);
  return best;
}
// Lanes are laid per city block, not sprayed at random. A random walk from a
// random doorway makes noise; an alley in a real town serves the block it cuts
// through, so each block is handed a pattern and lays it with its own angle.
//
// The authored lattice runs at 0/+-42/+-124/+-210 on both axes, which is where
// the 36 inner blocks come from. Each takes one of four patterns by a hash of
// its own corner, so neighbouring blocks differ and opposite quadrants do not
// mirror each other:
//
//   spine  a lane in from one edge, crooked, out the far side, with a spur
//   court  a short lane opening into a dead-end yard in the middle
//   fork   a lane that splits and reaches two different edges
//   solid  no lane at all — not every block should be cut, and the ones that
//          are not are what make the ones that are read as alleys
//
// Outside the mid wall the structure is rings rather than a lattice, so those
// get radial connectors between the ring roads at uneven angles instead.
const LINES = [-210, -124, -42, 0, 42, 124, 210];
let laneRuns = 0;
// A deterministic per-block hash, so a block's character does not move if the
// generator is run again.
const blockHash = (a, b) => {
  let h = (a * 73856093) ^ (b * 19349663);
  h = Math.imul(h ^ (h >>> 13), 0x85ebca6b);
  return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
};
function layLane(path, w) {
  if (path.length < 2) return false;
  // Truncate at the first blocked step rather than throwing the lane away. A
  // single bad waypoint used to cost the whole alley, which left 15 lanes in a
  // city of 36 blocks; a lane that runs until it meets a wall and stops there
  // is a real thing in an old town anyway.
  let cut = 0;
  while (cut < path.length && laneClear(path[cut][0], path[cut][1], w)) cut++;
  path = path.slice(0, cut);
  if (path.length < 2) return false;
  for (let i = 0; i + 1 < path.length; i++) {
    const [ax, az] = path[i], [bx, bz] = path[i + 1];
    const len = Math.hypot(bx - ax, bz - az);
    if (len < 3) continue;
    laneSegs.push([+ax.toFixed(2), +az.toFixed(2), +bx.toFixed(2), +bz.toFixed(2), +w.toFixed(2)]);
    const seg = { x1: ax, z1: az, len, w, ux: (bx - ax) / len, uz: (bz - az) / len };
    plan.roads.push(seg);
    const steps = Math.max(1, Math.ceil(len / CELL));
    for (let k = 0; k <= steps; k++)
      addTo(roadGrid, ax + seg.ux * (len * k / steps), az + seg.uz * (len * k / steps), w / 2 + 2, seg);
  }
  laneRuns++;
  return true;
}
// crooked walk from a point towards a target, wandering a little each step
function crooked(fromX, fromZ, toX, toZ, wobble) {
  const path = [[fromX, fromZ]];
  const span = Math.hypot(toX - fromX, toZ - fromZ);
  const steps = Math.max(2, Math.round(span / range(11, 17)));
  for (let i = 1; i <= steps; i++) {
    const t = i / steps;
    const side = Math.sin(t * Math.PI) * wobble * (rnd() - .5) * 2;
    const nx = fromX + (toX - fromX) * t, nz = fromZ + (toZ - fromZ) * t;
    const px = -(toZ - fromZ) / span, pz = (toX - fromX) / span;   // perpendicular
    path.push([nx + px * side, nz + pz * side]);
  }
  return path;
}
for (let a = 0; a + 1 < LINES.length; a++) {
  for (let b = 0; b + 1 < LINES.length; b++) {
    const x0 = LINES[a], x1 = LINES[a + 1], z0 = LINES[b], z1 = LINES[b + 1];
    const cx = (x0 + x1) / 2, cz = (z0 + z1) / 2;
    // A block whose centre falls in the citadel precinct or past the
    // build edge can still have buildable ground in one of its corners.
    if (![[cx,cz],[x0+8,z0+8],[x1-8,z0+8],[x0+8,z1-8],[x1-8,z1-8]].some(([px,pz])=>inBuildableRing(px,pz))) continue;
    const cuts = 2 + ((blockHash(a + 31, b + 17) * 2.4) | 0);   // two or three cuts a block
    for (let pass = 0; pass < cuts; pass++) {
    const roll = (blockHash(a, b) + pass * 0.37) % 1;
    const w = range(2.8, 4.0);
    const inset = 6;                              // start clear of the bounding street
    const wobble = range(3, 9);
    if (roll < .30) {
      // spine: in one side, out the other, plus a spur that stops dead
      const vertical = blockHash(a + 7, b + 3) < .5;
      const path = vertical
        ? crooked(range(x0 + inset, x1 - inset), z0 + inset, range(x0 + inset, x1 - inset), z1 - inset, wobble)
        : crooked(x0 + inset, range(z0 + inset, z1 - inset), x1 - inset, range(z0 + inset, z1 - inset), wobble);
      if (layLane(path, w)) {
        const at = path[1 + ((rnd() * (path.length - 2)) | 0)];
        const spurA = range(0, Math.PI * 2), spurLen = range(9, 16);
        layLane([at, [at[0] + Math.sin(spurA) * spurLen, at[1] + Math.cos(spurA) * spurLen]], range(2.4, 3.2));
      }
    } else if (roll < .55) {
      // court: a stub in from one edge that opens into a dead-end yard
      const side = (rnd() * 4) | 0;
      const from = side === 0 ? [range(x0 + inset, x1 - inset), z0 + inset]
                 : side === 1 ? [range(x0 + inset, x1 - inset), z1 - inset]
                 : side === 2 ? [x0 + inset, range(z0 + inset, z1 - inset)]
                              : [x1 - inset, range(z0 + inset, z1 - inset)];
      const to = [cx + range(-7, 7), cz + range(-7, 7)];
      layLane(crooked(from[0], from[1], to[0], to[1], wobble * .6), w);
    } else if (roll < .78) {
      // fork: one way in, two ways out
      const from = [x0 + inset, range(z0 + inset, z1 - inset)];
      const mid = [cx + range(-6, 6), cz + range(-6, 6)];
      if (layLane(crooked(from[0], from[1], mid[0], mid[1], wobble * .7), w)) {
        layLane(crooked(mid[0], mid[1], x1 - inset, range(z0 + inset, z1 - inset), wobble * .7), range(2.4, 3.4));
        layLane(crooked(mid[0], mid[1], range(x0 + inset, x1 - inset), z1 - inset, wobble * .7), range(2.4, 3.4));
      }
    }
    // the rest stay solid on purpose
    }
  }
}
// Outside the mid wall: radial cut-throughs between the ring roads, spaced
// unevenly so the outer wards stop reading as tree rings.
const outerRings = plan.rings.filter(g => g.r > CITY_RADIUS && g.r < BUILD_EDGE_R).sort((p, q) => p.r - q.r);
for (let i = 0; i + 1 < outerRings.length; i++) {
  const inner = outerRings[i].r, outer = outerRings[i + 1].r;
  if (outer - inner < 14) continue;
  let ang = rnd() * Math.PI * 2;
  while (ang < Math.PI * 2) {
    const a0 = ang + range(-.05, .05);
    const from = [Math.cos(a0) * (inner + 5.5), Math.sin(a0) * (inner + 5.5)];
    const a1 = a0 + range(-.06, .06);
    const to = [Math.cos(a1) * (outer - 5.5), Math.sin(a1) * (outer - 5.5)];
    layLane(crooked(from[0], from[1], to[0], to[1], range(2, 5)), range(2.6, 3.8));
    ang += range(.16, .42);                       // uneven spacing is the whole point
  }
}
console.log('PLAN lanes=' + laneRuns + ' segments=' + laneSegs.length);


// ---- pass one: street frontages -------------------------------------------
// Walk both sides of every street. Width, depth, setback and angle all come
// from the quarter the lot lands in, and each is jittered, so a terrace is a
// row of different houses rather than one house repeated.
let frontages = 0;
const streets = plan.roads.filter(r => r.len >= 22 && Math.hypot(r.x1 + r.ux * r.len / 2, r.z1 + r.uz * r.len / 2) <= BUILD_EDGE_R + 4);
// long streets first: the arterials get their pick of the ground
streets.sort((a, b) => b.len - a.len);
for (const road of streets) {
  for (const side of [-1, 1]) {
    const nx = -road.uz * side, nz = road.ux * side;
    const ry = Math.atan2(-nx, -nz);
    let t = range(2.5, 6.0);
    while (t < road.len - 4) {
      const mid = [road.x1 + road.ux * t, road.z1 + road.uz * t];
      const q = quarterAt(mid[0] + nx * 8, mid[1] + nz * 8);
      const [loW, hiW] = pick(q.sizes);
      // Depth is its own thing, not a function of width, and stays shallow:
      // these blocks are narrow, and a deep house set back from one street
      // puts its back corners into the street behind it.
      const w = range(loW, hiW), d = range(5.6, 8.0);
      const setback = range(q.setback[0], q.setback[1]);
      const off = road.w / 2 + 2.3 + setback + d / 2;
      const px = road.x1 + road.ux * (t + w / 2) + nx * off;
      const pz = road.z1 + road.uz * (t + w / 2) + nz * off;
      const lot = {
        x: px, z: pz, w, d,
        ry: ry + (rnd() - .5) * 0.035 * q.jitter,
        stories: pick(q.storeys), key: pick(q.palette),
        accent: rnd() < .12 ? 'arcane' : q.accent,
        quarter: q.id,
      };
      if (rnd() < q.density && fits(lot)) {
        accept(lot); frontages++;
        t += w + range(0.25, 1.1) * q.jitter;       // sometimes shoulder to shoulder, sometimes a gap
      } else {
        t += range(1.1, 2.6);            // try again soon: a refusal is usually one bad spot, not a bad street
      }
    }
  }
}
console.log('PLAN frontages=' + frontages);

// ---- pass two: the insides of the blocks -----------------------------------
// The old plan left these empty. Walk a coarse lattice over the whole build
// area and drop back-houses, workshops and stores wherever there is room that
// is not a street frontage — turned off the grid, because nothing behind a
// street ever lines up with it.
let interiors = 0;
for (let gx = -BUILD_EDGE_R; gx <= BUILD_EDGE_R; gx += 6) {
  for (let gz = -BUILD_EDGE_R; gz <= BUILD_EDGE_R; gz += 6) {
    const x = gx + range(-2.6, 2.6), z = gz + range(-2.6, 2.6);
    if (!inBuildableRing(x, z)) continue;
    const q = quarterAt(x, z);
    if (rnd() > q.density * (Math.hypot(x, z) > CITY_RADIUS ? 0.95 : 0.5)) continue;
    const small = rnd();
    const w = small < .45 ? range(3.0, 4.6) : small < .8 ? range(4.6, 6.4) : range(6.4, 8.6);
    const d = w * range(0.72, 1.25);
    const lot = {
      x, z, w, d,
      ry: rnd() * Math.PI * 2,                       // free of the street grid entirely
      stories: rnd() < .78 ? 1 : 2,
      key: pick(q.palette),
      accent: q.accent,
      quarter: q.id, yard: true,
    };
    if (fits(lot, 1.5)) { accept(lot); interiors++; }
  }
}
console.log('PLAN interiors=' + interiors);

// ---- shops and trades ------------------------------------------------------
// A shop wants a street, so only frontage lots are eligible, and the wider the
// street the more likely it is to carry trade.
let shops = 0, trades = 0;
for (const lot of lots) {
  if (lot.yard) { lot.shopLot = 0; lot.trade = 0; continue; }
  const r = Math.hypot(lot.x, lot.z);
  // Walk-in rooms are a big part of what the city is for, and the first cut
  // of this plan halved them: 106 doors against 173. Trade sits thickest in
  // the middle and thins outward, but every ward keeps a real share of it.
  // r132 gave the city far more street to build on — 1,253 frontages where
  // r131 had 459 — so the same percentages would have put a shop on every
  // other door. Scaled to land near the 108 walk-in shops r131 settled on.
  const odds = r < 150 ? .17 : r < 240 ? .14 : .10;
  lot.shopLot = rnd() < odds ? 1 : 0;
  lot.trade = (!lot.shopLot && r > CITY_RADIUS && rnd() < .16) ? 1 : 0;
  shops += lot.shopLot; trades += lot.trade;
}
console.log('PLAN shopLots=' + shops + ' trades=' + trades);

// ---- emit ------------------------------------------------------------------
const rows = lots.map(l => '[' + [
  +l.x.toFixed(4), +l.z.toFixed(4), +l.w.toFixed(4), +l.d.toFixed(4), +l.ry.toFixed(5),
  l.stories, JSON.stringify(l.key), JSON.stringify(l.accent), l.shopLot, l.trade
].join(',') + ']');
// The vacant list feeds the lot-yard dresser; the interior pass has taken that
// ground now, so it stays empty rather than fighting it.
const out = 'const CITY_LOTS_BUILT=[' + rows.join(',') + '];\nconst CITY_LOTS_VACANT=[];\n';
fs.writeFileSync(outPath, out);
// The lanes go in their own file: they have to be laid with the rest of the
// street plan, long before the lots are placed against them.
const lanesOut = 'const CITY_LANES=[' + laneSegs.map(s => '[' + s.join(',') + ']').join(',') + '];\n';
fs.writeFileSync(outPath.replace(/\.js$/, '-lanes.js'), lanesOut);
console.log('PLAN total=' + lots.length + ' bytes=' + out.length + ' -> ' + outPath);
console.log('PLAN lanes bytes=' + lanesOut.length + ' -> ' + outPath.replace(/\.js$/, '-lanes.js'));
