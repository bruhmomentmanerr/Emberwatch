// Handcarts: how many, whether each trails its hauler, and a look at two.
//   ... tools/harness app/renderer/index.html tools/probes/probe-carts.js 40 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = []; addEventListener('error', e => errors.push(String(e.message)));
  await wait(3000); E.setWatch('labour'); await wait(600);
  const haulers = E.villagers.filter(v => v.cart);
  const gap = () => haulers.filter(v => !v.indoors).map(v => Math.hypot(v.cart.position.x - v.g.position.x, v.cart.position.z - v.g.position.z));
  const samples = [];
  for (let i = 0; i < 6; i++) { await wait(4000); const g = gap(); samples.push({ walking: g.length, min: +Math.min(...g).toFixed(2), max: +Math.max(...g).toFixed(2) }); }
  const moved = haulers.map(v => Math.hypot(v.g.position.x - v.lastX0 || 0, 0)).length;
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const shots = haulers.filter(v => !v.indoors).slice(0, 2).map((v, i) => {
    const c = v.cart.position, px = c.x + Math.cos(v.cart.rotation.y) * 5, pz = c.z - Math.sin(v.cart.rotation.y) * 5;
    return { name: 'cart' + i, x: px, z: pz, y: 1.7, yaw: face(px, pz, c.x, c.z), pitch: -0.05 };
  });
  return { errors, carts: haulers.length, drawCallsAdded: haulers.length, samples, shots };
})()
