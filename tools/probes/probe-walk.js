// Walk a route the way a player does (r143): hold W, steer toward each
// waypoint, and record what happened — did we arrive, how high did we get,
// where did we stall. Traversal proof for authored places: a stair that
// photographs well but cannot be climbed is not a stair.
//
// window.__walk = { start:[x,z,y?], legs:[[x,z] | {from:[x,z,y?], to:[x,z]}], frames:per-leg budget }
//
// Counted in rendered frames, not seconds: under software rendering the game
// can run at a frame a second, and a clock-based "no progress in one second"
// test then reports stalls that are only slow frames. The render scale drops
// to a quarter while walking — nothing here is looked at — which speeds the
// frames up several times. A stall is under 0.25 m of progress in 25 frames.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 80 && !window.EMBER; i++) await wait(100);
  const E = window.EMBER, P = E.player, spec = window.__walk;
  if (!spec) return { error: 'no __walk' };
  if (E.sky) { E.sky.rain(0); E.sky.omen(0); }
  E.setPixel(.25);
  const frame = () => E.renderer.info.render.frame;
  const key = (type, code) => dispatchEvent(new KeyboardEvent(type, { code, key: code, bubbles: true, cancelable: true }));
  const put = ([x, z, y]) => { P.x = x; P.z = z; P.y = y ?? E.terrainAt(x, z); P.vy = 0; P.onGround = true; };
  put(spec.start);
  await wait(800);
  const legs = [];
  for (const raw of spec.legs) {
    const target = Array.isArray(raw) ? raw : raw.to;
    if (!Array.isArray(raw) && raw.from) { put(raw.from); await wait(500); }
    const [tx, tz] = target;
    const leg = { to: [+tx.toFixed(1), +tz.toFixed(1)], reached: false, minY: Infinity, maxY: -Infinity, stalls: [] };
    const f0 = frame(); let mark = f0, lastX = P.x, lastZ = P.z;
    key('keydown', 'KeyW');
    while (frame() - f0 < (spec.frames || 700)) {
      const dx = tx - P.x, dz = tz - P.z;
      if (Math.hypot(dx, dz) < 1.1) { leg.reached = true; break; }
      E.look(Math.atan2(-dx, -dz), 0);
      leg.minY = Math.min(leg.minY, P.y); leg.maxY = Math.max(leg.maxY, P.y);
      await wait(30);
      if (frame() - mark >= 25) {
        if (Math.hypot(P.x - lastX, P.z - lastZ) < .25) leg.stalls.push([+P.x.toFixed(1), +P.z.toFixed(1), +P.y.toFixed(2)]);
        lastX = P.x; lastZ = P.z; mark = frame();
        if (leg.stalls.length >= 3) break;
      }
    }
    key('keyup', 'KeyW');
    leg.frames = frame() - f0;
    leg.at = [+P.x.toFixed(1), +P.z.toFixed(1), +P.y.toFixed(2)];
    leg.minY = +leg.minY.toFixed(2); leg.maxY = +leg.maxY.toFixed(2);
    legs.push(leg);
    await wait(200);
  }
  E.setPixel(1);
  return { reached: legs.filter(l => l.reached).length + '/' + legs.length, legs };
})()
