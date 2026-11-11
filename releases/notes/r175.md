**r175 — fez and the connection deadline** · 1.75.0 · 2026-11-10 · phase 5, world depth

### Summary

Fez: Rainbow Belts × Moroccan Peaches, delivered once. Lorax write deadline and capability selection fixed; GitHub updates audited, wizard mesh study continues.

### Patch notes

**State: r175 / 1.75.0, "Fez and the connection deadline".** Reconciled with
GitHub main at 05ab7cb, including the post-r174 Dunna sculpt. The old local
r171 studio prototype was rejected and is not brought forward.

### What changed

- Fez arrives once in the journal, with Patrick's supplied lineage:
  Rainbow Belts × Moroccan Peaches. Form and effects are unspecified.
- A Lorax request deadline is observed even while a native write is pending;
  a stalled write no longer strands the timeout. GATT write mode selection
  respects device capabilities. r172's newer connection sequence is preserved.
- The new test covers six simulated connection outcomes, including the
  failure reproduced against current GitHub main. Physical Peak testing is pending.

### Wizard continuation

The rejected smooth studio wizard is not shipped. A new Blender rest-mesh
study follows the hooded dark-fantasy reference in hall-01-f00079.png.
It is a draft asset, not an animated NPC or a completed reference match.
The remaining work is surface detail, hands, rigging, staff grip and seated
cloth. See docs/2026-11-10-AUDIT.md for the full findings and boundaries.

### Validation

The baseline source audits passed. The updated simulated Lorax test passes
all six cases. Fez passed real-renderer checks for visible lineage, no duplicate
on reload and persistent removal. The same runtime check confirms the upstream
Dunna sculpt loads; her joints remain static by that implementation's design.
The final audit passes, all six variants boot and report r175, and the desktop
Bluetooth smoke check opens the chooser and settles cancellation. Live source
and its new archive are byte-identical. Installer/portable publication is
performed by the Windows release workflow after the push.

### In the code

- 5.18 MB (+109,625 bytes on r174).
- 1 function added: `swapDunnaSculpt`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
