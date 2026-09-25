// r108: drive every place beyond the wall the way a player would, and report
// what each one actually did.
(async () => {
  const E = window.EMBER, T = E.terrainAt, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  const out = {}, toast = () => (document.getElementById('gameToast') || {}).textContent || '';
  const stand = (x, z, yaw, pitch = 0) => { E.player.x = x; E.player.z = z; E.player.y = T(x, z); E.player.vy = 0; E.player.onGround = true; E.look(yaw, pitch); };
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const act = id => { const e = E.interactions.find(i => i.id === id); if (!e) return 'missing'; if (e.act) e.act(e); return toast(); };

  const d0 = E.diagnostics();
  out.interactions = { total: d0.interactions.total, unreachable: d0.interactions.unreachable,
    ids: E.interactions.map(i => i.id).filter(id => !/^grave-/.test(id)), graves: E.interactions.filter(i => /^grave-/.test(i.id)).length };

  // --- the stones: cast a real spell at every one -----------------------------
  const ring = E.wilds.stones;
  E.setWatch('labour'); await wait(300);
  for (let i = 0; i < ring.stones.length; i++) {
    const s = ring.stones[i];
    // stand three metres inside the ring from this stone and throw at it
    const ix = ring.cx + (s.x - ring.cx) * .55, iz = ring.cz + (s.z - ring.cz) * .55;
    stand(ix, iz, face(ix, iz, s.x, s.z), -0.05);
    await wait(120); E.cast(); await wait(700);
  }
  out.stones = { lit: ring.stones.filter(s => s.color).length, answered: ring.answered,
    pillarOpacityAfter2s: null, crystalFlare: ring.crystal && ring.crystal.flare, lastToast: toast() };
  await wait(2000);
  out.stones.pillarOpacityAfter2s = +ring.pillar.material.opacity.toFixed(3);
  out.stones.touch = act('standing-stones');
  E.setWatch('market'); await wait(600);
  out.stones.afterBell = { lit: ring.stones.filter(s => s.color).length, answered: ring.answered };

  // --- the pond: skim a stone from the bank --------------------------------------
  const fox = E.interactions.find(i => i.id === 'foxglove-water');
  stand(fox.x, fox.z, face(fox.x, fox.z, -340, 320), 0);
  out.pond = { interactionToWater: +Math.hypot(fox.x + 340, fox.z - 320).toFixed(1) };
  E.skimStone(); await wait(900);
  out.pond.ripplesMidThrow = document.querySelectorAll ? null : null;
  await wait(4500);
  out.pond.toast = toast();
  stand(fox.x, fox.z, face(fox.x, fox.z, 0, 0), 0);   // facing away from the water
  E.skimStone(); out.pond.facingAway = toast();

  // --- the graveyard: walk in, read a stone, then meet the family ----------------
  const graves = E.wilds.graves, grave = E.interactions.find(i => /^grave-/.test(i.id));
  stand(grave.x, grave.z + 1, 0, 0);
  out.graveyard = { read: act(grave.id), remembered: E.wildMemory().graves.slice() };
  out.graveyard.door = (() => { const e = E.interactions.find(i => i.id === 'mausoleum-door'); return e ? e.text : 'missing'; })();
  const house = E.wildMemory().graves[0];
  const kin = house && E.villagers.find(v => v.household === house && !v.indoors);
  if (kin) {
    const kx = kin.g.position.x, kz = kin.g.position.z;
    stand(kx + 1.2, kz, face(kx + 1.2, kz, kx, kz), 0); await wait(250);
    window.dispatchEvent(new KeyboardEvent('keydown', { code: 'KeyE', bubbles: true }));
    await wait(400);
    const lines = (document.getElementById('dialogueLines') || {}).textContent || '';
    out.graveyard.kinGreeting = { name: kin.name, mentionsGraveyard: /graveyard/.test(lines), excerpt: lines.slice(0, 260) };
    window.dispatchEvent(new KeyboardEvent('keydown', { code: 'Escape', bubbles: true }));
    await wait(200);
  }

  // --- the Fallen Hall: once a watch -----------------------------------------------
  out.hall = { first: act('fallen-hall') };
  out.hall.again = act('fallen-hall');
  E.setWatch('still'); await wait(600);
  out.hall.nextWatch = act('fallen-hall');
  out.hall.remembered = E.wildMemory().hall;

  // --- a waymark -------------------------------------------------------------------------
  out.waymark = act('waymark-0');
  out.errors = window.__probeErrors || null;
  return out;
})()
