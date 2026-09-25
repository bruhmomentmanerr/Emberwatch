/* ==========================================================================
   EMBERWATCH — EMBERFALL                                      variant layer
   --------------------------------------------------------------------------
   A survival reading of the same city. You carry one ember. It is your light
   and your clock, and it is always going out.

   The mechanic is built to push you along the roads rather than across the
   map, because the roads are the part of Vaneth that r75-r77 made worth
   walking. Braziers sit on the ring boulevard and the four gate avenues, so
   the safe route is literally the street network — wander off it and you are
   spending ember you cannot get back out there.

   Nothing is lost on death. The braziers you have lit stay lit, for good and
   across sessions, so a run is always net progress and the city gets steadily
   brighter as you learn it. That is the whole arc: the map becomes safe
   because you made it safe.

   Runs on top of the shipped engine through window.EMBER.
   ========================================================================== */
(function () {
  'use strict';

  const STORE     = 'emberwatch.emberfall.v1';
  // r121, after the balance probe played it: the ember read 100% at every one
  // of the 24 braziers a fifteen-minute run lit, because lighting one filled it
  // and five minutes of walking covers a city you can cross in one. It is a
  // clock again. At two and a half minutes of walking it still read 100 at every
  // brazier the probe lit — the braziers are close enough together that the
  // clock never accumulated — so it is a minute and a half: a leg of 200 m
  // costs about a quarter of it. Lighting a brazier gives back a good part of
  // an ember rather than all of it, and sheltering fills slower than it used to.
  const BURN      = 100 / 90;    // full ember lasts a minute and a half of walking
  const RELIGHT   = 45;          // what a newly lit brazier gives back
  const SHELTER   = 5;           // ember a second while standing in a lit pool
  const LIGHT_R   = 5.0;         // how close to start lighting a brazier
  const CHANNEL   = 1.4;         // seconds spent lighting it
  const FOG_CLEAR = 0.007;       // the base game's fog
  const FOG_LOST  = 0.030;       // fog when the ember is dead

  let E, T, hud, braziers = [], state, ember = 100, last = 0, channel = 0, channelling = null,
      playerLight = null, collapsed = false, won = false;

  function boot() {
    if (!window.EMBER || !window.THREE) return setTimeout(boot, 250);
    E = window.EMBER; T = window.THREE;
    try { start(); } catch (err) { console.warn('Emberfall layer failed to start:', err); }
  }

  function start() {
    state = load();
    placeBraziers();
    playerLight = E.lampLight(0xffb45e, 1.7, 26);
    E.scene.add(playerLight);
    // Every Emberfall lamp goes through the base light budget (r115); on their
    // own the 32 braziers and the ember were 33 lights always on.
    if (E.addLamp) { E.addLamp(playerLight); for (const g of braziers) E.addLamp(g.userData.light); }
    // Braziers and the carried ember add lights; compile for them now (r114).
    if (E.warmShaders) E.warmShaders();
    buildHud();
    requestAnimationFrame(loop);
  }

  function load() {
    try { const raw = JSON.parse(localStorage.getItem(STORE) || 'null');
      if (raw && Array.isArray(raw.lit)) return raw; } catch (_) {}
    return { lit: [], runs: 0 };
  }
  function save() { try { localStorage.setItem(STORE, JSON.stringify(state)); } catch (_) {} }

  // --- the braziers ------------------------------------------------------
  // Fixed polar positions on the authored road network, so they land on real
  // paving on every seed and never inside a generated façade.
  // The old wall is at 240 and the ring boulevard at 260. r94 added a second
  // wall at 380 with real quarters between them, so the ember now has to be
  // carried across a city twice the width — three rings of braziers instead of
  // one, and the gate roads run all the way out to the new gates.
  function brazierSites() {
    const sites = [];
    for (let i = 0; i < 8; i++) {                       // the ring boulevard
      const a = (i / 8) * Math.PI * 2 + 0.39;
      sites.push({ id: 'ring' + i, x: Math.cos(a) * 260, z: Math.sin(a) * 260, where: 'the ring boulevard' });
    }
    for (let i = 0; i < 8; i++) {                       // the outer ring street
      const a = (i / 8) * Math.PI * 2 + 0.78;
      sites.push({ id: 'outer' + i, x: Math.cos(a) * 316, z: Math.sin(a) * 316, where: 'the outer ring' });
    }
    [0, 90, 180, 270].forEach((deg, k) => {             // the four gate roads, in and out
      const a = deg * Math.PI / 180;
      sites.push({ id: 'gate' + k + 'a', x: Math.cos(a) * 196, z: Math.sin(a) * 196, where: 'the ' + compass(deg) + ' gate road' });
      sites.push({ id: 'gate' + k + 'b', x: Math.cos(a) * 104, z: Math.sin(a) * 104, where: 'the ' + compass(deg) + ' avenue' });
      sites.push({ id: 'gate' + k + 'c', x: Math.cos(a) * 356, z: Math.sin(a) * 356, where: 'the new ' + compass(deg) + ' gate' });
    });
    [45, 135, 225, 315].forEach((deg, k) => {           // the diagonal avenues
      const a = deg * Math.PI / 180;
      sites.push({ id: 'diag' + k, x: Math.cos(a) * 294, z: Math.sin(a) * 294, where: 'a crossing in the new quarters' });
    });
    return sites;
  }
  const compass = d => ({ 0: 'eastern', 90: 'northern', 180: 'western', 270: 'southern' }[d]);

  function placeBraziers() {
    const bowl = new T.CylinderGeometry(0.95, 0.62, 0.72, 8);
    const stem = new T.CylinderGeometry(0.26, 0.34, 1.15, 6);
    const fire = new T.ConeGeometry(0.62, 1.5, 6);
    const stone = new T.MeshStandardMaterial({ color: 0x4a4550, roughness: 1, flatShading: true });
    const dead  = new T.MeshStandardMaterial({ color: 0x241d1a, roughness: 1, flatShading: true });
    const flame = new T.MeshStandardMaterial({ color: 0x000000, emissive: 0xff9a3c, emissiveIntensity: 2.3, flatShading: true });

    for (const site of brazierSites()) {
      const g = new T.Group();
      const s = new T.Mesh(stem, stone);  s.position.y = 0.58; g.add(s);
      const b = new T.Mesh(bowl, stone);  b.position.y = 1.3;  g.add(b);
      const f = new T.Mesh(fire, flame);  f.position.y = 2.1;  g.add(f);
      const coal = new T.Mesh(new T.IcosahedronGeometry(0.5, 0), dead); coal.position.y = 1.45; g.add(coal);
      const light = E.lampLight(0xffa347, 0, 34); light.position.y = 2.2; g.add(light);
      g.position.set(site.x, 0, site.z);
      g.userData = { site, flame: f, coal, light, phase: Math.random() * 6.28 };
      E.scene.add(g); braziers.push(g);
      setLit(g, state.lit.includes(site.id));
    }
  }

  function setLit(g, on) {
    g.userData.on = on;
    g.userData.flame.visible = on;
    g.userData.coal.visible = !on;
    g.userData.light.intensity = (on ? 1.5 : 0) * g.userData.light.userData.lampScale;
  }

  // --- loop --------------------------------------------------------------
  function loop(now) {
    requestAnimationFrame(loop);
    const dt = Math.min(0.05, (now - last) / 1000 || 0); last = now;
    if (!dt) return;

    // Standing in a lit brazier's pool holds the ember steady — that is what
    // makes a lit road a road you can actually use.
    let sheltered = false, nearest = null, nearestD = Infinity;
    for (const g of braziers) {
      const d = Math.hypot(E.player.x - g.position.x, E.player.z - g.position.z);
      if (g.userData.on) {
        if (d < 13) sheltered = true;
        g.userData.phase += dt * 6;
        g.userData.flame.scale.setScalar(0.88 + Math.sin(g.userData.phase) * 0.13);
        g.userData.light.intensity = (1.35 + Math.sin(g.userData.phase * 0.7) * 0.25) * g.userData.light.userData.lampScale;
      } else if (d < nearestD) { nearestD = d; nearest = g; }
    }

    if (!collapsed) {
      // BURN is per second: a full ember is 300 seconds of walking.
      if (sheltered) ember = Math.min(100, ember + dt * SHELTER);
      else ember = Math.max(0, ember - BURN * dt);
      if (ember <= 0) collapse();
    }

    // lighting a brazier
    if (!collapsed && nearest && nearestD < LIGHT_R) {
      if (channelling !== nearest) { channelling = nearest; channel = 0; }
      channel += dt;
      if (channel >= CHANNEL) {
        setLit(nearest, true);
        state.lit.push(nearest.userData.site.id); save();
        ember = Math.min(100, ember + RELIGHT);
        flash('You set the brazier at ' + nearest.userData.site.where + ' burning.');
        channelling = null; channel = 0;
        if (state.lit.length >= braziers.length && !won) victory();
      }
    } else { channelling = null; channel = 0; }

    // Carried at 3.2 and converted at a fixed range of 8, which makes a full
    // ember about as bright as walking under a street lantern. Converted at its
    // live range (up to 32) it came out a blinding disc at the player's feet:
    // physical light falls off with the square of distance, and the ember sits
    // closer to the ground than any lamp in the city.
    playerLight.position.set(E.player.x, 3.2, E.player.z);
    const glow = Math.max(0, ember / 100);
    playerLight.intensity = E.lampPower(0.35 + glow * 1.9, 8);
    playerLight.distance = (10 + glow * 22) * E.LAMP_REACH;
    if (E.scene.fog) E.scene.fog.density = FOG_LOST + (FOG_CLEAR - FOG_LOST) * glow;

    paint(sheltered, nearest, nearestD);
  }

  function collapse() {
    collapsed = true; state.runs++; save();
    flash('The ember dies. The cold has you.');
    hud.veil.style.opacity = '1';
    setTimeout(() => {
      E.player.x = 0; E.player.z = 266; E.player.y = 0; E.player.vy = 0;
      ember = 60; collapsed = false; hud.veil.style.opacity = '0';
      flash('You wake at the gate with a half ember. The braziers you lit still burn.');
    }, 2400);
  }

  function victory() {
    won = true;
    flash('Every brazier in Vaneth is lit. The night is held.');
    hud.win.style.opacity = '1';
    setTimeout(() => { hud.win.style.opacity = '0'; }, 7000);
  }

  // --- HUD ---------------------------------------------------------------
  function buildHud() {
    const css = document.createElement('style');
    css.textContent = `
      #efHud{position:fixed;right:12px;top:96px;z-index:22;width:min(232px,calc(100vw - 24px));
        padding:10px 12px;border:1px solid rgba(196,124,60,.45);border-radius:8px;
        background:linear-gradient(150deg,rgba(30,21,14,.96),rgba(13,9,7,.97));
        box-shadow:0 16px 40px rgba(0,0,0,.6);font-family:system-ui,sans-serif;color:#f0e0cc;pointer-events:none}
      .ef-lab{font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:#d19a5c;opacity:.9}
      .ef-bar{height:8px;border-radius:4px;background:rgba(255,255,255,.08);overflow:hidden;margin-top:5px}
      .ef-fill{height:100%;background:linear-gradient(90deg,#ff7a2f,#ffd48a);transition:width .15s}
      .ef-fill.low{background:linear-gradient(90deg,#8a2b16,#d1552a)}
      .ef-row{display:flex;justify-content:space-between;margin-top:9px;font-size:11px;color:#dcc9b2}
      .ef-row b{color:#fff1dd;font-weight:600}
      .ef-chan{margin-top:8px;font-size:10.5px;color:#ffc98a;min-height:14px}
      .ef-hint{margin-top:7px;font-size:9px;color:#9c8975;line-height:1.5}
      #efVeil{position:fixed;inset:0;z-index:39;background:radial-gradient(circle,rgba(10,6,20,.35),rgba(0,0,0,.97));
        opacity:0;transition:opacity 1s;pointer-events:none}
      #efWin{position:fixed;inset:0;z-index:38;background:radial-gradient(circle,rgba(255,170,80,.16),transparent 60%);
        opacity:0;transition:opacity 1.4s;pointer-events:none}
      #efFlash{position:fixed;left:50%;top:23%;transform:translateX(-50%);z-index:41;padding:10px 18px;
        border:1px solid rgba(219,150,80,.5);border-radius:8px;background:rgba(22,14,9,.94);
        color:#ffe6c6;font-size:13px;opacity:0;transition:opacity .4s;pointer-events:none;font-family:Georgia,serif}
      #efFlash.on{opacity:1}`;
    document.head.appendChild(css);
    const root = document.createElement('div');
    root.id = 'efHud';
    root.innerHTML = `<div class="ef-lab">Ember</div>
      <div class="ef-bar"><div class="ef-fill" id="efFill"></div></div>
      <div class="ef-row"><span>Braziers lit</span><span><b id="efLit">0</b> / <span id="efTot">0</span></span></div>
      <div class="ef-row"><span>Nearest unlit</span><span><b id="efNear">—</b></span></div>
      <div class="ef-chan" id="efChan"></div>
      <div class="ef-hint">Stand by a lit brazier to hold the ember steady. Walk up to a dark one to set it burning — it stays lit for good.</div>`;
    document.body.appendChild(root);
    const veil = document.createElement('div'); veil.id = 'efVeil'; document.body.appendChild(veil);
    const win  = document.createElement('div'); win.id  = 'efWin';  document.body.appendChild(win);
    const fl   = document.createElement('div'); fl.id   = 'efFlash'; document.body.appendChild(fl);
    hud = { fill: root.querySelector('#efFill'), lit: root.querySelector('#efLit'),
            tot: root.querySelector('#efTot'), near: root.querySelector('#efNear'),
            chan: root.querySelector('#efChan'), veil, win, flash: fl };
    hud.tot.textContent = brazierSites().length;
  }

  function paint(sheltered, nearest, nearestD) {
    if (!hud) return;
    hud.fill.style.width = Math.max(0, Math.min(100, ember)) + '%';
    hud.fill.className = 'ef-fill' + (ember < 30 ? ' low' : '');
    hud.lit.textContent = state.lit.length;
    hud.near.textContent = nearest ? Math.round(nearestD) + ' paces' : 'none left';
    hud.chan.textContent = channelling
      ? 'lighting… ' + Math.round(100 * channel / CHANNEL) + '%'
      : (sheltered ? 'sheltered — the ember steadies' : '');
  }

  function flash(text) {
    hud.flash.textContent = text; hud.flash.classList.add('on');
    setTimeout(() => hud.flash.classList.remove('on'), 3000);
  }

  // Booted last on purpose. window.EMBER already exists by the time this
  // layer is injected, so boot() runs start() synchronously — called from the
  // top of the module it reached consts further down before they were
  // initialised and died in the temporal dead zone.
  boot();
})();
