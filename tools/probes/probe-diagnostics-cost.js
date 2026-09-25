// What a probe's own calls cost the frame. probe-soak samples E.diagnostics()
// and walks the scene every ten seconds, from inside the page, between frames —
// a slow call there is a long frame that the soak then reports as the game's.
// Times each call 25 times, a second apart, and logs frames over 150 ms while
// it does, with and without the calls, to tell the two apart.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-diagnostics-cost.js 15
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  let last = performance.now(), long = [];
  const count = () => { const now = performance.now(); if (now - last > 150) long.push(Math.round(now - last)); last = now; requestAnimationFrame(count); };
  requestAnimationFrame(count);
  const time = fn => { const t = performance.now(); fn(); return performance.now() - t; };
  const stats = a => { const s = [...a].sort((p, q) => p - q); return { min: +s[0].toFixed(1), median: +s[s.length >> 1].toFixed(1), max: +s[s.length - 1].toFixed(1) }; };
  await wait(2000);
  long = [];
  await wait(25000);
  const quiet = long.slice();
  long = [];
  const diag = [], traverse = [], info = [];
  for (let i = 0; i < 25; i++) {
    diag.push(time(() => E.diagnostics()));
    traverse.push(time(() => { let n = 0; E.scene.traverse(() => n++); }));
    info.push(time(() => E.renderer.info.programs && E.renderer.info.programs.length));
    await wait(1000);
  }
  return { revision: E.diagnostics().revision, diagnosticsMs: stats(diag), traverseMs: stats(traverse), infoMs: stats(info),
    longFramesQuiet25s: quiet, longFramesWhileCalling25s: long.slice() };
})()
