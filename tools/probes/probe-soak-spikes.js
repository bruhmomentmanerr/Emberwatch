// probe-soak's scripted session, but instead of ten-second samples it logs every
// frame over 150 ms with the last scripted action before it (r116, chasing
// occasional 300-500 ms frames). Each spike carries the JS heap change across
// it, and longFrames the browser's own long-animation-frame breakdown (script
// callbacks against rendering). Alternate two builds to compare them:
//
//   app/node_modules/.bin/electron tools/harness <html> tools/probes/probe-soak-spikes.js 15
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = [];
  addEventListener('error', e => errors.push(String(e.message).slice(0, 200)));
  const key = (code, type = 'keydown') => dispatchEvent(new KeyboardEvent(type, { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const SECONDS = 230, TICK = 500;
  const stops = [[0, 406], [0, 200], [0, 120], [-60, 40], [70, -20], [0, -150], [-200, 150], [180, -120],
                 [0, 470], [-330, 310], [318, 318], [-320, -320], [330, -330], [0, 300]];
  let action = 'start', actionAt = 0, last = performance.now();
  const t0 = performance.now(), spikes = [], frames = [];
  const programs = () => E.renderer.info.programs ? E.renderer.info.programs.length : null;
  // The JS heap each frame: a spike whose heap falls by tens of MB is a
  // garbage collection, not game code.
  const heap = () => performance.memory ? performance.memory.usedJSHeapSize / 1048576 : null;
  let lastHeap = heap();
  // Time the page's own frame callbacks (the game loop, a variant's layer) and
  // every renderer.render, summed between two ticks of the counter. A long frame
  // whose interval holds a long callback is the game's code; one that does not
  // is the browser and the GPU around it. (The long-animation-frame entries
  // below cannot name scripts on a file:// page.)
  const rawRaf = window.requestAnimationFrame.bind(window);
  let callbackMs = 0, renderMs = 0, worstCallback = 0, pending = null;
  window.requestAnimationFrame = cb => rawRaf(ts => { const s = performance.now(); try { cb(ts); } finally { const d = performance.now() - s; callbackMs += d; if (d > worstCallback) worstCallback = d; } });
  const rawRender = E.renderer.render.bind(E.renderer);
  E.renderer.render = (scene, camera) => { const s = performance.now(); try { rawRender(scene, camera); } finally { renderMs += performance.now() - s; } };
  // Since r119 the game itself says where a frame went; take the worst of each
  // part between two ticks of the counter.
  const cost = () => (E.frameCost ? E.frameCost() : null);
  let worstNav = 0, worstVillagers = 0, worstRender = 0;
  const parts = ['nav', 'watch', 'shelter', 'meetings', 'walk', 'anchor', 'villagers', 'render'];
  let worstPart = {};
  const countCost = () => { const c = cost(); if (!c) return;
    for (const k of parts) if ((c[k] || 0) > (worstPart[k] || 0)) worstPart[k] = c[k];
    if (c.nav > worstNav) worstNav = c.nav;
    if (c.villagers > worstVillagers) worstVillagers = c.villagers;
    if (c.render > worstRender) worstRender = c.render; };
  const count = () => { const now = performance.now(), dt = now - last, h = heap(); last = now;
    countCost();
    if (pending) { pending.nextCallbackMs = Math.round(callbackMs); pending.nextWorstCallbackMs = Math.round(worstCallback); pending.nextRenderMs = Math.round(renderMs); pending = null; }
    if (dt > 150) spikes.push(pending = { t: +((now - t0) / 1000).toFixed(1), ms: Math.round(dt), action, sinceAction: +((now - actionAt) / 1000).toFixed(2), programs: programs(),
      callbackMs: Math.round(callbackMs), worstCallbackMs: Math.round(worstCallback), renderMs: Math.round(renderMs),
      navMs: Math.round(worstNav), villagersMs: Math.round(worstVillagers), gameRenderMs: Math.round(worstRender),
      worstPartMs: Object.fromEntries(parts.map(k => [k, Math.round(worstPart[k] || 0)])),
      heapMB: h != null ? +h.toFixed(1) : null, heapChangeMB: h != null && lastHeap != null ? +(h - lastHeap).toFixed(1) : null,
      toast: (document.getElementById('gameToast')?.textContent || '').slice(0, 80) });
    callbackMs = 0; renderMs = 0; worstCallback = 0; worstNav = 0; worstVillagers = 0; worstRender = 0; worstPart = {};
    lastHeap = h;
    rawRaf(count); };
  rawRaf(count);
  // Long animation frames (Chromium): how much of a long frame was script, and
  // which callbacks, against rendering and time spent outside any task.
  try {
    new PerformanceObserver(list => { for (const f of list.getEntries()) if (f.duration > 150) frames.push({
      t: +((f.startTime - t0) / 1000).toFixed(1), ms: Math.round(f.duration), blockingMs: Math.round(f.blockingDuration || 0),
      scriptMs: Math.round((f.scripts || []).reduce((s, x) => s + x.duration, 0)),
      renderMs: Math.round(f.startTime + f.duration - f.renderStart), styleLayoutMs: Math.round(f.startTime + f.duration - f.styleAndLayoutStart),
      scripts: (f.scripts || []).filter(x => x.duration > 20).map(x => ({ ms: Math.round(x.duration), invoker: x.invoker, fn: x.sourceFunctionName, at: x.sourceCharPosition, layoutMs: Math.round(x.forcedStyleAndLayoutDuration || 0) })) }); })
      .observe({ type: 'long-animation-frame', buffered: false });
  } catch (err) { frames.push({ unsupported: String(err.message) }); }
  const did = label => { action = label; actionAt = performance.now(); };
  await wait(2000);
  const watches = E.watches.map(w => w.id), modes = ['night', 'dusk', 'ember'];
  let yaw = 0, stop = 0, walking = false;
  for (let tick = 1; (performance.now() - t0) / 1000 < SECONDS; tick++) {
    if (!walking) { key('KeyW'); walking = true; }
    yaw += 0.35; E.look(yaw, -0.02);
    if (tick % 9 === 0) { key('Space'); setTimeout(() => key('Space', 'keyup'), 120); }
    if (tick % 6 === 0) { did('cast'); E.cast(); }
    if (tick % 40 === 0) { stop = (stop + 1) % stops.length; const [x, z] = stops[stop]; did('teleport ' + x + ',' + z);
      E.player.x = x; E.player.z = z; E.player.vy = 0; E.player.y = (E.terrainAt ? E.terrainAt(x, z) : 0) + 0.2; }
    if (tick % 50 === 25) { const w = watches[(tick / 25) % watches.length | 0]; did('watch ' + w); E.setWatch(w); }
    if (tick % 90 === 45) { const m = modes[(tick / 45) % modes.length | 0]; did('light ' + m); document.querySelector('[data-light="' + m + '"]')?.click(); }
    if (tick % 28 === 14) { did('E'); key('KeyE'); await wait(300); did('F'); key('KeyF'); await wait(200); did('Escape'); key('Escape'); }
    if (tick % 70 === 35) { for (const k of ['KeyM', 'KeyJ', 'KeyP']) { did('panel ' + k); key(k); await wait(150); key('Escape'); await wait(100); } }
    if (tick % 110 === 55) { const b = document.getElementById('bloomBtn'); did('bloom off'); b?.click(); await wait(1500); did('bloom on'); b?.click(); }
    await wait(TICK);
  }
  key('KeyW', 'keyup');
  did('end: night'); document.querySelector('[data-light="night"]')?.click();
  if (E.bloom && !E.bloom.on) { did('end: bloom on'); document.getElementById('bloomBtn')?.click(); }
  await wait(1500);
  return { title: document.title, revision: E.diagnostics().revision, errors: [...new Set(errors)], spikes, longFrames: frames };
})()
