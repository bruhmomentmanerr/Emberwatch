// r113: E takes the closest thing in reach, F the next closest of another kind.
// Stands at a shop counter whose keeper is at work and checks that the hint
// offers both, that E and F reach different things, and that F with nothing
// second on offer does nothing (so a variant's own F binding still hears it).
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-interact-alt.js 20
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = []; addEventListener('error', e => errors.push(String(e.message)));
  const key = code => { const ev = new KeyboardEvent('keydown', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }); dispatchEvent(ev); return ev; };
  const hint = () => ({ shown: getComputedStyle(document.getElementById('interactHint')).display !== 'none',
    e: document.querySelector('#interactHint > span').textContent,
    f: document.getElementById('interactAlt').hidden ? null : document.querySelector('#interactAlt span').textContent });
  const dialogue = () => document.getElementById('dialoguePanel').classList.contains('open');
  const toast = () => document.getElementById('gameToast').textContent;
  await wait(2500);
  E.setWatch('labour'); await wait(35000);           // keepers walk to their counters
  const out = { errors };
  const withKeeper = E.shops.filter(s => s.keeper && !s.keeper.indoors && Math.hypot(s.keeper.g.position.x - s.frontX, s.keeper.g.position.z - s.frontZ) < 2.5);
  out.keepersAtCounters = withKeeper.length;
  let tried = 0;
  for (const shop of withKeeper.slice(0, 8)) {
    tried++;
    const k = shop.keeper.g.position;
    // Between the counter's interaction point and the keeper, so both are in reach.
    E.player.x = (shop.frontX + k.x) / 2; E.player.z = (shop.frontZ + k.z) / 2; E.player.y = 0; E.player.vy = 0;
    await wait(400);
    const h = hint();
    if (!h.f) continue;
    out.shop = shop.name || shop.kind; out.hint = h;
    // F first.
    let before = toast(); key('KeyF'); await wait(250);
    out.fOpenedDialogue = dialogue(); out.fToast = toast() !== before ? toast() : null;
    if (dialogue()) { key('Escape'); await wait(150); }
    before = toast(); key('KeyE'); await wait(250);
    out.eOpenedDialogue = dialogue(); out.eToast = toast() !== before ? toast() : null;
    if (dialogue()) { key('Escape'); await wait(150); }
    out.differ = out.fOpenedDialogue !== out.eOpenedDialogue;
    break;
  }
  out.shopsTried = tried;
  // Nothing second on offer: F is not consumed.
  E.player.x = 0; E.player.z = 560; E.player.y = E.terrainAt(0, 560); await wait(400);
  out.lonelyHint = hint();
  const ev = key('KeyF'); await wait(100);
  out.lonelyFConsumed = ev.defaultPrevented;
  out.mobileAltButton = !!document.getElementById('interactAltBtn');
  return out;
})()
