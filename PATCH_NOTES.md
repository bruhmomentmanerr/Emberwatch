**r46 — vaneth directors cut** · 2026-08-20 · phase 3, NPCs, collision, city compiler

In its own panel header: *r46 steady control deck*.

### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

### In the code

- 0.88 MB (+26,030 bytes on r45).
- 21 functions added: `anyOverlayOpen`, `cityLifeDetails`, `deviceAction`, `failedConnectCleanup`, `loadWayfinder`, `maybeDiscoverLandmarks`, `nextLandmark`, `npcPathClear`, `renderChronicle`, `renderLink`, `resetTouchInput`, `returnToNorthGate`, `saveWayfinder`, `setDeviceBusy`, `spellVillagerBarrier`, `talkSpotFor`, `toggleChronicle`, `updateGraphicsButton`, `updateWayfinder`, `wardAt`, `worldRandom`.
- 1 function removed: `triggerPuffcoBonding`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
