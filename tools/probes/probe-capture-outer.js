// Captures the outer-residents IIFE's exact live output, saved via
// window.__harnessSave. Run against a copy of index.html instrumented per
// scratchpad/instrument-outer.txt.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(3500);
  if (!window.__OUTER_RESIDENTS) return { error: 'no capture — file not instrumented' };
  const saved = window.__harnessSave('outer-residents.json', JSON.stringify(window.__OUTER_RESIDENTS));
  return { n: window.__OUTER_RESIDENTS.length, seed: E.diagnostics().world.seed, file: saved.file };
})()
