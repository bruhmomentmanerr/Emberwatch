// Fixed standpoints for comparing how two builds look. Same seed, same watch.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  E.setWatch('labour'); await wait(500);
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  return { revision: E.diagnostics().revision, three: THREE.REVISION, shots: [
    { name: '1-gate-out', x: 0, z: 414, yaw: Math.PI, pitch: 0.02 },
    { name: '2-market-fire', x: 0, z: 134, yaw: face(0, 134, 0, 108), pitch: -0.08 },
    { name: '3-lantern-street', x: 0, z: 192, yaw: face(0, 192, 0, 230), pitch: -0.02 },
    { name: '4-rampart-city', x: 60, z: 372, y: 14.9, yaw: face(60, 372, 0, 100), pitch: -0.22 },
    { name: '5-pond', x: -329.1, z: 309.7, yaw: face(-329.1, 309.7, -340, 320), pitch: -0.16 },
    { name: '6-hillside', x: Math.cos(1.17) * 585, z: Math.sin(1.17) * 585, yaw: face(Math.cos(1.17) * 585, Math.sin(1.17) * 585, Math.cos(1.5) * 585, Math.sin(1.5) * 585), pitch: -0.06 },
    { name: '7-stones-crystal', x: 318, z: 318, yaw: face(318, 318, 330, 330), pitch: 0 }
  ] };
})()
