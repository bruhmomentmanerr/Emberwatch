// Anything standing on a carriageway, by what it is. auditRoadObstructions only
// counts colliders; a signboard, an awning or a lamp arm that carries no
// collider slips straight past it, which is how a notice board ended up in the
// middle of a street with every audit still reading clean.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 60 && !window.EMBER; i++) await wait(500);
  const E = window.EMBER; if (!E) return { error: 'no EMBER' };
  await wait(2500);
  const K = E.kit;
  const onRoad = (x, z, pad) => {
    for (const r of K.roads) { let t = (x - r.x1) * r.ux + (z - r.z1) * r.uz; t = t < 0 ? 0 : (t > r.len ? r.len : t);
      const dx = x - (r.x1 + r.ux * t), dz = z - (r.z1 + r.uz * t);
      if (dx * dx + dz * dz < (r.w * .5 + pad) * (r.w * .5 + pad)) return true; }
    const rad = Math.hypot(x, z);
    for (const g of K.rings) if (Math.abs(rad - g.r) < g.w * .5 + pad) return true;
    return false;
  };
  // Every lantern and every shop's own street furniture, tested directly.
  const lanterns = K.lanterns.filter(l => !l.removed && onRoad(l.x, l.z, .4))
    .map(l => ({ what: 'lantern', at: [+l.x.toFixed(1), +l.z.toFixed(1)] }));
  const shopBits = [];
  for (const s of K.shops) {
    if (s.lamp && onRoad(s.lamp[0], s.lamp[1], .3)) shopBits.push({ what: 'shop sign lamp', kind: s.kind, at: [+s.lamp[0].toFixed(1), +s.lamp[1].toFixed(1)] });
    if (s.shutter && onRoad(s.shutter[0], s.shutter[1], .3)) shopBits.push({ what: 'shop shutter', kind: s.kind, at: [+s.shutter[0].toFixed(1), +s.shutter[1].toFixed(1)] });
    if (s.frontX !== undefined && onRoad(s.frontX, s.frontZ, .3)) shopBits.push({ what: 'shop front point', kind: s.kind, at: [+s.frontX.toFixed(1), +s.frontZ.toFixed(1)] });
  }
  const awnings = (K.awnings || []).filter(a => onRoad(a.x, a.z, .3)).map(a => ({ what: 'awning valance', at: [+a.x.toFixed(1), +a.z.toFixed(1)] }));
  return { lanternsInRoad: lanterns.length, shopBitsInRoad: shopBits.length, awningsInRoad: awnings.length,
    sample: [...lanterns.slice(0, 6), ...shopBits.slice(0, 10), ...awnings.slice(0, 6)] };
})()
