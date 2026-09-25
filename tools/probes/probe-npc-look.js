// Close visual QA for the resident kit. One frame per outfit makes the actual
// street silhouettes obvious without staging fake NPCs.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(resolve => setTimeout(resolve, ms));
  await wait(1800);
  E.setWatch('labour'); await wait(500);
  const outfits = ['hooded traveller','layered tunic','watch uniform','artisan apron','road vest','town dress','forge apron','scholar coat'];
  const peoples = ['gnome','human','long-ear','stonekin','mossfolk'];
  const outfitPeople = outfits.map(outfit =>
    E.villagers.find(person => person.outfit === outfit && person.smokes && !person.indoors) ||
    E.villagers.find(person => person.outfit === outfit && !person.indoors)
  ).filter(Boolean);
  const racePeople = peoples.map((people, species) =>
    E.villagers.find(person => person.species === species && !person.indoors)
  ).filter(Boolean);
  // Keep a close actor-level shot when a reported resident exists. It catches
  // grip/hand/readability regressions that an outfit-wide street shot can miss.
  const handFocus = E.villagers.find(person => person.name === 'Jarek Quarrier');
  const selected = [
    ...(handFocus ? [{ npc:handFocus, label:'hands-jarek-quarrier' }] : []),
    ...outfitPeople.map(npc => ({ npc, label:'outfit-' + npc.outfit.replaceAll(' ','-') })),
    ...racePeople.map(npc => ({ npc, label:'race-' + npc.people }))
  ];
  const shots = selected.map(({npc,label}) => {
    const distance = label.startsWith('hands-') ? 1.28 : 1.9;
    const x = npc.g.position.x - distance, z = npc.g.position.z - distance;
    return { name: 'resident-' + label, x, z,
      yaw: Math.atan2(-(npc.g.position.x - x), -(npc.g.position.z - z)), pitch: label.startsWith('hands-') ? -.08 : -.24 };
  });
  return { revision: E.diagnostics().revision,
    people: selected.map(({npc,label}) => ({ label, name: npc.name, people: npc.people, bodyType:npc.bodyType, outfit:npc.outfit, smoking: !!npc.smokes })), shots };
})()
