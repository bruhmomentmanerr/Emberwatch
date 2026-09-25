// r139 reference-build proof. Captures the place-bound NPC roles introduced
// from the supplied frame grammar: not generic resident styling, but people
// anchored to specific map functions.
(async () => {
  const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER;
  if (!E) return { error: 'EMBER missing' };

  E.setWatch('labour');
  E.setPixel(1);
  await wait(1000);

  const style = document.getElementById('referenceBuildCleanCapture') || document.createElement('style');
  style.id = 'referenceBuildCleanCapture';
  style.textContent = `
    body.reference-build-clean #gameTitle,
    body.reference-build-clean #hint,
    body.reference-build-clean #interactHint,
    body.reference-build-clean #gameToast,
    body.reference-build-clean #sessionRamble,
    body.reference-build-clean #wayfinder,
    body.reference-build-clean #dialoguePanel,
    body.reference-build-clean #stick,
    body.reference-build-clean #castBtn,
    body.reference-build-clean #interactBtn,
    body.reference-build-clean #interactAltBtn,
    body.reference-build-clean #drop,
    body.reference-build-clean #gear,
    body.reference-build-clean #settings,
    body.reference-build-clean #puffBtn,
    body.reference-build-clean #strainBtn,
    body.reference-build-clean #strainPanel,
    body.reference-build-clean #puffPanel,
    body.reference-build-clean #btChooser,
    body.reference-build-clean #loader,
    body.reference-build-clean #cross {
      opacity: 0 !important;
      visibility: hidden !important;
      pointer-events: none !important;
    }`;
  document.head.append(style);
  document.body.classList.add('reference-build-clean');

  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const roleOrder = [
    'cliff-watcher',
    'citadel-guard',
    'pilgrim-climber',
    'bridge-resident',
    'mourner',
    'caretaker',
    'ruin-wizard',
    'rain-pilgrim',
    'skywatch-companion',
    'runner-witness'
  ];
  const roles = roleOrder.map(role => E.villagers.find(npc => npc.referenceBuild && npc.referenceRole === role)).filter(Boolean);
  for (const npc of roles) {
    npc.indoors = false;
    npc.g.visible = true;
    npc.sessionAnchor = { x: npc.g.position.x, z: npc.g.position.z };
    npc.pauseLeft = 60;
  }
  await wait(800);

  const shots = roles.map((npc, index) => {
    const tx = npc.g.position.x, tz = npc.g.position.z;
    const source = npc.activityAnchor || { x: tx + Math.sin(npc.g.rotation.y) * 4, z: tz + Math.cos(npc.g.rotation.y) * 4 };
    let dx = source.x - tx, dz = source.z - tz, len = Math.hypot(dx, dz);
    if (len < 0.01) { dx = Math.sin(npc.g.rotation.y); dz = Math.cos(npc.g.rotation.y); len = 1; }
    const side = index % 2 ? 0.9 : -0.9;
    const nx = dx / len, nz = dz / len, sx = -nz, sz = nx;
    const x = tx + nx * 3.1 + sx * side, z = tz + nz * 3.1 + sz * side;
    return {
      name: 'reference-role-' + npc.referenceRole,
      x, z,
      y: (E.terrainAt ? E.terrainAt(x, z) : 0) + 0.15,
      yaw: face(x, z, tx, tz),
      pitch: -0.14
    };
  });

  const diag = E.diagnostics();
  return {
    revision: diag.revision,
    visualCanon: diag.visualCanon,
    uiHidden: document.body.classList.contains('reference-build-clean'),
    roles: roles.map(npc => ({
      name: npc.name,
      role: npc.referenceRole,
      place: npc.referencePlaceId,
      pose: npc.referencePose,
      district: npc.district,
      tags: npc.referenceTags || [],
      outfit: npc.outfit,
      people: npc.people,
      styleTags: npc.styleTags || []
    })),
    shots
  };
})();
