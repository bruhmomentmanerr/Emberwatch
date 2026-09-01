**r79 — residents interiors** · 2026-09-01 · phase 5, world depth

In its own panel header: *r79 residents & interiors*.

### Summary

residents merged to 6 meshes from 16.1 — draw calls 3,386 -> 1,425 at the spawn; interior counters, the Great Hall dais and lectern, the shrine altar given the footprints they never had; a lintel above every interior door, which had all been open to the sky; Fawwk added to the strain library

### In the code

- 1.12 MB (+4,755 bytes on r78).
- 2 functions added: `interiorSolid`, `mergeTinted`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
