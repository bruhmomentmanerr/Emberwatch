**r173 — the wizard and the lens** · 1.73.0 · 2026-10-06 · phase 5, world depth

### Summary

The wizard and the lens. Hold Z to look through a 45 degree lens, which the vista captures use too: the ruin vista through it, Orren large on the left, the castle and falls across the middle, the moon over the keep. Orren after the reference wizard: long white hair down his back, a dark drooping hat, a taller staff, nothing else in his hands. Verified: the zoom read off a run, the vista and Orren from three sides, a walk over the knoll, diagnostics, audits, variants 6/6, smoke.

### Patch notes

**State: r173 / 1.73.0, sealed 2026-10-06 ("The wizard and the lens").**
The owner asked what was holding the ruin vista back from matching the
reference to a tee, then said "continue". The walkthrough's order: the lens,
then Orren, then the land's scale. r173 does the first two.

**Next:** the owner's look, and the **Peak test** of r172's connect sequence
(still owed). For the ruin vista what remains is the land: in the reference
the cliff towers over the viewer's rock and the valley below is green, with
a river; ours is a 15 m cliff and a dark valley. A taller cliff means the
stair, the shelf and the keep go up with it. The castle over the river
bridge is the last of the three vistas furthest from their frames. Still
open on the residents: rigid joints, sleeve and trouser wrinkles, a skirt
that does not drape when its wearer sits.

### What was wrong

- **The lens.** The game sees 75 degrees up and down, 107 across, a very
  wide lens that shrinks everything in the middle distance. The reference
  is a phone frame through a narrow one, so its castle is large. Ours was a
  small castle in a wide night.
- **Orren.** His hat brim was a wide, pale lavender disc where the
  reference's is narrow, dark and drooping; his hair was short and grey
  where the reference's is long and white down his back; he held an open
  book in his other hand, the book his kind of resident carries; his staff
  ended at his hat.
- **Why the brim was pale.** Not its colour: the hat was already near black.
  The staff's crystal light hung forty centimetres over it. Read off the
  brim's pixel with each light switched off in turn, the crystal gave it two
  thirds of its light, the fill most of the rest.

### What r173 does

- **Hold Z to look closer.** A 45 degree lens where the eye sees 75, eased in
  and out, shown in the controls line. A capture can ask for a lens
  (`canonSetCapture`'s last argument; `EMBER.lens(fov)` holds one, and the
  harness applies a shot's `fov`), so a photograph of a place shows what
  holding Z there shows.
- **The ruin vista through it.** From three metres behind Orren and a step to
  his left, both on the knoll's crown (its level top widened from 3 to 5 m
  so he and the camera stand at one height): Orren large on the left, the
  castle and the three falls across the middle, the moon over the keep.
- **Orren.** Long white hair down his back to the shoulder blades, over his
  shoulders at the sides (a new hair style in the kit, `mane`); the
  wizard's brim narrower and drooping; his hat near black; nothing in his
  left hand; his staff taller, its crystal over his hat, and its light a
  third as strong (the crystal glows by itself). He stands on the crown now,
  watching the keep.

### Measured

- Hold Z, read off a run: 75 degrees at rest, 52.5 two frames into holding
  it, 45.0 at twenty; 67.5 two frames after letting go, 75.0 at twenty.
  `EMBER.lens(45)` gives 45 at once and clearing it gives 75.
- Walk, as a player: from the valley up the knoll to the crown (13.0 m),
  round behind Orren, down its front and on to the basin, 6 of 6. The rest
  of the Veilscar is as r172 walked it.
- Boot, three runs each, totals r172 7.66, 7.86, 8.26 s against r173 7.72,
  7.57, 7.51 s. Within the runs' spread (both slower than r172's own runs on
  an earlier machine).
- Colliders 13,045, as r172.

### Verified

- `check-parse`, `audit-source` (A 228, B and C 0), `audit-dom`,
  `audit-dead` (702, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The vista through the new lens in four framings; Orren from behind, the
  side and the front.
- Diagnostics: no unreachable interactions, nothing in a road, the four
  gate approaches whole, Orren on the knoll's crown.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r173 in its
  diagnostics.

### The pale square, seen again

A pale blue square about a hundred pixels across showed once more in a
harness screenshot, in empty sky in front of Orren. Standing at the same
place and reading the game's own finished frames six times over, the
square was not there. Both times it showed, the screenshot came straight
after the camera jumped; it has never shown in a frame read from the game
itself, and its colour is that of the moonlit cloud. Likely a stale patch
of an earlier frame in the software renderer's screenshot, not something
the game draws. Not confirmed.

### In the code

- 5.01 MB (+2,564 bytes on r172).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
