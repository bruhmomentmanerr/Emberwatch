// r117: the mourners. At the Working Watch bell up to two residents whose
// household has a legible headstone walk out to the Old Graveyard, keep the
// Still Hours at the stone, and walk home at the Ember Watch bell.
//
//   HARNESS_TIMEOUT=760 app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-mourners.js 8 [shotsDir]
//
// Follows them out (legs left, how long to the stone, feet on the terrain),
// reads their stone and talks to one at the vigil, then rings the Ember Watch
// and checks they turn for home. The walk takes minutes, hence the timeout.
// With a shotsDir it returns a shot of the vigil, but the harness takes shots
// after the probe, when they have gone home: for the shot, set localStorage
// 'probe.mourners.shotsOnly' to '1' first and the probe stops before the bell.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = [];
  addEventListener('error', e => errors.push(String(e.message).slice(0, 200)));
  const key = code => { for (const type of ['keydown', 'keyup']) dispatchEvent(new KeyboardEvent(type, { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true })); };
  const shotsOnly = localStorage.getItem('probe.mourners.shotsOnly') === '1';
  localStorage.removeItem('probe.mourners.shotsOnly');                 // one run only
  const out = { revision: E.diagnostics().revision, errors };

  // Is the ground under the wall continuous where residents switch to terrain?
  out.groundAtWall = [0, 90, 180, 270].map(deg => { const a = deg * Math.PI / 180;
    return { deg, heights: [360, 377, 379, 384, 410].map(r => +E.terrainAt(Math.cos(a) * r, Math.sin(a) * r).toFixed(2)) }; });

  // The game opens on the Working Watch, whose bell picks the day's mourners,
  // so they are already on their way. Do not ring it again: the walk is the test.
  if (E.watch().id !== 'labour') { E.setWatch('labour'); await wait(16000); }
  const first = E.mourners();
  out.startedIn = E.watch().id;
  out.chosen = first.map(m => ({ name: m.name, house: m.house, legs: m.legs }));
  if (!first.length) { out.note = 'nobody was sent'; return out; }

  // Follow them until both stand at their stone, or 560 s pass.
  const t0 = performance.now(), track = [], arrived = {};
  let worstGround = 0;
  while ((performance.now() - t0) / 1000 < 560) {
    const now = E.mourners().filter(m => m.house);
    for (const m of now) {
      if (m.vigil && arrived[m.name] === undefined) arrived[m.name] = +((performance.now() - t0) / 1000).toFixed(0);
      if (Math.hypot(m.x, m.z) > 380) worstGround = Math.max(worstGround, Math.abs(m.y - E.terrainAt(m.x, m.z)));
    }
    if (track.length < 60 && Math.round((performance.now() - t0) / 1000) % 15 === 0)
      track.push({ s: Math.round((performance.now() - t0) / 1000), watch: E.watch().id, at: now.map(m => [m.name.split(' ')[0], m.legs, m.vigil ? 'vigil' : Math.round(Math.hypot(m.x - (m.spot ? m.spot[0] : 0), m.z - (m.spot ? m.spot[1] : 0))) + ' m to go']) });
    if (now.length && now.every(m => m.vigil)) break;
    await wait(1000);
  }
  out.secondsToStone = arrived;
  out.track = track.filter((row, i, all) => i === 0 || row.s !== all[i - 1].s);
  out.worstFeetOffGroundOutsideWall = +worstGround.toFixed(3);
  const atStone = E.mourners().filter(m => m.vigil);
  out.atStone = atStone.map(m => ({ name: m.name, house: m.house, y: m.y, ground: +E.terrainAt(m.x, m.z).toFixed(2) }));
  if (!atStone.length) return out;

  // Read their stone, then talk to them.
  const m = atStone[0], npc = E.villagers.find(v => v.name === m.name);
  const stoneEntry = E.interactions.find(i => i.id === 'grave-' + m.stone);
  // Stand on the open ground inside the yard, toward its centre: a stone by the
  // gap puts anything offset the other way on the wall, and the game pushes the
  // player off it, out of talking range. Wait out the toast for entering the
  // wilds before reading anything.
  const yard = E.wilds.graves, toward = (x, z, d) => { const dx = yard.cx - x, dz = yard.cz - z, l = Math.hypot(dx, dz) || 1; return [x + dx / l * d, z + dz / l * d]; };
  const [px, pz] = toward(npc.g.position.x, npc.g.position.z, 2);
  E.player.x = px; E.player.z = pz; E.player.vy = 0; E.player.y = E.terrainAt(px, pz);
  await wait(2500);
  if (stoneEntry) { stoneEntry.act(); await wait(200);
    out.stoneToast = document.getElementById('gameToast').textContent; out.stoneNamesMourner = out.stoneToast.includes(m.name); }
  E.look(Math.atan2(-(npc.g.position.x - E.player.x), -(npc.g.position.z - E.player.z)), -0.15);
  await wait(900);
  out.talkDistance = +Math.hypot(npc.g.position.x - E.player.x, npc.g.position.z - E.player.z).toFixed(2);
  // r117 called the resident's stay `vigil`; r118 made it `stay` for every outing.
  const stay = npc.stay || npc.vigil;
  out.facesStoneNotPlayer = !!stay && Math.abs(Math.sin(npc.g.rotation.y - Math.atan2(stay.face[0] - npc.g.position.x, stay.face[1] - npc.g.position.z))) < 0.05;
  // Their own stone is usually nearer than they are, so E reads it and F talks.
  out.hintNear = document.querySelector('#interactHint > span')?.textContent;
  out.hintAlt = document.getElementById('interactAlt').hidden ? null : document.querySelector('#interactAlt > span')?.textContent;
  key(/^talk/.test(out.hintNear || '') ? 'KeyE' : 'KeyF'); await wait(600);
  out.dialogueOpened = document.getElementById('dialoguePanel').classList.contains('open');
  out.dialogueName = document.getElementById('dialogueName').textContent;
  const body = document.getElementById('dialogueLines')?.textContent || '';
  out.greetingMentionsStone = /stone/.test(body);
  out.greetingExcerpt = body.slice(0, 420);
  key('Escape'); await wait(600);
  out.stillAtVigilAfterTalk = E.mourners().some(x => x.name === m.name && x.vigil);

  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  // From inside the yard, past their stone: they face the stone, so this sees
  // their face over it rather than their back against the gate posts.
  const [sx, sz] = toward(npc.g.position.x, npc.g.position.z, 4.2);
  out.shots = [{ name: 'mourner-vigil', x: sx, z: sz, y: E.terrainAt(sx, sz), yaw: face(sx, sz, npc.g.position.x, npc.g.position.z), pitch: -0.12 }];
  if (shotsOnly) return out;

  // The Ember Watch: back the way they came.
  E.player.x = 0; E.player.z = 406; E.player.y = 0;
  // Wait until each has stood the minimum vigil, then ring the Ember Watch and
  // give them a minute to turn for home.
  const before = E.mourners().filter(x => x.house);
  for (let i = 0; i < 60 && E.mourners().some(x => x.vigil && x.stood < 45); i++) await wait(1000);
  const bell = performance.now();
  E.setWatch('ember');
  out.homeward = {};
  while ((performance.now() - bell) / 1000 < 75) {
    for (const b of before) {
      const v = E.villagers.find(x => x.name === b.name), row = E.mourners().find(x => x.name === b.name);
      if (out.homeward[b.name] === undefined && !(row && row.house) && Math.hypot(v.g.position.x - b.spot[0], v.g.position.z - b.spot[1]) > 4)
        out.homeward[b.name] = { leftAfter: +((performance.now() - bell) / 1000).toFixed(0), legsHome: row ? row.legs : 0, wasAtVigil: b.vigil };
    }
    if (before.every(b => out.homeward[b.name] !== undefined)) break;
    await wait(1000);
  }
  out.stillOutAfterBell = before.filter(b => out.homeward[b.name] === undefined).map(b => E.mourners().find(x => x.name === b.name) || b.name);
  return out;
})()
