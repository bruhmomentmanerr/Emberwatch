**r150 — bells ring the watch in** · 1.50.0 · 2026-10-01 · phase 5, world depth

### Summary

the bells ring the watch in. The cathedral's two bells are their own model (cathedral-bell) and swing when the watch turns: rung up, full, dying away, over 27 s. A landmark mover can swing as well as spin. Sixteen doves on the nave ridge and the spire drums go up when the bells ring, wheel over the church, and land back where they sat: one mesh for the flock, rewritten only while it flies. Verified: parse/audit/dead clean; a full ring read off at runtime, every dove back on its perch; runtime audit against r149, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r150 in the title).

### Patch notes

**State: r150 / 1.50.0, sealed 2026-10-01 ("the bells ring the watch in").**
Same instruction: keep modelling, build systems where they give the most
polish. The Cathedral of Hours has always been said to turn the watches with
its bells; until r150 the bells were part of a static model and nothing
happened when the watch turned but a line of text. Now the bells swing, and
the cathedral's doves go up.

**Next:** the towers of the Moon Archive and the Northwatch Guild, which are
still only outsides; stairs up to the outer wall's walk. The game has no
sound at all — the bells are the obvious first thing to hear, but sound is a
system of its own (a mixer, a mute, distance), not a one-off. The Windows
installers for r143–r150 have not been built.

### The bells swing

- The bells were modelled into `cathedral-furnishing`, merged with the pews
  and the frame, so they could not move. They are their own model now,
  `cathedral-bell` (`tools/assets/cathedral.py`): the headstock with its
  gudgeons and straps, the bell with two bands of moulding, the clapper; its
  origin is the pivot, under the frame's beam. 256 triangles.
- `cathedralBellTower()` hangs two as landmark movers — the second at three
  quarters the size — in bronze (metalness 0.82: at 0.55 the belfry lantern
  a metre away burnt them to a flat orange). `placeLandmark`'s mover path
  takes the point's scale now.
- A mover used to mean a wheel: `spin` radians a second. A mover with
  `swing` swings that far either side of hanging, at its own `period`
  (2.5 s the big bell, 2.1 s the small), scaled by `bellsRinging(t)`: 0 at
  rest, rung up over 4 s, full for 16, dying away over 7, eased at both ends.
  The angle is set from the clock, not accumulated, so a bell the player was
  too far away to update is right again the moment they are near.
- `applyWatch` calls `ringBells(t)` where it already showed "The bell turns
  to …". `EMBER.sky.bells(hold)` rings them from the harness; `hold` keeps
  them swinging for shots.

### The doves

Sixteen doves (`cathedralDoves`, `updateDoves`): ten along the nave's ridge,
three round each spire's drum on the side away from the flèche. When the
bells ring they go up — each after its own short delay, wings beating —
wheel over the church on circles round the flèche (a third of the ridge
birds inside the spires, the rest outside them), gliding and beating in
turns, banked into the turn, and three seconds after the bells stop they
come back down, each to where it sat. Nothing in the city is moved for them:
their variety is `planHash`, not the world stream.

- One mesh for the whole flock, rewritten only while it flies (at rest it is
  drawn once and left alone): 23 triangles a bird — a plump body, a round
  head, a tail, two wings of two panels that fold along the back.
- 1.8 × life, pale, with a faint cool emissive. At life size and unlit they
  were invisible against the night sky from the street: dark specks on a
  dark sky.
- A bird that strays into a spire or the flèche once clear of its perch is
  put back out on its surface.
- **The first version never flew on the harness.** `updateDoves` skipped
  its work once the flock was drawn at rest, except in the two seconds after
  a ring — and the harness draws a frame every three seconds, so it never
  saw those two. It wakes on the ring itself now.

### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are the
  `CATHEDRAL_BELL` asset marker and comment words), `audit-dom`,
  `audit-dead` (590 functions, 0 dead), `test-switch-frames`,
  `test-switch-b9`: clean.
- A full ring, unheld, the player at the parvis, sampled every few
  seconds: the bells read 0.34/−0.44, 0.59/0.04, 0.50/−0.70, −0.10/0.36 rad through the
  peal and 0 from 24.7 s on; all 16 doves airborne from the first sample,
  as high as 37.3 m and as far as 44.3 m from their perches, and all 16 back on them —
  0.00 m off — by 35.8 s. Rung with the player far from the cathedral, the
  doves went up and came back the same (every one on its perch by 42.4 s),
  and the bells, correctly, did not move.
- Runtime audit, r149 → r150: errors 0 → 0; villagers 374 → 374;
  draw calls 459 → 462 (the two bells and the flock); triangles
  2,244,877 → 2,245,477; colliders 11,939 → 11,939; doors 202 → 202;
  dialogue 17 wards / 102 branches, none failed; road obstructions in the
  carriageway 0 → 0, intruding 231 → 231.
- Shots looked at: the bells from the belfry mid-swing, before and after
  the bronze was darkened; both bells in their frame from the corner; the
  flock over the west front from the parvis, enlarged; the perched doves on the ridge and on
  a spire's drum, before and after they had heads; all 15 captures.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r150".
- Not run: `npm run dist` (no Windows toolchain here).

### In the code

- 2.99 MB (+10,021 bytes on r149).
- 5 functions added: `bellsRinging`, `cathedralDoves`, `doveShape`, `ringBells`, `updateDoves`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
