(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(3000);
  const out = {}, toast = () => (document.getElementById('gameToast') || {}).textContent || '';
  const S = E.shops, d = E.diagnostics(), a = E.audit();
  const byKind = {}; S.forEach(s => byKind[s.kind] = (byKind[s.kind] || 0) + 1);
  const r = s => Math.hypot(s.x, s.z);
  out.shops = { total: S.length, diagnosticsField: d.city.shops, byKind,
    insideOldWall: S.filter(s => r(s) < 240).length, betweenWalls: S.filter(s => r(s) >= 240).length,
    nearCinderMarket: S.filter(s => Math.hypot(s.x, s.z - 108) < 90).length,
    withKeeper: S.filter(s => s.keeper).length };
  out.world = { inRoad: d.city.roadObstructions.inRoad, blockedAnchors: d.city.blockedAnchors, roadOverlaps: d.city.roadOverlaps,
    blockedDoors: a.blockedDoors, doorsClear: a.doorsClear, interactions: d.interactions.total, unreachable: d.interactions.unreachable.length };

  const visit = s => { const e = E.interactions.find(i => i.act && i.x === s.frontX && i.z === s.frontZ); e.act(e); return toast(); };
  const keeperDist = s => s.keeper ? Math.hypot(s.keeper.g.position.x - s.frontX, s.keeper.g.position.z - s.frontZ) : null;

  E.setWatch('still'); await wait(800);
  const sample = S.find(s => s.keeper && r(s) < 240) || S[0];
  out.still = { toast: visit(sample), label: E.interactions.find(i => i.x === sample.frontX).label() };

  E.setWatch('market'); await wait(35000);
  const keepers = S.filter(s => s.keeper), atCounter = keepers.filter(s => keeperDist(s) < 4.5);
  out.market = { keepers: keepers.length, atTheirCounterAfter35s: atCounter.length, label: E.interactions.find(i => i.x === sample.frontX).label() };
  const present = atCounter[0];
  if (present) { E.player.x = present.frontX + 1; E.player.z = present.frontZ; out.market.visitWithKeeper = visit(present); }
  const flow = E.flow();
  out.flow = { residents: flow.residents, stalled: flow.stalledCount, clusters: flow.clusterCount };
  return out;
})()
