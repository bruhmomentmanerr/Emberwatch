**r174 — the chandler and the monk** · 1.74.0 · 2026-10-20 · phase 5, world depth

### Summary

The chandler and the monk. Muse's new residents and poses released with their fixes: Brother Fenwick a hooded monk in a brown habit; Bram, Sarella and Tallow given looks of their own; Dunna Wex's stall modelled in Blender, a trestle counter of lit candles and tapers, a drying frame and a dipping pot. Verified: every new resident from four sides, diagnostics, audits, variants 6/6, smoke.

### Patch notes

**State: r174 / 1.74.0, sealed 2026-10-20 ("The chandler and the monk").**
Between r173 and this session ten commits by Muse landed on `main`,
unreleased: new resident roles and poses, slimmer limbs, props that no
longer clip the hands, a weathering pass over the environment tiles, and a
read-only Bluetooth diagnostic page for the 2025 Proxy. The owner asked what
was wrong with them, then: "fix them and ship it as r174, use blender
workflow where applicable. make it look nice and polished." r174 is Muse's
work and the fixes to it, released together.

**Next:** the owner's look, and the **Peak test** of r172's connect sequence
(still owed). Then the ruin vista's land (r173's §0a). Seen in this
session's shots and not fixed: a hood's inner edge shows as a pale
sawtooth on the kit's hooded figures; Dunna wears glasses she was not
given (her look leaves them to chance).

### What was wrong with the new residents

- **Brother Fenwick, Bram Starling, Sarella of the Ninth Vow and Tallow of
  Foxglove Bank had no look of their own.** The kit dressed them at random
  from their variant: Fenwick, the Oathfield's lantern-carrying ritualist,
  came out a spiky-haired lad in a short tunic and striped stockings;
  Tallow had a sky-marked resident's wings and a wide hat.
- **Dunna Wex leaned over a counter that was not there.** Her pose, "tend
  wares", is the chandler at her stall; she stood in the middle of a lane.
- **The figure "sunk to the hips" beside Pip** was Tallow, whole and on the
  bridge deck, cut off by the parapet in a low camera. Not a bug in the
  game; the earlier camera stood below the deck.
- **"Bram renders standing"** was the same: a low camera in front of him.
  Shot from the side he sits, one knee up, one leg out.
- **Muse's comments were dated r175 to r178**, revisions that do not exist.
  They are r174 now.

### What r174 does

- **Looks for the four.** Fenwick a monk: a brown habit to the ankle, its
  hood up, a pale cord at the waist, clean-shaven. Bram a stargazer in a
  long midnight coat, bareheaded, a short beard. Sarella a long-eared woman
  in a plum rain cloak, hood up, over a violet dress. Tallow a gnome in a
  river-blue coat and a wide rain hat, a ginger beard. A look can now say
  `wings:false`, which keeps the canon's sky-marked wings off too.
- **Dunna's stall, modelled in Blender** (`tools/assets/chandler-stall.py`,
  bpy 4.5 as a Python module): a trestle counter with an amber cloth, a
  candle tree with five lit tapers, two lit pillar candles, bundles of
  tapers, beeswax and a basket of rushlights; a drying frame of tapers hung
  in pairs at her left; the dipping pot on its tripod over embers behind.
  2,710 triangles, 36 KB packed. It stands where she does, facing her way,
  with a warm candle light over the counter and colliders for the counter,
  the frame and the pot. The lane round it was mapped first (house wall on
  her right, clear on her left).
- **Sarella's oath.** Her hands came straight out in front of her; they
  come in now, resting on the raised knee.

### Measured

- The arm's turn about z, read off a run in the figure's own frame: a
  positive turn takes the left hand in and the right hand out. Dunna's
  hands at rest, Pip's pipe hand and Sarella's kneel all agree with it
  (Muse's signs were right; one attempt of mine to flip them was wrong and
  is undone).
- Boot, three runs each on this machine: r173 10.6, 10.8, 10.7 s against
  r174 10.6, 11.1, 11.0 s.
- Colliders 13,048: r173's 13,045 and the stall's three.

### Verified

- `check-parse`, `audit-source` (A 229, as in r173's run: the stall's
  asset marker adds a name, a comment Muse reworded drops one; B and C 0), `audit-dom`, `audit-dead` (704, 0 dead), `audit-comments`,
  `test-switch-frames`, `test-switch-b9`, `test-bluetooth-pairing`: clean.
- Every new resident shot from the front, both sides and behind: Pip,
  Tallow, Dunna at her stall, Fenwick, Sarella, Bram, Lysa, Morwen, Orren.
- Diagnostics: doors clear, no blocked anchors, the four gate approaches
  whole, the stall in the canon record.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r174 in its
  diagnostics.
- The Proxy diagnostic page (`tools/proxy-v2-ble-diagnostic.html`) sends
  only Lorax's seed request, unlock and read commands (0x00, 0x01, 0x10):
  nothing that writes device state. It is not part of the game.

### In the code

- 5.08 MB (+71,035 bytes on r173).
- 2 functions added: `chandlerStall`, `grimeTex`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
