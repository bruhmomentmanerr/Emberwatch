// Photograph the road ends the game dressed at build (diagnostics().world
// .roadEnds.spots): once low, 12 m back toward the middle of the city, and once
// from a raised viewpoint 30 m back, which clears the houses that line a road.
//   ... tools/harness app/renderer/index.html tools/probes/probe-look-roadends.js 40 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2000); E.setWatch('labour'); await wait(600);
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z)), shots = [];
  E.diagnostics().world.roadEnds.spots.forEach(([x, z, r], i) => {
    const cx = x - x / r * 12, cz = z - z / r * 12;
    shots.push({ name: 'end' + i + '_r' + r + '_low', x: cx, z: cz, y: 1.7, yaw: face(cx, cz, x, z), pitch: 0 });
    const hx = x - x / r * 30, hz = z - z / r * 30;
    shots.push({ name: 'end' + i + '_r' + r + '_high', x: hx, z: hz, y: 7, yaw: face(hx, hz, x, z), pitch: -0.2 });
  });
  return { shots };
})()
