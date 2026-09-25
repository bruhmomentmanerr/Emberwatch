// r113 walk-in homes. Counts them, fingerprints the seeded layout (run it on the
// previous build in the same profile and the fingerprint must match — homes are
// hash-chosen and must not move a single house), walks through one front door
// with E, checks the room is recognised and its lamp takes a light slot only
// while you are inside, and returns street and inside shots of the three homes
// nearest the North Ward.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-homes.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = []; addEventListener('error', e => errors.push(String(e.message)));
  const key = code => dispatchEvent(new KeyboardEvent('keydown', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  await wait(2500);
  const d = E.diagnostics(), round = v => Math.round(v * 100);
  const out = { revision: d.revision, errors,
    fingerprint: { shops: E.shops.length, shopSum: E.shops.reduce((s, p) => s + round(p.x) * 3 + round(p.z), 0),
      residentHomes: E.villagers.reduce((s, v) => s + round(v.homeX || 0) * 3 + round(v.homeZ || 0), 0),
      parcels: d.city.parcels, intruding: d.city.roadObstructions.intruding } };
  const homes = (E.doors || []).filter(x => x.kind === 'home');
  out.homes = homes.length; out.doors = (E.doors || []).length;
  if (!homes.length) return out;
  const names = new Set(homes.map(h => h.name)); out.uniqueNames = names.size === homes.length;
  const near = homes.slice().sort((a, b) => Math.hypot(a.x, a.z - 150) - Math.hypot(b.x, b.z - 150));
  const h = near[0];
  // Walk in through the door rather than teleporting inside.
  E.player.x = h.outsideX; E.player.z = h.outsideZ; E.player.y = 0; E.player.vy = 0;
  await wait(600);
  out.hintOutside = document.querySelector('#interactHint > span').textContent;
  const litBefore = (() => { let n = 0; E.scene.traverse(o => { if (o.isPointLight && o.visible && o.color.getHex() === 0xff9a4a) n++; }); return n; })();
  key('KeyE'); await wait(900);
  out.toast = document.getElementById('gameToast').textContent;
  out.insideAfterE = Math.hypot(E.player.x - h.insideX, E.player.z - h.insideZ) < 1;
  out.saved = (() => { try { return JSON.parse(localStorage.getItem('emberwatch.game-state.v3')).interior; } catch { return null; } })();
  const litInside = (() => { let n = 0; E.scene.traverse(o => { if (o.isPointLight && o.visible && o.color.getHex() === 0xff9a4a && Math.hypot(o.position.x - h.cx, o.position.z - h.cz) < 6) n++; }); return n; })();
  out.homeLampLitInside = litInside; out.homeLampsLitOutsideBefore = litBefore;
  key('KeyE'); await wait(600);
  out.backOutside = Math.hypot(E.player.x - h.outsideX, E.player.z - h.outsideZ) < 1;
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  out.sample = near.slice(0, 3).map(x => [x.name, x.purpose]);
  out.shots = [];
  near.slice(0, 3).forEach((x, i) => {
    const sx = x.outsideX + (x.outsideX - x.cx) * 0.9, sz = x.outsideZ + (x.outsideZ - x.cz) * 0.9;
    out.shots.push({ name: 'home' + i + '-street', x: sx, z: sz, yaw: face(sx, sz, x.cx, x.cz), pitch: 0.05 });
    out.shots.push({ name: 'home' + i + '-inside', x: x.insideX, z: x.insideZ, yaw: face(x.insideX, x.insideZ, x.cx, x.cz), pitch: -0.12 });
  });
  return out;
})()
