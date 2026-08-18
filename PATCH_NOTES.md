**r16 — lorax fix audit** · 2026-08-18 · phase 1, Puffco BLE panel

In its own panel header: *r16 direct control*.

### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

### In the code

- 0.74 MB (+1,276 bytes on r15).
- 3 functions added: `clearPlaylist`, `disposeModel`, `releaseBlobURL`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
