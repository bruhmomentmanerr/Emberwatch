// Try lighting values at runtime, without editing index.html, and shoot them.
// How r111's physical lighting was tuned (2026-09-13).
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-light-tune.js 20 <shotsDir>
//   node tools/diff-shots.js tools/probes/reference-r111 <shotsDir>
//
// Edit CFG below; every key is optional and {} shoots the build as it is.
//   mode         'night' | 'dusk' | 'ember' — clicks that lighting button first
//   tone         'ACESFilmic' | 'AgX' | 'Neutral' | ... (THREE.<tone>ToneMapping)
//   exposure     renderer.toneMappingExposure
//   hemi, moon   multiply the fill / moon intensity (survives setLighting writes)
//   hemiSky, hemiGround, moonColor   colours as numbers, e.g. 0x4a55a0
//   point        { gain, rangeMul, decay, match } for every point light. Scales on
//                write, so the game's flicker keeps working. On an r111+ build the
//                lights are already converted: use gain/rangeMul as multipliers
//                and leave match off (match converts r128 values, as r110 had).
//   emissive     multiply every emissiveIntensity
//   shadowRadius moon.shadow.radius
//   shaderSpace  add colorspace_fragment to custom shaders that lack it
//   fog, fogDensity
//   bloom        { on, threshold, knee, strength, radius } merged into EMBER.bloom (r112+)
//   only         ['2-market-fire', ...] to shoot a subset
// 8-hearth and 9-resident are found at runtime; the resident walks, so that shot
// is not comparable between runs.
const CFG = {};
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  E.setWatch('labour'); await wait(500);
  if (CFG.mode) { document.querySelector('[data-light="' + CFG.mode + '"]').click(); await wait(200); }
  const R = E.renderer, S = E.scene, out = { lights: 0, emissive: 0, shaders: 0 };
  if (CFG.tone) R.toneMapping = THREE[CFG.tone + 'ToneMapping'];
  if (CFG.exposure != null) R.toneMappingExposure = CFG.exposure;
  // The game rewrites intensity every frame (flicker), so scale on write.
  const scale = (o, K) => { let v = o.intensity * K;
    Object.defineProperty(o, 'intensity', { configurable: true, get() { return v; }, set(x) { v = x * K; } }); };
  const mats = new Set();
  S.traverse(o => {
    if (o.isHemisphereLight) { if (CFG.hemi != null) scale(o, CFG.hemi); if (CFG.hemiSky != null) o.color.setHex(CFG.hemiSky); if (CFG.hemiGround != null) o.groundColor.setHex(CFG.hemiGround); }
    if (o.isDirectionalLight) { if (CFG.moonColor != null) o.color.setHex(CFG.moonColor); if (CFG.moon != null) scale(o, CFG.moon); if (CFG.shadowRadius != null) { o.shadow.radius = CFG.shadowRadius; } }
    if (o.isPointLight && CFG.point) {
      const p = CFG.point, R0 = o.distance || 20;
      if (p.decay != null) o.decay = p.decay;
      // match: equal to the r128 light at a third of its old range
      const K = p.match ? 0.233 * R0 * R0 * p.gain : p.gain;
      o.distance = R0 * (p.rangeMul || 1);
      scale(o, K); out.lights++;
    }
    if (o.material) (Array.isArray(o.material) ? o.material : [o.material]).forEach(m => mats.add(m));
  });
  for (const m of mats) {
    if (CFG.emissive != null && m.emissive && m.emissiveIntensity > 0) { m.emissiveIntensity *= CFG.emissive; out.emissive++; }
    if (CFG.shaderSpace && m.isShaderMaterial && !/colorspace_fragment/.test(m.fragmentShader)) {
      const f = m.fragmentShader;
      m.fragmentShader = f.includes('#include <fog_fragment>')
        ? f.replace('#include <fog_fragment>', '#include <colorspace_fragment>\n#include <fog_fragment>')
        : f.slice(0, f.lastIndexOf('}')) + '#include <colorspace_fragment>\n}';
      m.needsUpdate = true; out.shaders++;
    }
  }
  if (CFG.fog != null) { S.fog.color.setHex(CFG.fog); S.background.setHex(CFG.fog); }
  if (CFG.fogDensity != null) S.fog.density = CFG.fogDensity;
  if (CFG.bloom && E.bloom) Object.assign(E.bloom, CFG.bloom);
  R.shadowMap.needsUpdate = true;
  await wait(800);
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  // A hearth (the only 0xff6a1e light at fire height) and a resident near the market.
  let hearth = null; S.traverse(o => { if (!hearth && o.isPointLight && o.color.getHex() === 0xff6a1e && Math.abs(o.position.y - .95) < .01) hearth = o; });
  const extra = [];
  if (hearth) extra.push({ name: '8-hearth', x: hearth.position.x + 1.2, z: hearth.position.z + 4.6, yaw: face(hearth.position.x + 1.2, hearth.position.z + 4.6, hearth.position.x, hearth.position.z), pitch: -0.12 });
  const res = E.villagers.filter(v => !v.indoors).map(v => v.g).filter(g => g && g.position).sort((a, b) => Math.hypot(a.position.x, a.position.z - 120) - Math.hypot(b.position.x, b.position.z - 120))[0];
  if (res) { res.userData.frozen = true; extra.push({ name: '9-resident', x: res.position.x, z: res.position.z + 3.2, yaw: face(res.position.x, res.position.z + 3.2, res.position.x, res.position.z), pitch: -0.1 }); }
  return { cfg: CFG, out, three: THREE.REVISION, shim: THREE.EMBERWATCH_SHIM, shots: [
    { name: '1-gate-out', x: 0, z: 414, yaw: Math.PI, pitch: 0.02 },
    { name: '2-market-fire', x: 0, z: 134, yaw: face(0, 134, 0, 108), pitch: -0.08 },
    { name: '3-lantern-street', x: 0, z: 192, yaw: face(0, 192, 0, 230), pitch: -0.02 },
    { name: '4-rampart-city', x: 60, z: 372, y: 14.9, yaw: face(60, 372, 0, 100), pitch: -0.22 },
    { name: '5-pond', x: -329.1, z: 309.7, yaw: face(-329.1, 309.7, -340, 320), pitch: -0.16 },
    { name: '6-hillside', x: Math.cos(1.17) * 585, z: Math.sin(1.17) * 585, yaw: face(Math.cos(1.17) * 585, Math.sin(1.17) * 585, Math.cos(1.5) * 585, Math.sin(1.5) * 585), pitch: -0.06 },
    { name: '7-stones-crystal', x: 318, z: 318, yaw: face(318, 318, 330, 330), pitch: 0 }
  ].concat(extra).filter(s => !CFG.only || CFG.only.includes(s.name)) };
})()
