// r118: the outings past the wall other than the graveyard — someone sifting
// the ash at the Fallen Hall, an angler at Foxglove Pond. (probe-mourners covers
// the graveyard.) At the Working Watch bell each is picked for the day; they
// walk out through a gate, stay through the Market Watch and the Still Hours,
// and walk home at the Ember Watch bell.
//
//   HARNESS_TIMEOUT=760 app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-outings.js 8 [shotsDir]
//
// Follows both out, checks the pose each takes and the angler's rod, talks to
// each, sifts the ash and skims a stone with them there, then rings the Ember
// Watch and checks they turn for home. The shots are of them staying; as with
// probe-mourners the harness takes shots after the probe, so set localStorage
// 'probe.outings.shotsOnly' to '1' first to stop before the bell.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = [];
  addEventListener('error', e => errors.push(String(e.message).slice(0, 200)));
  const key = code => dispatchEvent(new KeyboardEvent('keydown', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  const shotsOnly = localStorage.getItem('probe.outings.shotsOnly') === '1';
  localStorage.removeItem('probe.outings.shotsOnly');
  const out = { revision: E.diagnostics().revision, errors };
  const toast = () => document.getElementById('gameToast').textContent;

  if (E.watch().id !== 'labour') { E.setWatch('labour'); await wait(16000); }
  const all = E.outings();
  out.chosen = all.map(o => ({ name: o.name, kind: o.kind, place: o.place }));
  const kinds = ['hall', 'angler'];
  const mine = () => E.outings().filter(o => kinds.includes(o.kind));
  const names = mine().map(o => o.name);
  if (!names.length) { out.note = 'nobody sent to the hall or the pond'; return out; }
  const lamplighter = E.villagers.find(v => v.name === (mine().find(o => o.kind === 'hall') || {}).name);
  out.hallVisitorWorksAt = lamplighter ? lamplighter.workName : null;

  // Follow them until both are staying, or 560 s pass.
  const t0 = performance.now(), arrived = {};
  let worstGround = 0;
  while ((performance.now() - t0) / 1000 < 560) {
    const now = mine();
    for (const o of now) {
      if (o.staying && arrived[o.name] === undefined) arrived[o.name] = +((performance.now() - t0) / 1000).toFixed(0);
      if (Math.hypot(o.x, o.z) > 380) worstGround = Math.max(worstGround, Math.abs(o.y - E.terrainAt(o.x, o.z)));
    }
    if (now.length === names.length && now.every(o => o.staying)) break;
    await wait(1000);
  }
  out.secondsToPlace = arrived;
  out.worstFeetOffGroundOutsideWall = +worstGround.toFixed(3);
  const staying = mine().filter(o => o.staying);
  out.staying = staying.map(o => {
    const v = E.villagers.find(x => x.name === o.name), p = v.parts;
    return { name: o.name, kind: o.kind, pose: o.pose, rod: o.rod, armsX: p ? +p.leftArm.rotation.x.toFixed(2) : null, headX: p ? +p.headPivot.rotation.x.toFixed(2) : null,
      facingPlace: Math.abs(Math.sin(v.g.rotation.y - Math.atan2(v.outing.face[0] - v.g.position.x, v.outing.face[1] - v.g.position.z))) < 0.05,
      dry: E.waterDepthAt(v.g.position.x, v.g.position.z) <= 0.02 };
  });
  const shots = [];

  // Stand in front of each, a little out from the place they are facing, and talk.
  for (const o of staying) {
    const v = E.villagers.find(x => x.name === o.name), [fx, fz] = v.outing.face;
    const dx = v.g.position.x - fx, dz = v.g.position.z - fz, l = Math.hypot(dx, dz) || 1;
    // Beside them, on the side away from what they face, so nothing else is nearer.
    const px = v.g.position.x + dx / l * 1.8, pz = v.g.position.z + dz / l * 1.8;
    E.player.x = px; E.player.z = pz; E.player.vy = 0; E.player.y = E.terrainAt(px, pz);
    E.look(Math.atan2(-(v.g.position.x - px), -(v.g.position.z - pz)), -0.1);
    await wait(2500);                                                   // let the wilds' own toast pass
    const hint = document.querySelector('#interactHint > span')?.textContent || '';
    const alt = document.getElementById('interactAlt').hidden ? '' : document.querySelector('#interactAlt > span')?.textContent || '';
    key(/^talk/.test(hint) ? 'KeyE' : /^talk/.test(alt) ? 'KeyF' : 'KeyE'); await wait(600);
    const row = { name: o.name, kind: o.kind, hint, alt, opened: document.getElementById('dialoguePanel').classList.contains('open'),
      greeting: (document.getElementById('dialogueLines')?.textContent || '').slice(0, 360) };
    const errand = [...document.querySelectorAll('#dialogueChoices button')].find(b => /doing right now/.test(b.textContent));
    if (errand) { errand.click(); await wait(300); row.errand = (document.getElementById('dialogueLines')?.textContent || '').slice(0, 300); }
    key('Escape'); await wait(500);
    row.stillStayingAfterTalk = E.outings().some(x => x.name === o.name && x.staying);
    out['talk_' + o.kind] = row;
    const sx = v.g.position.x + dx / l * 4.5 + dz / l * 2, sz = v.g.position.z + dz / l * 4.5 - dx / l * 2;
    shots.push({ name: 'outing-' + o.kind, x: sx, z: sz, y: E.terrainAt(sx, sz), yaw: Math.atan2(-(v.g.position.x - sx), -(v.g.position.z - sz)), pitch: -0.1 });
  }

  // With them there: sift the ash, skim a stone.
  const hallEntry = E.interactions.find(i => i.id === 'fallen-hall');
  if (hallEntry && staying.some(o => o.kind === 'hall')) {
    E.player.x = hallEntry.x + 1.5; E.player.z = hallEntry.z + 1.5; await wait(1500);
    hallEntry.act(hallEntry); await wait(200); out.siftToast = toast();
    out.siftNamesVisitor = out.siftToast.includes(staying.find(o => o.kind === 'hall').name);
  }
  const angler = staying.find(o => o.kind === 'angler');
  if (angler) {
    const pondEntry = E.interactions.find(i => i.id === 'foxglove-water');
    E.player.x = pondEntry.x; E.player.z = pondEntry.z; E.player.y = E.terrainAt(pondEntry.x, pondEntry.z);
    const p = E.clearings.find(c => c.id === 'pond');
    E.look(Math.atan2(-(p.x - pondEntry.x), -(p.z - pondEntry.z)), -0.05);
    await wait(1500);
    for (let i = 0; i < 3 && !/skip|gone/.test(toast()); i++) { E.skimStone(); await wait(4500); }
    out.skimToast = toast(); out.skimNamesAngler = out.skimToast.includes(angler.name);
  }
  out.shots = shots;
  if (shotsOnly) return out;

  // The Ember Watch: home again, once each has stayed the minimum.
  E.player.x = 0; E.player.z = 406; E.player.y = 0;
  for (let i = 0; i < 60 && mine().some(o => o.staying && o.stood < 45); i++) await wait(1000);
  const before = mine().filter(o => o.staying);
  const bell = performance.now();
  E.setWatch('ember');
  out.homeward = {};
  while ((performance.now() - bell) / 1000 < 75) {
    for (const b of before) {
      const v = E.villagers.find(x => x.name === b.name), row = E.outings().find(x => x.name === b.name);
      if (out.homeward[b.name] === undefined && !(row && row.kind) && Math.hypot(v.g.position.x - b.spot[0], v.g.position.z - b.spot[1]) > 4)
        out.homeward[b.name] = { kind: b.kind, leftAfter: +((performance.now() - bell) / 1000).toFixed(0), legsHome: row ? row.legs : 0, rodGone: !v.rod, armsX: v.parts ? +v.parts.leftArm.rotation.x.toFixed(2) : null };
    }
    if (before.every(b => out.homeward[b.name] !== undefined)) break;
    await wait(1000);
  }
  out.stillOutAfterBell = before.filter(b => out.homeward[b.name] === undefined).map(b => b.name);
  return out;
})()
