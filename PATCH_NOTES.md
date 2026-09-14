**r115 — audit fixes** · 2026-09-14 · phase 5, world depth

### Summary

the audit's fixes. The 2026-09-14 audit (run by a background agent on r113) found 16 things; this fixes 13. Switch 2: Start and Stop sent a remembered preset of 3, and a half-failed connect could still write the frozen capture body over the owner's settings — both gone; writes wait for the device's state; raw writes parse one byte at a time, so "-48" is no longer a disguised factory reset. Residents: 144 were parked on one-point routes and never pathed; now none, and those moving 25 m in two minutes went 94 → 229; the path queue served 11,749 requests a minute saturated, 18 residents never, and now 5,927 with none left out. Lights: one budget, exactly 5 or 14 lit at the gate and market in the base and every variant (Emberfall had 46); the light pool retired; homes no longer lit from the street. Moon shadows follow the player (84% of the city had none). Late-blocked homes stay shut. Long Night stopped firing on menu clicks; variant hotkeys stopped firing while typing; Ember Hour counts 12 arches; Wardens stopped sending you to door hinges. Door leaves cast no shadow: walking residents had set the Cinder and Keg's door swinging and restamping the shadow map. Cost against r114: market level, gate and pond about 1.2 ms slower on the harness. Seven dead functions deleted; tools/audit-dead.js; the Switch frame test now reads the real decode.

Also: **the audit's fixes** — the Switch panel no longer writes a remembered preset or the frozen capture body, raw writes parse strictly; residents who could not see a stop now walk (moved 25 m in two minutes: 94 → 229) and the path queue no longer starves; one light budget for the city and every variant, padded with dark lights; moon shadows follow the player; late-blocked homes stay shut; seven dead functions gone and `audit-dead.js` to find more

### In the code

- 1.35 MB (+3,189 bytes on r114).
- 1 function added: `followMoonShadow`.
- 7 functions removed: `building`, `canRestoreSavedPosition`, `keep`, `market`, `streets`, `town`, `worldLayoutFromSave`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. The Bluetooth device panel needs a secure origin, which a file opened from disk does not have; the desktop app in `app/` gives it one.
