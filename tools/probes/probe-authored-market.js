// Verifies the hand-authored market dressing table.  It deliberately reports
// the requested coordinates exactly; unlike offRoad(), it must never move a
// fixture to a nearby location behind the author's back.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html \
//     tools/probes/probe-authored-market.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(resolve => setTimeout(resolve, ms));
  await wait(2200);
  const candidates = [
    ['north-west stall', -20, 126, Math.PI], ['north-east stall', 20, 126, Math.PI],
    ['north-west alternate', -20, 116, Math.PI], ['north-east alternate', 20, 118, Math.PI],
    ['south-west stall', -20, 90, 0], ['south-east stall', 20, 90, 0],
    ['south-west alternate', -20, 98, 0], ['south-east alternate', 20, 98, 0],
    ['west stall', -28, 108, Math.PI / 2], ['east stall', 28, 108, -Math.PI / 2],
    ['west north stall', -25, 120, Math.PI / 2], ['east north stall', 25, 120, -Math.PI / 2],
    ['fire ring', 0, 108, 0]
  ];
  const footprintOnRoad = (x, z, w, d, ry) => {
    const co = Math.cos(ry), si = Math.sin(ry);
    for (const [lx, lz] of [[0, 0], [-w / 2, -d / 2], [w / 2, -d / 2], [-w / 2, d / 2], [w / 2, d / 2]]) {
      const px = x + lx * co + lz * si, pz = z - lx * si + lz * co;
      if (E.onRoad(px, pz, .25)) return true;
    }
    return false;
  };
  const checks = candidates.map(([name, x, z, ry]) => ({
    name, at: [x, z], roadAtCentre: E.onRoad(x, z, .25),
    stallFootprintTouchesRoad: footprintOnRoad(x, z, 3.7, 2.55, ry),
    blocked: E.colliders.some(c => Math.hypot(c.x - x, c.z - z) < (c.r || Math.hypot(c.hw || 0, c.hd || 0)) + 1.1)
  }));
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  return {
    revision: E.diagnostics().revision,
    checks,
    shots: [
      {name: 'market-authored-overview', x: 0, z: 146, yaw: face(0, 146, 0, 108), pitch: -.15},
      {name: 'market-authored-west', x: -42, z: 108, yaw: face(-42, 108, 0, 108), pitch: -.08},
      {name: 'market-authored-east', x: 42, z: 108, yaw: face(42, 108, 0, 108), pitch: -.08}
    ]
  };
})()
