// (r176) The Veilscar vista and Orren from four sides, for the match score.
//
//   XSCREEN=1400x1100x24 <harness> app/renderer/index.html tools/probes/probe-orren-vista.js 40 <shotsDir>
//   python3 tools/match-score.py <shotsDir>/o-vista.png tools/video-frames/reference/wizard-vista.jpg \
//     --mask 0.62,0.17,0.99,0.36 --mask 0.25,0.66,0.62,0.74
//
// Shots are 540x960 (the reference is portrait), so the virtual screen must be
// tall. The clouds are held still so two runs compare, and the first shot of a
// run is thrown away: it lands before the frame has settled and scores a few
// points off. Without the hold the same build scored 36.3 and 41.7.
//
// o-vista is the canon capture vista-ruin-waterfall (behind Orren's shoulder,
// as the reference stands); o-back, o-front and o-side circle him at about
// three metres.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 900 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER;
  E.setWatch('still'); E.setPixel(1); if (E.sky) { E.sky.rain(0); E.sky.omen(0); }
  await wait(1500);
  const style = document.createElement('style');
  style.textContent = 'body.cap-clean *:not(canvas):not(#app):not(body):not(html){visibility:hidden!important}';
  document.head.append(style); document.body.classList.add('cap-clean');
  E.sky.hold(120);
  const cap = E.visualCanon.captures.find(c => c.id === 'vista-ruin-waterfall');
  const o = E.villagers.find(n => n.name === 'Orren of the Broken Hall'), p = o.g.position, ry = o.g.rotation.y;
  const fx = Math.sin(ry), fz = Math.cos(ry);
  let sculpt = null; o.g.traverse(c => { if (c.name === 'sculpt-orren') sculpt = c; });
  const at = (ang, d, up, look = 1.35, fov = 50) => { const a = Math.atan2(fx, fz) + ang, cx = p.x + Math.sin(a) * d, cz = p.z + Math.cos(a) * d;
    return { x: cx, z: cz, y: p.y + up, yaw: Math.atan2(-(p.x - cx), -(p.z - cz)), pitch: Math.atan2((p.y + look) - (p.y + up + 1.6), d), fov, size: [540, 960] }; };
  const shots = [
    { name: 'warm', x: cap.x, z: cap.z, y: cap.y, yaw: cap.yaw, pitch: cap.pitch, fov: cap.fov, size: [540, 960] },
    { name: 'o-vista', x: cap.x, z: cap.z, y: cap.y, yaw: cap.yaw, pitch: cap.pitch, fov: cap.fov, size: [540, 960] },
    { name: 'o-back', ...at(Math.PI * .88, 2.6, .1) },
    { name: 'o-front', ...at(.45, 3.0, -.1) },
    { name: 'o-side', ...at(-Math.PI / 2, 3.0, -.1) }
  ];
  return { sculpt: !!sculpt, at: [p.x, p.y, p.z].map(v => +v.toFixed(2)), scale: o.g.scale.y, shots };
})()
