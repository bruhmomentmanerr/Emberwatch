**r166 — faces and figures** · 1.66.0 · 2026-10-03 · phase 5, world depth

### Summary

Faces and figures. Heads redrawn after the owner's reference frames: a round wide skull, a small chin forward, all thirty-two faces repainted with large eyes (iris, pupil, catchlights, lashes, crease), slim brows, a small nose and mouth. One presentation per resident that hair, beard, face and body shape follow. Figures a tenth fuller, broader shoulders, shorter legs, larger heads and hands. Verified: studio and in-game shots against the references; audits; variants 6/6; smoke.

### Patch notes

**State: r166 / 1.66.0, sealed 2026-10-03 ("Faces and figures").** The
owner, on r165: "do you see what i mean? they're all very skinny and weird
and disproportionate, and the faces gotta be reworked".

**Next:** the owner's look. Still open on the residents: rigid joints (§0d),
and clothes that are painted tubes where the references' are loose and
folded. The Plasma test of r164's pairing fix is still owed.

### Against the references

The reference videos are still in the session uploads; frames were pulled
with the imageio ffmpeg binary in the scratch Blender venv. The girl in the
blue tartan dress and the pair under the meteors were the measure:

- **Faces.** Theirs: a round, wide skull, cheekbones as wide as the
  temples, a small chin standing forward, large eyes at mid-head with a big
  iris, a dark pupil and catchlights under a heavy lash line, slim brows,
  a small nose, a small mouth close to the chin. Ours: a narrow egg,
  longest chin to crown, narrow slit eyes, a tube of a nose standing off
  the face with its top above the eyes, and a long jaw below the mouth.
  r166: `NPC_HEAD_RINGS` redrawn (wider, rounder, the chin raised and
  forward, a flatter face front); all thirty-two painted faces redrawn
  (`npcFaceTile`): eyes about a sixth wider and far taller, the iris
  filling the eye lid to lid, a pupil, two catchlights, a heavy upper lash
  line with a flick, a lid crease, slim brows well above, a shadow under a
  small nose, a small mouth with a lower lip, shading under the
  cheekbones; the face projection a little lower; the nose small and
  round-tipped, between the eyes.
- **Who they are.** The kit chose hair, beard, face, body shape and dress
  each on its own, so one figure could carry a moustache with long red
  hair and lashes, or a bust with a beard. Every resident now has one
  presentation (`fem` in the look): a hand-made look may say; a beard
  says man, a dress woman, the town-dress trade women; otherwise the seed,
  a little under half women. Hair styles, beards (men only), faces (every
  third, the heavier-lashed, are women's: `NPC_FACES_MEN`), the jaw and the
  body's shape follow it. Wren Halloway, the reference's boy, is
  beardless. This re-rolls every unscripted resident's look.
- **Skinny.** About a tenth fuller for every people and build; the legs of
  humans and long-ears shorter; shoulders broader (the arms' pivots at
  0.19 W, the torso's shoulder line out to meet them); larger hands;
  heads about 5 % larger; the head lower on a fuller neck.
- Also: hair locks are chunkier clumps over a fuller cap, and use only the
  top of the hair tile, so long hair no longer has a pale band across it at
  the shoulders (the sheen stays a ring on the crown); a puffed sleeve has
  no shoulder cap on top of its puff.

Building the residents costs the same: `villager()` 1,237 and 1,156 ms on
r166 against 1,208 ms on r165, same session.

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (685, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- Studio head close-ups after each pass, against the reference frames; the
  full row r165 against r166; the market lineup and close views in the game.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r166 in the title.
- Not run: the runtime audit.

### In the code

- 4.99 MB (+3,924 bytes on r165).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
