// Is The Long Night balanced? Its claim is that lamplight burns wraiths, so the
// lit streets are the safe ones and stepping off them costs something. This
// plays three stretches of two and a half minutes each and measures whether
// that is true:
//
//   1. under a street lantern, fighting back at a human rate (about 2.5 casts
//      a second — the layer has no cooldown, so a mashed key proves nothing);
//   2. out in the dark between the walls, fighting back the same way;
//   3. out in the dark, not fighting at all — the raw pressure.
//
// It also stands in the citadel quarter for half a minute, where the layer says
// nothing spawns.
//
//   HARNESS_TIMEOUT=900 app/node_modules/.bin/electron tools/harness \
//     variants/emberwatch_long-night.html tools/probes/probe-balance-longnight.js 15
//
// Numbers to read: deaths and minVitality per stretch, kills, the wave reached,
// and how much worse the dark is than the lit street.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = [];
  addEventListener('error', e => errors.push(String(e.message).slice(0, 200)));
  const castKey = () => dispatchEvent(new KeyboardEvent('keydown', { code: 'KeyF', key: 'f', bubbles: true, cancelable: true }));
  const vit = () => parseFloat(document.getElementById('lnFill').style.width) || 0;
  const wave = () => Number(document.getElementById('lnWave').textContent) || 0;
  const kills = () => Number(document.getElementById('lnKills').textContent) || 0;
  const alive = () => Number(document.getElementById('lnAlive').textContent) || 0;
  const flash = () => document.getElementById('lnFlash')?.textContent || '';
  const wraiths = () => { const out = []; E.scene.traverse(o => { if (o.userData && typeof o.userData.hp === 'number' && o.userData.core) out.push(o); }); return out; };

  const out = { revision: E.diagnostics().revision, title: document.title, errors };
  if (!document.getElementById('lnFill')) { out.note = 'no vitality bar — is this The Long Night?'; return out; }

  // A lantern to stand under, and a dark spot between the walls, both away from
  // the citadel quarter the layer keeps clear (SAFE_RADIUS 120).
  const lamps = [];
  E.scene.traverse(o => { if (o.isPointLight && o.position.y > 3 && o.position.y < 5 && Math.hypot(o.position.x, o.position.z) > 150) lamps.push(o); });
  const lamp = lamps.sort((a, b) => Math.hypot(a.position.x, a.position.z) - Math.hypot(b.position.x, b.position.z))[0];
  const darkAt = (() => {
    for (let r = 300; r <= 350; r += 10) for (let deg = 0; deg < 360; deg += 7) {
      const a = deg * Math.PI / 180, x = Math.cos(a) * r, z = Math.sin(a) * r;
      if (E.onRoad(x, z, 0)) continue;                                   // a road is a lit road
      let clear = true;
      for (const l of lamps) if (Math.hypot(l.position.x - x, l.position.z - z) < 26) { clear = false; break; }
      if (clear) return { x, z };
    }
    return { x: 318, z: 318 };
  })();
  out.lamp = lamp ? { x: +lamp.position.x.toFixed(0), z: +lamp.position.z.toFixed(0) } : null;
  out.darkSpot = { x: Math.round(darkAt.x), z: Math.round(darkAt.z) };

  const stand = (x, z) => { E.player.x = x; E.player.z = z; E.player.y = E.terrainAt ? E.terrainAt(x, z) : 0; E.player.vy = 0; };

  // One stretch: stand still, look at whatever is nearest, cast or do not.
  async function stretch(name, at, seconds, fight) {
    stand(at.x, at.z);
    await wait(1200);
    const startKills = kills(), t0 = performance.now();
    let deaths = 0, minVit = 100, contact = 0, aliveSum = 0, samples = 0, lastFlash = '', castAt = 0;
    let touchedWave = null, hurtAt = null;
    while ((performance.now() - t0) / 1000 < seconds) {
      const near = wraiths().map(w => ({ w, d: Math.hypot(w.position.x - E.player.x, w.position.z - E.player.z) })).sort((a, b) => a.d - b.d)[0];
      if (near) {
        E.look(Math.atan2(-(near.w.position.x - E.player.x), -(near.w.position.z - E.player.z)), -0.05);
        if (fight && near.d < 46 && performance.now() - castAt > 400) { castKey(); castAt = performance.now(); }
        if (near.d < 2.4) contact += 0.2;
      }
      const v = vit(); if (v < minVit) minVit = v;
      if (v < 100 && hurtAt === null) { hurtAt = +((performance.now() - t0) / 1000).toFixed(0); touchedWave = wave(); }
      aliveSum += alive(); samples++;
      const message = flash();
      if (message && message !== lastFlash) { lastFlash = message; if (/dark takes you/.test(message)) { deaths++; minVit = 0; } }
      await wait(200);
      // Death walks you back to the gate; return to the stretch's own ground.
      if (Math.hypot(E.player.x - at.x, E.player.z - at.z) > 12) { await wait(2500); stand(at.x, at.z); }
    }
    return { seconds, deaths, minVitality: Math.round(minVit), kills: kills() - startKills, wave: wave(),
      secondsInContact: +contact.toFixed(1), averageAbroad: +(aliveSum / Math.max(1, samples)).toFixed(1),
      firstTouchedAtWave: touchedWave, firstHurtAfterSeconds: hurtAt };
  }

  out.citadelQuarter = await stretch('citadel', { x: 0, z: 40 }, 30, false);
  out.litStreetFighting = await stretch('lit', lamp ? { x: lamp.position.x, z: lamp.position.z } : { x: 0, z: 260 }, 180, true);
  // Long enough to find the wave where it stops being free: at 150 s the waves
  // only reached 6, and nothing had laid a hand on the player (r121).
  out.darkFightingLong = await stretch('dark', darkAt, 420, true);
  out.darkNotFighting = await stretch('dark, hands down', darkAt, 120, false);
  out.finalWave = wave();
  out.totalKills = kills();
  return out;
})()
