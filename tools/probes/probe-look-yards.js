// Stand in the street in front of the dressed lot yards (diagnostics().world
// .lotYards.spots) and look at them: one of each kind where there is one.
// The lot's front is local +z, (sin ry, cos ry), so the camera goes 9 m out
// along it and looks back at the lot.
//   ... tools/harness app/renderer/index.html tools/probes/probe-look-yards.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2000); E.setWatch('labour'); await wait(600);
  const y = E.diagnostics().world.lotYards, seen = {}, shots = [];
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  for (const s of y.spots) {
    if (seen[s.kind] >= 2) continue; seen[s.kind] = (seen[s.kind] || 0) + 1;
    const px = s.x + Math.sin(s.ry) * 9, pz = s.z + Math.cos(s.ry) * 9;
    shots.push({ name: s.kind + seen[s.kind], x: px, z: pz, y: 1.7, yaw: face(px, pz, s.x, s.z), pitch: -0.02 });
  }
  return { dressed: y.dressed, kinds: seen, shots };
})()
