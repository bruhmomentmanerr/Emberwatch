// Things a walker notices that no audit used to count: street lanterns standing
// side by side, a lantern planted in front of somebody's door, and roads that
// stop dead. Reads EMBER.kit (fronts, lanterns, roads, rings) and the collider
// list; nothing is placed or moved.
//
//   ... tools/harness app/renderer/index.html tools/probes/probe-street-logic.js 20
//
// A dead end here is a road end with no other road, ring or plaza within 3 m of
// it. `ahead` says what stands 4 m past it: a wall or building (a road that runs
// into something), or open ground (a road that just stops).
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(3500);
  const K = E.kit, out = {};
  const live = K.lanterns.filter(l => !l.removed);
  // 1. lanterns side by side
  const pairs = [];
  for (let i = 0; i < live.length; i++) for (let j = i + 1; j < live.length; j++) {
    const d = Math.hypot(live[i].x - live[j].x, live[i].z - live[j].z);
    if (d < 6) pairs.push({ d: +d.toFixed(1), a: [+live[i].x.toFixed(0), +live[i].z.toFixed(0)] });
  }
  out.lanterns = { total: live.length, closerThan6m: pairs.length, closerThan4m: pairs.filter(p => p.d < 4).length, sample: pairs.slice(0, 6) };
  // 2. lanterns in front of a door
  const doors = K.fronts.map(f => ({ x: f.x + Math.sin(f.ry) * (f.d * .5 + .05), z: f.z + Math.cos(f.ry) * (f.d * .5 + .05), n: 'house' }))
    .concat((E.doors || []).map(d => ({ x: d.outsideX, z: d.outsideZ, n: d.name })));
  const atDoor = [];
  for (const l of live) for (const d of doors) { const dd = Math.hypot(l.x - d.x, l.z - d.z); if (dd < 1.9) { atDoor.push({ lantern: [+l.x.toFixed(0), +l.z.toFixed(0)], door: d.n, d: +dd.toFixed(1) }); break; } }
  out.lanternInFrontOfDoor = { count: atDoor.length, sample: atDoor.slice(0, 6) };
  // 3. roads that stop
  const segDist = (px, pz, r) => { const dx = px - r.x1, dz = pz - r.z1, t = Math.max(0, Math.min(r.len, dx * r.ux + dz * r.uz));
    return Math.hypot(px - (r.x1 + r.ux * t), pz - (r.z1 + r.uz * t)) - r.w / 2; };
  const ringDist = (px, pz, g) => Math.abs(Math.hypot(px, pz) - g.r) - g.w / 2;
  const cs = E.colliders;
  const blockedAt = (x, z) => cs.some(c => Math.hypot(c.x - x, c.z - z) < (c.r || 0) + 1);
  const ends = [];
  K.roads.forEach((r, i) => {
    if (r.len < 12) return;
    for (const end of [0, 1]) {
      const px = end ? r.x1 + r.ux * r.len : r.x1, pz = end ? r.z1 + r.uz * r.len : r.z1, sgn = end ? 1 : -1;
      const joined = K.roads.some((o, j) => j !== i && segDist(px, pz, o) < 3) || K.rings.some(g => ringDist(px, pz, g) < 3);
      if (joined) continue;
      // A road is laid in pieces and stops short of a building or a wall, then
      // carries on beyond it. That is a broken road, not a dead one: look ahead
      // along the same line for anything paved before calling it a dead end.
      let resumes = false;
      for (let ahead = 4; ahead <= 30 && !resumes; ahead += 2) {
        const qx = px + r.ux * sgn * ahead, qz = pz + r.uz * sgn * ahead;
        resumes = K.roads.some((o, j) => j !== i && segDist(qx, qz, o) < 1.5) || K.rings.some(g => ringDist(qx, qz, g) < 1.5);
      }
      if (resumes) continue;
      const ax = px + r.ux * sgn * 4, az = pz + r.uz * sgn * 4;
      ends.push({ at: [+px.toFixed(0), +pz.toFixed(0)], len: +r.len.toFixed(0), w: r.w, radius: +Math.hypot(px, pz).toFixed(0), ahead: blockedAt(ax, az) ? 'blocked' : 'open' });
    }
  });
  out.roadEnds = { roads: K.roads.length, deadEnds: ends.length, intoSomething: ends.filter(e => e.ahead === 'blocked').length,
    justStop: ends.filter(e => e.ahead === 'open').length, sample: ends.slice(0, 12) };
  return out;
})()
