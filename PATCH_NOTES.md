**r188 — at home after dark** · 1.88.0 · 2026-11-23 · phase 5, world depth

### Summary

At home after dark. Households are in their cells through the still hours, posed at the room's spots and ready to talk; a house's door is knocked at then and opens only if someone is home; residents sit on the benches by their doors at the ember watch. Verified: audits, unit tests, behaviour run in the game, diagnostics against r187, boot time, variants 6/6, smoke.

### Patch notes

**State: r188 / 1.88.0, "At home after dark".** Built on r187, the third of
the four the owner asked for (doors, clutter, people, sound).

### What was wrong

r186 opened the houses and r187 put things at their doors, but nobody used
either. Through the still hours a resident whose door had no walk-in room
went in at it and was simply not drawn, so the new cells were always empty.
The benches were never sat on. A house's door opened the same at every
hour.

### What changed

- **At home after dark.** Whoever went in at a cell's door is in that cell
  (`cellHousehold`): the residents who are indoors with no walk-in home and
  whose doorway is within 3 m of the cell's door. When you enter, they are
  placed at the room's spots and posed (`seatHousehold`, `poseAtHome`): in
  bed, at the table, tending the hearth or the forge. Every cell now keeps
  its spots, lifted with it: a home's from `furnishHome`, and a trade's of
  its own (the smithy's at the forge and the anvil, the grain store's by the
  bin and the sacks, the yard's on the mending stool and at the casks, the
  workroom's at the bench). They can be talked to as a walk-in home's people
  can, and when the watch turns they are back on their doorstep as before.
- **Doors that answer the hour.** In the working, market and ember watches a
  house's door opens to a hand on the latch, and its people are out at
  their day. In the still hours it is barred (`cellBarred`): the offer reads
  "knock at" and its button KNOCK (`offerLabel`, `offerButton`). If someone
  is home they let you in, with a word about the hour (`tryCell`); if
  nobody is, nobody answers.
- **The benches.** When the still hours end, the ember watch begins: the
  one the city spends visiting. A resident who comes out of a door with one
  of r187's benches within 4.5 m sits on it (`tryBench`), posed, for 40 to
  100 seconds by their name, then stands and walks on (`standFromBench`).
  They can be talked to while they sit. Each bench records its seat
  (`BENCH_SEATS`, 214).
- `EMBER.cells` gains `knock`, `household` and `benches` for probes.

### Not done, and next

- **Few households yet.** 33 residents have a door that opens on a cell,
  across 30 houses; most residents' doors are walk-in homes or none. Giving
  more of the city's houses a household is the way to fill the cells.
- **Shops with stock and coin** need a purse and an inventory for the
  player, which the game does not have; not started.
- Sound is the fourth item (r189).

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 735 functions are reachable, none dead, and no
  comment holds a call. Section A is 244, as in r187.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Behaviour, run in the game** (`p-people`): in the still hours a
  resident sent to her own door (Nessa Greenlatch) went in; knocking at her
  cottage let the player in and she was there, posed. A door with nobody
  home stayed barred. By day the same door opened. A resident with a bench
  by her door (Merrit Underhill), sent in at night, came out at the ember
  watch and sat on it; shot from the street.
- **Diagnostics against r187**, same profile: doors 1,515 (none blocked),
  anchors 98 (none blocked), colliders 14,431, render calls at the spawn
  point 491, all as r187.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r187: 6.8, 6.8 and 7.1 s
  - r188: 6.5, 6.9 and 6.8 s
- **Variants** 6/6 built, and 6/6 boot and report r188.
- **Smoke check** clean: the game boots at r188, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.38 MB (+4,599 bytes on r187).
- 7 functions added: `cellBarred`, `cellHousehold`, `seatHousehold`, `standFromBench`, `tryBench`, `tryCell`, `updateBenchSitters`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
