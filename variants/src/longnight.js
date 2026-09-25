/* ==========================================================================
   EMBERWATCH — THE LONG NIGHT                                 variant layer
   --------------------------------------------------------------------------
   The base game has a cast button that does nothing but look good. This
   variant asks what Vaneth is like if the dark pushes back.

   Design constraints kept deliberately tight, because the thing worth
   protecting about Emberwatch is its mood:
     - Wraiths drift, they do not charge. Being caught is a slow mistake, not
       a reflex failure.
     - They never spawn in your line of sight, and never inside the inner
       city. The lit centre stays a refuge; the empty wards get dangerous.
     - Death costs you the walk back, nothing else. No lost progress.
     - Lamplight genuinely protects: a wraith inside a lantern's pool burns.
   Wraiths float, so they need no collision and cannot get stuck on the city.

   Runs on top of the shipped engine through window.EMBER; it adds meshes and
   a HUD and touches no world geometry.
   ========================================================================== */
(function () {
  'use strict';

  const MAX_ALIVE   = 14;
  const SPAWN_MIN   = 46;     // never closer than this
  const SPAWN_MAX   = 92;
  const SAFE_RADIUS = 120;    // the citadel and the old quarter stay a refuge
  const TOUCH       = 2.4;
  const DRAIN       = 17;     // vitality per second in contact
  const REGEN       = 2.6;    // vitality per second out of contact
  const BOLT_RANGE  = 46;
  const BOLT_ARC    = 0.30;   // radians of forgiveness on the aim cone
  const LAMP_BURN   = 9.5;    // wraith HP per second inside a lantern pool
  // r121, after the balance probe played it: standing still and casting as fast
  // as the key repeats cleared everything the night could send and never lost a
  // point of vitality, in the dark as readily as under a lantern — so the lamps
  // meant nothing and the dark was simply the better hunting. A bolt now has to
  // be drawn (CAST_EVERY), and the lit street thins what comes: fewer abroad
  // while you stand in a lantern's pool, and longer between them.
  const CAST_EVERY  = 0.7;    // seconds between bolts
  const LAMP_NEAR   = 9;      // standing this close to a lantern is standing in the light
  const LIT_ALIVE   = 8;      // how many may be abroad while you do
  const LIT_SPAWN   = 1.9;    // and how much longer the next one takes

  let E, T, hud, wraiths = [], lamps = [], bolts = [];
  let vit = 100, kills = 0, wave = 1, waveKills = 0, dead = false, last = 0, spawnTimer = 0, lastCast = -9;
  let shared = null;
  // Wraith light comes from a fixed set of lamps handed to the nearest wraiths
  // each frame, not one lamp per wraith. three.js compiles a shader program for
  // every distinct number of lights in view, so a light born and killed with
  // each wraith recompiled the city's materials all through the first waves:
  // a four-minute soak (r113) logged 120 new programs and stalls of up to 3.5 s
  // on the harness. A dark lamp still counts, so the count never changes.
  const WRAITH_LIGHTS = 4;
  let wraithLights = [];

  function boot() {
    if (!window.EMBER || !window.THREE) return setTimeout(boot, 250);
    E = window.EMBER; T = window.THREE;
    try { start(); } catch (err) { console.warn('Long Night layer failed to start:', err); }
  }

  function start() {
    E.scene.traverse(o => { if (o.isPointLight && o.position.y > 3 && o.position.y < 5) lamps.push(o); });
    // One geometry and one material set, shared by every wraith — the base game
    // batches obsessively and it would be rude to undo that with 14 of these.
    shared = {
      body:  new T.ConeGeometry(0.62, 2.5, 6),
      core:  new T.IcosahedronGeometry(0.3, 0),
      shell: new T.MeshStandardMaterial({ color: 0x1b1430, emissive: 0x2b1d54, emissiveIntensity: 0.75,
                                          transparent: true, opacity: 0.82, flatShading: true }),
      glow:  new T.MeshStandardMaterial({ color: 0x000000, emissive: 0xb07bff, emissiveIntensity: 2.1, flatShading: true }),
      bolt:  new T.MeshStandardMaterial({ color: 0x000000, emissive: 0xffd08a, emissiveIntensity: 2.4, flatShading: true }),
      boltG: new T.IcosahedronGeometry(0.22, 0)
    };
    for (let i = 0; i < WRAITH_LIGHTS; i++) { const l = E.lampLight(0x9a6bff, 0, 9); E.scene.add(l); wraithLights.push(l); if (E.addLamp) E.addLamp(l); }
    // A hidden wraith and bolt, so their materials are compiled with everything
    // else instead of on the first spawn and the first strike (r114).
    const sample = new T.Group(); sample.visible = false;
    sample.add(new T.Mesh(shared.body, shared.shell), new T.Mesh(shared.core, shared.glow), new T.Mesh(shared.boltG, shared.bolt));
    E.scene.add(sample);
    if (E.warmShaders) E.warmShaders();
    buildHud();
    // onAttack(always) took the MouseEvent as "always", so the pointer-lock
    // guard never applied and clicking the menu fired a bolt (r114 audit).
    addEventListener('mousedown', () => onAttack(false));
    addEventListener('keydown', e => { if (e.key === 'f' || e.key === 'F') onAttack(true); });
    const castBtn = document.getElementById('castBtn');
    if (castBtn) castBtn.addEventListener('click', () => onAttack(true));
    requestAnimationFrame(loop);
  }

  const pdist = (x, z) => Math.hypot(E.player.x - x, E.player.z - z);

  // --- spawning ----------------------------------------------------------
  function spawn() {
    if (wraiths.length >= MAX_ALIVE) return;
    const fwd = forward();
    for (let attempt = 0; attempt < 12; attempt++) {
      const a = Math.random() * Math.PI * 2;
      const d = SPAWN_MIN + Math.random() * (SPAWN_MAX - SPAWN_MIN);
      const x = E.player.x + Math.cos(a) * d, z = E.player.z + Math.sin(a) * d;
      if (Math.hypot(x, z) < SAFE_RADIUS) continue;                 // the centre stays safe
      if (Math.hypot(x, z) > 400) continue;                         // and they keep off the mountains
      // Not in front of you: appearing in view is cheap and breaks the mood.
      const toX = (x - E.player.x) / d, toZ = (z - E.player.z) / d;
      if (toX * fwd.x + toZ * fwd.z > 0.15) continue;
      make(x, z); return;
    }
  }

  function make(x, z) {
    const g = new T.Group();
    const body = new T.Mesh(shared.body, shared.shell); body.position.y = 1.25; g.add(body);
    const core = new T.Mesh(shared.core, shared.glow);  core.position.y = 1.55; g.add(core);
    g.position.set(x, 0, z);
    // Still slower than a walk at every wave — you can always leave — but by
    // the late waves they close while you are drawing the next bolt (r121).
    g.userData = { hp: 26 + wave * 5, phase: Math.random() * 6.28, speed: 1.5 + Math.random() * 0.9 + wave * 0.12, core };
    E.scene.add(g); wraiths.push(g);
  }

  function forward() {
    const v = new T.Vector3(); E.camera.getWorldDirection(v);
    const len = Math.hypot(v.x, v.z) || 1; return { x: v.x / len, z: v.z / len };
  }

  // --- attacking ---------------------------------------------------------
  // Mouse clicks require pointer lock, so a click on a panel is not a swing.
  // The F key and the touch cast button never do — if pointer lock is refused
  // by the browser or the platform, a mouse-only guard would leave you unable
  // to fight at all.
  function onAttack(always) {
    if (dead) return;
    if (!always && !document.pointerLockElement) return;
    const at = performance.now() / 1000;
    if (at - lastCast < CAST_EVERY) return;                          // the bolt has to be drawn
    const fwd = forward();
    let best = null, bestScore = Infinity;
    for (const w of wraiths) {
      const dx = w.position.x - E.player.x, dz = w.position.z - E.player.z;
      const d = Math.hypot(dx, dz);
      if (d > BOLT_RANGE || d < 0.4) continue;
      const dot = (dx / d) * fwd.x + (dz / d) * fwd.z;
      const off = Math.acos(Math.max(-1, Math.min(1, dot)));
      if (off > BOLT_ARC) continue;
      if (off * 40 + d < bestScore) { bestScore = off * 40 + d; best = w; }
    }
    if (!best) return;
    lastCast = at;
    const b = new T.Mesh(shared.boltG, shared.bolt);
    b.position.set(E.player.x, 1.5, E.player.z);
    b.userData = { target: best, t: 0 };
    E.scene.add(b); bolts.push(b);
  }

  function damage(w, amount) {
    w.userData.hp -= amount;
    if (w.userData.hp <= 0) {
      E.scene.remove(w); wraiths = wraiths.filter(o => o !== w);
      kills++; waveKills++;
      if (waveKills >= 6 + wave * 2) { wave++; waveKills = 0; flash('The night deepens — wave ' + wave); }
    }
  }

  // --- loop --------------------------------------------------------------
  function loop(now) {
    requestAnimationFrame(loop);
    const dt = Math.min(0.05, (now - last) / 1000 || 0); last = now;
    if (!dt) return;

    if (!dead) {
      spawnTimer -= dt;
      if (spawnTimer <= 0) {
        // Under a lantern the night sends fewer, and slower. That is the whole
        // reason to keep to the lit streets (r121).
        const inLight = lamps.some(l => pdist(l.position.x, l.position.z) < LAMP_NEAR);
        if (!(inLight && wraiths.length >= LIT_ALIVE)) spawn();
        spawnTimer = Math.max(0.7, 3.4 - wave * 0.18) * (inLight ? LIT_SPAWN : 1);
      }
    }

    // The nearest wraiths carry the lamps.
    const near = wraiths.slice().sort((a, b) => pdist(a.position.x, a.position.z) - pdist(b.position.x, b.position.z));
    wraithLights.forEach((l, i) => {
      const w = near[i];
      if (!w) { l.intensity = 0; return; }
      l.position.set(w.position.x, w.position.y + 1.6, w.position.z);
      l.intensity = 0.85 * l.userData.lampScale;
    });

    let touching = false;
    for (const w of wraiths) {
      const dx = E.player.x - w.position.x, dz = E.player.z - w.position.z;
      const d = Math.hypot(dx, dz) || 1;
      if (!dead && d > TOUCH * 0.6) {
        const s = w.userData.speed * dt;
        w.position.x += (dx / d) * s; w.position.z += (dz / d) * s;
      }
      w.userData.phase += dt * 2.1;
      w.position.y = Math.sin(w.userData.phase) * 0.22;
      w.rotation.y += dt * 0.7;
      w.userData.core.scale.setScalar(1 + Math.sin(w.userData.phase * 2) * 0.18);
      if (d < TOUCH) touching = true;
      // Lamplight burns them. This is the whole reason to keep to lit streets.
      for (const l of lamps) {
        if (Math.hypot(l.position.x - w.position.x, l.position.z - w.position.z) < 6.5) { damage(w, LAMP_BURN * dt); break; }
      }
    }

    for (const b of bolts.slice()) {
      const w = b.userData.target;
      if (!w || !w.parent) { E.scene.remove(b); bolts = bolts.filter(o => o !== b); continue; }
      const dx = w.position.x - b.position.x, dy = (w.position.y + 1.4) - b.position.y, dz = w.position.z - b.position.z;
      const d = Math.hypot(dx, dy, dz);
      if (d < 1.1) { damage(w, 22); E.scene.remove(b); bolts = bolts.filter(o => o !== b); continue; }
      const s = 58 * dt;
      b.position.x += (dx / d) * s; b.position.y += (dy / d) * s; b.position.z += (dz / d) * s;
      b.userData.t += dt;
      if (b.userData.t > 3) { E.scene.remove(b); bolts = bolts.filter(o => o !== b); }
    }

    if (!dead) {
      vit += (touching ? -DRAIN : REGEN) * dt;
      vit = Math.max(0, Math.min(100, vit));
      if (vit <= 0) die();
    }
    paint(touching);
  }

  function die() {
    dead = true;
    flash('The dark takes you. You wake at the gate.');
    hud.veil.style.opacity = '1';
    setTimeout(() => {
      for (const w of wraiths) E.scene.remove(w);
      wraiths = [];
      E.player.x = 0; E.player.z = 266; E.player.y = 0; E.player.vy = 0;
      vit = 100; wave = Math.max(1, wave - 1); waveKills = 0; dead = false;
      hud.veil.style.opacity = '0';
    }, 2100);
  }

  // --- HUD ---------------------------------------------------------------
  function buildHud() {
    const css = document.createElement('style');
    css.textContent = `
      #lnHud{position:fixed;right:12px;top:96px;z-index:22;width:min(224px,calc(100vw - 24px));
        padding:10px 12px;border:1px solid rgba(150,110,190,.45);border-radius:8px;
        background:linear-gradient(150deg,rgba(22,17,34,.95),rgba(10,8,16,.97));
        box-shadow:0 16px 40px rgba(0,0,0,.6);font-family:system-ui,sans-serif;color:#e4dcf5;pointer-events:none}
      .ln-lab{font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:#a58fd0;opacity:.85}
      .ln-bar{height:7px;border-radius:4px;background:rgba(255,255,255,.09);overflow:hidden;margin-top:5px}
      .ln-fill{height:100%;width:100%;background:linear-gradient(90deg,#d0554f,#f0a06a);transition:width .12s}
      .ln-fill.hurt{background:linear-gradient(90deg,#ff4d4d,#ff9d5c)}
      .ln-row{display:flex;justify-content:space-between;margin-top:9px;font-size:11px;color:#cfc3e8}
      .ln-row b{color:#f3ecff;font-weight:600}
      .ln-hint{margin-top:8px;font-size:9px;color:#8a7fa8;line-height:1.5}
      #lnVeil{position:fixed;inset:0;z-index:39;background:radial-gradient(circle,rgba(40,0,20,.2),rgba(0,0,0,.96));
        opacity:0;transition:opacity .8s;pointer-events:none}
      #lnFlash{position:fixed;left:50%;top:24%;transform:translateX(-50%);z-index:41;padding:10px 18px;
        border:1px solid rgba(176,123,255,.5);border-radius:8px;background:rgba(16,11,26,.94);
        color:#e9dcff;font-size:13px;opacity:0;transition:opacity .4s;pointer-events:none;font-family:Georgia,serif}
      #lnFlash.on{opacity:1}
      #lnEdge{position:fixed;inset:0;z-index:20;pointer-events:none;opacity:0;transition:opacity .2s;
        box-shadow:inset 0 0 120px 20px rgba(190,40,60,.55)}`;
    document.head.appendChild(css);
    const root = document.createElement('div');
    root.id = 'lnHud';
    root.innerHTML = `<div class="ln-lab">Vitality</div>
      <div class="ln-bar"><div class="ln-fill" id="lnFill"></div></div>
      <div class="ln-row"><span>Wave <b id="lnWave">1</b></span><span><b id="lnKills">0</b> banished</span></div>
      <div class="ln-row"><span>Abroad</span><span><b id="lnAlive">0</b></span></div>
      <div class="ln-hint">Click or F to strike. Lamplight burns them — the lit streets are safe, the dark wards are not.</div>`;
    document.body.appendChild(root);
    const veil = document.createElement('div'); veil.id = 'lnVeil'; document.body.appendChild(veil);
    const edge = document.createElement('div'); edge.id = 'lnEdge'; document.body.appendChild(edge);
    const fl = document.createElement('div'); fl.id = 'lnFlash'; document.body.appendChild(fl);
    hud = { fill: root.querySelector('#lnFill'), wave: root.querySelector('#lnWave'),
            kills: root.querySelector('#lnKills'), alive: root.querySelector('#lnAlive'),
            veil, edge, flash: fl };
  }

  function paint(touching) {
    if (!hud) return;
    hud.fill.style.width = vit + '%';
    hud.fill.className = 'ln-fill' + (vit < 35 ? ' hurt' : '');
    hud.wave.textContent = wave; hud.kills.textContent = kills; hud.alive.textContent = wraiths.length;
    hud.edge.style.opacity = touching ? String(Math.min(0.9, (100 - vit) / 100 + 0.25)) : '0';
  }

  function flash(text) {
    hud.flash.textContent = text; hud.flash.classList.add('on');
    setTimeout(() => hud.flash.classList.remove('on'), 2400);
  }

  // Booted last on purpose. window.EMBER already exists by the time this
  // layer is injected, so boot() runs start() synchronously — called from the
  // top of the module it reached consts further down before they were
  // initialised and died in the temporal dead zone.
  boot();
})();
