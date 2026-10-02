**r162 — load time** · 1.62.0 · 2026-10-02 · phase 5, world depth

### Summary

Load time. Every landmark, kit piece and the forest used to warm the shaders of the whole scene, three light tiers each: 68 passes on one boot, 67 after the loader, 16.9 s. Now only the piece that arrived is warmed, and pieces arriving together share a pass: 2 passes, 0.56 s. Verified: audits clean; screenshots after load; variants 6/6. Not measured on Windows.

### Patch notes

**State: r162 / 1.62.0, sealed 2026-10-02 ("Load time").** The owner, on
r161: "why does it take a full minute to load? this isn't fallout 4". Also,
on the residents: "I do like the direction we're going with the NPCs, but
they still sort of look like geometric. I would like to just have them as
like modeled masses or something" — noted for after this, not started.

**Next:** the owner's launch on Windows, and the Plasma test from r161. Then
the residents as modelled masses rather than assembled shapes.

### Where the minute went

The shader warm-up. Every landmark, kit piece and the forest is parsed after
the loader has gone, and each one called `warmShaders()`, which compiled the
**whole scene** under each of the three light tiers. On one boot in the
harness (r161): 68 warm-up passes, 67 of them after the loader had gone,
16,872 ms of warm-up in all, 16,355 ms of it after the loader — the game
looking loaded and freezing in 200-300 ms steps behind it. On Windows each
new program is a Direct3D compile on top of that.

r162: a caller passes the piece it just added, and only that piece is
compiled (against the scene's lights, under each tier); pieces that arrive
in the same moment are warmed together on the next tick. With no piece (the
boot, a variant's `EMBER.warmShaders()`) the whole scene is. Same harness:
**2 passes, 556 ms in all, 132 ms of it after the loader.** Programs at the
end: 129 (r161: 131); the two left over compile the first time they are
drawn.

The harness cannot show what that is worth on a real GPU: under software
rendering each frame takes about 5 s, so long tasks after the loader came to
about 121-122 s on both builds. `loop()` itself was 4.2 s of that, over 22
frames. Not measured on Windows. The portable `.exe` still unpacks itself on
every launch (r161 §0f); the setup `.exe` does not.

### Verified

- `check-parse`, `audit-source` (B and C 0), `audit-dom`, `audit-dead`
  (669, 0 dead), `audit-comments`, `test-switch-frames`, `test-switch-b9`:
  clean.
- Screenshots after load, at the gate and in the citadel: the kit, lamps,
  landmarks (56) and sky all drawn; 0 errors.
- Variants 6/6 built, 6/6 booted.
- Bluetooth smoke: r162 passed 2 of 4 runs, r161 1 of 3 in the same
  container; every failure was the software GPU process exiting (a lost
  context or a timeout), on both builds.
- Not run: the runtime audit; a Windows launch.

### In the code

- 4.97 MB (+1,291 bytes on r161).
- 1 function added: `warmTiers`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
