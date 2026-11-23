**r186 — every door opens** · 1.86.0 · 2026-11-23 · phase 5, world depth

### Summary

Every door opens. 1,313 shut house fronts become doors onto cells: rooms built on first entry in a pocket beyond the map's edge, with their own colliders and lamps, furnished as homes or for the quarter's trade (smithy, grain store, carter's yard, workroom). Doors 202 to 1,515. Verified: audits, unit tests, diagnostics against r185, cells walked and shot, frame time, boot time, variants 6/6, smoke.

### Patch notes

**State: r186 / 1.86.0, "Every door opens".** Built on r185. The owner asked
for the first four items of the remaining list: every door opens, clutter
where work happens, people using the place, and more sound, one revision
each, interiors to follow up after. This is the first.

### What was wrong

202 doors opened: the fifteen halls and the walk-in homes and shops (r113).
Every other house was a solid block with a painted door. Building a room
into each, as the walk-in homes are built, would cost what they cost a
hundredfold in geometry, lights and colliders.

### What changed

- **Cells.** Every house `wardHouse` builds (the infill's and the avenues')
  names its lot (`CELL_LOTS`). Once the city is final, `openCells` gives each
  one whose doorstep is clear a door record (`kind:'cell'`) in
  `interiorDoors`, so the offer, enter and leave paths are the ones every
  door uses. Of 1,544 houses, 1,313 opened; 231 had their doorstep taken or
  stood within 2.2 m of another door's.
- **Built on first entry, then kept** (`ensureCell`). Each house has its own
  slot in a grid beyond the map's edge (from x 900; the player is held
  within ±705 m) and 400 m up. Up there the movement code treats you as
  aloft and consults no street colliders at all, so a cell's colliders are
  gathered into its record (`COLLIDER_CAPTURE` in `addCollider` and
  `addBoxCollider`) and checked by `cellBlocked`; they never join the
  city's grid. Its floor is a stacked deck the room's size. It is laid at
  ground height and lifted as one group; its lamps carry the record as
  their `home`, so they light only while you are inside. It is drawn only
  then too. The map's clamp does not apply inside a cell.
- **What a room holds.** A home: r113's `furnishHome` (bed, hearth and its
  lamp, table and stools, shelf, rug) in r183's stone (`dressRoom`), boards
  underfoot. A traded house takes its quarter's trade, on flagstone:
  - Westreach, a smithy: the forge with its coals, hood and low orange lamp,
    an anvil, the quench barrel, a tool rack and a bench;
  - the New North, a grain store: sacks along the back wall, a grain bin,
    chests and a ladder;
  - the Long Southing, a carter's yard room: casks, harness on a rack, a
    mending bench;
  - Eastreach, a workroom: a workbench and stools, shelves, a chest.

  Counts: 1,230 homes, 29 yards, 27 smithies, 20 grain stores, 7 workrooms.
- Entering puts you just inside the cell's door at its floor; leaving puts
  you on the house's doorstep at the ground's height. A save made in a cell
  is saved on its doorstep. `EMBER.cells` exposes the doors, the built
  cells and `enter`/`leave` for probes.

### Not done, and next

- **Nobody is home.** The cells are empty of people; residents using rooms
  and furniture is the third item of this run (r188).
- A cell is bigger inside than a narrow house outside (at least 4.6 by 4.4
  m), as the old games' were.
- The 231 shut fronts, and the district buildings that are not `wardHouse`'s,
  stay shut.

### Validation

- **Source audits.** Every script block parses. Sections B and C are 0, and
  markup and script agree. All 726 functions are reachable, none dead, and no
  comment holds a call. Section A is 244, as in r185.
- **Unit tests** pass: switch frames, b9, Bluetooth pairing, and Lorax.
- **Diagnostics against r185**, same profile: doors 1,515 against 202 (the
  1,313 cells), none blocked; anchors 98, none blocked; gate approaches 4,
  none broken; colliders 13,167 and render calls at the spawn point 491,
  both as r185 (a cell adds neither until it is entered, and then only to
  itself).
- **Walked.** In a smithy and in a home: into each of the four walls for
  14 s; the player stayed inside the room every time and at its floor. Its
  lamps lit, and leaving put the player on the doorstep at ground height
  with the room hidden.
- **Looked at.** Six cells entered, one of each kind and a second home,
  from the door and from the back wall.
- **Frame time**, at a fixed standpoint in the Cinder Market, alternated,
  median of 30 frames under software rendering: r185 2,444 and 2,488 ms,
  r186 2,410 and 2,403 ms. Seven times the door records cost nothing that
  shows.
- **Boot time**, three runs each, alternated, from the game's own load
  report:
  - r185: 6.6, 6.5 and 6.9 s
  - r186: 6.8, 6.3 and 6.5 s
- **Variants** 6/6 built, and 6/6 boot and report r186.
- **Smoke check** clean: the game boots at r186, the Bluetooth chooser
  selects and cancels, pairing is confirmed and the WebGL context holds.
- The live source and its archive are byte-identical.

### In the code

- 8.37 MB (+10,172 bytes on r185).
- 6 functions added: `cellBlocked`, `ensureCell`, `enterCell`, `furnishCell`, `leaveCell`, `openCells`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
