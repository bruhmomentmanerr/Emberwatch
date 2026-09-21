**r126 — nothing left to roll** · 2026-09-21 · phase 5, world depth

### Summary

nothing left to roll. The owner: "I don't even want any part generated." The two remaining systems that move where anything stands — 268 outer residents walked down every arterial street, and the district compiler's 126 attempted lots — are baked the same way r125 baked the terrace walk. Proven with two fresh, never-used seeds: both give the exact city the fixed seed always has (shops 115, parcels 98, same shop sum, same resident-address sum). WORLD_SEED no longer moves a building, a shop or a resident anywhere. About fifteen worldRandom() calls remain, all decorative (texture dither, a ruin's rubble, which good sits on a counter) and none of them move a single fingerprint number — left as is, documented, not hidden.

### In the code

- 1.70 MB (+49,528 bytes on r125).
- 2 functions removed: `compilerLotClear`, `outerDistrictFor`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
