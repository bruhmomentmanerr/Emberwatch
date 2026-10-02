// A lineup, not a street (r143). Residents walk off between the teleport and
// the capture, so a portrait of one in the street is usually of the road
// where they were. This pins one resident per outfit and per people in a row
// on open ground outside the north gate, facing the camera with the moon
// behind it, and photographs the row wide and then face by face.
//
// window.__studio = { names: [...] } photographs those residents instead.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER;
  if (!E) return { error: 'EMBER missing' };
  E.setWatch('labour');
  if (E.sky) { E.sky.rain(0); E.sky.omen(0); }
  await wait(800);
  const style = document.createElement('style');
  style.textContent = 'body.studio *:not(canvas):not(#app):not(body):not(html){visibility:hidden!important}';
  document.head.append(style); document.body.classList.add('studio');

  const V = E.villagers.filter(v => !v.shop && !v.outing && !v.referenceBuild);
  const want = (window.__studio && window.__studio.names) || null;
  let picks = [];
  if (want) picks = want.map(n => E.villagers.find(v => v.name === n)).filter(Boolean);
  else {
    const outfits = ['hooded traveller','layered tunic','watch uniform','artisan apron','road vest','town dress','forge apron','scholar coat'];
    for (const o of outfits) { const v = V.find(p => p.outfit === o && !picks.includes(p)); if (v) picks.push(v); }
    for (let s = 0; s < 5; s++) if (!picks.some(p => p.species === s)) { const v = V.find(p => p.species === s && !picks.includes(p)); if (v) picks.push(v); }
    const roles = E.villagers.filter(v => v.referenceBuild);
    picks.push(...roles);
  }
  const Z = 434, gap = 1.35, x0 = -(picks.length - 1) * gap / 2;
  picks.forEach((npc, i) => {
    const x = x0 + i * gap, y = E.terrainAt(x, Z);
    npc.indoors = false; npc.g.visible = true; npc.atHome = null; npc.stay = null;
    npc.sessionAnchor = { x, z: Z }; npc.pauseLeft = 9999; npc.path = null;
    npc.lastX = x; npc.lastZ = Z; npc.g.position.set(x, y, Z); npc.g.rotation.y = Math.PI;
    if (npc.referenceBuild) npc.activityAnchor = { x, z: Z - 5 };
  });
  await wait(1500);
  const cam = (name, x, z, tx, tz, pitch, lift) => ({ name, x, z, y: E.terrainAt(x, z) + (lift || 0), yaw: Math.atan2(-(tx - x), -(tz - z)), pitch });
  const shots = [
    cam('studio-00-lineup-wide', 0, Z - 9.5, 0, Z, -.08),
    cam('studio-01-lineup-left', x0 + gap * 2, Z - 4.2, x0 + gap * 2, Z, -.14),
    cam('studio-02-lineup-right', -x0 - gap * 2, Z - 4.2, -x0 - gap * 2, Z, -.14)
  ];
  picks.slice(0, 14).forEach((npc, i) => {
    const x = x0 + i * gap;
    shots.push(cam('studio-face-' + String(i + 1).padStart(2, '0') + '-' + npc.outfit.replace(/ /g, '-') + '-' + npc.people, x, Z - 1.55, x, Z, -.05, -.05));
  });
  return { revision: E.diagnostics().revision, picks: picks.map((p, i) => ({ i, name: p.name, outfit: p.outfit, people: p.people, build: p.bodyType, role: p.referenceRole || null, tags: p.styleTags })), shots };
})()
