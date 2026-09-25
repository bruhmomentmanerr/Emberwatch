// Count the wall banners (blue 0x4a72c8 and ochre 0xb8862f, 28 triangles = 84
// vertices each, in placement order) and stand 7 m out from a few to look at
// them. The arm leaves the wall along local +z, so the mesh's long axis is
// the street-facing direction; the camera goes out along it.
//   ... tools/harness app/renderer/index.html tools/probes/probe-look-banners.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2000); E.setWatch('labour'); await wait(600);
  const meshes = [];
  E.scene.traverse(o => { if (o.isMesh && o.material && o.material.color) { const c = o.material.color.getHex(); if (c === 0x4a72c8 || c === 0xb8862f) meshes.push(o); } });
  const counts = meshes.map(m => m.geometry.attributes.position.count / 84);
  const shots = [], face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const pos = meshes[0] && meshes[0].geometry.attributes.position;
  for (const n of [4, 30, 90]) {
    if (!pos || n >= counts[0]) continue;
    let x0 = 1e9, x1 = -1e9, z0 = 1e9, z1 = -1e9, y1 = -1e9;
    for (let i = n * 84; i < n * 84 + 84; i++) { const px = pos.getX(i), pz = pos.getZ(i);
      x0 = Math.min(x0, px); x1 = Math.max(x1, px); z0 = Math.min(z0, pz); z1 = Math.max(z1, pz); y1 = Math.max(y1, pos.getY(i)); }
    const cx = (x0 + x1) / 2, cz = (z0 + z1) / 2, armAlongX = (x1 - x0) > (z1 - z0);
    for (const s of [-1, 1]) {
      // stand along the street (across the arm), looking at the banner's face
      const px = armAlongX ? cx : cx + s * 7, pz = armAlongX ? cz + s * 7 : cz;
      shots.push({ name: 'b' + n + (s < 0 ? 'a' : 'b'), x: px, z: pz, y: 1.7, yaw: face(px, pz, cx, cz), pitch: 0.1 });
    }
  }
  return { meshes: meshes.length, banners: counts, shots };
})()
