// Captures the current seed's innerInfill output as fixed data, saved via
// window.__harnessSave. Run against a copy of index.html that has been
// instrumented to expose CITY_LOTS_BUILT (see tools/bake-city.js).
//   HARNESS_SAVE_DIR=<dir> ... tools/harness <instrumented.html> \
//     tools/probes/probe-capture-lots.js 15
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(3500);
  if (!window.__CITY_LOTS_BUILT) return { error: 'no capture arrays on window — file was not instrumented' };
  const saved = window.__harnessSave('city-lots.json', JSON.stringify({
    seed: E.diagnostics().world.seed,
    built: window.__CITY_LOTS_BUILT,
    vacant: window.__CITY_LOTS_VACANT,
  }));
  return { seed: E.diagnostics().world.seed, built: window.__CITY_LOTS_BUILT.length, vacant: window.__CITY_LOTS_VACANT.length, file: saved.file };
})()
