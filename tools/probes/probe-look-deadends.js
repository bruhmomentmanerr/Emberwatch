// Stand 14 m back along each true dead-end road and look at its end. Uses the
// same definition as probe-street-logic (no road within 3 m of the end and none
// resumes within 30 m ahead).
//   ... tools/harness app/renderer/index.html tools/probes/probe-look-deadends.js 40 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2000); E.setWatch('labour'); await wait(600);
  const K = E.kit, shots = [], list = [];
  const segDist = (px, pz, r) => { const dx = px - r.x1, dz = pz - r.z1, t = Math.max(0, Math.min(r.len, dx * r.ux + dz * r.uz));
    return Math.hypot(px - (r.x1 + r.ux * t), pz - (r.z1 + r.uz * t)) - r.w / 2; };
  const ringDist = (px, pz, g) => Math.abs(Math.hypot(px, pz) - g.r) - g.w / 2;
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  K.roads.forEach((r, i) => { if (r.len < 12) return;
    for (const end of [0, 1]) {
      const sgn = end ? 1 : -1, px = end ? r.x1 + r.ux * r.len : r.x1, pz = end ? r.z1 + r.uz * r.len : r.z1;
      if (K.roads.some((o, j) => j !== i && segDist(px, pz, o) < 3) || K.rings.some(g => ringDist(px, pz, g) < 3)) continue;
      let resumes = false;
      for (let a = 4; a <= 30 && !resumes; a += 2) { const qx = px + r.ux * sgn * a, qz = pz + r.uz * sgn * a;
        resumes = K.roads.some((o, j) => j !== i && segDist(qx, qz, o) < 1.5) || K.rings.some(g => ringDist(qx, qz, g) < 1.5); }
      if (resumes) continue;
      const cx = px - r.ux * sgn * 14, cz = pz - r.uz * sgn * 14;
      list.push({ end: [Math.round(px), Math.round(pz)], radius: Math.round(Math.hypot(px, pz)) });
      shots.push({ name: 'end' + list.length + '_r' + Math.round(Math.hypot(px, pz)), x: cx, z: cz, y: 1.7, yaw: face(cx, cz, px, pz), pitch: 0 });
    } });
  return { ends: list, shots };
})()
