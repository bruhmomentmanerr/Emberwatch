// Look at rooftops from a low rise, close enough to see whether a dormer sits
// on its slope or floats off it. Same shot format as probe-tour.
//   ... tools/harness app/renderer/index.html tools/probes/probe-look-roofs.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2000); E.setWatch('labour'); await wait(600);
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const at = (name, x, z, tx, tz, pitch, y) => ({ name, x, z, y, yaw: face(x, z, tx, tz), pitch, });
  return { shots: [
    at('r1', 60, 372, 20, 330, -0.3, 8.5),
    at('r2', 60, 372, 100, 340, -0.3, 8.5),
    at('r3', -120, 150, -80, 100, -0.32, 9),
    at('r4', 200, 90, 160, 50, -0.3, 8.5),
    at('r5', -250, -250, -215, -215, -0.3, 8.5),
    at('r6', 250, 250, 215, 215, -0.3, 8.5),
  ] };
})()
