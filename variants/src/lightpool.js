/* ==========================================================================
   RETIRED in r115 — build-variants.js no longer injects this file. The base
   game’s light budget (cullLights) replaced it in r91-r92, and running both
   lit the nearest lamps twice. Kept only as the record of what it did.

   LIGHT POOL                                        shared layer, all variants
   --------------------------------------------------------------------------
   Vaneth lights itself with real point lights: every lantern, every interior
   glow, every torch, the keep crown, the market fire. Measured on r86 that is
   108 of them live in the scene at once.

   Three.js compiles the light count into every lit material and loops all of
   them for every shaded fragment. At 108 point lights each pixel of every
   MeshStandardMaterial in view does 108 lighting evaluations. That is the
   single largest cost in the frame, well ahead of the 1,170 draw calls, and it
   is why the game is heavy everywhere and worse the moment anything transparent
   and additive is drawn over the top of it — a spell.

   The fix is the standard one: keep a small fixed pool of real lights and move
   them to whichever sources are nearest the camera. Eight lights instead of a
   hundred and eight, and the count never changes, so the shaders are compiled
   once and never recompiled.

   What is preserved:
     - the original lights keep being updated by the game's own flicker code,
       and the pool copies their live intensity, so lanterns still gutter
     - colour, distance falloff and world position all come from the source,
       including sources parented to something that moves
     - nothing is deleted, so anything the game later looks up still exists

   What changes: only the eight nearest sources actually illuminate. Past the
   pool's reach a lantern still glows, because its head is an emissive material
   and always was, but it stops casting on the ground. At night, in fog, across
   a street, that is not a difference you can see.
   ========================================================================== */
(function () {
  'use strict';

  const POOL  = 8;    // how many real lights exist at any moment
  const REACH = 70;   // sources further than this are never considered

  let E, T, pool = [], sources = [];

  function start() {
    // Collect first, mutate second: traversing while changing visibility is a
    // good way to miss half the tree.
    const found = [];
    E.scene.traverse(o => { if (o.isPointLight) found.push(o); });
    if (found.length <= POOL) return;   // nothing to gain, leave it alone

    for (const light of found) {
      sources.push({
        light,
        colour: light.color.clone(),
        distance: light.distance,
        pos: new T.Vector3()
      });
      // Hidden, not removed. Three.js only counts visible lights, so this is
      // what actually takes them out of the shader — and the game's flicker
      // code keeps writing intensity to them, which is what we read back.
      light.visible = false;
    }

    for (let i = 0; i < POOL; i++) {
      const l = new T.PointLight(0xffffff, 0, 30);
      l.castShadow = false;
      E.scene.add(l);
      pool.push(l);
    }

    requestAnimationFrame(tick);
  }

  // Sources are re-sorted every frame rather than on a timer: a lantern coming
  // round a corner should light the corner as you reach it, not a beat later.
  const scratch = [];
  function tick() {
    requestAnimationFrame(tick);
    const cam = E.camera.position;
    scratch.length = 0;

    for (const s of sources) {
      if (s.light.intensity <= 0.001) continue;          // guttered out
      s.light.getWorldPosition(s.pos);
      const dx = s.pos.x - cam.x, dy = s.pos.y - cam.y, dz = s.pos.z - cam.z;
      const d2 = dx * dx + dy * dy + dz * dz;
      if (d2 > REACH * REACH) continue;
      s.d2 = d2;
      scratch.push(s);
    }
    scratch.sort((a, b) => a.d2 - b.d2);

    for (let i = 0; i < POOL; i++) {
      const l = pool[i], s = scratch[i];
      if (!s) { l.intensity = 0; continue; }
      l.position.copy(s.pos);
      l.color.copy(s.colour);
      l.distance = s.distance;
      l.intensity = s.light.intensity;   // live, so flicker carries through
    }
  }

  function boot() {
    if (!window.EMBER || !window.THREE) return setTimeout(boot, 250);
    E = window.EMBER; T = window.THREE;
    try { start(); } catch (err) { console.warn('Light pool failed to start:', err); }
  }

  boot();
})();
