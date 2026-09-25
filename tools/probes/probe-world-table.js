// The numbers behind PROJECT.md §4's world table, read off a running build, so
// the table can be refreshed from a run instead of copied forward. Run it on
// the default harness profile (the docs' seed, 2749632622) at the north gate.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-world-table.js 20
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  E.player.x = 0; E.player.z = 406; E.player.y = 0; E.look(0, -0.02);
  await wait(1500);
  const d = E.diagnostics(), a = E.audit ? E.audit() : null, info = E.renderer.info;
  let pointLights = 0; E.scene.traverse(o => { if (o.isPointLight) pointLights++; });
  return {
    revision: d.revision, seed: d.world.seed,
    districtsParcelsBuildings: [d.city.districts, d.city.parcels, d.city.buildings],
    innerInfill: E.inner || null,
    wilderness: d.city.wilderness,
    colliders: d.runtime.colliders, colliderGridCells: a ? a.cells : null,
    residents: d.runtime.villagers, doors: d.runtime.doors, homes: d.world.homes,
    interactions: d.interactions.total, shops: d.city.shops,
    roadRects: E.roads ? E.roads.length : null, rings: E.rings ? E.rings.length : null,
    drawCallsTrianglesTextures: [info.render.calls, info.render.triangles, info.memory.textures],
    pointLights, atmosphereParticles: d.runtime.atmosphereParticles,
    residentBatch: d.runtime.residentBatch, shaderWarmMs: d.world.shaderWarmMs
  };
})()
