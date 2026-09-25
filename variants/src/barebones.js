/* ==========================================================================
   EMBERWATCH — R0 / BAREBONES                                 variant layer
   --------------------------------------------------------------------------
   The proof of concept with everything else taken off it.

   What it is for: showing the one idea, that the Peak controls live inside a
   place you walk around in, without the rest of the build arguing for
   attention alongside it or giving away how far along it actually is.

   What it strips:
     - every resident, and the interaction prompts that came with them
     - the chronicle, the strain journal, the wayfinder, the title card
     - all of the styling. The panels are handed back to the browser: native
       buttons, default fonts, flat white boxes with a black rule round them.
       A first pass at this restyled everything into a tidy dark monospace
       theme, which was the wrong instinct. A considered theme reads as
       designed no matter how minimal it is. Unfinished looks like nobody has
       been near the CSS yet, so nobody has.

   What it keeps: movement, the inner city, and the Peak bridge untouched.

   The world itself is cut back by a source transform in build-variants.js, not
   from here. By the time this layer runs every static mesh is already merged
   into batches by material, so a layer can empty the streets but it cannot
   un-build them.
   ========================================================================== */
(function () {
  'use strict';

  let E, residents = [], hud = null, flame = null, fireLight = null, embers = null;
  let mats = null, tongues = [], burn = 0;

  function start() {
    stripResidents();
    hideFinishedParts();
    unstyle();
    relabel();
    findFire();
    readout();
    requestAnimationFrame(tick);
  }

  // --- residents -----------------------------------------------------------
  // updateVillagers() keeps running and keeps writing positions, and the
  // proximity checks that raise "talk to X" read those positions. Taking the
  // groups out of the scene only stops them drawing, so they are also parked
  // far outside the map every frame. That is what actually kills the prompts.
  function stripResidents() {
    E.scene.children.slice().forEach(o => {
      if (!o.isGroup) return;
      let pivots = 0;
      for (const c of o.children) if (c.isGroup) pivots++;
      if (pivots < 4) return;
      residents.push(o);
      E.scene.remove(o);
    });
  }

  function park() {
    for (const g of residents) { g.position.x = 1e6; g.position.z = 1e6; }
  }

  // --- interface -----------------------------------------------------------
  function hideFinishedParts() {
    const gone = ['gameTitle', 'wayfinder', 'chroniclePanel', 'dialoguePanel',
                  'strainBtn', 'strainPanel', 'sessionRamble', 'interactHint',
                  'gameToast', 'hint'];
    const css = document.createElement('style');
    css.textContent = gone.map(id => '#' + id).join(',') + '{display:none!important}';
    document.head.appendChild(css);
  }

  // Hand the controls back to the browser. `all:revert` on the buttons and
  // fields drops them to the user agent stylesheet, which is why they come out
  // as real OS widgets rather than as anything anybody chose.
  function unstyle() {
    const css = document.createElement('style');
    css.textContent = `
      #loader{background:#000!important}
      #loader .orb{display:none!important}
      #loader .g,#loader .s{font:13px sans-serif!important;letter-spacing:normal!important;
        color:#ccc!important;text-shadow:none!important}
      #loader #startBtn{all:revert!important}

      #puffPanel,#settings,#btChooser .btc-box{
        background:#fff!important;color:#000!important;border:2px solid #000!important;
        border-radius:0!important;box-shadow:none!important;padding:4px!important;
        font:13px sans-serif!important}
      #puffPanel *,#settings *,#btChooser .btc-box *{
        color:#000!important;background:transparent!important;border-radius:0!important;
        box-shadow:none!important;text-shadow:none!important;letter-spacing:normal!important;
        text-transform:none!important;font:13px sans-serif!important;transition:none!important}
      #puffPanel button,#settings button,#btChooser button,
      #puffPanel input,#settings input,#puffPanel select,#settings select,
      #puffPanel textarea{all:revert!important;font:13px sans-serif!important}
      #puffHead,#btChooser .btc-head{background:#ccc!important;border-bottom:2px solid #000!important;
        font-weight:bold!important;padding:2px 4px!important}
      #puffPanel .pstat{border:1px solid #999!important;padding:1px 3px!important}
      #puffPanel .puff-section{font-weight:bold!important;margin-top:6px!important}
      #puffPanel .pnote,#settings .pnote{color:#444!important;font-size:11px!important}
      #btChooser{background:rgba(0,0,0,.5)!important}
      #btChooser .btc-item{border:1px solid #000!important;background:#eee!important;padding:3px!important}

      #puffBtn,#gear,#menu{all:revert!important;position:fixed!important;z-index:24!important;
        font:12px sans-serif!important}
      #puffBtn{left:8px!important;bottom:26px!important}
      #gear{right:8px!important;bottom:26px!important}

      #r0bar{position:fixed;left:0;right:0;bottom:0;z-index:30;padding:2px 6px;
        background:#fff;color:#000;border-top:2px solid #000;
        font:12px sans-serif;pointer-events:none;display:flex;gap:14px;flex-wrap:wrap}
      #r0tag{position:fixed;left:6px;top:4px;z-index:30;color:#fff;
        font:12px sans-serif;pointer-events:none}`;
    document.head.appendChild(css);
  }

  // The panel header carries the live revision label, which rather gives away
  // how many revisions this build is pretending not to have.
  function relabel() {
    const head = document.querySelector('#puffHead span');
    if (head) head.textContent = 'peak';
  }

  // The one thing in r0 that demonstrates what the build is actually for. The
  // campfire is not decoration: it is wired to the Peak. Idle it sits low, and
  // it climbs while the device heats and runs, then falls back when the cycle
  // ends. Somebody watching a clip should be able to work out what is happening
  // without being told, which no amount of UI achieves.
  // Called once at start and then again from the loop until it finds the fire.
  // The retry is a guard, not a fix for an observed failure: the layer boots as
  // soon as EMBER and THREE exist, and both are published before the loading
  // stages raise the campsite, so the order is not actually guaranteed. Every
  // load measured so far has won that race at start(). Costs one traverse per
  // fifteen frames until it resolves and nothing at all afterwards.
  function findFire() {
    E.scene.traverse(o => {
      if (o.name === 'r0-flame')  flame = o;
      if (o.name === 'r0-fire')   fireLight = o;
      if (o.name === 'r0-embers') embers = o;
    });
    if (flame) { mats = flame.userData.mats; tongues = flame.children; }
  }

  // 0 idle, 1 full. Heating counts as part of the way up, because the wait for
  // the Peak to come to temperature is a real part of the thing being modelled.
  function peakBurn() {
    const bridge = globalThis.emberwatchPeakSession;
    if (!bridge || !bridge.status) return { want: 0.10, label: 'no device' };
    let st;
    try { st = bridge.status(); } catch (e) { return { want: 0.10, label: 'device error' }; }
    if (!st.connected) return { want: 0.10, label: 'disconnected' };
    if (st.active) return { want: 1, label: 'cycle running' };
    if (st.busy)   return { want: 0.55, label: 'heating' };
    return { want: 0.25, label: 'connected, idle' };
  }

  // Deliberately narrow ranges. An earlier pass drove scale and emissive hard
  // enough that the flame came out as a white cone taller than the tents, which
  // is not a fire, it is a lamp. The device state should be legible in how the
  // fire behaves, not in how much of the screen it takes up: it grows by about
  // half again from idle to a running cycle, and everything else is colour,
  // reach of the light, and how hard the embers climb.
  function burnTick(dt, now) {
    if (!flame || !fireLight) return '';
    const state = peakBurn();
    // Eased rather than snapped: a fire does not step between sizes, and the
    // climb is most of what makes the link readable.
    burn += (state.want - burn) * Math.min(1, dt * 1.4);

    const sway = 1 + Math.sin(now / 260) * 0.03;
    flame.scale.set(sway, 0.72 + burn * 0.50, sway);
    // No spin. A rotating cone announces itself as a rotating cone; the
    // motion has to come from the tongues moving against each other instead.
    // Each tongue on its own phase, so they lick past each other instead of
    // pulsing as one shape.
    for (let i = 0; i < tongues.length; i++) {
      const t = tongues[i], ph = t.userData.ph;
      t.scale.y = 1 + Math.sin(now / (105 + ph * 26) + ph) * (0.10 + burn * 0.16);
      t.scale.x = t.scale.z = 1 + Math.sin(now / (150 + ph * 33) + ph) * 0.06;
    }
    // Stays orange the whole way. Lightness moves a little, hue barely at all.
    mats.outer.color.setHSL(0.045 + burn * 0.018, 1, 0.44 + burn * 0.10);
    mats.core.color.setHSL(0.100 + burn * 0.020, 1, 0.60 + burn * 0.10);

    const flicker = 0.92 + Math.sin(now / 90) * 0.05 + Math.sin(now / 37) * 0.03;
    // Lamp units, converted by the base game (r111 physical lighting). The
    // power is converted at a fixed range of 14 rather than the live one: the
    // conversion grows with the square of the range, and a fire whose reach
    // doubles would otherwise come out four times hotter on top of its own
    // climb, which at a metre off the ground is a white disc, not a campfire.
    fireLight.intensity = E.lampPower(0.9 + burn * 2.0, 14) * flicker;
    fireLight.distance = (14 + burn * 14) * E.LAMP_REACH;
    fireLight.color.copy(mats.outer.color);

    if (embers) {
      const p = embers.geometry.attributes.position, arr = p.array;
      const rise = dt * (0.5 + burn * 2.4);
      for (let i = 1; i < arr.length; i += 3) {
        arr[i] += rise;
        if (arr[i] > 1.0 + burn * 3.0) {
          arr[i] = 0.35;
          arr[i - 1] = (Math.random() - 0.5) * 0.7;
          arr[i + 1] = (Math.random() - 0.5) * 0.7;
        }
      }
      p.needsUpdate = true;
      embers.material.opacity = 0.25 + burn * 0.6;
    }
    return state.label;
  }

  // Values, not atmosphere. This replaces the wayfinder.
  function readout() {
    const tag = document.createElement('div');
    tag.id = 'r0tag';
    tag.textContent = 'r0';
    document.body.appendChild(tag);

    const bar = document.createElement('div');
    bar.id = 'r0bar';
    bar.innerHTML = '<span>x <b id="r0x">0</b></span><span>z <b id="r0z">0</b></span>' +
                    '<span>fps <b id="r0fps">0</b></span><span>draws <b id="r0calls">0</b></span>' +
                    '<span>peak <b id="r0peak">no device</b></span>' +
                    '<span>wasd / shift / space / P</span>';
    document.body.appendChild(bar);
    hud = { x: bar.querySelector('#r0x'), z: bar.querySelector('#r0z'),
            fps: bar.querySelector('#r0fps'), calls: bar.querySelector('#r0calls'),
            peak: bar.querySelector('#r0peak') };
  }

  // --- loop ----------------------------------------------------------------
  let frames = 0, mark = 0, fps = 0, lastNow = 0, hunt = 0;
  function tick(now) {
    requestAnimationFrame(tick);
    park();
    // Give up after about twenty seconds rather than traversing the scene for
    // the life of the process if the campsite never arrives.
    if (!flame && ++hunt < 1200 && hunt % 15 === 0) findFire();
    const dt = Math.min(0.05, (now - lastNow) / 1000 || 0); lastNow = now;
    const peakLabel = burnTick(dt, now);
    frames++;
    if (now - mark > 500) { fps = Math.round(frames * 1000 / (now - mark)); frames = 0; mark = now; }
    if (!hud) return;
    hud.x.textContent = Math.round(E.player.x);
    hud.z.textContent = Math.round(E.player.z);
    hud.fps.textContent = fps;
    hud.calls.textContent = E.renderer.info.render.calls;
    if (peakLabel) hud.peak.textContent = peakLabel;
  }

  function boot() {
    if (!window.EMBER || !window.THREE) return setTimeout(boot, 250);
    E = window.EMBER;
    try { start(); } catch (err) { console.warn('Barebones layer failed to start:', err); }
  }

  // Booted last so every module-level declaration above is initialised first.
  boot();
})();
