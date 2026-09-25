// A door with no house on it. The owner saw one standing in the middle of
// nowhere (2026-09-19), and a door leaf only exists because something put an
// interior door record there — so either its building was never raised, or the
// record is somewhere its building is not.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-doors-standing-alone.js 20 [shotsDir]
//
// For every door: what stands within ten metres of it that is not a wall or the
// door's own collider, whether its room box holds any building at all, and how
// far out it is. Anything with nothing around it is reported with a shot of it.
(async () => {
  const E = window.EMBER;
  const out = { revision: E.diagnostics().revision, doors: E.doors.length, errors: [] };
  addEventListener('error', e => out.errors.push(String(e.message).slice(0, 200)));

  // Everything but the door's own collider counts as "something is there": a
  // walk-in room is built out of wall colliders, so filtering walls out left
  // every landmark looking like it stood in a field.
  const solid = E.colliders.filter(c => !c.door);
  // Distance to the thing itself, not to its centre: a landmark is a box twenty
  // metres across and its centre is nowhere near its own door.
  const gap = (c, x, z) => c.box
    ? Math.hypot(Math.max(Math.abs(c.x - x) - c.hw, 0), Math.max(Math.abs(c.z - z) - c.hd, 0))
    : Math.max(Math.hypot(c.x - x, c.z - z) - c.r, 0);
  const nearest = (x, z) => {
    let best = Infinity, which = null;
    for (const c of solid) { const d = gap(c, x, z); if (d < best) { best = d; which = c; } }
    return { metres: +best.toFixed(2), box: which ? !!which.box : null };
  };
  const within = (x, z, r) => solid.filter(c => Math.hypot(c.x - x, c.z - z) < r).length;

  const rows = E.doors.map(d => {
    const x = d.doorX ?? d.outsideX, z = d.doorZ ?? d.outsideZ;
    return {
      name: d.name, kind: d.kind || 'landmark',
      at: [Math.round(x), Math.round(z)], radius: Math.round(Math.hypot(x, z)),
      room: d.w && d.d ? [Math.round(d.w), Math.round(d.d)] : null,
      buildingsWithin10: within(x, z, 10),
      nearestBuilding: nearest(x, z),
      insideSolid: E.colliders.some(c => !c.door && !c.wall && (c.box
        ? Math.abs(c.x - (d.insideX ?? x)) < c.hw && Math.abs(c.z - (d.insideZ ?? z)) < c.hd
        : Math.hypot(c.x - (d.insideX ?? x), c.z - (d.insideZ ?? z)) < c.r))
    };
  });

  // A door is "standing alone" when nothing that could be a building is within
  // ten metres of it — the room it belongs to is 6-20 m across, so its own walls
  // should be right there.
  const alone = rows.filter(r => r.buildingsWithin10 === 0 || r.nearestBuilding.metres > 3);
  out.nearestSpread = rows.map(r => r.nearestBuilding.metres).sort((a, b) => a - b);
  out.standingAlone = alone;
  out.aloneCount = alone.length;
  out.furthestFromAnything = rows.slice().sort((a, b) => b.nearestBuilding.metres - a.nearestBuilding.metres).slice(0, 6);
  out.byKind = rows.reduce((m, r) => { m[r.kind] = (m[r.kind] || 0) + 1; return m; }, {});
  out.homesOutsideTheWall = rows.filter(r => r.kind === 'home' && r.radius > 380).map(r => ({ name: r.name, at: r.at }));

  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  out.shots = alone.slice(0, 3).map((r, i) => {
    const a = Math.atan2(r.at[1], r.at[0]);
    const sx = r.at[0] + Math.cos(a) * 9, sz = r.at[1] + Math.sin(a) * 9;
    return { name: 'lone-door-' + i, x: sx, z: sz, y: E.terrainAt ? E.terrainAt(sx, sz) : 0, yaw: face(sx, sz, r.at[0], r.at[1]), pitch: -0.05 };
  });
  return out;
})()
