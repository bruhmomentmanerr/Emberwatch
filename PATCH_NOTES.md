**r124b — material and street logic** · 2026-09-21 · phase 5, world depth

In its own panel header: *r124 material & resident pass*.

### Summary

The second file archived as r124: the material and resident pass carried on into the street logic, on the way to r125. material & resident pass. Structured 128 px painted building materials, 82% balanced rendering (98% clear / 62% performance), tight warm bloom and the existing FXAA finish. Five peoples now have three build axes and eight job silhouettes; hooded people are rare, and props are fixed to animated arm pivots rather than clipping through bodies. City layout, road and collision generation untouched.

### In the code

- 1.48 MB (+7,281 bytes on r124).
- 6 functions added: `assignCarts`, `carryCart`, `cartGeometry`, `shopRoomCache`, `syncShopRooms`, `withBins`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
