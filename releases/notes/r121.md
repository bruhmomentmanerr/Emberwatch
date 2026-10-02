**r121 — the city takes shape** · 2026-09-20 · phase 5, world depth

In its own panel header: *r121 city kit*.

### Summary

the city takes shape. The generator now dresses its existing façades with authored stone surrounds, shutters, upper timber, hooded lanterns and rare verdigris panes. Rendering moves from a deliberately pixel/purple default to a glossy saturated low-poly cobalt night; mixed-stature residents smoke pipes. The city keeps its seed, nav, doors, collision and routes; the balance work first measured at r120 ships alongside it.

Also: **the city takes shape** — the first authored façade pass: stone door surrounds, framed shutters, heavy timber upper fronts, hooded lantern silhouettes and sparse verdigris leadlight; the renderer shifts to a glossy saturated low-poly night, then receives a clean-poly finish (higher default render buffer, trilinear/aniso texture filtering, tight bloom, less grit). The market has readable merchant bays, while a mixed five-people resident kit brings distinct silhouettes, faces, clothes, gait and pipes/smoke. The generator, seed and collision rules stay intact. Sealed after the full runtime audit and a 6/6 variant boot check; no r121 installer yet.

### In the code

- 1.43 MB (+55,211 bytes on r120).
- 4 functions added: `dressCityFronts`, `dressPoints`, `kitGeometry`, `update`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
