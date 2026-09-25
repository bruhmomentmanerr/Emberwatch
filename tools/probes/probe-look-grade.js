// Apply one named colour-grade setting, then hand back the standard three
// standpoints so the harness photographs the city under it. One look per run —
// the harness takes its shots after the probe returns, so a single run cannot
// show two looks. Pick the look with HARNESS_LOOK:
//
//   HARNESS_LOOK=hollow ... tools/harness app/renderer/index.html \
//     tools/probes/probe-look-grade.js 60 <shotsDir>
//
// The settings are aimed at the owner's reference clips in
// tools/video-frames/reference: deep teal shadow, desaturated stone, heavy
// depth fog, a strong vignette, and the warm lamps left to carry the colour.
const LOOKS = {
  current: { contrast: 1.06, saturation: 1.10, vignette: .09, shadowTeal: 0x0b3040, fog: .0054, exposure: 1.12 },
  dusk:    { contrast: 1.14, saturation: .94, vignette: .22, shadowTeal: 0x0c3448, fog: .0072, exposure: 1.05 },
  hollow:  { contrast: 1.20, saturation: .86, vignette: .30, shadowTeal: 0x0d3a52, fog: .0092, exposure: 1.00 },
  drowned: { contrast: 1.26, saturation: .78, vignette: .38, shadowTeal: 0x10425e, fog: .0120, exposure: .94 },
};
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 60 && !window.EMBER; i++) await wait(500);
  const E = window.EMBER;
  if (!E || !E.setLook) return { error: 'EMBER.setLook missing — file is older than r129' };
  await wait(2000);
  const name = window.__HARNESS_LOOK || 'current';
  const look = LOOKS[name];
  if (!look) return { error: 'no such look: ' + name };
  E.setWatch('ember'); await wait(600);
  const applied = E.setLook(look);
  await wait(800);
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const stands = [
    ['street', -120, 130, -40, 60, -0.02],
    ['gate', 0, 350, 0, 240, 0],
    ['market', 0, 136, 0, 108, -0.04],
    ['wilds', 470, 0, 380, 0, -0.02],
  ];
  return { look: name, applied,
    shots: stands.map(([where, x, z, tx, tz, pitch]) =>
      ({ name: where + '-' + name, x, z, y: 1.7, yaw: face(x, z, tx, tz), pitch })) };
})()
