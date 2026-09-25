// A long play session, scripted: about four minutes of walking, casting, talking,
// turning the watch and the lighting, opening panels and toggling bloom, with
// a sample every ten seconds of what tends to leak or drift — JS heap, GPU
// geometries/textures/programs, scene size, spells alive, frame time, errors.
// Works on the base game and on every variant (their own layers keep running
// underneath: Emberfall's ember drains, Long Night's wraiths come, and so on).
//
//   app/node_modules/.bin/electron tools/harness <html> tools/probes/probe-soak.js 15
//
// The harness kills a page 300 s after its wait, so the session stays under
// that. Leaves bloom on and the lighting on night, whatever it found.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = [], warnings = [];
  addEventListener('error', e => errors.push(String(e.message).slice(0, 200)));
  addEventListener('unhandledrejection', e => errors.push('rejection: ' + String(e.reason).slice(0, 200)));
  const key = (code, type = 'keydown') => dispatchEvent(new KeyboardEvent(type, { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const SECONDS = 230, TICK = 500;
  const stops = [[0, 406], [0, 200], [0, 120], [-60, 40], [70, -20], [0, -150], [-200, 150], [180, -120],
                 [0, 470], [-330, 310], [318, 318], [-320, -320], [330, -330], [0, 300]];
  let frames = 0, frameMs = 0, last = performance.now(), worstFrame = 0;
  const count = () => { const now = performance.now(), dt = now - last; last = now; frames++; frameMs += dt; if (dt > worstFrame) worstFrame = dt; requestAnimationFrame(count); };
  requestAnimationFrame(count);
  const children = () => { let n = 0; E.scene.traverse(() => n++); return n; };
  const sample = t => {
    const info = E.renderer.info, d = E.diagnostics();
    const s = { t, heapMB: performance.memory ? +(performance.memory.usedJSHeapSize / 1048576).toFixed(1) : null,
      geometries: info.memory.geometries, textures: info.memory.textures, programs: info.programs ? info.programs.length : null,
      objects: children(), spells: d.runtime ? d.runtime.spells : null, calls: info.render.calls,
      avgFrameMs: frames ? +(frameMs / frames).toFixed(1) : null, worstFrameMs: +worstFrame.toFixed(0), errors: errors.length };
    frames = 0; frameMs = 0; worstFrame = 0;
    return s;
  };
  await wait(2000);
  const samples = [sample(0)];
  const watches = E.watches.map(w => w.id), modes = ['night', 'dusk', 'ember'];
  let yaw = 0, stop = 0, walking = false;
  const t0 = performance.now();
  for (let tick = 1; (performance.now() - t0) / 1000 < SECONDS; tick++) {
    const sec = tick * TICK / 1000;
    // Walk in a slow circle, holding W, and jump now and then.
    if (!walking) { key('KeyW'); walking = true; }
    yaw += 0.35; E.look(yaw, -0.02);
    if (tick % 9 === 0) { key('Space'); setTimeout(() => key('Space', 'keyup'), 120); }
    if (tick % 6 === 0) E.cast();
    if (tick % 40 === 0) { stop = (stop + 1) % stops.length; const [x, z] = stops[stop];
      E.player.x = x; E.player.z = z; E.player.vy = 0; E.player.y = (E.terrainAt ? E.terrainAt(x, z) : 0) + 0.2; }
    if (tick % 50 === 25) E.setWatch(watches[(tick / 25) % watches.length | 0]);
    if (tick % 90 === 45) document.querySelector('[data-light="' + modes[(tick / 45) % modes.length | 0] + '"]')?.click();
    if (tick % 28 === 14) { key('KeyE'); await wait(300); key('KeyF'); await wait(200); key('Escape'); }
    if (tick % 70 === 35) { for (const k of ['KeyM', 'KeyJ', 'KeyP']) { key(k); await wait(150); key('Escape'); await wait(100); } }
    if (tick % 110 === 55) { const b = document.getElementById('bloomBtn'); b?.click(); await wait(1500); b?.click(); }
    if (tick % 20 === 0) samples.push(sample(+sec.toFixed(0)));
    await wait(TICK);
  }
  key('KeyW', 'keyup');
  document.querySelector('[data-light="night"]')?.click();
  if (E.bloom && !E.bloom.on) document.getElementById('bloomBtn')?.click();
  await wait(1500);
  samples.push(sample(SECONDS));
  const first = samples[1] || samples[0], end = samples[samples.length - 1];
  return { title: document.title, revision: E.diagnostics().revision, seconds: SECONDS,
    growth: { heapMB: end.heapMB != null ? +(end.heapMB - first.heapMB).toFixed(1) : null, geometries: end.geometries - first.geometries,
      textures: end.textures - first.textures, programs: end.programs - first.programs, objects: end.objects - first.objects },
    errors: [...new Set(errors)].slice(0, 12), samples };
})()
