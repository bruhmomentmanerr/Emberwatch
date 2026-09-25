(async () => {
  const E = window.EMBER, T = E.terrainAt, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2000);
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const stand = (x, z, yaw, pitch = 0) => { E.player.x = x; E.player.z = z; E.player.y = T(x, z); E.player.vy = 0; E.player.onGround = true; E.look(yaw, pitch); };
  const ring = E.wilds.stones;
  E.setWatch('labour'); await wait(300);
  for (const s of ring.stones) {
    const ix = ring.cx + (s.x - ring.cx) * .55, iz = ring.cz + (s.z - ring.cz) * .55;
    stand(ix, iz, face(ix, iz, s.x, s.z), -0.05); await wait(120); E.cast(); await wait(700);
  }
  await wait(3000);
  const g = E.wilds.graves, fox = E.interactions.find(i => i.id === 'foxglove-water');
  stand(fox.x, fox.z, face(fox.x, fox.z, -340, 320), 0); E.skimStone();
  const ga = Math.atan2(-g.cz, -g.cx), gx = g.cx + Math.cos(ga) * 22, gz = g.cz + Math.sin(ga) * 22;
  return { answered: ring.answered, shots: [
    { name: 'a-pond-skim', x: fox.x, z: fox.z, yaw: face(fox.x, fox.z, -340, 320), pitch: -0.2 },
    { name: 'b-stones-answered', x: ring.cx - 16, z: ring.cz - 16, yaw: face(ring.cx - 16, ring.cz - 16, ring.cx, ring.cz), pitch: 0.12 },
    { name: 'c-pillar-from-rampart', x: 60, z: 372, y: 14.9, yaw: face(60, 372, ring.cx, ring.cz), pitch: 0.05 },
    { name: 'd-graveyard-gate', x: gx, z: gz, yaw: face(gx, gz, g.cx, g.cz - 3), pitch: -0.04 }
  ] };
})()
