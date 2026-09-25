// Focused visual and numeric QA for the resident hand rig and trailing carts.
//
//   HARNESS_WINDOW_X=-3200 HARNESS_WINDOW_Y=0 \
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html \
//   tools/probes/probe-props-and-carts.js 5 <shotsDir>
//
// It deliberately checks the combinations that have historically looked like
// a dark board crossing an NPC: the forge apron/hammer, the scholar's book,
// the watch shield, and a working cart porter.
(async () => {
  const wait = ms => new Promise(resolve => setTimeout(resolve, ms));
  for (let tick = 0; tick < 60 && !window.EMBER; tick++) await wait(500);
  const E = window.EMBER;
  if (!E) return { error: 'Emberwatch did not boot before prop/cart QA began' };
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const errors = [];
  addEventListener('error', event => errors.push(String(event.message || event.error || 'window error')));
  await wait(1400);
  E.setWatch('labour');
  await wait(900);

  const outside = predicate => E.villagers.find(npc => !npc.indoors && predicate(npc));
  const jarek = outside(npc => npc.name === 'Jarek Quarrier') || outside(npc => npc.outfit === 'forge apron');
  const scholar = outside(npc => npc.outfit === 'scholar coat');
  const guard = outside(npc => npc.outfit === 'watch uniform');
  const hauler = outside(npc => !!npc.cart);
  const gripSummary = npc => {
    if (!npc) return null;
    const left = npc.parts.leftArm.userData.grip, right = npc.parts.rightArm.userData.grip;
    return { name: npc.name, outfit: npc.outfit,
      leftGripChildren: left ? left.children.length : -1,
      rightGripChildren: right ? right.children.length : -1,
      held: npc.held };
  };
  // Screenshots happen after a probe returns. Staging the four subjects on
  // collision-free ground and pausing them prevents a walker from crossing a
  // house, leaving the camera behind, before capture actually occurs.
  const blocked = (x, z, extra = .5) => E.colliders.some(collider => {
    const dx = x - collider.x, dz = z - collider.z;
    if (collider.box) {
      const lx = dx * collider.co - dz * collider.si, lz = dx * collider.si + dz * collider.co;
      return Math.abs(lx) < collider.hw + extra && Math.abs(lz) < collider.hd + extra;
    }
    return dx * dx + dz * dz < (collider.r + extra) ** 2;
  });
  const staged = [];
  const stageFor = index => {
    const baseX = E.player.x, baseZ = E.player.z;
    for (let radius = 7; radius < 70; radius += 2.5) for (let step = 0; step < 24; step++) {
      const angle = index * .83 + step / 24 * Math.PI * 2;
      const x = baseX + Math.sin(angle) * radius, z = baseZ + Math.cos(angle) * radius;
      const cameraX = x + Math.sin(angle) * 2.25, cameraZ = z + Math.cos(angle) * 2.25;
      if (blocked(x, z) || blocked(cameraX, cameraZ)) continue;
      if (staged.some(spot => Math.hypot(spot.x - x, spot.z - z) < 5.5)) continue;
      const spot = { x, z, cameraX, cameraZ, yaw: face(cameraX, cameraZ, x, z) };
      staged.push(spot); return spot;
    }
    return null;
  };
  const shots = [];
  const stageActor = (name, npc, index, cartView = false) => {
    if (!npc) return;
    const spot = stageFor(index); if (!spot) return;
    npc.pauseLeft = 20; npc.atStop = true;
    npc.g.position.set(spot.x, E.terrainAt(spot.x, spot.z), spot.z);
    // A local face points along +Z. Turn it toward the camera, so the palm and
    // held item are never hidden by the subject's own back.
    npc.g.rotation.y = Math.atan2(spot.cameraX - spot.x, spot.cameraZ - spot.z);
    npc.lastX = spot.x; npc.lastZ = spot.z;
    if (npc.cart) {
      npc.cart.position.set(spot.x - Math.sin(npc.g.rotation.y) * 2.45, E.terrainAt(spot.x, spot.z), spot.z - Math.cos(npc.g.rotation.y) * 2.45);
      npc.cart.rotation.y = npc.g.rotation.y;
    }
    const targetX = cartView && npc.cart ? (npc.g.position.x + npc.cart.position.x) * .5 : spot.x;
    const targetZ = cartView && npc.cart ? (npc.g.position.z + npc.cart.position.z) * .5 : spot.z;
    shots.push({ name, x: spot.cameraX, z: spot.cameraZ, y: E.terrainAt(spot.cameraX, spot.cameraZ) + 1.55,
      yaw: face(spot.cameraX, spot.cameraZ, targetX, targetZ), pitch: cartView ? -.05 : -.08 });
  };
  stageActor('forge-jarek-grip', jarek, 0);
  stageActor('scholar-book-grip', scholar, 1);
  stageActor('watch-shield-grip', guard, 2);
  stageActor('porter-cart-clearance', hauler, 3, true);
  const carts = E.villagers.filter(npc => npc.cart && !npc.indoors).map(npc => ({
    name: npc.name,
    outfit: npc.outfit,
    gap: +Math.hypot(npc.cart.position.x - npc.g.position.x, npc.cart.position.z - npc.g.position.z).toFixed(3)
  }));
  return {
    revision: E.diagnostics().revision,
    errors,
    grips: [gripSummary(jarek), gripSummary(scholar), gripSummary(guard)].filter(Boolean),
    carts: { count: carts.length, minGap: carts.length ? +Math.min(...carts.map(cart => cart.gap)).toFixed(3) : null,
      encumberedHaulers: carts.filter(cart => cart.outfit !== 'layered tunic'), samples: carts },
    shots
  };
})()
