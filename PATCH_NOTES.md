**r125 — the city holds still** · 2026-09-21 · phase 5, world depth

### Summary

the city holds still. innerInfill's live terrace walk — worldRandom() rolls for every house and shop's width, depth, storeys, material, accent and whether it became a shop, one after another down every street — is retired. The walk was run once and its exact output frozen into a table (CITY_LOTS_BUILT / CITY_LOTS_VACANT); innerInfill replays it. Same city, verified house-for-house and shop-for-shop against the live build it replaced, but it can no longer reshuffle when something else changes, and any one lot is now a line in a table instead of a hash to reverse-engineer. First step of a larger, explicit move away from procedural generation toward one hand-finished map; the rest — residents, wilderness, clutter, the roads and districts themselves — is still generated and is the next phase, not this one.

### In the code

- 1.65 MB (+171,442 bytes on r124b).
- 1 function removed: `frontageClear`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
