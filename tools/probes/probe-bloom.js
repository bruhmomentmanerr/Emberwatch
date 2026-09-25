// r112 bloom: the menu toggle, the saved setting, that the glow reaches the
// screen, and that renderer.info still counts frames rather than passes.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-bloom.js 20
//
// Leaves bloom ON in the harness's saved state, whatever it found. Earlier runs
// that turned it off persisted that through localStorage and made every later
// screenshot look bloomless — the setting is saved, as it should be.
//
// Does the glow reach the screen? Until r116 this compared the mean brightness
// of the whole frame with bloom on and off, and the r114 audit showed that is
// no evidence: the sky and the fires move more between two frames than bloom
// adds (it once read darker with bloom on). A first replacement aimed at the
// moon disc, which at the harness's render scale is three pixels across and
// blooms too little to measure. Now the probe hangs its own white card in
// front of the camera against the dark sky overhead, compares the band just
// outside the card's edges with a band of empty sky, alternating bloom on and
// off four times, and calls the glow real only if the edge gains clearly more
// than the sky does.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = []; addEventListener('error', e => errors.push(String(e.message)));
  await wait(2000);
  const btn = document.getElementById('bloomBtn'), saved = () => { try { return JSON.parse(localStorage.getItem('emberwatch.game-state.v3')).bloom; } catch { return 'unreadable'; } };
  const out = { found: E.bloom ? { ...E.bloom } : null, button: btn ? btn.textContent : null };
  if (!E.bloom.on) { btn.click(); await wait(100); }
  // Frame counter: frames, not passes.
  const f0 = E.renderer.info.render.frame, t0 = performance.now(); await wait(1000);
  out.framesPerSecondCounted = +((E.renderer.info.render.frame - f0) / ((performance.now() - t0) / 1000)).toFixed(1);

  // A white card, two metres square, ten metres in front of the camera,
  // against the dark sky overhead. It is the probe's own object, not game
  // content, so it is static, unfogged, untonemapped and certain to cross the
  // threshold; what is measured is whether the bloom pipeline puts light
  // outside its edges. It is removed afterwards.
  E.player.x = 0; E.player.z = 300; E.player.y = 0; E.player.vy = 0;
  E.look(0, 1.25);
  await wait(600);
  const card = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), new THREE.MeshBasicMaterial({ color: 0xffffff, fog: false, toneMapped: false }));
  E.camera.updateMatrixWorld();
  card.position.copy(E.camera.position).add(new THREE.Vector3(0, 0, -10).applyQuaternion(E.camera.quaternion));
  card.quaternion.copy(E.camera.quaternion);
  E.scene.add(card);
  await wait(800);
  const canvas = E.renderer.domElement;
  const toScreen = v => { const p = v.clone().project(E.camera); return [(p.x + 1) / 2 * canvas.width, (1 - p.y) / 2 * canvas.height]; };
  const [cx, cy] = toScreen(card.position);
  const [ex] = toScreen(card.position.clone().add(new THREE.Vector3(1, 0, 0).applyQuaternion(E.camera.quaternion)));
  const half = Math.abs(ex - cx);
  out.card = { centre: [Math.round(cx), Math.round(cy)], halfPx: +half.toFixed(1), canvas: [canvas.width, canvas.height] };
  // Mean luminance of the square band from `inner` to `outer` pixels beyond the
  // card's edge, around (x, y).
  const band = (d, w, x0, y0, inner, outer) => { let s = 0, n = 0;
    for (let y = Math.max(0, Math.floor(y0 - half - outer)); y < Math.min(canvas.height, y0 + half + outer); y++)
      for (let x = Math.max(0, Math.floor(x0 - half - outer)); x < Math.min(canvas.width, x0 + half + outer); x++) {
        const dx = Math.max(0, Math.abs(x - x0) - half), dy = Math.max(0, Math.abs(y - y0) - half), r = Math.max(dx, dy);
        if (r < inner || r > outer) continue;
        const i = (y * w + x) * 4; s += .2126 * d[i] + .7152 * d[i + 1] + .0722 * d[i + 2]; n++; }
    return n ? s / n : 0; };
  const grab = () => new Promise(done => requestAnimationFrame(() => {
    const c = document.createElement('canvas'); c.width = canvas.width; c.height = canvas.height;
    const g = c.getContext('2d'); g.drawImage(canvas, 0, 0);
    const d = g.getImageData(0, 0, c.width, c.height).data;
    const sx = cx + (cx < canvas.width / 2 ? 1 : -1) * canvas.width * .3;
    done({ halo: band(d, c.width, cx, cy, 2, 14), sky: band(d, c.width, sx, cy, 2, 14) });
  }));
  const on = [], off = [];
  for (let i = 0; i < 4; i++) {
    if (!E.bloom.on) btn.click(); await wait(250); on.push(await grab());
    if (E.bloom.on) btn.click(); await wait(250); off.push(await grab());
  }
  E.scene.remove(card); card.geometry.dispose(); card.material.dispose();
  const avg = (list, k) => list.reduce((s, v) => s + v[k], 0) / list.length;
  out.halo = { edgeOn: +avg(on, 'halo').toFixed(2), edgeOff: +avg(off, 'halo').toFixed(2),
    skyOn: +avg(on, 'sky').toFixed(2), skyOff: +avg(off, 'sky').toFixed(2) };
  out.halo.edgeGain = +(out.halo.edgeOn - out.halo.edgeOff).toFixed(2);
  out.halo.skyGain = +(out.halo.skyOn - out.halo.skyOff).toFixed(2);
  out.glowReachesScreen = out.halo.edgeGain > Math.max(2, 4 * Math.abs(out.halo.skyGain));

  // The toggle and the saved setting.
  if (!E.bloom.on) { btn.click(); await wait(200); }
  out.onCallsPerFrame = E.renderer.info.render.calls;
  btn.click(); await wait(300);
  out.offButton = btn.textContent; out.offState = E.bloom.on; out.offSaved = saved(); out.offCallsPerFrame = E.renderer.info.render.calls;
  btn.click(); await wait(300);
  out.onButton = btn.textContent; out.onState = E.bloom.on; out.onSaved = saved();
  out.diagnosticsBloom = E.diagnostics().world.bloom;
  out.errors = errors;
  return out;
})()
