**r78 — road edges** · 2026-09-01 · phase 5, world depth

### Summary

kerbs stop at junctions instead of crossing through them; wall colliders flagged so the new road obstruction audit stops counting the city's own gates as obstructions; props nudged to the verge

### In the code

- 1.12 MB (+5,202 bytes on r77).
- 4 functions added: `auditRoadObstructions`, `emitKerbs`, `offRoad`, `onOtherRoad`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
