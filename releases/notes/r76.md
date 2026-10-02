**r76 — device probe** · 2026-09-01 · phase 5, world depth

### Summary

wired the Electron Bluetooth chooser — the renderer had never answered select-bluetooth-device, so requestDevice() never settled and Connect hung in the desktop app; read-only BLE device probe; chooser handshake now covered by the smoke test

### In the code

- 1.11 MB (+12,107 bytes on r75).
- 4 functions added: `close`, `dismiss`, `probe`, `show`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
