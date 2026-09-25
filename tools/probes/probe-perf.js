// Frame cost and draw load at three standpoints, same camera every run so r106
// and r107 compare like for like. The harness renders in software, so the
// milliseconds are only good for comparison, not as a figure for real hardware.
(async () => {
  const E = window.EMBER, R = E.renderer;
  const wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  const frames = n => new Promise(done => {
    const times = []; let last = performance.now();
    const tick = () => { const now = performance.now(); times.push(now - last); last = now;
      if (times.length < n) requestAnimationFrame(tick); else done(times); };
    requestAnimationFrame(tick);
  });
  const stand = async (name, x, z, yaw, pitch) => {
    E.player.x = x; E.player.z = z; E.player.vy = 0;
    E.player.y = E.terrainAt ? E.terrainAt(x, z) : 0; E.player.onGround = true;
    E.look(yaw, pitch);
    await wait(1200);
    const t = await frames(60);
    t.sort((a, b) => a - b);
    return { name, calls: R.info.render.calls, triangles: R.info.render.triangles,
             medianMs: +t[30].toFixed(1), p90Ms: +t[54].toFixed(1) };
  };
  const out = [];
  out.push(await stand('north gate, looking out', 0, 406, 0, -0.02));
  out.push(await stand('track by the pond, looking at the hills', -300, 300, Math.PI * 0.78, 0.02));
  out.push(await stand('cinder market', 0, 108, 0, -0.02));
  return { revision: E.diagnostics().revision, three: THREE.REVISION, out };
})()
