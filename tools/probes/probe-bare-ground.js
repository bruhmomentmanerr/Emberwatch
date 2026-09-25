// How much of the city is bare? Samples the buildable rings on a 5 m grid and
// reports, per radius band, the share of samples with no collider within 6 m —
// open ground with nothing on it. Roads are open ground too, so read it as a
// comparison between builds rather than as an absolute: run it before and after
// a dressing change and the difference is what the change filled.
//   ... tools/harness app/renderer/index.html tools/probes/probe-bare-ground.js 20
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(3000);
  const cs = E.colliders, sample = cs[0];
  const centre = c => ({ x: c.x !== undefined ? c.x : (c.minX + c.maxX) / 2, z: c.z !== undefined ? c.z : (c.minZ + c.maxZ) / 2,
                         r: c.r !== undefined ? c.r : Math.hypot((c.maxX - c.minX) / 2 || 0, (c.maxZ - c.minZ) / 2 || 0) });
  const pts = cs.map(centre).filter(p => Number.isFinite(p.x) && Number.isFinite(p.z));
  // grid bucket so 20k samples do not scan 8k colliders each
  const CELL = 12, grid = new Map();
  for (const p of pts) { const k = Math.floor(p.x / CELL) + ',' + Math.floor(p.z / CELL); (grid.get(k) || grid.set(k, []).get(k)).push(p); }
  const near = (x, z, R) => {
    const cx = Math.floor(x / CELL), cz = Math.floor(z / CELL), reach = Math.ceil((R + 8) / CELL);
    for (let i = -reach; i <= reach; i++) for (let j = -reach; j <= reach; j++) {
      const l = grid.get((cx + i) + ',' + (cz + j)); if (!l) continue;
      for (const p of l) if (Math.hypot(p.x - x, p.z - z) - p.r < R) return true;
    } return false;
  };
  const bands = [[70, 190], [190, 300], [300, 400]], out = {};
  for (const [a, b] of bands) {
    let n = 0, bare = 0;
    for (let x = -b; x <= b; x += 5) for (let z = -b; z <= b; z += 5) {
      const r = Math.hypot(x, z); if (r < a || r >= b) continue; n++; if (!near(x, z, 6)) bare++;
    }
    out[a + '-' + b] = { samples: n, bare: bare, bareShare: +(bare / n).toFixed(3) };
  }
  return { colliders: cs.length, sampleShape: Object.keys(sample), out };
})()
