**r71 — stability access** · 2026-08-31 · phase 5, world depth

In its own panel header: *r71 stability & access*.

### Summary

full-world doorstep repair; zero blocked anchors; safer app:// containment; leaner permissions; WebGL context recovery; reduced-motion and diagnostics

### In the code

- 1.08 MB (+1,828 bytes on r70).
- 1 function added: `emberDiagnostics`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
