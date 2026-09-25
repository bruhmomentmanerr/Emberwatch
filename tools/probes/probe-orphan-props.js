// Something standing in a field. The owner saw "a random door standing in the
// middle of nowhere" (2026-09-19), and every interior door in the build has its
// own house within a metre — so whatever it is, it is not one of those.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-orphan-props.js 20 [shotsDir]
//
// Walks the whole scene for door-shaped meshes — tall, upright, thin, about a
// person wide — and for every live mesh that stands more than 12 m from any
// collider, and reports where they are with shots of the worst offenders.
(async () => {
  const E = window.EMBER, T = window.THREE;
  const out = { revision: E.diagnostics().revision, errors: [] };
  addEventListener('error', e => out.errors.push(String(e.message).slice(0, 200)));

  const gap = (c, x, z) => c.box
    ? Math.hypot(Math.max(Math.abs(c.x - x) - c.hw, 0), Math.max(Math.abs(c.z - z) - c.hd, 0))
    : Math.max(Math.hypot(c.x - x, c.z - z) - c.r, 0);
  const nearestCollider = (x, z) => { let best = Infinity; for (const c of E.colliders) { const d = gap(c, x, z); if (d < best) best = d; } return +best.toFixed(1); };

  const box = new T.Box3(), size = new T.Vector3(), centre = new T.Vector3();
  const doorish = [], adrift = [];
  E.scene.updateMatrixWorld(true);
  E.scene.traverse(o => {
    if (!o.isMesh || o.isInstancedMesh || o.isBatchedMesh) return;
    if (!o.geometry || !o.geometry.attributes || !o.geometry.attributes.position) return;
    if (o.geometry.attributes.position.count > 400) return;            // merged city geometry, not a prop
    box.setFromObject(o);
    if (!isFinite(box.min.x)) return;
    box.getSize(size); box.getCenter(centre);
    const x = +centre.x.toFixed(1), z = +centre.z.toFixed(1);
    if (Math.hypot(x, z) < 1 && size.y > 50) return;                   // the sky, the moon
    const tall = size.y > 1.6 && size.y < 3.2, wide = size.x > .6 && size.x < 2.6, thin = Math.min(size.x, size.z) < .4;
    const away = nearestCollider(x, z);
    const row = { name: o.name || o.geometry.type, at: [x, z], radius: Math.round(Math.hypot(x, z)),
      size: [+size.x.toFixed(2), +size.y.toFixed(2), +size.z.toFixed(2)], metresFromAnything: away };
    if (tall && wide && thin) doorish.push(row);
    if (away > 12 && size.y > 1) adrift.push(row);
  });

  const sortAway = (a, b) => b.metresFromAnything - a.metresFromAnything;
  out.doorShaped = doorish.length;
  out.doorShapedAwayFromAnything = doorish.filter(r => r.metresFromAnything > 6).sort(sortAway);
  out.meshesAdrift = adrift.sort(sortAway).slice(0, 20);
  out.adriftCount = adrift.length;

  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const worst = (out.doorShapedAwayFromAnything.length ? out.doorShapedAwayFromAnything : out.meshesAdrift).slice(0, 3);
  out.shots = worst.map((r, i) => {
    const a = Math.atan2(r.at[1], r.at[0]);
    const sx = r.at[0] + Math.cos(a) * 10, sz = r.at[1] + Math.sin(a) * 10;
    return { name: 'adrift-' + i, x: sx, z: sz, y: E.terrainAt ? E.terrainAt(sx, sz) : 0, yaw: face(sx, sz, r.at[0], r.at[1]), pitch: -0.03 };
  });
  return out;
})()
