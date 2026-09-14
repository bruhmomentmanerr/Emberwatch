**r117 — mourners** · 2026-09-14 · phase 5, world depth

### Summary

the mourners. Somebody does go out to the Old Graveyard now: at the Working Watch bell two residents whose family has a legible stone walk out through the nearest gate, stand at the stone through the Still Hours with their head bowed, and walk home at the Ember Watch. The stone names whoever is standing at it; they tell you whose it is. Residents can carry a list of legs for a long walk, and walk on the terrain outside the wall. After a context-recovery reload the ward's welcome line no longer buries "The renderer recovered". The harness takes HARNESS_TIMEOUT for long probes; probe-soak-spikes records long- animation frames: none over 150 ms in three soaks, but three 306-345 ms frames in the next three soaks without it. Still open.

Also: **the mourners** — each day two residents whose family has a legible headstone walk out through a gate to the Old Graveyard, keep the Still Hours at the stone and walk home at the Ember Watch; residents walk on the terrain outside the wall; a context-recovery reload no longer buries its own message

### In the code

- 1.36 MB (+8,613 bytes on r116).
- 8 functions added: `chooseMourners`, `endMourning`, `graveSpot`, `headstoneFor`, `homeFromVigil`, `legsDone`, `mournGateFor`, `setOutToMourn`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
