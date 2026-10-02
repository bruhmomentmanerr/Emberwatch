**r128 — rooms you can see** · 2026-09-22 · phase 5, world depth

### Summary

rooms you can see. The owner: "there's weird clipping in all the interiors." Not clipping — one point lamp per room, physical falloff, so the shelf beside it blew out and the floor three metres away was black. Every walk-in room gets a second light now: dim, wide, cool, high, budgeted exactly like the first and only alive while you are inside. Warm pool against cold fill, which is the grammar the owner's reference clips use. Found while fixing it: the street kit's glTF callback could reach shaderWarmMs before that `let` had been evaluated, killing every kit piece — door surrounds, frames, banners, the lot — with nothing but a console warning. Declared early now. That race means some sessions have been running with the kit missing.

### In the code

- 1.70 MB (+2,211 bytes on r127).
- 1 function added: `interiorFill`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
