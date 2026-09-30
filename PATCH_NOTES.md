**r149 — the bell tower** · 1.49.0 · 2026-09-30 · phase 5, world depth

### Summary

the bell tower. The Cathedral of Hours' east tower, a solid block, is hollow and climbable: a door from the east aisle, a stone newel stair of ten flights to a belfry at 19 m, open arches, two bells, a lantern; a new capture from the belfry over the roofs. Walkable surfaces can be stacked: one marked so counts only within 1.5 m of the walker, so a stair can pass over itself. Verified: parse/audit/dead clean; walked door to belfry 14/14; runtime audit against r148, no errors, 102 dialogue branches none broken, road obstructions 0; all captures looked at; 6/6 variants built and booted; smoke clean (r149 in the title).

### Patch notes

**State: r149 / 1.49.0, sealed 2026-09-30 ("the bell tower").** Same
instruction again. With the city lit at night, the payoff for all of it is a
place high enough to look down on it, so r149 made one: the Cathedral of
Hours' east tower, climbed from inside.

**Next:** the towers of the Moon Archive and the Northwatch Guild, which are
still only outsides — stacked surfaces (below) make their stairs
straightforward now; stairs up to the outer wall's walk. The Windows
installers for r143–r149 have not been built.

### The bell tower

The east tower of the west front was a solid block of stone under its spire.
It is hollow now (`tools/assets/cathedral.py`, the `BELL_*` numbers): a door
from the east aisle into its foot; a square newel stair of stone steps
winding up the inside walls — ten flights of eight, 1.9 m each, a landing at
every corner — to a timber belfry floor at 19 m; open pointed arches on all
four faces (the west tower keeps its louvres, and its lit glow is what you
see across from the west arches); two bronze bells in a timber frame, a
lantern, and a lamp half way up the shaft. `cathedralBellTower()` lays the
walls as colliders with the door gap, and the steps, landings and floor as
surfaces from the same numbers. A new capture, `vista-cathedral-belfry`,
looks out of a south arch over the roofs, the chimney smoke and the citadel.

Two things found by walking it: the flights are a metre wide, and with a
body's half-metre radius the middle of a flight touched a wall collider set
on the masonry's face — the climb stalled on the third step. The colliders
sit 15 cm inside the masonry now. And the door was widened from 1.2 to 1.5 m
for the same reason.

### Stacked surfaces

`surfaceAt` took the highest walkable surface under you, which is right for
a deck or a rampart stair and impossible for a stair that passes over
itself: on the first flight you would have been lifted to the fifth. A
`SURFACES` record can now be marked `stacked`; given the walker's height
(`surfaceAt`'s new third argument, which only the player passes), a stacked
surface more than 1.5 m (`STACK_REACH`) above them does not count. Every
unmarked surface and every caller without a height — residents, captures —
behaves exactly as before. This is what any multi-storey interior needs.

### Verified

Read off runs on the sealed file, in the harness (software WebGL, the
standard profile's seed) unless it says otherwise.

- `check-parse`, `audit-source` (B and C 0; section A's new names are
  comment words), `audit-dom`, `audit-dead` (585 functions, 0 dead),
  `test-switch-frames`, `test-switch-b9`: clean.
- Walked: from the east aisle through the tower door, up all ten flights
  and onto the belfry floor, 14/14 legs; each flight's top read 1.9, 3.8,
  … 19.0 m, the floor 19.0.
- Runtime audit, r148 → r149: errors 0 → 0; villagers 374 → 374; draw
  calls 459 → 459; triangles 2,243,105 → 2,244,877; colliders 11,931 →
  11,939; doors 202 → 202; dialogue 17 wards / 102 branches, none
  failed; road obstructions in the carriageway 0 → 0, intruding 230 →
  231 — the new one is the tower's front-wall collider, which replaced
  its single block: the audit measures a box by its bounding circle, and that
  circle reaches the lane before the cathedral, but the box itself stops at
  the façade, as the block did.
- Shots looked at: the tower door from the aisle, the foot of the stair, a
  flight half way up, the bells, the view from three arches; all 15
  captures, the new belfry one among them.
- Variants 6/6 built, 6/6 booted. Smoke: game booted, WebGL, bridge,
  chooser installed, `requestDevice` settles, "Emberwatch — r149".
- Not run: `npm run dist` (no Windows toolchain here).

### In the code

- 2.99 MB (+35,632 bytes on r148).
- 1 function added: `cathedralBellTower`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
