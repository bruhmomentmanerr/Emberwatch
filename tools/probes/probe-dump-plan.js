// Dump everything a new city layout has to respect: the carriageways, the ring
// roads, the compiler's no-build zones, every landmark doorstep, and the lot
// table as it stands. Written for the r131 plan rebuild, where the lots are
// regenerated offline against these constraints and baked back in.
//
//   HARNESS_SAVE_DIR=<dir> ... tools/harness app/renderer/index.html \
//     tools/probes/probe-dump-plan.js 45
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 60 && !window.EMBER; i++) await wait(500);
  const E = window.EMBER; if (!E) return { error: 'no EMBER' };
  if (!window.__harnessSave) return { error: 'no __harnessSave' };
  await wait(2500);
  const K = E.kit;
  const doors = (E.doors || []).map(d => ({ x: +d.outsideX.toFixed(2), z: +d.outsideZ.toFixed(2), kind: d.kind }));
  // Colliders that are not buildings from the lot table: walls, landmarks,
  // compiler buildings, monuments, wilderness. A new lot has to miss these.
  const solid = E.colliders
    .filter(c => !c.door && (c.box ? Math.hypot(c.hw, c.hd) > .5 : (c.r || 0) > .5))
    .map(c => c.box
      ? { box: 1, x: +c.x.toFixed(2), z: +c.z.toFixed(2), hw: +c.hw.toFixed(2), hd: +c.hd.toFixed(2), co: +c.co.toFixed(4), si: +c.si.toFixed(4) }
      : { box: 0, x: +c.x.toFixed(2), z: +c.z.toFixed(2), r: +c.r.toFixed(2) });
  const out = {
    roads: K.roads.map(r => ({ x1: +r.x1.toFixed(2), z1: +r.z1.toFixed(2), len: +r.len.toFixed(2), w: r.w, ux: +r.ux.toFixed(5), uz: +r.uz.toFixed(5) })),
    rings: K.rings.map(g => ({ r: g.r, w: g.w })),
    doors,
    solid,
    lots: K.lots ? K.lots.length : null,
  };
  const saved = window.__harnessSave('city-plan.json', JSON.stringify(out));
  return { roads: out.roads.length, rings: out.rings.length, doors: doors.length, solid: solid.length, file: saved.file };
})()
