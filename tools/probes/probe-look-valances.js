// Stand in front of shop awnings and look at their fringe. The valances are one
// merged mesh (teal, 0x3f7f86); each is 76 triangles = 228 vertices in order, so
// the Nth valance is verts 228N..228N+227. Camera goes 6 m out either side of
// the awning's long axis and looks at it; the shot on the street side has sky.
//   ... tools/harness app/renderer/index.html tools/probes/probe-look-valances.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2000); E.setWatch('labour'); await wait(600);
  let mesh = null;
  E.scene.traverse(o => { if (o.isMesh && o.material && o.material.color && o.material.color.getHex() === 0x3f7f86) mesh = o; });
  if (!mesh) return { error: 'no valance mesh' };
  const pos = mesh.geometry.attributes.position, shots = [];
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  for (const n of [3, 20, 55]) {
    let x0 = 1e9, x1 = -1e9, z0 = 1e9, z1 = -1e9, y = 0;
    for (let i = n * 228; i < n * 228 + 228; i++) { const px = pos.getX(i), pz = pos.getZ(i);
      x0 = Math.min(x0, px); x1 = Math.max(x1, px); z0 = Math.min(z0, pz); z1 = Math.max(z1, pz); y = pos.getY(i); }
    const cx = (x0 + x1) / 2, cz = (z0 + z1) / 2, alongX = (x1 - x0) > (z1 - z0);
    for (const s of [-1, 1]) {
      const px = alongX ? cx : cx + s * 6, pz = alongX ? cz + s * 6 : cz;
      shots.push({ name: 'v' + n + (s < 0 ? 'a' : 'b'), x: px, z: pz, yaw: face(px, pz, cx, cz), pitch: 0.06 });
    }
  }
  return { valances: pos.count / 228, shots };
})()
