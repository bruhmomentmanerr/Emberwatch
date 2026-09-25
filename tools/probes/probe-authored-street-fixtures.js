// Walk-through QA for the hand-authored public-fixture contract.
// It captures the three r134 regression sites: the gate-centre light bar, the
// north-avenue signboard, and the loose Cinder Market clutter.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html \
//     tools/probes/probe-authored-street-fixtures.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(resolve => setTimeout(resolve, ms));
  await wait(2200);
  E.setWatch('labour');
  await wait(600);
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const lamps = E.kit.lanterns.filter(lamp => !lamp.removed);
  const gateLamps = lamps.filter(lamp => String(lamp.id || '').startsWith('gate-'));
  const at = (x, z) => lamps.filter(lamp => Math.hypot(lamp.x - x, lamp.z - z) < 1.1).map(lamp => lamp.id || 'legacy');
  return {
    revision: E.diagnostics().revision,
    handAuthoredGateLamps: gateLamps.map(lamp => ({id: lamp.id, at: [+lamp.x.toFixed(1), +lamp.z.toFixed(1)]})),
    roadCentreFixtures: {
      northGate: at(0, 216), southGate: at(0, -216), eastGate: at(216, 0), westGate: at(-216, 0),
      formerNorthAvenueSign: at(0, 187), formerSouthAvenueSign: at(0, -117)
    },
    shots: [
      {name: 'north-gate-marker-cleared', x: 0, z: 191, yaw: face(0, 191, 0, 216), pitch: -.06},
      {name: 'north-avenue-sign-cleared', x: 0, z: 173, yaw: face(0, 173, 0, 187), pitch: -.03},
      {name: 'cinder-market-loose-clutter-cleared', x: 0, z: 146, yaw: face(0, 146, 0, 108), pitch: -.15}
    ]
  };
})()
