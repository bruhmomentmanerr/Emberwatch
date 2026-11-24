**r190 — a lamp on the table** · 1.90.0 · 2026-11-24 · phase 5, world depth

### Summary

A lamp on the table. A lantern and a warm lamp on every home's table, walk-in and cell, lit only while you are inside: mean brightness 11 to 23, near-black 81% to 65% over sixteen home shots. Verified: audits, unit tests, diagnostics against r189, homes shot and measured before and after, boot time, variants 6/6, smoke.

### Patch notes

**State: r190 / 1.90.0, "A lamp on the table".** Built on r189. The owner
asked for the interiors follow-up: the homes dark away from the hearth, and
the furniture's own forms (r191).

### What was wrong

A home, walk-in or cell, was lit by its hearth's lamp and the cool fill.
Away from the hearth it was nearly black: shot from the door and facing the
front wall, four walk-in homes and two home cells averaged a mean
brightness of 11 (of 255), and 81% of each frame was near black (under 15).

### What changed

- **A lantern on the table** (`furnishHome`): a small iron-framed lantern with
  glowing panes on the table, which stands on the bed side of the room, and
  a warm lamp inside its glass (`HOME_LANTERN`, power 0.42, range 5). It
  lights the half of the room the hearth does not. Like the hearth's, it is
  in the light budget only while you are inside (`home.lanternEntry`, set to
  the record by `openHomes`; a cell's lamps all carry its record). Every
  home has it, since the cells are furnished by the same function.
- The kit (`tools/assets/_kit.py`) gains a chamfer option for r191's
  furniture work; it is off unless a script sets it, and no model in this
  revision was rebuilt with it.

Measured on the same twelve walk-in shots and four cell shots, r189 to r190:
mean brightness 11.1 to 22.8; near-black share 80.8% to 64.5%. Every frame
of a home seen from its far side brightened (one, shot facing the front
wall, from 0.5 to 18.1). Inside a home cell all three lamps were confirmed
lit: the hearth, the fill and the lantern.

### Not done, and next

- **The furniture's forms**, r191.
- **Few households**: 33 residents in 30 cells.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 743 functions are reachable, none dead, and no
  comment holds a call. Section A is 243, as in r189.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Diagnostics against r189**, same profile: doors 1,515 (none blocked),
  anchors 98 (none blocked), colliders 14,431, render calls at the spawn
  point 491, all as r189.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r189: 6.9, 6.5 and 6.6 s
  - r190: 6.4, 6.8 and 6.5 s
- **Variants** 6/6 built, and 6/6 boot and report r190.
- **Smoke check** clean: the game boots at r190, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.39 MB (+1,036 bytes on r189).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
