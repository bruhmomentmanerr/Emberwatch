**r165 — facing out** · 1.65.0 · 2026-10-03 · phase 5, world depth

### Summary

Facing out. Every sleeve, thigh, shin and boot had been built inside out since r159 (lofts written top to bottom face inward); loft now orders its rings. Hands, thumbs, toes, beards, human ears and staff feet end in round domes, not points. Boots follow the shin front, side and back; thighs start inside the hips; shoulder caps lower; necks shorter. Verified: a loft normals test, studio close-ups before and after, in-game lineup, audits, variants 6/6, smoke.

### Patch notes

**State: r165 / 1.65.0, sealed 2026-10-03 ("Facing out").** The owner, on
r164: "loads better now, push some more npc fixes".

**Next:** the owner's look at the residents; the Plasma test of r164's
pairing fix is still owed. The residents' joints are still rigid pieces
(§0d says what a continuous body would take).

### What the residents still got wrong

Shot close in a brightly lit studio page built from the kit, front and
three-quarter, the figures had faults that night hid:

- **Half the body was inside out.** `NpcMesh.loft` builds an outward
  surface only from rings written bottom to top. Every sleeve, thigh, shin
  and boot was written from the joint down, so since r159 each was built
  facing inward: normals and winding both reversed. A small test with the
  kit's own code showed it plainly (rings ascending: 39 normals out, 0 in;
  descending: 0 out, 39 in). From outside you saw the far inner wall, lit
  backwards, and whatever was inside showed through it: the leg through
  the boot (the boot looked like a dark band with the stocking showing
  below it), the arm's skin through its sleeve. Much of the flat,
  geometric look was this. `loft` now orders its rings, so a loft faces
  out whichever way it is written.
- **Points.** Every hand, thumb, toe, beard lock, human or gnome ear and
  staff foot narrowed to a point and read as a spike. `tube` takes
  `cap:'round'` (`npcRoundEnds`): an end that closes to nothing becomes a
  dome over its last span. Hair locks, elves' ears, hat tips and feathers
  keep their points. The hand is a fuller mitten with the thumb laid along
  it.
- **Boots cut by the calf.** A boot ring took the shin's side radius only,
  so a calf deeper than it is wide came through the leather in a sawtooth.
  Each boot ring is now the shin's own front, side and back at that height,
  plus the leather.
- **What facing out uncovered:** thighs wider than the hips at the top
  stood off the seat in flaps; they now start inside it. The shin's top
  sits inside the thigh at the knee.
- **Shoulder caps** stood above the sloped shoulder like pads; lower, and
  leaning out with the slope. Their pattern is laid on from above (a check
  wrapped round the cap gathered to a bullseye on top).
- **Necks** looked long on the sloped shoulders: the head stands at
  0.585 T above the hip (was 0.6), on a fuller neck.

Building the residents costs a little more for the domes and the fitted
boots: `villager()` over a boot, in this session's harness, 1,088 and 1,073
ms on r164 against 1,281 and 1,140 ms on r165. One boot read "loaded in 6.0
s · page 0.3 · world 1.9 · people 1.9 · lamps 0.3 · first frame 1.7"
(this session's container runs faster than the last one's; compare within
a session only).

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (685, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The loft normals test above, before and after.
- Studio close-ups, ten residents front and three-quarter, before and
  after each fix; head close-ups front and back. The market lineup in the
  game.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r165 in the title.
- Not run: the runtime audit.

### In the code

- 4.99 MB (+3,511 bytes on r164).
- 1 function added: `npcRoundEnds`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
