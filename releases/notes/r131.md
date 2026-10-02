**r131 — the plan redrawn** · 2026-09-22 · phase 5, world depth

### Summary

the plan redrawn. A Blender top-down of the exported city showed what screenshots never had: Vaneth was a bullseye. Concentric rings, four dead-straight avenues, every block a rectangle, every house the same footprint, every block interior a void, and the four quadrants mirroring each other. The lot table is rebuilt against that. Nine hand-placed quarters give character by nearest seed rather than by angle, so no quarter is another's mirror; building width spread goes from 2.8 m to 10.9 m, sheds through halls; 1,054 buildings now stand inside the blocks that used to be empty; and 95 segments of crooked lane cut through the lattice, two or three to a block, by pattern — spine, court, fork or left solid. 1,513 lots, up from 1,325, denser in every ring. Two latent crashes found on the way: sync() read a const still in its dead zone, and the function it read had a `node` out of scope, so it had never once run successfully. Verified: nothing floating, nothing buried, no building in a road, no blocked anchor, 149 walk-in doors all clear.

### In the code

- 1.64 MB (−3 bytes on r130).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
