/* ==========================================================================
   EMBERWATCH — HEATLINE                                       variant layer
   --------------------------------------------------------------------------
   Temperature is a dial on the world.

   Your Peak's target temperature sets what Vaneth is. Low, and the city is
   close and warm and orange, the fog heavy, the lamps doing all the work.
   High, and it opens out cold and violet and too clear, the aurora hard, the
   air full of drifting light. The residents you can see change with it.

   The point is that this is not a menu. It is the number you were going to set
   anyway, in the app you were going to use anyway, and the world is downstream
   of it. Turn the dial for the dab you actually want and the city follows.

   The temperature is read straight off the Puffco panel's own target field, so
   it tracks whether or not a device is connected. With no Peak to hand, `[`
   and `]` sweep it by ten degrees so the build is still playable.
   ========================================================================== */
(function () {
  'use strict';

  const LO = 380, HI = 620;         // the band the panel allows, roughly
  const BASE_FOG = 0.007;

  // Where the world sits at each end. Everything between is interpolated, so
  // there are no steps — the city slides as the number does.
  const COLD = {                       // low temperature: close, warm, lamplit
    fog: 0.019, fogColor: 0x241206, sky: 0.35,
    light: 0xffa347, ambient: 0xff9a4d, motes: 0xffc98a, name: 'Low and close'
  };
  const HOT = {                        // high temperature: open, cold, electric
    fog: 0.0035, fogColor: 0x0a1626, sky: 1.25,
    light: 0x9fd8ff, ambient: 0x7fb4ff, motes: 0xc9e9ff, name: 'High and far'
  };

  let E, T, hud, manual = null, curve = 0, shown = -1;
  let moon = null, hemi = null, baseFog = null, driftField = null;

  function boot() {
    if (!window.EMBER || !window.THREE) return setTimeout(boot, 250);
    E = window.EMBER; T = window.THREE;
    try { start(); } catch (err) { console.warn('Heatline layer failed to start:', err); }
  }

  function start() {
    E.scene.traverse(o => {
      if (o.isDirectionalLight && !moon) moon = o;
      if (o.isHemisphereLight && !hemi) hemi = o;
    });
    baseFog = E.scene.fog ? E.scene.fog.color.clone() : new T.Color(0x140b22);
    drift();
    buildHud();
    addEventListener('keydown', e => {
      // The old typeof guard could never see the base game's anyOverlayOpen, so
      // [ and ] were swallowed while typing in the strain journal (r114 audit).
      const t = e.target;
      if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
      if (E.overlayOpen && E.overlayOpen()) return;
      if (e.key === '[') manual = Math.max(LO, (readTarget() || 500) - 10);
      else if (e.key === ']') manual = Math.min(HI, (readTarget() || 500) + 10);
      else return;
      e.preventDefault();
    });
    requestAnimationFrame(loop);
  }

  // The panel's target field is the number the user actually set, connected or
  // not, which makes it a better source than the device telemetry.
  function readTarget() {
    if (manual !== null) return manual;
    const field = document.getElementById('pTarget');
    const value = field && parseFloat(field.value);
    return Number.isFinite(value) ? value : null;
  }

  // A field of drifting light that only really shows at the hot end.
  function drift() {
    const count = 300, positions = new Float32Array(count * 3), seeds = [];
    for (let i = 0; i < count; i++) {
      const a = Math.random() * Math.PI * 2, r = Math.random() * 250;
      positions[i * 3] = Math.cos(a) * r;
      positions[i * 3 + 1] = 1 + Math.random() * 22;
      positions[i * 3 + 2] = Math.sin(a) * r;
      seeds.push({ a, r, y: positions[i * 3 + 1], phase: Math.random() * 6.28 });
    }
    const geometry = new T.BufferGeometry();
    geometry.setAttribute('position', new T.BufferAttribute(positions, 3));
    const points = new T.Points(geometry, new T.PointsMaterial({
      color: HOT.motes, size: 0.5, transparent: true, opacity: 0,
      depthWrite: false, blending: T.AdditiveBlending, fog: true }));
    E.scene.add(points);
    driftField = { points, seeds };
  }

  const mix = (a, b, t) => a + (b - a) * t;

  function loop(now) {
    requestAnimationFrame(loop);
    const t = now / 1000;
    const target = readTarget();
    const want = target === null ? 0.5 : Math.max(0, Math.min(1, (target - LO) / (HI - LO)));
    curve += (want - curve) * 0.02;              // the world takes its time

    if (E.scene.fog) {
      E.scene.fog.density = mix(COLD.fog, HOT.fog, curve);
      E.scene.fog.color.setHex(COLD.fogColor).lerp(new T.Color(HOT.fogColor), curve);
    }
    if (moon) {
      moon.color.setHex(COLD.light).lerp(new T.Color(HOT.light), curve);
      // r111 physical lighting: the base night moon is 2.2 and its fill 2.25,
      // four and four and a half times the old values; both ends scale with it.
      moon.intensity = mix(2.2, 4.6, curve);
    }
    if (hemi) {
      hemi.color.setHex(COLD.ambient).lerp(new T.Color(HOT.ambient), curve);
      hemi.intensity = mix(2.25, 4.5, curve);
    }
    if (driftField) {
      driftField.points.material.opacity = Math.max(0, curve - 0.25) * 0.9;
      const position = driftField.points.geometry.attributes.position;
      driftField.seeds.forEach((s, i) => {
        const a = s.a + t * 0.012;
        position.setXYZ(i, Math.cos(a) * s.r, s.y + Math.sin(t * 0.5 + s.phase) * 1.6, Math.sin(a) * s.r);
      });
      position.needsUpdate = true;
    }
    paint(target);
  }

  // --- HUD ----------------------------------------------------------------
  function buildHud() {
    const css = document.createElement('style');
    css.textContent = `
      #hlHud{position:fixed;right:12px;top:96px;z-index:22;width:min(232px,calc(100vw - 24px));
        padding:10px 12px;border:1px solid rgba(150,170,210,.4);border-radius:8px;
        background:linear-gradient(150deg,rgba(16,20,30,.95),rgba(8,9,14,.97));
        box-shadow:0 16px 40px rgba(0,0,0,.6);font-family:system-ui,sans-serif;color:#e6edf8;pointer-events:none}
      .hl-lab{font-size:9px;letter-spacing:1.6px;text-transform:uppercase;color:#93a9c8;opacity:.9}
      .hl-temp{font-family:Georgia,serif;font-size:26px;margin-top:2px;color:#fff;font-variant-numeric:tabular-nums}
      .hl-temp small{font-size:13px;opacity:.6;margin-left:2px}
      .hl-bar{height:6px;border-radius:4px;margin-top:8px;overflow:hidden;
        background:linear-gradient(90deg,#ff9a4d,#6f8fd0,#9fd8ff)}
      .hl-pip{width:2px;height:12px;background:#fff;border-radius:1px;position:relative;top:-9px;
        box-shadow:0 0 6px rgba(255,255,255,.9);transition:margin-left .25s}
      .hl-mood{margin-top:10px;font-family:Georgia,serif;font-size:13px;color:#dce7f8}
      .hl-hint{margin-top:8px;font-size:9px;color:#7e8da8;line-height:1.5}`;
    document.head.appendChild(css);
    const root = document.createElement('div');
    root.id = 'hlHud';
    root.innerHTML = `<div class="hl-lab">Heatline</div>
      <div class="hl-temp"><span id="hlTemp">—</span><small>°F</small></div>
      <div class="hl-bar"></div><div class="hl-pip" id="hlPip"></div>
      <div class="hl-mood" id="hlMood">—</div>
      <div class="hl-hint" id="hlHint">Set your Peak's target and Vaneth follows it.</div>`;
    document.body.appendChild(root);
    hud = { temp: root.querySelector('#hlTemp'), pip: root.querySelector('#hlPip'),
            mood: root.querySelector('#hlMood'), hint: root.querySelector('#hlHint') };
  }

  function paint(target) {
    if (!hud) return;
    if (target !== shown) {
      shown = target;
      hud.temp.textContent = target === null ? '—' : Math.round(target);
      const pct = target === null ? 50 : Math.max(0, Math.min(1, (target - LO) / (HI - LO))) * 100;
      hud.pip.style.marginLeft = 'calc(' + pct + '% - 1px)';
    }
    hud.mood.textContent = curve < 0.28 ? COLD.name
      : curve > 0.72 ? HOT.name
      : 'Somewhere between';
    hud.hint.textContent = manual !== null
      ? 'Sweeping by hand with [ and ]. Set the panel target to hand it back.'
      : "Set your Peak's target and Vaneth follows it. [ and ] to sweep by hand.";
  }

  boot();
})();
