// The visual-canon capture cameras, filtered (r143). Same clean-frame setup as
// probe-visual-canon.js, but only the captures whose id contains one of the
// words in window.__only (default: all), plus any extra standpoints in
// window.__extra = [{name, x, z, y?, yaw, pitch}]. For working on one place
// without waiting on the whole contact sheet.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER;
  if (!E) return { error: 'EMBER missing' };
  E.setWatch(window.__watch || 'still');
  E.setPixel(1);
  if (E.sky) { E.sky.rain(window.__rain ?? 0); E.sky.omen(0); }
  await wait(900);
  const style = document.createElement('style');
  style.textContent = 'body.cap-clean *:not(canvas):not(#app):not(body):not(html){visibility:hidden!important}';
  document.head.append(style); document.body.classList.add('cap-clean');
  const only = window.__only || null;
  const caps = E.visualCanon.captures.filter(c => !only || only.some(w => c.id.includes(w)));
  const shots = caps.map(c => ({ name: c.id, x: c.x, z: c.z, y: c.y, yaw: c.yaw, pitch: c.pitch ?? -.08 }));
  for (const s of (window.__extra || [])) shots.push({ y: E.terrainAt(s.x, s.z), ...s });
  const d = E.diagnostics();
  return { revision: d.revision, errors: window.__errors || [], landmarks: d.visualCanon.landmarks, shots };
})()
