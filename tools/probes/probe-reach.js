// Can a player-sized body get from the track into the middle of each landmark?
// Flood fill on a 0.4 m grid using the real collider list and the player's
// own radius, from the track point nearest each clearing.
(async () => {
  const E = window.EMBER;
  await new Promise(r => setTimeout(r, 3000));
  const R = E.CONFIG.playerRadius;
  const near = (x, z) => E.colliders.filter(c => Math.abs(c.x - x) < 40 && Math.abs(c.z - z) < 40);
  const blockedBy = (list, x, z) => list.some(c => {
    if (c.open) return false;
    if (c.box) { const dx = x - c.x, dz = z - c.z, lx = dx * c.co - dz * c.si, lz = dx * c.si + dz * c.co;
      return Math.abs(lx) < c.hw + R && Math.abs(lz) < c.hd + R; }
    return Math.hypot(x - c.x, z - c.z) < c.r + R;
  });
  const out = {};
  for (const site of E.clearings) {
    const list = near(site.x, site.z), a = Math.atan2(site.z, site.x);
    const sx = Math.cos(a) * 440, sz = Math.sin(a) * 440, step = .4, span = 46;
    const key = (i, j) => i + ',' + j, seen = new Set([key(0, 0)]), queue = [[0, 0]];
    let reached = false, bestD = Infinity;
    while (queue.length) {
      const [i, j] = queue.shift(), x = sx + i * step, z = sz + j * step, d = Math.hypot(x - site.x, z - site.z);
      bestD = Math.min(bestD, d);
      if (d < 2.5) { reached = true; break; }
      for (const [di, dj] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const ni = i + di, nj = j + dj, nx = sx + ni * step, nz = sz + nj * step;
        if (Math.abs(ni * step) > span || Math.abs(nj * step) > span || seen.has(key(ni, nj))) continue;
        seen.add(key(ni, nj));
        if (!blockedBy(list, nx, nz)) queue.push([ni, nj]);
      }
    }
    out[site.id] = { reachedCentre: reached, closestApproach: +bestD.toFixed(1), wallColliders: list.filter(c => c.wall && Math.hypot(c.x - site.x, c.z - site.z) < 17).length };
  }
  return out;
})()
