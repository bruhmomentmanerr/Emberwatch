// Export the city as one .glb, to open in Blender.
//
//   HARNESS_SAVE_DIR=<dir> app/node_modules/.bin/electron tools/harness \
//     app/renderer/index.html tools/probes/probe-export-city.js 25
//
// It writes through window.__harnessSave (tools/harness/preload.js) rather than
// returning the bytes, because the city is tens of megabytes and the probe's
// result travels back as JSON.
//
// What goes in: the merged static city — walls, roofs, roads, terrain, the
// landmarks, and the street kit. What stays out, and why:
//   - the sky dome, the aurora, the water and the bloom card, which are custom
//     shaders that mean nothing outside this renderer;
//   - the residents, which live in a BatchedMesh the exporter cannot read, and
//     are people rather than city anyway;
//   - lights, which do not survive the trip usefully.
(async () => {
  const E = window.EMBER, T = window.THREE, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(3500);                                                  // let the city finish building
  if (!window.__harnessSave) return { error: 'this harness cannot save files — update tools/harness/preload.js' };
  // The game ships the loader, not the exporter: nothing a probe alone needs
  // belongs in the one file the player downloads. Pull the tools-only bundle in
  // here instead (tools/three-vendor/exporter.bundle.js, built by the snippet in
  // its entry file's comment).
  if (!window.THREE_EXPORT) {
    await new Promise((resolve, reject) => {
      const tag = document.createElement('script');
      tag.src = '../../tools/three-vendor/exporter.bundle.js';
      tag.onload = resolve; tag.onerror = () => reject(new Error('could not load exporter.bundle.js'));
      document.head.appendChild(tag);
    }).catch(err => { window.__exportLoadError = String(err.message); });
  }
  const Exporter = window.THREE_EXPORT && window.THREE_EXPORT.GLTFExporter;
  if (!Exporter) return { error: window.__exportLoadError || 'no GLTFExporter available' };

  const skipMaterial = m => !m || m.isShaderMaterial || m.isRawShaderMaterial;
  const group = new T.Group();
  let meshes = 0, triangles = 0, skipped = [];
  E.scene.updateMatrixWorld(true);
  E.scene.traverse(o => {
    if (!o.isMesh) return;
    if (o.isBatchedMesh) { skipped.push('batched(' + (o.name || 'residents') + ')'); return; }
    const material = Array.isArray(o.material) ? o.material[0] : o.material;
    if (skipMaterial(material)) { skipped.push('shader(' + (o.name || o.geometry.type) + ')'); return; }
    const geometry = o.geometry;
    if (!geometry || !geometry.attributes || !geometry.attributes.position) return;
    // Bake the world matrix in: Blender wants the city where it stands.
    const copy = o.isInstancedMesh ? o.clone() : new T.Mesh(geometry, material);
    copy.applyMatrix4(o.matrixWorld);
    copy.name = o.name || ('part_' + meshes);
    group.add(copy);
    meshes++;
    const count = geometry.index ? geometry.index.count : geometry.attributes.position.count;
    triangles += Math.round(count / 3) * (o.isInstancedMesh ? o.count : 1);
  });

  const buffer = await new Promise((resolve, reject) => {
    new Exporter().parse(group, resolve, reject, { binary: true, onlyVisible: true, truncateDrawRange: true });
  }).catch(err => ({ failed: String(err && err.message || err) }));
  if (buffer && buffer.failed) return { error: 'export failed: ' + buffer.failed, meshes, triangles };

  const saved = window.__harnessSave('Vaneth-city.glb', buffer);
  return { revision: E.diagnostics().revision, seed: E.diagnostics().world.seed, meshes, triangles,
    megabytes: +(saved.bytes / 1048576).toFixed(1), file: saved.file,
    leftOut: [...new Set(skipped)].slice(0, 8) };
})()
