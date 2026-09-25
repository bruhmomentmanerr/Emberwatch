// Find residents standing inside one another, and say what put them there.
// A clump is any pair closer than 1.1 m — two bodies are about 0.8 m wide, so
// anything under that is visibly intersecting.
(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 60 && !window.EMBER; i++) await wait(500);
  const E = window.EMBER; if (!E) return { error: 'no EMBER' };
  await wait(2500);
  const look = async (watch) => {
    E.setWatch(watch); await wait(3500);
    const out = E.villagers.filter(v => !v.indoors);
    const pairs = [];
    for (let i = 0; i < out.length; i++) for (let j = i + 1; j < out.length; j++) {
      const a = out[i], b = out[j];
      const d = Math.hypot(a.g.position.x - b.g.position.x, a.g.position.z - b.g.position.z);
      if (d < 1.1) pairs.push({ d: +d.toFixed(2), a: a.name, b: b.name,
        at: [+a.g.position.x.toFixed(1), +a.g.position.z.toFixed(1)],
        aPaused: +(a.pauseLeft || 0).toFixed(1), bPaused: +(b.pauseLeft || 0).toFixed(1),
        aShop: !!a.shop, bShop: !!b.shop, aStay: !!a.stay, bStay: !!b.stay,
        aMeet: !!a.meetingWith, bMeet: !!b.meetingWith });
    }
    // how many distinct bodies are involved, and the worst pile
    const names = new Set(); pairs.forEach(p => { names.add(p.a); names.add(p.b); });
    return { watch, outdoors: out.length, pairs: pairs.length, bodies: names.size,
      worst: pairs.sort((x, y) => x.d - y.d).slice(0, 8) };
  };
  return { labour: await look('labour'), market: await look('market'), ember: await look('ember') };
})()
