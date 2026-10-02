**r104 — ramparts** · 2026-09-06 · phase 5, world depth

### Summary

ramparts. Both walls walkable: surfaceAt() gives the world surfaces above y=0, gravity lands on them, street-level colliders stop applying once you stand on top of them. Climbed 0->12.9 and 0->14.9, walked 65 and 67 units of circuit. Curved ramparts need solid edges — a tangent leaves a 4 m walkway inside thirty paces. Also: downloaded the vendor bundle and replaced the guessed a9 field map with their parser. Temperature is 16-bit Fahrenheit across bytes 10-11; the reported "drops to zero then climbs" was the low byte wrapping at 256 F. b5 is the heating profile, not a temperature.

### In the code

- 1.19 MB (+6,054 bytes on r103).
- 3 functions added: `stairAt`, `surfaceAt`, `walkAt`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
