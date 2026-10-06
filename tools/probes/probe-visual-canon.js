// Visual-canon proof points for r135 follow-on work.
// The harness screenshots are canon proof, not UI review, so this probe hides
// normal DOM chrome before it returns shot positions. Puffco/Switch/device
// code is untouched; this only changes the test page's CSS state.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER;
  if (!E) return { error: 'EMBER missing' };
  E.setWatch('still');
  E.setPixel(1);
  // Since r143 rain and the omen come and go on the clock, and jumping straight
  // to the Still Hours lands on an omen night. Pin both off so every run of
  // this probe photographs the same sky.
  if (E.sky) { E.sky.rain(0); E.sky.omen(0); }
  await wait(900);

  const style = document.getElementById('visualCanonCleanCapture') || document.createElement('style');
  style.id = 'visualCanonCleanCapture';
  style.textContent = `
    body.visual-canon-clean #gameTitle,
    body.visual-canon-clean #hint,
    body.visual-canon-clean #interactHint,
    body.visual-canon-clean #gameToast,
    body.visual-canon-clean #sessionRamble,
    body.visual-canon-clean #wayfinder,
    body.visual-canon-clean #dialoguePanel,
    body.visual-canon-clean #stick,
    body.visual-canon-clean #castBtn,
    body.visual-canon-clean #interactBtn,
    body.visual-canon-clean #interactAltBtn,
    body.visual-canon-clean #drop,
    body.visual-canon-clean #gear,
    body.visual-canon-clean #settings,
    body.visual-canon-clean #puffBtn,
    body.visual-canon-clean #strainBtn,
    body.visual-canon-clean #strainPanel,
    body.visual-canon-clean #puffPanel,
    body.visual-canon-clean #btChooser,
    body.visual-canon-clean #loader,
    body.visual-canon-clean #cross {
      opacity: 0 !important;
      visibility: hidden !important;
      pointer-events: none !important;
    }`;
  document.head.append(style);
  document.body.classList.add('visual-canon-clean');

  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const canon = E.visualCanon || { captures: [], authored: [] };
  const required = [
    'vista-lower-town-overlook',
    'route-cliff-citadel-ascent',
    'vista-river-bridge-castle',
    'site-memorial-field',
    'vista-ruin-waterfall',
    'site-ritual-circle',
    'site-quiet-companion-skywatch',
    'site-rain-oath'
  ];
  const shots = canon.captures.map(c => ({
    name: c.id,
    x: c.x,
    z: c.z,
    y: c.y,
    yaw: Number.isFinite(c.yaw) ? c.yaw : face(c.x, c.z, 0, 0),
    pitch: c.pitch ?? -0.08,
    fov: c.fov,
    target: c.target
  }));
  const authoredByType = {};
  for (const item of canon.authored) authoredByType[item.type] = (authoredByType[item.type] || 0) + 1;
  const diag = E.diagnostics();
  return {
    revision: diag.revision,
    layoutVersion: diag.world.layoutVersion,
    visualCanon: diag.visualCanon,
    health: {
      uiHidden: document.body.classList.contains('visual-canon-clean'),
      missingCaptures: required.filter(id => !canon.captures.some(c => c.id === id)),
      authoredByType
    },
    authored: canon.authored.map(item => ({ type: item.type, id: item.id, x: item.x, z: item.z })),
    shots
  };
})();
