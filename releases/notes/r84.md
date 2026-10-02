**r84 — rooms walls crowds** · 2026-09-03 · phase 5, world depth

In its own panel header: *r84 rooms, walls & crowds*.

### Summary

interior dressing: a prop vocabulary and a pass that scales with the room and seeds off its name (the Great Hall went 12 -> 58 colliders); continuous NPC separation, since the old unstick only ran while a resident was walking and never for one standing at its stop; a wall-aware road layer, roads through walls 232 -> 0; K copies a resident flow report

### In the code

- 1.14 MB (+14,618 bytes on r83).
- 20 functions added: `dressInterior`, `interiorBarrel`, `interiorBench`, `interiorCask`, `interiorChest`, `interiorCrate`, `interiorRack`, `interiorSack`, `interiorStool`, `interiorThrone`, `interiorTrestle`, `layRoad`, `nameSeed`, `npcCellKey`, `npcNeighbours`, `rebuildNpcGrid`, `residentFlowReport`, `roomRandom`, `sampleResidentFlow`, `throughWall`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
