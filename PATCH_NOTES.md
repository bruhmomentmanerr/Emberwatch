**r168 — proportions** · 1.68.0 · 2026-10-03 · phase 5, world depth

### Summary

Proportions. The residents measured over 120 of them in head heights: 5.4 heads tall with hips at 2.5, big heads on short legs. Heads a fifth smaller, legs longer, widths a tenth less, women's shoulders narrower, thighs fuller at the top: humans now 7 heads, hips at 3.6. Verified: the measurements, studio and in-game shots, audits, variants 6/6, smoke.

### Patch notes

**State: r168 / 1.68.0, sealed 2026-10-03 ("Proportions").** The owner,
on r167: "continue, still stocky and skinny".

**Next:** the owner's look at the residents. Still open: rigid joints, and
clothes that are smooth tubes where the references' are loose and folded
(§0b). The Peak test of r167 is still owed (§0a).

### Measured, not guessed

r166 had answered "skinny" by making everything fuller and the heads
bigger, which made the figures stockier. This time the residents were
measured: a studio page builds 120 of them at rest and reports their
proportions in head heights (chin to crown), the unit figure artists judge
proportions in: height, hip height, shoulder span, the thickness of upper
arm, forearm, thigh and calf, chest, waist and hips.

| | r167 | r168 | a stylised-realistic adult |
|---|---|---|---|
| height (humans) | 5.6 heads | 7.0 | about 7 |
| height (all adults) | 5.4 | 6.55 | |
| gnomes | 4.6 | 5.45 | small people, big heads |
| hip height (humans) | 2.6 heads | 3.6 | about half the height |
| shoulders, men / women | 2.07 (both) | 2.26 / 2.09 | about 2.2 / 2.0 |
| thigh at the top, against hips | 0.57 / 1.35 | 0.73 / 1.45 (men) | two thighs about the hips |

Big heads on short legs read as stocky; thin thighs against wide hips, and
everyone's shoulders a man's, read as skinny and boxy. r168:

- **Heads** about a fifth smaller (humans `H` 1.18 to 0.94; every people's
  set from the table in `npcKitLook`), **legs** longer (humans `L` 0.92 to
  1.0, long-ears 1.04). Overall height is about the same, so doors, seats
  and interiors are unaffected.
- **Widths** about a tenth less for every people: with the smaller head the
  shoulders measured 2.4 heads, and 0.65 m in metres.
- **Women's shoulders** a tenth narrower than men's (`shape.shoulder`, used
  by `npcDims` and the torso's shoulder rings).
- **Thighs** fuller at the top, so the two together are about as wide as
  the hips, tapering to the same knee.

The measuring page is `measure.js` in the session's studio scratch; the
numbers above are read off it.

### Verified

- `check-parse`, `audit-source` (A 229, B and C 0), `audit-dom`,
  `audit-dead` (688, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- The measurements above; the studio row r167 against r168; the market
  lineup and close views in the game.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r168 in the title.
- Not run: the runtime audit.

### In the code

- 4.98 MB (+941 bytes on r167).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
