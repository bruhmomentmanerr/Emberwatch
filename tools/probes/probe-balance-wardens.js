// What is Wardens like to play? It has no failure state, so its balance is
// pace: how long a commission takes, and how fast the seven ranks come.
//
//   HARNESS_PROFILE=<tmp dir> HARNESS_TIMEOUT=1300 app/node_modules/.bin/electron \
//     tools/harness variants/emberwatch_wardens.html tools/probes/probe-balance-wardens.js 15
//
// Walks each commission on a route from EMBER.findPath, reads the ledger's own
// HUD for the target's bearing and distance, and records how long each takes.
// Its own storage, or it inherits an earlier run's rank.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = [];
  addEventListener('error', e => errors.push(String(e.message).slice(0, 200)));
  const down = code => dispatchEvent(new KeyboardEvent('keydown', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const up = code => dispatchEvent(new KeyboardEvent('keyup', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const rankText = () => document.getElementById('wlRank')?.textContent || '';
  const title = () => document.getElementById('wlTitle')?.textContent || '';
  const done = () => { const m = /(\d+) written up/.exec(rankText()); return m ? Number(m[1]) : 0; };

  const out = { revision: E.diagnostics().revision, title: document.title, errors };
  if (!document.getElementById('wlTitle')) { out.note = 'no ledger — is this Wardens?'; return out; }
  if (!E.findPath) { out.note = 'this build has no EMBER.findPath (r120)'; return out; }

  // Where the ledger is actually pointing (EMBER.wardens, r121). Steering by the
  // HUD's prose bearing instead spent a fourteen-minute run walking into walls
  // and finished one commission.
  const aim = () => {
    const w = E.wardens ? E.wardens() : null;
    if (!w || !w.title) return null;
    if (w.points) { const next = w.points.find(p => !p.hit) || w.points[0]; return [next.x, next.z]; }
    return w.target ? [w.target.x, w.target.z] : null;
  };

  const TICK = 100, LIMIT = 14 * 60 * 1000, t0 = performance.now();
  const finished = [], startedDone = done();
  let commissions = 0, current = title(), legStart = t0, walked = 0;
  let lastX = E.player.x, lastZ = E.player.z, route = null, routeAt = 0, stuck = 0, replans = 0;

  let plannedTo = null;
  const planTowards = () => {
    const a = aim();
    if (!a) return null;
    route = E.findPath(E.player.x, E.player.z, a[0], a[1]) || [[a[0], a[1]]];
    plannedTo = a; routeAt = 0;
    while (routeAt < route.length - 1 && Math.hypot(E.player.x - route[routeAt][0], E.player.z - route[routeAt][1]) < 3) routeAt++;
    return a;
  };

  down('KeyW');
  planTowards();
  while (performance.now() - t0 < LIMIT) {
    if (title() !== current) {                                        // the ledger moved on
      const at = performance.now();
      finished.push({ commission: current.slice(0, 48), seconds: +((at - legStart) / 1000).toFixed(1), rank: rankText().split(' · ')[0] });
      commissions++; current = title(); legStart = at; route = null;
      await wait(2600);                                               // the ledger pauses before the next
      planTowards();
    }
    // Re-plan when the ledger moves its mark — but a "find the resident"
    // commission tracks someone who is walking, and re-planning on every tick
    // left the probe pivoting on the spot for a whole run (r121). Only when the
    // mark has actually gone somewhere.
    const a = aim();
    if (!route || !plannedTo || (a && Math.hypot(a[0] - plannedTo[0], a[1] - plannedTo[1]) > 6)) planTowards();

    const point = route && route[routeAt] ? route[routeAt] : null;
    if (point) {
      while (routeAt < route.length - 1 && Math.hypot(E.player.x - route[routeAt][0], E.player.z - route[routeAt][1]) < 1.6) routeAt++;
      E.look(Math.atan2(-(point[0] - E.player.x), -(point[1] - E.player.z)), -0.05);
    }
    down('KeyW');
    await wait(TICK);

    const moved = Math.hypot(E.player.x - lastX, E.player.z - lastZ);
    walked += moved; lastX = E.player.x; lastZ = E.player.z;
    if (moved < 0.06) { stuck += TICK; if (stuck > 600) { down('Space'); setTimeout(() => up('Space'), 150); stuck = 0; replans++; planTowards(); } }
    else stuck = 0;
    // At the end of a route with the ledger still asking: aim again from here.
    if (route && routeAt >= route.length - 1 && Math.hypot(E.player.x - route[route.length - 1][0], E.player.z - route[route.length - 1][1]) < 3) planTowards();
  }
  up('KeyW');

  out.playedSeconds = +((performance.now() - t0) / 1000).toFixed(0);
  out.commissionsFinished = commissions;
  out.writtenUp = done() - startedDone;
  out.rank = rankText();
  out.metresWalked = Math.round(walked);
  out.replansWhenStuck = replans;
  out.secondsEach = finished.map(f => f.seconds);
  out.medianSeconds = finished.length ? finished.map(f => f.seconds).sort((a, b) => a - b)[finished.length >> 1] : null;
  out.finished = finished.slice(0, 12);
  return out;
})()
