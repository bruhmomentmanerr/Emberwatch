// Walk into several walk-in shops and homes and look around each, close up,
// from inside the doorway — the way the owner would actually see clipping or
// a room lit only by a hotspot.
//   ... tools/harness app/renderer/index.html tools/probes/probe-look-interiors.js 60 <shotsDir>
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  // The world takes a while to build and EMBER only exists at the end of it;
  // capture it after the wait, not before, or it stays undefined forever.
  for (let i = 0; i < 60 && !window.EMBER; i++) await wait(500);
  const E = window.EMBER;
  if (!E) return { error: 'EMBER never appeared' };
  await wait(2500);
  const rooms = (E.doors || []).filter(d => (d.kind === 'shop' || d.kind === 'home'));
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const shots = [];
  const picks = rooms.filter(r => r.kind === 'shop').slice(0, 4).concat(rooms.filter(r => r.kind === 'home').slice(0, 4));
  picks.forEach((r, i) => {
    shots.push({ name: (r.kind) + i + '-' + r.name.replace(/[^a-z0-9]+/gi, '_').slice(0, 24),
      x: r.insideX, z: r.insideZ, y: 1.6, yaw: face(r.insideX, r.insideZ, r.cx, r.cz), pitch: -0.08 });
  });
  return { rooms: rooms.length, shots };
})()
