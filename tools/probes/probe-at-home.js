// r114: residents who live in a walk-in home go in during the still hours
// instead of vanishing, can be spoken to from inside, and come back out onto
// their doorstep when the bell turns. Returns counts, one conversation, and
// inside shots of an occupied home.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-at-home.js 20 <shotsDir>
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = []; addEventListener('error', e => errors.push(String(e.message)));
  const key = code => dispatchEvent(new KeyboardEvent('keydown', { code, key: code.replace('Key', '').toLowerCase(), bubbles: true, cancelable: true }));
  await wait(2500);
  const homes = E.doors.filter(d => d.kind === 'home');
  const out = { errors, homes: homes.length,
    residentsLinked: E.villagers.filter(v => v.dwelling).length,
    occupiedHomes: homes.filter(h => h.residents && h.residents.length).length,
    households: homes.filter(h => /household’s home/.test(h.purpose)).length };
  E.setWatch('still');
  let atHome = 0, hidden = 0;
  for (let s = 0; s < 14; s++) {          // they have to walk home first
    await wait(5000);
    atHome = E.villagers.filter(v => v.atHome).length;
    hidden = E.villagers.filter(v => v.indoors && !v.atHome).length;
    if (atHome >= out.residentsLinked * 0.6) break;
  }
  out.still = { atHome, hiddenTheOldWay: hidden, visibleAtHome: E.villagers.filter(v => v.atHome && v.g.visible).length };
  const occupied = homes.find(h => h.residents && h.residents.some(v => v.atHome === h));
  if (!occupied) return out;
  const npc = occupied.residents.find(v => v.atHome === occupied);
  out.home = occupied.name; out.purpose = occupied.purpose; out.resident = npc.name;
  out.insideRoom = (() => { const dx = npc.g.position.x - occupied.cx, dz = npc.g.position.z - occupied.cz, co = Math.cos(occupied.ry), si = Math.sin(occupied.ry);
    const lx = dx * co - dz * si, lz = dx * si + dz * co; return Math.abs(lx) < occupied.w / 2 && Math.abs(lz) < occupied.d / 2; })();
  // From the street, they should not be offered through the wall.
  E.player.x = occupied.outsideX; E.player.z = occupied.outsideZ; E.player.y = 0; await wait(700);
  out.hintOutside = document.querySelector('#interactHint > span').textContent;
  key('KeyE'); await wait(900);                                        // in through the door
  out.hintInside = document.querySelector('#interactHint > span').textContent;
  out.altInside = document.getElementById('interactAlt').hidden ? null : document.querySelector('#interactAlt span').textContent;
  // Walk up to them from the middle of the room: a point between them and the
  // door can land in the bed, and the collision push-out can put you outside.
  { const dx = occupied.cx - npc.g.position.x, dz = occupied.cz - npc.g.position.z, len = Math.hypot(dx, dz) || 1, step = Math.min(1.2, len * 0.8);
    E.player.x = npc.g.position.x + dx / len * step; E.player.z = npc.g.position.z + dz / len * step; }
  await wait(600);
  out.hintNear = document.querySelector('#interactHint > span').textContent;
  key('KeyE'); await wait(500);
  out.dialogueOpened = document.getElementById('dialoguePanel').classList.contains('open');
  out.dialogueName = document.getElementById('dialogueName').textContent;
  key('Escape'); await wait(400);
  out.stillAtHomeAfterTalk = npc.atHome === occupied && npc.indoors;
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const shots = [{ name: 'at-home-inside', x: occupied.insideX, z: occupied.insideZ, yaw: face(occupied.insideX, occupied.insideZ, npc.g.position.x, npc.g.position.z), pitch: -0.1 }];
  // The bell turns: out onto the doorstep.
  E.player.x = occupied.outsideX; E.player.z = occupied.outsideZ; await wait(300);
  E.setWatch('labour'); await wait(1500);
  out.afterBell = { atHome: E.villagers.filter(v => v.atHome).length, residentVisible: npc.g.visible, residentIndoors: npc.indoors,
    residentOutsideRoom: (() => { const dx = npc.g.position.x - occupied.cx, dz = npc.g.position.z - occupied.cz, co = Math.cos(occupied.ry), si = Math.sin(occupied.ry);
      const lx = dx * co - dz * si, lz = dx * si + dz * co; return !(Math.abs(lx) < occupied.w / 2 && Math.abs(lz) < occupied.d / 2); })() };
  await wait(6000);
  const p0 = [npc.g.position.x, npc.g.position.z]; await wait(4000);
  out.afterBell.movedOn = +Math.hypot(npc.g.position.x - p0[0], npc.g.position.z - p0[1]).toFixed(2);
  // Back to the still hours, so they are home again for the shot: they are on
  // their doorstep, so they should go straight back in.
  E.setWatch('still');
  for (let i = 0; i < 120 && npc.atHome !== occupied; i++) await wait(500);   // since r115 they have walked off by now
  out.backHomeForShot = npc.atHome === occupied;
  out.shots = shots;
  return out;
})()
