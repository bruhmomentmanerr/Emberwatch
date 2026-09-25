// What is Ember Hour like to play? Its clock is a real Peak session, and with
// no device to hand `H` opens a stand-in hour of ninety seconds. Its balance is
// reach: how many of the twelve sealed arches you can get to before the hour
// shuts, and whether any of them is simply too far from the rest.
//
//   HARNESS_PROFILE=<tmp dir> HARNESS_TIMEOUT=900 app/node_modules/.bin/electron \
//     tools/harness variants/emberwatch_ember-hour.html tools/probes/probe-balance-emberhour.js 15
//
// Walks from the north gate on routes from EMBER.findPath, three hours in a row.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = [];
  addEventListener('error', e => errors.push(String(e.message).slice(0, 200)));
  const down = code => dispatchEvent(new KeyboardEvent('keydown', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const up = code => dispatchEvent(new KeyboardEvent('keyup', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const found = () => Number(document.getElementById('ehFound')?.textContent) || 0;
  const state = () => document.getElementById('ehState')?.textContent || '';

  const out = { revision: E.diagnostics().revision, title: document.title, errors };
  if (!document.getElementById('ehFound')) { out.note = 'no arch counter — is this Ember Hour?'; return out; }
  if (!E.findPath) { out.note = 'this build has no EMBER.findPath (r120)'; return out; }

  // The arches are the layer's own meshes: a pair of posts and a lintel, with a
  // glow light hung in them. Find them by that shape.
  // Each arch group carries its spec and its glow (emberhour.js build()).
  const arches = [];
  E.scene.traverse(o => { if (o.userData && o.userData.spec && o.userData.glow) arches.push(o); });
  out.arches = arches.length;
  const reached = new Set();

  const hour = async (n) => {
    E.player.x = 0; E.player.z = 300; E.player.y = 0; E.player.vy = 0;   // just inside the new north gate
    await wait(800);
    down('KeyH'); await wait(600);                                        // the stand-in hour
    const opened = state();
    const t0 = performance.now(), before = found();
    let route = null, routeAt = 0, target = null, stuck = 0, visited = 0;
    down('KeyW');
    while ((performance.now() - t0) / 1000 < 95) {
      if (!target || Math.hypot(E.player.x - target.position.x, E.player.z - target.position.z) < 3.4) {
        if (target) { reached.add(target.uuid); visited++; }
        target = arches.filter(a => !reached.has(a.uuid))
          .sort((a, b) => Math.hypot(a.position.x - E.player.x, a.position.z - E.player.z) - Math.hypot(b.position.x - E.player.x, b.position.z - E.player.z))[0];
        if (!target) break;
        route = E.findPath(E.player.x, E.player.z, target.position.x, target.position.z) || [[target.position.x, target.position.z]];
        routeAt = 0;
        while (routeAt < route.length - 1 && Math.hypot(E.player.x - route[routeAt][0], E.player.z - route[routeAt][1]) < 3) routeAt++;
      }
      while (route && routeAt < route.length - 1 && Math.hypot(E.player.x - route[routeAt][0], E.player.z - route[routeAt][1]) < 1.6) routeAt++;
      const point = route && route[routeAt] ? route[routeAt] : [target.position.x, target.position.z];
      const px = E.player.x, pz = E.player.z;
      E.look(Math.atan2(-(point[0] - px), -(point[1] - pz)), -0.05);
      down('KeyW');
      await wait(120);
      if (Math.hypot(E.player.x - px, E.player.z - pz) < 0.06) { stuck += 120; if (stuck > 700) { down('Space'); setTimeout(() => up('Space'), 150); stuck = 0; routeAt = Math.min(routeAt + 1, (route || [0]).length - 1); } }
      else stuck = 0;
    }
    up('KeyW');
    return { hour: n, opened, archesReached: visited, counterWent: found() - before, stateAfter: state() };
  };

  out.hours = [];
  for (let n = 1; n <= 3; n++) out.hours.push(await hour(n));
  out.arcesFoundTotal = found();
  out.spread = arches.map(a => ({ at: [Math.round(a.position.x), Math.round(a.position.z)], radius: Math.round(Math.hypot(a.position.x, a.position.z)) }))
    .sort((a, b) => a.radius - b.radius);
  return out;
})()
