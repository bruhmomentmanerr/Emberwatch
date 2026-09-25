// r107 verification: the land, what stands on it, the water, the player on a
// hillside, and the Tree Flip arrival. Every check returns counts, not opinions.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  const out = {};
  const T = E.terrainAt;
  if (!T) return { error: 'terrainAt not exposed' };

  // --- the land ---------------------------------------------------------------
  let maxH = 0, minH = 0, cityNonZero = 0;
  for (let i = 0; i < 40000; i++) {
    const x = (Math.random() - .5) * 1400, z = (Math.random() - .5) * 1400, h = T(x, z);
    maxH = Math.max(maxH, h); minH = Math.min(minH, h);
    if (Math.hypot(x, z) < 400 && Math.abs(h) > 1e-6) cityNonZero++;
  }
  out.land = { maxHeight: +maxH.toFixed(2), minHeight: +minH.toFixed(2), nonZeroInsideCity: cityNonZero };

  // --- roads beyond the wall stay flat -----------------------------------------
  let roadSamples = 0, roadRaised = 0, worstRoad = 0;
  for (const r of E.roads) {
    const far = Math.max(Math.hypot(r.x1, r.z1), Math.hypot(r.x1 + r.ux * r.len, r.z1 + r.uz * r.len));
    if (far < 390) continue;
    for (let t = 0; t <= r.len; t += 1.5) for (const side of [-.5, -.25, 0, .25, .5]) {
      const x = r.x1 + r.ux * t - r.uz * r.w * side, z = r.z1 + r.uz * t + r.ux * r.w * side, h = T(x, z);
      roadSamples++; if (h > .03) { roadRaised++; worstRoad = Math.max(worstRoad, h); }
    }
  }
  for (const ring of E.rings) {
    if (ring.r < 390) continue;
    for (let i = 0; i < 2000; i++) { const a = i / 2000 * Math.PI * 2;
      for (const side of [-.5, 0, .5]) { const rr = ring.r + ring.w * side, h = T(Math.cos(a) * rr, Math.sin(a) * rr);
        roadSamples++; if (h > .03) { roadRaised++; worstRoad = Math.max(worstRoad, h); } } }
  }
  out.roadsBeyondWall = { samples: roadSamples, raisedAbove3cm: roadRaised, worst: +worstRoad.toFixed(3) };

  // --- landmark clearings stay flat (the pond basin is allowed below) -------
  out.clearings = {};
  for (const c of E.clearings) {
    let raised = 0, n = 0;
    for (let i = 0; i < 600; i++) { const a = Math.random() * 6.283, r = Math.sqrt(Math.random()) * c.r;
      const h = T(c.x + Math.cos(a) * r, c.z + Math.sin(a) * r); n++; if (h > .03) raised++; }
    out.clearings[c.id] = { samples: n, raised };
  }

  // --- trees: on the ground, and out of the landmarks and the brook -------------
  const inst = []; E.scene.traverse(o => { if (o.isInstancedMesh && o.count >= 4200) inst.push(o); });
  const trunks = inst[0], m = new THREE.Matrix4(), p = new THREE.Vector3(), q = new THREE.Quaternion(), s = new THREE.Vector3();
  let floating = 0, sunkDeep = 0, inClearing = 0, inBrook = 0;
  const nearBrook = (x, z) => { for (let i = 0; i < E.brook.length - 1; i++) { const a = E.brook[i], b = E.brook[i + 1];
      const dx = b.x - a.x, dz = b.z - a.z, l2 = dx * dx + dz * dz, t = Math.max(0, Math.min(1, ((x - a.x) * dx + (z - a.z) * dz) / l2));
      if (Math.hypot(x - (a.x + dx * t), z - (a.z + dz * t)) < a.hw + 1.5) return true; } return false; };
  for (let i = 0; i < trunks.count; i++) {
    trunks.getMatrixAt(i, m); m.decompose(p, q, s);
    const base = p.y - s.y * .5, ground = T(p.x, p.z);
    if (base > ground + .05) floating++;
    if (base < ground - .6) sunkDeep++;
    if (E.clearings.some(c => Math.hypot(p.x - c.x, p.z - c.z) < c.r)) inClearing++;
    if (nearBrook(p.x, p.z)) inBrook++;
  }
  out.trees = { count: trunks.count, floating, sunkDeep, inClearing, inBrook };

  // --- the brook ------------------------------------------------------------------
  let edgeBuried = 0, edgeSamples = 0, bedAbove = 0;
  for (let i = 0; i < E.brook.length - 1; i++) {
    const a = E.brook[i], b = E.brook[i + 1], dx = b.x - a.x, dz = b.z - a.z, l = Math.hypot(dx, dz), nx = -dz / l, nz = dx / l;
    for (let t = 0; t < 1; t += .2) {
      const x = a.x + dx * t, z = a.z + dz * t, level = a.level + (b.level - a.level) * t, hw = a.hw + (b.hw - a.hw) * t;
      if (T(x, z) > level) bedAbove++;
      for (const side of [-1, 1]) { edgeSamples++; if (T(x + nx * hw * side, z + nz * hw * side) > level + .02) edgeBuried++; }
    }
  }
  const src = E.brook[0];
  out.brook = { points: E.brook.length, sourceLevel: +src.level.toFixed(2), mouthLevel: +E.brook[E.brook.length - 1].level.toFixed(2),
    bedAboveWater: bedAbove, ribbonEdgeUnderGround: edgeBuried, edgeSamples,
    sourceInsideCollider: E.colliders.some(c => Math.hypot(c.x - src.x, c.z - src.z) < c.r) };
  out.pond = { depthAtCentre: +E.waterDepthAt(-340, 320).toFixed(2), depthAt10: +E.waterDepthAt(-330, 320).toFixed(2), depthAt16: +E.waterDepthAt(-324, 320).toFixed(2) };

  // --- the player on a hillside ---------------------------------------------------
  // Find a real slope along a bearing with no road, walk up it, and check the
  // feet stay on the surface the whole way.
  const fire = (type, code) => window.dispatchEvent(new KeyboardEvent(type, { code, bubbles: true }));
  const bearing = 22 * Math.PI / 180;          // between the east gate road and the stones
  const startR = 452;
  E.player.x = Math.cos(bearing) * startR; E.player.z = Math.sin(bearing) * startR;
  E.player.y = E.player.z * 0 + T(E.player.x, E.player.z); E.player.vy = 0; E.player.onGround = true;
  // yaw 0 looks toward -Z; forward is (-sin yaw, -cos yaw). Face straight out.
  E.look(Math.atan2(-Math.cos(bearing), -Math.sin(bearing)), 0);
  const trace = []; let worstGap = 0, airborneFrames = 0;
  fire('keydown', 'KeyW');
  for (let i = 0; i < 60; i++) {
    await wait(50);
    const g = T(E.player.x, E.player.z), gap = E.player.y - g;
    worstGap = Math.max(worstGap, Math.abs(gap));
    if (gap > .3) airborneFrames++;
    if (i % 10 === 0) trace.push([+Math.hypot(E.player.x, E.player.z).toFixed(1), +E.player.y.toFixed(2), +g.toFixed(2)]);
  }
  fire('keyup', 'KeyW');
  out.walkUphill = { startR, endR: +Math.hypot(E.player.x, E.player.z).toFixed(1), climbed: +(T(E.player.x, E.player.z)).toFixed(2),
    worstFeetGap: +worstGap.toFixed(3), framesMoreThan30cmUp: airborneFrames, trace };

  // Walk into a tree that stands on high ground: it must still stop you.
  let blockedByHighTree = null;
  const high = E.colliders.filter(c => !c.wall && !c.box && c.r < .7 && Math.hypot(c.x, c.z) > 520 && T(c.x, c.z) > 4)[0];
  if (high) {
    const g = T(high.x + 3, high.z);
    E.player.x = high.x + 3; E.player.z = high.z; E.player.y = g; E.player.vy = 0; E.player.onGround = true;
    E.look(Math.PI / 2, 0);                 // yaw pi/2 faces -X, toward the tree
    fire('keydown', 'KeyW'); await wait(1500); fire('keyup', 'KeyW');
    blockedByHighTree = { treeGround: +T(high.x, high.z).toFixed(2), stoppedAt: +(E.player.x - high.x).toFixed(2), passedThrough: E.player.x < high.x - .2 };
  }
  out.highTree = blockedByHighTree;

  // --- the world still audits ------------------------------------------------------
  const d = E.diagnostics();
  out.diagnostics = { revisionField: d.revision, layoutVersion: d.world.layoutVersion, obstructions: d.city.roadObstructions,
    blockedAnchors: d.city.blockedAnchors, roadOverlaps: d.city.roadOverlaps, wilderness: d.city.wilderness,
    colliders: d.runtime.colliders, calls: d.renderer.calls, triangles: d.renderer.triangles };

  // --- Tree Flip ---------------------------------------------------------------------
  try {
    const j = JSON.parse(localStorage.getItem('emberwatch.personal-strains.v1') || '{}');
    const jar = (j.records || []).find(r => r.name === 'Tree Flip');
    out.treeFlip = { inLedger: !!jar, form: jar && jar.form, arrivals: j.arrivals, records: (j.records || []).length };
  } catch (e) { out.treeFlip = { error: e.message }; }
  return out;
})()
