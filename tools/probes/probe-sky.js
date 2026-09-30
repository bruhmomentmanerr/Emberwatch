// The night sky from across the map (r143). The moon is a direction now, not a
// place, so it must hang in the same part of the sky from the city, the gate
// and every wilderness site. Each shot faces the moon's bearing from somewhere
// different; the last looks north-west for the small ember moon.
//
// Optional knobs, read from window.__skyProbe before the probe runs:
//   { rain: 0..1, omen: 0..1, shower: true }  — force a weather/event state.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER;
  if (!E) return { error: 'EMBER missing' };
  E.setWatch('still');
  const knobs = window.__skyProbe || {};
  if (E.sky) { E.sky.rain(knobs.rain ?? 0); E.sky.omen(knobs.omen); if (knobs.shower) E.sky.shower(); }
  await wait(1200);
  const style = document.createElement('style');
  style.textContent = 'body.sky-clean *:not(canvas):not(#app):not(body):not(html){visibility:hidden!important}';
  document.head.append(style); document.body.classList.add('sky-clean');

  const m = E.sky ? E.sky.moonDir : { x: .39, y: .38, z: -.84 };
  const moonYaw = Math.atan2(-m.x, -m.z), moonPitch = Math.asin(m.y) * .55;
  const at = (name, x, z, yaw, pitch, lift = 0) => ({ name, x, z, y: (E.terrainAt ? E.terrainAt(x, z) : 0) + lift, yaw, pitch });
  const shots = [
    at('sky-01-north-gate-spawn', 0, 406, 0, .10),
    at('sky-02-market-to-moon', 0, 160, moonYaw, moonPitch),
    at('sky-03-fallen-hall-to-moon', 326, -300, moonYaw, moonPitch),
    at('sky-04-graveyard-to-moon', -338, -306, moonYaw, moonPitch),
    at('sky-05-foxglove-to-moon', -368, 322, moonYaw, moonPitch),
    at('sky-06-skywatch-to-moon', -70, 446, moonYaw, moonPitch),
    at('sky-07-ember-moon-northwest', 0, 150, Math.atan2(.5, -.62), .45),
    at('sky-08-east-gate-street', 300, 0, Math.PI / 2, .02)
  ];
  const d = E.diagnostics();
  return { revision: d.revision, visualCanon: { rainLevel: d.visualCanon.rainLevel, skyEvent: d.visualCanon.skyEvent, omen: d.visualCanon.omen, moonDir: d.visualCanon.moonDir }, shots };
})()
