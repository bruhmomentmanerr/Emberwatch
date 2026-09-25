// Teleport between two spots in the city a few times and record, for the frames
// after each arrival, the longest frame and (on builds that have it) the cost of
// the shop-room manager, FRAME_COST.rooms. The soak flagged a 155-470 ms frame at
// its teleport to (0, 200) that the sealed r123 does not have; this isolates it.
//
//   ... tools/harness <html> tools/probes/probe-teleport-hitch.js 60
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = []; addEventListener('error', e => errors.push(String(e.message).slice(0, 160)));
  await wait(3500);
  const place = (x, z) => { E.player.x = x; E.player.z = z; E.player.y = 0; E.player.vy = 0; };
  const spots = [[0, 200], [0, 406], [-120, 130], [0, 136], [180, 60], [0, 200]];
  const runs = [];
  for (const [x, z] of spots) {
    place(x, z);
    const frames = [], rooms = []; let last = performance.now();
    await new Promise(done => { const tick = () => { const now = performance.now(); frames.push(now - last); last = now;
      const c = E.frameCost(); if (c && c.rooms !== undefined) rooms.push(c.rooms);
      if (frames.length < 40) requestAnimationFrame(tick); else done(); }; requestAnimationFrame(tick); });
    runs.push({ at: x + ',' + z, worstFrame: +Math.max(...frames).toFixed(0), medianFrame: +frames.slice().sort((a, b) => a - b)[20].toFixed(0),
      worstRooms: rooms.length ? +Math.max(...rooms).toFixed(1) : null });
    await wait(1500);
  }
  return { errors, runs };
})()
