**r99 — the probe listens** · 2026-09-05 · phase 5, world depth

### Summary

the probe listens. The Dr. Dabber notes settled where to write on a Switch 2 and left one question open — what the device says first, since drdabber.app has both an initialPacketStackReceivedAtom and a bluetoothDeviceAuthenticatedAtom. After its survey the probe now subscribes to everything that can notify and prints twenty seconds of traffic, timestamped. That is the read-out the notes ask for, and it is the honest limit of what can be built without the hardware: the UUIDs are the app's own constants, the packet format is not in the bundle, and this project has no Switch 2 to watch.

### In the code

- 1.16 MB (+2,060 bytes on r98).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
