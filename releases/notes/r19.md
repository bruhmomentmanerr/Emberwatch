**r19 — village profiles** · 2026-08-18 · phase 1, Puffco BLE panel

In its own panel header: *r19 control deck*.

### Summary

Part of r04–r19: Puffco BLE panel: diagnostics, autodetect, reconnect, auth retry, single-bond, Fahrenheit profiles

### In the code

- 0.75 MB (+7,479 bytes on r18).
- 7 functions added: `applyQuickProfile`, `setSpellToneFromFahrenheit`, `shareSmoke`, `showGameToast`, `updateVillagers`, `villager`, `writeProfileTemp`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
