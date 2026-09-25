// Walk into the Great Hall through its actual door and look around, the way a
// player would, rather than teleporting to a diagnostic angle.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  return { shots: [
    { name: 'entering', x: 0, z: 6, y: 1.7, yaw: Math.PI, pitch: 0 },
    { name: 'well-inside', x: 0, z: -3, y: 1.7, yaw: Math.PI, pitch: -0.05 },
  ] };
})()
