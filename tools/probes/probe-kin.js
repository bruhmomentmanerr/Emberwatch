(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms)), T = E.terrainAt;
  await wait(3000);
  const toast = () => (document.getElementById('gameToast') || {}).textContent || '';
  const houses = [...new Set(E.villagers.map(v => v.household).filter(Boolean))].sort();
  const read = E.wildMemory().graves;
  const graves = E.interactions.filter(i => /^grave-/.test(i.id));
  // find a grave whose household nobody has read yet
  let chosen = null;
  for (const g of graves) { const k = Number(g.id.slice(6)); const house = houses[k % houses.length]; if (!read.includes(house)) { chosen = { g, house }; break; } }
  if (!chosen) return { note: 'every legible stone already read in this harness profile' };
  E.player.x = chosen.g.x; E.player.z = chosen.g.z + 1; E.player.y = T(E.player.x, E.player.z);
  chosen.g.act(chosen.g);
  const text = toast();
  const kin = E.villagers.find(v => v.household === chosen.house && !v.indoors);
  const kx = kin.g.position.x, kz = kin.g.position.z;
  E.player.x = kx + 1.2; E.player.z = kz; E.player.y = T(kx + 1.2, kz); E.look(Math.atan2(1.2, 0), 0); await wait(250);
  window.dispatchEvent(new KeyboardEvent('keydown', { code: 'KeyE', bubbles: true })); await wait(400);
  const lines = (document.getElementById('dialogueLines') || {}).textContent || '';
  return { read: text.slice(0, 60), kin: kin.name, mentionsGraveyard: /graveyard/.test(lines) };
})()
