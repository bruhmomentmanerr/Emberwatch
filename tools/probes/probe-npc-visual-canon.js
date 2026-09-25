// Clean NPC visual-canon proof. Stages representative residents in open space
// and hides normal UI so screenshots review silhouettes, accessories and event
// acting rather than dialogue chrome. Device/Puffco code is untouched.
(async () => {
  const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER;
  if (!E) return { error: 'EMBER missing' };

  E.setWatch('labour');
  E.setPixel(1);
  await wait(1000);

  const style = document.getElementById('npcVisualCanonCleanCapture') || document.createElement('style');
  style.id = 'npcVisualCanonCleanCapture';
  style.textContent = `
    body.npc-visual-canon-clean #gameTitle,
    body.npc-visual-canon-clean #hint,
    body.npc-visual-canon-clean #interactHint,
    body.npc-visual-canon-clean #gameToast,
    body.npc-visual-canon-clean #sessionRamble,
    body.npc-visual-canon-clean #wayfinder,
    body.npc-visual-canon-clean #dialoguePanel,
    body.npc-visual-canon-clean #stick,
    body.npc-visual-canon-clean #castBtn,
    body.npc-visual-canon-clean #interactBtn,
    body.npc-visual-canon-clean #interactAltBtn,
    body.npc-visual-canon-clean #drop,
    body.npc-visual-canon-clean #gear,
    body.npc-visual-canon-clean #settings,
    body.npc-visual-canon-clean #puffBtn,
    body.npc-visual-canon-clean #strainBtn,
    body.npc-visual-canon-clean #strainPanel,
    body.npc-visual-canon-clean #puffPanel,
    body.npc-visual-canon-clean #btChooser,
    body.npc-visual-canon-clean #loader,
    body.npc-visual-canon-clean #cross {
      opacity: 0 !important;
      visibility: hidden !important;
      pointer-events: none !important;
    }`;
  document.head.append(style);
  document.body.classList.add('npc-visual-canon-clean');

  const villagers = E.villagers.filter(npc => npc && npc.g && npc.parts);
  const used = new Set();
  const pick = (label, test) => {
    const npc = villagers.find(person => !used.has(person) && test(person));
    if (npc) used.add(npc);
    return npc ? { label, npc } : null;
  };
  const picks = [
    pick('glasses-identity', npc => npc.styleTags?.includes('glasses')),
    pick('moon-pale-accent', npc => npc.styleTags?.includes('moonPale')),
    pick('sky-marked-fins', npc => npc.styleTags?.includes('skyMarked')),
    pick('striped-sock-bands', npc => npc.styleTags?.includes('sockBands') && npc.outfit === 'town dress'),
    pick('long-ear-profile', npc => npc.people === 'long-ear'),
    pick('stonekin-profile', npc => npc.people === 'stonekin'),
    pick('mossfolk-profile', npc => npc.people === 'mossfolk'),
    pick('watch-uniform-cuffs', npc => npc.outfit === 'watch uniform')
  ].filter(Boolean);

  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const baseX = -10, baseZ = 106;
  picks.forEach((entry, index) => {
    const x = baseX + (index % 4) * 6.2;
    const z = baseZ + Math.floor(index / 4) * 7.4;
    const y = E.terrainAt ? E.terrainAt(x, z) : 0;
    const npc = entry.npc;
    npc.indoors = false;
    npc.g.visible = true;
    npc.sessionAnchor = { x, z };
    npc.pauseLeft = 60;
    npc.lastX = x;
    npc.lastZ = z;
    npc.g.position.set(x, y, z);
  });

  // Hold the visual-canon meteor witness branch open long enough for the
  // harness' delayed screenshots to catch arms, heads and braced legs.
  if (E.visualCanon?.events) {
    E.visualCanon.events.meteors = true;
    E.visualCanon.events.lastMeteorAt = 1e9;
  }

  await wait(500);
  const shots = picks.map((entry, index) => {
    const npc = entry.npc;
    const distance = 2.05;
    const cx = npc.lastX - distance;
    const cz = npc.lastZ - distance;
    return {
      name: 'npc-canon-' + entry.label,
      x: cx,
      z: cz,
      y: (E.terrainAt ? E.terrainAt(cx, cz) : 0) + 0.08,
      yaw: face(cx, cz, npc.lastX, npc.lastZ),
      pitch: -0.16
    };
  });

  const diag = E.diagnostics();
  return {
    revision: diag.revision,
    visualCanon: diag.visualCanon,
    uiHidden: document.body.classList.contains('npc-visual-canon-clean'),
    staged: picks.map(entry => ({
      label: entry.label,
      name: entry.npc.name,
      people: entry.npc.people,
      bodyType: entry.npc.bodyType,
      outfit: entry.npc.outfit,
      styleTags: entry.npc.styleTags || []
    })),
    shots
  };
})();
