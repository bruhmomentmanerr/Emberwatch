// The Cinder Market's authored table, checked in the running game (r144).
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html \
//     tools/probes/probe-cinder-market.js 20 <shotsDir>
//
// Reports what was built from EMBER.market and what was left out, whether any
// stall footprint touches a carriageway, which stalls have their keeper behind
// the counter, and takes the walk-through shots. Like probe-authored-market.js
// it reports coordinates verbatim and moves nothing.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER; await wait(2500);
  const M = E.market;
  if (!M) return { error: 'no EMBER.market' };
  const footprintOnRoad = s => {
    const co = Math.cos(s.ry), si = Math.sin(s.ry);
    return [[0, 0], [-2.35, -1.55], [2.35, -1.55], [2.35, 1.65], [-2.35, 1.65]].some(([lx, lz]) =>
      E.onRoad(s.x + lx * co + lz * si, s.z - lx * si + lz * co, 0));
  };
  const skipped = new Set(M.built.skipped);
  const stalls = M.stalls.map(s => {
    const kx = s.x - Math.sin(s.ry) * .06, kz = s.z - Math.cos(s.ry) * .06;
    const keeper = E.villagers.find(v => Math.hypot(v.g.position.x - kx, v.g.position.z - kz) < .9);
    return { id: s.id, trade: s.trade, built: !skipped.has(s.id), onRoad: footprintOnRoad(s), keeper: keeper ? keeper.name : null };
  });
  const d = E.diagnostics();
  const look = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const shot = (name, x, z, tx, tz, pitch = .02) => ({ name, x, z, yaw: look(x, z, tx, tz), pitch });
  return {
    revision: d.revision,
    built: M.built,
    stallsOnRoad: stalls.filter(s => s.onRoad).map(s => s.id),
    keepers: stalls.filter(s => s.keeper).map(s => s.id + ': ' + s.keeper),
    unattended: stalls.filter(s => s.built && !s.keeper).length,
    roadObstructions: d.city.roadObstructions,
    unreachable: d.interactions.unreachable,
    shots: [
      shot('market-from-the-south', 0, 92, 0, 125, .03),
      shot('market-avenue', -5, 76, -6, 125, .02),
      shot('market-hearth-court', -4, 100, M.hearth.x + 2, M.hearth.z + 2, .05),
      shot('market-east-aisle', 12, 84, 11, 124, .03),
      shot('market-west-aisle', -21.5, 94, -22.5, 122, .03),
      shot('market-from-the-north', -6, 134, -4, 90, .0)
    ]
  };
})()
