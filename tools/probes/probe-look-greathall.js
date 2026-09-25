// Stand inside the Great Hall and look toward the throne, then turn to look
// back at the middle of the room where dressInterior's generic filler runs.
//   ... tools/harness app/renderer/index.html tools/probes/probe-look-greathall.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  return { shots: [
    { name: 'throne-view', x: 0, z: -8, y: 1.7, yaw: 0, pitch: 0.02 },
    { name: 'mid-room-back', x: 0, z: 6, y: 1.7, yaw: Math.PI, pitch: 0.02 },
    { name: 'mid-room-side', x: -10, z: 0, y: 1.7, yaw: Math.PI / 2, pitch: 0.02 },
  ] };
})()
