**r105 — the whole protocol** · 2026-09-06 · phase 5, world depth

In its own panel header: *r105 the whole Switch protocol*.

### Summary

the whole Switch 2 protocol. All thirteen notification handlers and all thirteen command builders read out of the vendor bundle: the target temperature lives in a3, statistics in a2, custom profile points in aa/ab, and a write is always its read plus 0x10. Which exposed a real bug — the b9 frame is the entire settings block, and Emberwatch had been sending a body frozen from one capture, writing that evening's light mode, brightness, auto-shut-off, haptics and temperature unit over the owner's own every time a preset was pressed. It builds from the live state frame now. The panel names every frame type instead of shouting UNEXPECTED, and the raw-write preview names the opcode — b8 is a four-byte factory reset one nibble from b9.

### In the code

- 1.20 MB (+4,820 bytes on r104).
- 1 function added: `customPoints`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
