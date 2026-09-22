**r134 — people in the square** · 1.34.0 · 2026-09-22 · phase 5, world depth

### Summary

people in the square. The owner's note on r133 was that the residents look weird, and that r133 had been thinking functionally where they were thinking aesthetically. Both were true: the residents walked and pathed and did not clip, and they still looked wrong. Portraits of one resident per species showed why. The head was a quarter of the figure and sat straight on the collar — there was a neck mesh, but it was 0.2 tall centred on headY while the head's underside reaches headY-0.12, so it had spent its whole life inside the head. Long-ear ears used a rotation of exactly ninety degrees, so a 0.43 cone starting 0.30 out reached 0.73 from the centre on a figure with 0.32 shoulders: wings. And every leg ended in a bare cylinder with no foot. All three fixed, the feet merged into the leg mesh so the draw calls are unchanged at 27,806. Aiming the portrait camera also caught a convention error that had quietly spoiled every look-at screenshot of the session: the camera's forward vector is the negation of the one residents face along. The market was thickened at the owner's request — it had twenty stalls and bays with counters, awnings, stock and lanterns, and nobody at a single one of them. Sixteen market people later the plaza holds 24.6 on average instead of 11.1. Two residents were found standing inside walls, having walked in: the shove that unsticks a stalled resident only pushed away from other bodies, so anyone stuck in geometry alone had no escape. Wedged 2 to 0, clumps 0, 319 of 342 walking.

### Patch notes

**State: r134 / 1.34.0, sealed 2026-09-22.** The owner's correction on r133
was exact and worth keeping in front of whoever reads this next:
*"no the npcs look weird, you're thinking functionally i'm thinking
aesthetically, thicken the market for sure."* r133 had proved the residents
walked, pathed and did not clip — and concluded they were fine. They were
fine, and they still looked wrong. **An audit that returns zero is not the
same as something looking right, and no metric in this project measures how a
resident reads.**

**Look at them before changing them — and check the camera first.** Portraits
of eight residents, one per species and build, are what this revision was
worked from. Aiming that camera exposed a convention error that had silently
spoiled every "look at X" screenshot taken this session: **`EMBER.look(yaw)`
drives a camera whose forward vector is `(-sin yaw, -cos yaw)`, the opposite
of the NPC facing convention `(sin ry, cos ry)`.** To point a camera at a
target from C, the yaw is `Math.atan2(C.x-T.x, C.z-T.z)`. Get the sign wrong
and the shot looks plausible — a street still looks like a street when you are
facing the other way down it — so nothing tells you except a subject that
never appears in frame.

**What the portraits showed, and what was done:**

- **A head a quarter of the figure tall, sitting straight on the collar.**
  There *was* a neck mesh: 0.2 tall, centred exactly on `headY`, while the
  head sphere's underside reaches `headY-0.12` — so the entire neck was inside
  the head and had never been visible. The neck is now 0.42 and dropped to
  bridge collar to jaw, and the head pivot is scaled to .86. **Scaling the
  pivot, not the sphere** takes the eyes, brows, nose, mouth, ears, hair and
  hats down with it, so nothing drifts off the face.
- **Long-ear ears stuck straight out sideways.** `rotation.z = side*PI*.5` is
  exactly horizontal: a 0.43 cone starting 0.30 out reached 0.73 from the
  centre line on a figure whose shoulders are 0.32. Wings, not ears. Shorter,
  and swept up and back off the skull.
- **Legs that stopped in the air.** Every resident ended in a bare cylinder.
  They have feet now, merged into the leg mesh the way the palm already merges
  into the sleeve — **draw calls are unchanged at 27,806**, measured against
  the r133 archive.

**The market is thickened.** It had twelve ring stalls and eight merchant bays
— counters, awnings, stock, lanterns — and **not one person at any of them**,
in a square whose ward text calls it "a dozen overlapping conversations".
Sixteen market people: eight keepers at the bay counters, four at the fire,
four walking the square. Twelve of them hold their ground, which a resident
with no route does, facing an anchor. **Plaza population went 11.1 to 24.6
average** (min 22, max 27) over eight samples in a 31 m radius.

**Two resident faults found on the way, both real:**

1. **Two residents standing inside walls**, permanently — Brother Cael in a
   0.3-thick chapel wall, and an outer resident in a shed. They are authored
   clear of it and *walk* in, so no spawn check can help. The shove that
   unsticks a stalled resident only pushes away from other **bodies**: someone
   stuck in geometry with nobody near them had no escape at all. They do now,
   and wedged went 2 to 0. **This same fix was written and then withdrawn
   during r133 because it appeared never to fire — it was validated against a
   test that did not exclude `npc.indoors`, so the only "buried" residents it
   saw were people at home in their own houses.** See §6.
2. **Two residents in the same spot, distance 0.00.** `navPlace` finds
   walkable ground and does not care who is already standing on it; adding the
   market keepers put one exactly on top of an existing resident. Spawning now
   spirals out until the spot is clear of geometry *and* of everybody else.

Verified: `inRoad` 0, `roadOverlaps` 0, `blockedAnchors` 0, doors clear, gates
0 broken, `errors` empty, 319 of 342 residents walking, 0 wedged, 0 clumps,
2 of 311 stalled (the same order as before any of this). Audits B 0 / C 0 /
dead 0, 6/6 variants, smoke clean.

**Still open:** the face itself is still two dots and a line, and hands are
still round mittens on straight arms — the next aesthetic pass, if the owner
wants one, is faces and arm rest poses. The seeded walk-in-home roll and the
world-seed UI wording remain open from r132.

### In the code

- 1.67 MB (+6,685 bytes on r133).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
