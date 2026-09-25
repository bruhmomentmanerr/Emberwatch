'use strict';
// Audit the city's solids for clutter that no scene-graph test can see.
//
//   node tools/trace-solids.js <out.html>        # a copy that records them
//   electron tools/harness <out.html> <dump.js>  # run it, save solids.json
//   node tools/audit-solids.js                   # floating / in-road / keyless
//
// Why it exists. aBox, aCyl and aCone MERGE into one mesh per material, so by
// the time the city is on screen there is no such thing as an individual prop
// to test: traversing the scene finds a handful of giant meshes. Tapping the
// three constructors is the only way to get a true inventory. r133 found 42
// trade signs hanging in mid-air and 33 boxes with no material this way.
//
// Two traps, both already paid for:
//   - Trace the cylinders and cones too. Leave them out and everything
//     standing on a tower drum, a barrel or a post reads as floating: the
//     count went 230 -> 53 purely by adding them.
//   - aRoof builds raw BufferGeometry and calls none of the three, so roofs
//     are absent and anything sitting on a roof apex still reads as floating.
//     That is what the last nine are; they are not defects.
const fs = require('fs');
const S = 'C:/Users/Patrick/AppData/Local/Temp/claude/D---KEEP-Emberwatch/84c6a425-253e-4e2a-a6a2-19d974ee84ca/scratchpad/plan/';
const B = JSON.parse(fs.readFileSync(S + 'boxes.json', 'utf8'));
const plan = JSON.parse(fs.readFileSync(S + 'city-plan-r132b.json', 'utf8'));

// world AABB of a box rotated about Y
const aabb = ([w, h, d, x, y, z, k, ry]) => {
  const c = Math.abs(Math.cos(ry || 0)), s = Math.abs(Math.sin(ry || 0));
  const ex = (w * c + d * s) / 2, ez = (w * s + d * c) / 2;
  return { x0: x - ex, x1: x + ex, z0: z - ez, z1: z + ez, y0: y - h / 2, y1: y + h / 2, x, z, k, w, h, d };
};
const boxes = B.map(aabb);

const onRoad = (x, z, pad = 0) => {
  for (const r of plan.roads) {
    let t = (x - r.x1) * r.ux + (z - r.z1) * r.uz; t = t < 0 ? 0 : (t > r.len ? r.len : t);
    const dx = x - (r.x1 + r.ux * t), dz = z - (r.z1 + r.uz * t);
    if (dx * dx + dz * dz < (r.w / 2 + pad) ** 2) return true;
  }
  const rad = Math.hypot(x, z);
  for (const g of plan.rings) if (Math.abs(rad - g.r) < g.w / 2 + pad) return true;
  return false;
};

// ---- 1. boxes with no material key ----
const noKey = boxes.filter(b => b.k === undefined || b.k === null);

// ---- 2. grounded, tall things standing in a carriageway ----
const inStreet = boxes.filter(b =>
  Math.hypot(b.x, b.z) < 250 && b.y0 < 0.45 && b.y1 > 0.9 &&
  (b.x1 - b.x0) < 6 && (b.z1 - b.z0) < 6 && (b.x1 - b.x0) > 0.15 && (b.z1 - b.z0) > 0.15 &&
  b.k !== 'cobble' && onRoad(b.x, b.z, 0));

// ---- 3. floating: nothing within reach below or beside it ----
const CELL = 5, grid = new Map();
boxes.forEach((b, i) => {
  for (let a = Math.floor(b.x0 / CELL); a <= Math.floor(b.x1 / CELL); a++)
    for (let c = Math.floor(b.z0 / CELL); c <= Math.floor(b.z1 / CELL); c++) {
      const kk = a + ':' + c; let arr = grid.get(kk); if (!arr) grid.set(kk, arr = []); arr.push(i);
    }
});
const PAD = 0.6, DROP = 0.5;
const floating = [];
for (let i = 0; i < boxes.length; i++) {
  const b = boxes[i];
  if (b.y0 < 1.2) continue;
  if (Math.hypot(b.x, b.z) > 250) continue;
  if (b.k === 'foliage') continue;
  if ((b.x1 - b.x0) < 0.3 && (b.z1 - b.z0) < 0.3) continue;
  let ok = false; const seen = new Set();
  for (let a = Math.floor((b.x0 - PAD) / CELL); a <= Math.floor((b.x1 + PAD) / CELL) && !ok; a++)
    for (let c = Math.floor((b.z0 - PAD) / CELL); c <= Math.floor((b.z1 + PAD) / CELL) && !ok; c++) {
      const arr = grid.get(a + ':' + c); if (!arr) continue;
      for (const j of arr) {
        if (j === i || seen.has(j)) continue; seen.add(j);
        const o = boxes[j];
        if (o.x1 < b.x0 - PAD || o.x0 > b.x1 + PAD || o.z1 < b.z0 - PAD || o.z0 > b.z1 + PAD) continue;
        if (o.y1 >= b.y0 - DROP && o.y0 <= b.y1) { ok = true; break; }
      }
    }
  if (!ok) floating.push(b);
}

const brief = a => a.slice(0, 12).map(b => ({ at: [+b.x.toFixed(1), +b.z.toFixed(1)], y: +b.y0.toFixed(2), size: [+b.w.toFixed(2), +b.h.toFixed(2), +b.d.toFixed(2)], k: b.k }));
console.log('boxes total        ', boxes.length);
console.log('no material key    ', noKey.length, JSON.stringify(brief(noKey).slice(0, 6)));
const tally = a => { const t = {}; for (const b of a) t[b.k] = (t[b.k] || 0) + 1; return t; };
const cluster = a => { const g = []; for (const b of a) { const q = g.find(q => Math.hypot(q.x - b.x, q.z - b.z) < 3); if (q) { q.n++; q.keys.add(b.k); } else g.push({ x: b.x, z: b.z, n: 1, keys: new Set([b.k]) }); } return g.map(q => ({ at: [+q.x.toFixed(1), +q.z.toFixed(1)], n: q.n, keys: [...q.keys].join('/') })); };
console.log('standing in a road ', inStreet.length, JSON.stringify(tally(inStreet)));
console.log('  clusters:'); for (const c of cluster(inStreet).slice(0, 14)) console.log('   ', JSON.stringify(c));
console.log('floating in city   ', floating.length, JSON.stringify(tally(floating)));
console.log('  detail:'); for (const b of brief(floating)) console.log('   ', JSON.stringify(b));
const sizes={}; for(const b of floating){const k=b.k+' '+b.w.toFixed(2)+'x'+b.h.toFixed(2)+'x'+b.d.toFixed(2); sizes[k]=(sizes[k]||0)+1;}
console.log('  shapes:'); for(const [k,v] of Object.entries(sizes).sort((a,b)=>b[1]-a[1]).slice(0,8)) console.log('   ',v+'x',k);
