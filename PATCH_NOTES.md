**r185 — violet round the moon** · 1.85.0 · 2026-11-22 · phase 5, world depth

### Summary

Violet round the moon. The Veilscar vista's moon sky (its difference 18.6 to 8.3) and left mountain (10.0 to 3.0): a new mood control, dramaMoon, a violet aureole round the moon, and the peaks tinted lighter and violet. Match score 58.6 to 61.7. Verified: audits, unit tests, diagnostics against r184, two variant sweeps, boot time, variants 6/6, smoke.

### Patch notes

**State: r185 / 1.85.0, "Violet round the moon".** Built on r184, the last
of the backlog run (r182 to r185). r180's list named the moon's sky and the
left mountain as the vista's worst regions.

### What was wrong

The vista shot on r184 (clouds held, a warm-up thrown away, r180's masks)
scored 58.6. By region, worst first: the moon's sky 18.6, the left mountain
10.0, the sky 9.0, the wizard 8.8. The moon's sky was a pale lilac where the
reference's is a deep, full violet (its a\* 22 against 35, its b\* −42
against −55): the dramatic sky's lit cloud runs to a pale colour fixed in
the shader. The left mountain was darker and greyer than the reference's lit
peak (lightness 29 against 34, a\* 9.6 against 16).

### What changed

- **`dramaMoon`**, a fourth mood control after r180's three, 0 by default so
  no other place changes: a saturated violet added round the moon, deepest
  in the lit cloud, fainter in the gaps (`uDramaMoon` in the sky shader).
  Swept in one boot per run with harness `before` scripts writing the live
  mood (`EMBER.moods`). A first, wider aureole cut the moon's sky to 7.9 at
  0.4 but bled onto the castle (1.6 to 5.7) and the sky (9.0 to 12.1). It
  was narrowed, and 0.5 chosen: of the five strengths tried it left the
  least difference over the moon's sky, the sky and the castle together
  (21.4, against 29.3 without it). 0.9 scored higher overall (62.2) but cost
  the sky 2 more.
- **The peaks lighter and violet**: their material's tint from a flat 1.6 to
  (2.0, 1.65, 2.3). Of three tints tried this one left the mountain least
  different (9.0 to 2.9 in the sweep).

### The match score

| | r184 | r185 |
|---|---|---|
| Overall | 58.6 | 61.7 |
| Moon's sky | 18.6 | 8.3 |
| Left mountain | 10.0 | 3.0 |
| Sky | 9.0 | 10.3 |
| Wizard | 8.8 | 8.7 |
| Valley | 5.2 | 5.1 |
| Rock | 2.3 | 2.4 |
| Castle | 2.0 | 2.3 |
| Cliff and falls | 1.7 | 1.7 |

### Not done, and next

- **The sky** (10.3) is now the vista's worst region, raised by the
  aureole's spread. **The wizard** (8.7) is less violet than the
  reference's (a\* 10 against 14, b\* −15 against −23).
- The owner asked for a list of what remains after this run; it is in the
  session's report, and the open items are in each section's "Not done".

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 720 functions are reachable, none dead, and no
  comment holds a call. Section A is 244, as in r184.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Diagnostics against r184**, same profile: doors 202 (none blocked),
  anchors 98 (none blocked), colliders 13,167, render calls at the spawn
  point 491, all as r184.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r184: 7.0, 6.9 and 7.3 s
  - r185: 6.8, 7.4 and 7.0 s
- **Variants** 6/6 built, and 6/6 boot and report r185.
- **Smoke check** clean: the game boots at r185, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.36 MB (+816 bytes on r184).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
