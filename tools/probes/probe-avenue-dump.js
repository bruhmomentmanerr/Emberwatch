// The avenues' surroundings, dumped for tools/plan-avenues.py (r146).
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html \
//     tools/probes/probe-avenue-dump.js 25 > avdump.log
//
// Prints the street plan, every recorded house front, every collider within
// 26 m of a 10 m avenue, the interior doors and the interactions, as one
// RESULT object; the planner reads that object saved as avdump.json.
// Before avenueFrontage() is live this is the city the table was planned
// against; after, the table's own houses are among the colliders, so a
// re-plan finds no room where it already built.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER; await wait(1500);
  const r2 = v => +(+v).toFixed(2);
  const av = E.kit.roads.filter(r => r.w >= 9.5);
  const near = (x, z, pad) => av.some(r => { const t = Math.max(0, Math.min(r.len, (x - r.x1) * r.ux + (z - r.z1) * r.uz));
    return Math.hypot(x - (r.x1 + r.ux * t), z - (r.z1 + r.uz * t)) < r.w / 2 + pad; });
  const cols = E.colliders.filter(c => !c.open && near(c.x, c.z, 26 + (c.r || 0))).map(c => c.box ? [r2(c.x), r2(c.z), r2(c.hw), r2(c.hd), +c.co.toFixed(5), +c.si.toFixed(5), 1] : [r2(c.x), r2(c.z), r2(c.r), 0, 0, 0, 0]);
  const doors = E.doors.map(d => [r2(d.outsideX), r2(d.outsideZ)]);
  const inter = E.interactions.map(i => [r2(i.x), r2(i.z), r2(i.r || 1.5), i.id]);
  const fronts = E.kit.fronts.map(f => [r2(f.x), r2(f.z), r2(f.w), r2(f.d), +f.ry.toFixed(5), f.stories || 1, f.accent || '']);
  const roads = E.kit.roads.map(r => [r2(r.x1), r2(r.z1), +r.ux.toFixed(5), +r.uz.toFixed(5), r2(r.len), r.w]);
  const rings = (E.kit.rings || []).map(g => [g.r, g.w]);
  return { cols, doors, inter, fronts, roads, rings };
})()
