**r45 — audit overhaul** · 2026-08-20 · phase 3, NPCs, collision, city compiler

In its own panel header: *r45 steady control deck*.

### Summary

Part of r36–r52: NPC conversations, city collision, seeded city compiler, test plans

### In the code

- 0.86 MB (+8,789 bytes on r44).
- 10 functions added: `boostSessionTime`, `boostTemperature`, `colliderBlocked`, `collidersAlong`, `collidersNearPoint`, `flushPending`, `loadGameState`, `perimeterWards`, `saveGameState`, `scheduleRefresh`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
