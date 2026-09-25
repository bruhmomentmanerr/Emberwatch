(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(3500);
  if (!window.__COMPILER_LOTS) return { error: 'no capture — file not instrumented' };
  const saved = window.__harnessSave('compiler-lots.json', JSON.stringify(window.__COMPILER_LOTS));
  return { n: window.__COMPILER_LOTS.length, nulls: window.__COMPILER_LOTS.filter(x => !x).length, seed: E.diagnostics().world.seed, file: saved.file };
})()
