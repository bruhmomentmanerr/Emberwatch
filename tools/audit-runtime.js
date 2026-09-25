// One pass over everything that can only be checked with the game running.
(async () => {
  const out = { errors: [] };
  addEventListener('error', e => out.errors.push(String(e.message)));
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const key = code => dispatchEvent(new KeyboardEvent('keydown', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true }));
  const cls = id => { const el = document.getElementById(id); return el ? el.classList.contains('open') : 'NO ELEMENT'; };

  // ---- 1. world -----------------------------------------------------------
  const d = E.diagnostics();
  out.world = {
    revision: d.revision, parcels: d.city.parcels, buildingsInRoad: d.city.roadOverlaps,
    blockedAnchors: d.city.blockedAnchors, gates: d.city.gateApproaches,
    obstructions: d.city.roadObstructions, doors: d.runtime.doors,
    unreachableInteractions: d.interactions.unreachable,
    unreachableDetails: E.interactions.filter(entry => d.interactions.unreachable.includes(entry.id)).map(entry => ({
      id: entry.id, x: +entry.x.toFixed(2), z: +entry.z.toFixed(2), radius: entry.r,
      interior: entry.interior || null
    })),
    villagers: d.runtime.villagers,
    calls: d.renderer.calls, triangles: d.renderer.triangles, colliders: d.runtime.colliders
  };
  out.audit = E.audit();

  // ---- 2. panels and keybinds --------------------------------------------
  const panels = {};
  key('KeyJ'); await wait(60); panels.J_strains = cls('strainPanel'); key('Escape'); await wait(60);
  key('KeyM'); await wait(60); panels.M_menu = cls('settings'); key('Escape'); await wait(60);
  key('KeyP'); await wait(60); panels.P_puffco = cls('puffPanel'); key('Escape'); await wait(60);
  panels.allClosedAfterEscape = !cls('strainPanel') && !cls('settings') && !cls('puffPanel');
  out.panels = panels;

  // ---- 3. every dialogue branch, one resident per ward --------------------
  // Candidates per ward, not just the first resident. Since r109 the first one
  // can be a shopkeeper standing at a counter: teleporting beside them lands the
  // player inside the shop's collider, which pushes them out of talking range,
  // and the ward was reported as "didNotOpen" for a reason that had nothing to
  // do with dialogue. Keepers and indoor residents go to the back of the queue,
  // and a teleport that gets pushed away tries the next resident.
  const byWard = new Map();
  for (const n of E.villagers) if (n && n.g) { if (!byWard.has(n.district)) byWard.set(n.district, []); byWard.get(n.district).push(n); }
  for (const list of byWard.values()) list.sort((a, b) => (!!(a.shop || a.indoors)) - (!!(b.shop || b.indoors)));
  const seen = new Set(); let branches = 0; const broke = [];
  async function walk(npc, depth) {
    if (depth > 3) return;
    const buttons = [...document.getElementById('dialogueChoices').children];
    for (const b of buttons) {
      const label = b.textContent;
      if (/Leave the conversation|Return to the conversation/.test(label)) continue;
      const tag = npc.district + ' :: ' + label;
      if (seen.has(tag)) continue;
      seen.add(tag);
      const before = out.errors.length;
      b.click(); await wait(80);
      if (out.errors.length > before) broke.push(tag + ' -> ' + out.errors[out.errors.length - 1]);
      else branches++;
      await walk(npc, depth + 1);
      const home = [...document.getElementById('dialogueChoices').children].find(x => /Return to the conversation/.test(x.textContent));
      if (home) { home.click(); await wait(60); } else break;
    }
  }
  const didNotOpen = [], pushedAway = [];
  for (const list of byWard.values()) {
    let npc = null;
    for (const candidate of list.slice(0, 6)) {
      E.player.x = candidate.g.position.x + 1.3; E.player.z = candidate.g.position.z + 1.3; E.player.y = 0;
      await wait(500);
      if (Math.hypot(E.player.x - candidate.g.position.x, E.player.z - candidate.g.position.z) > 3) { pushedAway.push(candidate.district + ' :: ' + candidate.name); continue; }
      key('KeyE'); await wait(280);
      if (cls('dialoguePanel')) { npc = candidate; break; }
    }
    if (!npc) { didNotOpen.push(list[0].district); continue; }
    // Not compared against the npc we teleported beside: another resident is
    // often nearer, and the game correctly opens on them. What matters is that a
    // real name got written at all — the r85 failure left the markup's own
    // placeholder standing in the panel.
    const shown = document.getElementById('dialogueName').textContent;
    if (!E.villagers.some(v => v.name === shown)) broke.push(npc.district + ' :: panel showed "' + shown + '"');
    await walk(npc, 0);
    key('Escape'); await wait(100);
  }
  out.dialogue = { wards: byWard.size, branchesWalked: branches, didNotOpen, pushedAway, broke };

  // ---- 4. residents actually move, and do not pile up ---------------------
  E.player.x = 0; E.player.z = 200;
  const start = E.villagers.map(n => n.g ? [n.g.position.x, n.g.position.z] : null);
  const worst = [];
  for (let sample = 0; sample < 5; sample++) {
    await wait(6000);
    let w = 0;
    for (const a of E.villagers) {
      if (!a.g) continue;
      let near = 0;
      for (const b of E.villagers) {
        if (a === b || !b.g) continue;
        if (Math.hypot(a.g.position.x - b.g.position.x, a.g.position.z - b.g.position.z) < 2.2) near++;
      }
      if (near > w) w = near;
    }
    worst.push(w);
  }
  let moved = 0, total = 0;
  E.villagers.forEach((n, i) => {
    if (!n.g || !start[i]) return;
    const dist = Math.hypot(n.g.position.x - start[i][0], n.g.position.z - start[i][1]);
    if (dist > 1) moved++;
    total += dist;
  });
  out.residents = {
    count: E.villagers.length, movedOverThirtySeconds: moved,
    averageDistance: +(total / E.villagers.length).toFixed(1),
    worstClusterPerSample: worst
  };

  out.frames = E.renderer.info.render.frame;
  return out;
})()
