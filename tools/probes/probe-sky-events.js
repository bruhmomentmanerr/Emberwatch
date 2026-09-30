// The rare sky states on demand (r143): rain with wet paving, the omen, and a
// meteor shower with its witnesses. Each is forced through EMBER.sky, because
// on the clock a shower comes round only every nine minutes or so.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER;
  if (!E || !E.sky) return { error: 'EMBER.sky missing' };
  E.setWatch('market');
  E.sky.rain(1); E.sky.omen(1); E.sky.shower();
  await wait(9000);   // into the shower's peak, rain and omen faded fully in
  const style = document.createElement('style');
  style.textContent = 'body.sky-clean *:not(canvas):not(#app):not(body):not(html){visibility:hidden!important}';
  document.head.append(style); document.body.classList.add('sky-clean');
  const o = E.sky.moonDir;
  const toward = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const at = (name, x, z, yaw, pitch) => ({ name, x, z, y: E.terrainAt(x, z), yaw, pitch });
  const shots = [
    // the omen rides the sky to the north-east; from open ground past the gate
    at('events-01-omen-from-north-road', 0, 452, Math.atan2(-.62, -.65), .40),
    // wet paving under the lamps outside the citadel gate
    at('events-02-rain-citadel-gate', 0, 70, 0, -.05),
    // up toward the meteor radiant (south-south-west, high)
    at('events-03-shower-radiant', 0, 452, Math.atan2(.30, .52), .70),
    // people in a busy street reacting
    at('events-04-witnesses', 20, 110, toward(20, 110, 0, 130), 0)
  ];
  const d = E.diagnostics();
  return { rainLevel: d.visualCanon.rainLevel, skyEvent: d.visualCanon.skyEvent, omen: d.visualCanon.omen, meteors: d.visualCanon.meteors, poses: d.visualCanon.npcActivePoses, shots };
})()
