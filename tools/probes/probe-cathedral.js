(async () => {
  await new Promise(r => setTimeout(r, 3000));
  const E = window.EMBER;
  if (!E) return { booted: false };
  // Stand on the z = -42 avenue looking toward the cathedral at (89, -46).
  E.player.x = 89;
  E.player.z = -42;
  E.player.y = 0;
  E.look(Math.PI, 0); // face north along the avenue
  await new Promise(r => setTimeout(r, 1000));
  return { shots: [
    { name: 'cathedral-avenue', x: 89, z: -42, yaw: Math.PI, pitch: 0 },
    { name: 'cathedral-close', x: 89, z: -60, yaw: Math.PI / 2, pitch: 0 }
  ]};
})()
