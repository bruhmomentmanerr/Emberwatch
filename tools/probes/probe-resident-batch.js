// r113 resident batch. Draw calls at three standpoints (run on the previous build
// in the same HARNESS_PROFILE to compare), that the batch is in the scene, that
// instance matrices change frame to frame (animation reaches it), how many parts
// are visible, and that only the carried lanterns still draw themselves.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-resident-batch.js 20
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = []; addEventListener('error', e => errors.push(String(e.message)));
  await wait(3000);
  const d = E.diagnostics(), out = { revision: d.revision, batch: d.runtime.residentBatch, errors };
  const stand = async (name, x, z, yaw) => {
    E.player.x = x; E.player.z = z; E.player.vy = 0; E.player.y = 0; E.player.onGround = true; E.look(yaw, -0.02);
    await wait(1500);
    return { name, calls: E.renderer.info.render.calls, triangles: E.renderer.info.render.triangles };
  };
  out.views = [await stand('north gate', 0, 406, 0), await stand('market', 0, 108, 0), await stand('market back', 0, 108, Math.PI)];
  // A near resident's limb matrices change frame to frame (animation reaches the batch).
  // By name since r159: the city's cells are BatchedMeshes too (r153), and the
  // first one in the scene is a street cell, not the residents.
  const batch = E.scene.getObjectByName('resident-batch');
  out.batchInScene = !!batch;
  if (batch) {
    const m1 = [], m2 = [], M = new THREE.Matrix4();
    const n = Math.min(batch.instanceCount ?? 64, 64);
    for (let i = 0; i < n; i++) { batch.getMatrixAt(i, M); m1.push(M.elements.slice()); }
    await wait(600);
    let changed = 0; for (let i = 0; i < n; i++) { batch.getMatrixAt(i, M); if (M.elements.some((v, k) => Math.abs(v - m1[i][k]) > 1e-5)) changed++; }
    out.instancesChangedIn600ms = changed + '/' + n;
    let visible = 0, total = 0; for (let i = 0; i < (d.runtime.residentBatch ? d.runtime.residentBatch.instances : 0); i++) { total++; if (batch.getVisibleAt(i)) visible++; }
    out.visibleInstances = visible + '/' + total;
  }
  out.villagerMeshesOnLayer0 = (() => { let n = 0; for (const v of E.villagers) v.g && v.g.traverse(o => { if (o.isMesh && o.layers.test(E.camera.layers)) n++; }); return n; })();
  out.errors = errors;
  return out;
})()
