// Is Emberfall a game? The scripted soak (r113) only ever showed that the
// variant does not break. This one plays it: route to the nearest dark brazier,
// walk there on the city's own streets, light it, on to the next — and see
// whether the ember lasts, how long a full clear takes, and how often you die.
//
// It holds W and steers along a route from EMBER.findPath (r120), which is what
// a player who knows Vaneth does; the first version of this probe simply aimed
// at the target and shoved at whatever wall was in the way, which measured the
// probe, not the game (6 braziers in 15 minutes, 1.4 m/s against a walk of 8).
// Give it its own storage, or it inherits the braziers an earlier run lit:
//
//   HARNESS_PROFILE=<tmp dir> HARNESS_TIMEOUT=1300 app/node_modules/.bin/electron \
//     tools/harness variants/emberwatch_emberfall.html tools/probes/probe-balance-emberfall.js 15
//
// Numbers to read: minEmber (how close the clock came), longestLegSeconds
// against the 300 s a full ember buys, deaths, and whether it cleared at all.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = [];
  addEventListener('error', e => errors.push(String(e.message).slice(0, 200)));
  const down = code => dispatchEvent(new KeyboardEvent('keydown', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const up = code => dispatchEvent(new KeyboardEvent('keyup', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const ember = () => parseFloat(document.getElementById('efFill').style.width) || 0;
  const litCount = () => Number(document.getElementById('efLit').textContent) || 0;
  const flash = () => document.getElementById('efFlash').textContent || '';

  const braziers = [];
  E.scene.traverse(o => { if (o.userData && o.userData.site && o.userData.flame) braziers.push(o); });
  const out = { revision: E.diagnostics().revision, title: document.title, braziers: braziers.length, litAtStart: litCount(), errors };
  if (!braziers.length) { out.note = 'no braziers — is this Emberfall?'; return out; }
  if (!E.findPath) { out.note = 'this build has no EMBER.findPath (r120)'; return out; }

  const TICK = 100, LIMIT = 15 * 60 * 1000;
  const t0 = performance.now(), lights = [], legs = [];
  let deaths = 0, minEmber = 100, walked = 0, lastFlash = '';
  // What the ember was on the way here, not after the brazier topped it up:
  // reading it afterwards said 100 at every light and told us nothing (r121).
  let legLow = 100, beforeLight = 100;
  let lastX = E.player.x, lastZ = E.player.z, legStart = t0, lit = litCount();
  let route = null, routeAt = 0, target = null, stuckFor = 0, replans = 0;

  const nearestDark = () => {
    let best = Infinity, pick = null;
    for (const g of braziers) {
      if (g.userData.on) continue;
      const d = Math.hypot(E.player.x - g.position.x, E.player.z - g.position.z);
      if (d < best) { best = d; pick = g; }
    }
    return pick;
  };
  // A route starts at the player's own nav cell, which is often a step behind
  // them: walking at it means walking backwards into whatever is there. Drop
  // the points that are already underfoot.
  const plan = g => {
    route = E.findPath(E.player.x, E.player.z, g.position.x, g.position.z) || [[g.position.x, g.position.z]];
    routeAt = 0;
    while (routeAt < route.length - 1 && Math.hypot(E.player.x - route[routeAt][0], E.player.z - route[routeAt][1]) < 3) routeAt++;
  };

  down('KeyW');
  while (performance.now() - t0 < LIMIT) {
    const pick = nearestDark();
    if (!pick) break;                                                 // everything is lit
    if (pick !== target) { target = pick; plan(pick); }

    // Steer at the next point on the route; the last one is the brazier itself.
    while (route && routeAt < route.length - 1 && Math.hypot(E.player.x - route[routeAt][0], E.player.z - route[routeAt][1]) < 1.6) routeAt++;
    const point = route && route[routeAt] ? route[routeAt] : [target.position.x, target.position.z];
    E.look(Math.atan2(-(point[0] - E.player.x), -(point[1] - E.player.z)), -0.05);
    down('KeyW');
    await wait(TICK);

    const moved = Math.hypot(E.player.x - lastX, E.player.z - lastZ);
    walked += moved; lastX = E.player.x; lastZ = E.player.z;
    // Caught on something the route walked straight through: jump, then re-plan.
    if (moved < 0.06) {
      stuckFor += TICK;
      if (stuckFor > 600) {
        down('Space'); setTimeout(() => up('Space'), 150); stuckFor = 0; replans++;
        // Twice at the same point means the point is the problem: step past it.
        if (route && routeAt < route.length - 1 && replans % 2 === 0) routeAt++;
        else plan(target);
      }
    } else stuckFor = 0;

    const now = ember();
    if (now < minEmber) minEmber = now;
    if (now < legLow) legLow = now;
    beforeLight = now;
    const message = flash();
    if (message && message !== lastFlash) {
      lastFlash = message;
      if (/ember dies/.test(message)) { deaths++; minEmber = 0; await wait(3000); plan(target); }
    }
    if (litCount() > lit) {
      lit = litCount();
      const at = performance.now();
      lights.push({ lit, where: target.userData.site.where, seconds: +((at - t0) / 1000).toFixed(1),
        emberOnArrival: Math.round(beforeLight), lowestOnTheWay: Math.round(legLow) });
      legs.push(+((at - legStart) / 1000).toFixed(1));
      legStart = at; target = null; route = null; legLow = 100;
    }
  }
  up('KeyW');

  out.playedSeconds = +((performance.now() - t0) / 1000).toFixed(0);
  out.litAtEnd = litCount();
  out.clearedEverything = litCount() >= braziers.length;
  out.deaths = deaths;
  out.minEmberPercent = +minEmber.toFixed(0);
  out.metresWalked = Math.round(walked);
  out.metresPerSecond = +(walked / Math.max(1, (performance.now() - t0) / 1000)).toFixed(2);
  out.replansWhenStuck = replans;
  out.longestLegSeconds = legs.length ? Math.max(...legs) : null;
  out.medianLegSeconds = legs.length ? legs.slice().sort((a, b) => a - b)[legs.length >> 1] : null;
  out.emberBuysSeconds = 90;                                          // BURN = 100/90 per second, from the layer (r121)
  out.lowestOnArrival = lights.length ? Math.min(...lights.map(l => l.lowestOnTheWay)) : null;
  out.medianOnArrival = lights.length ? lights.map(l => l.emberOnArrival).sort((a, b) => a - b)[lights.length >> 1] : null;
  out.lights = lights;
  return out;
})()
