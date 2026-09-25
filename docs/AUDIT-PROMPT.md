# Emberwatch — read-only audit prompt

Hand this to a fresh agent session. It reads and understands the whole project,
audits it, and reports — without touching the source tree.

---

You are auditing **Emberwatch**, at `D:\_KEEP\Emberwatch`. Your job is to read
it until you genuinely understand it, then find what is wrong with it. You are
not fixing anything this session.

## Hard constraints

**Do not create, modify, or delete a single file inside `D:\_KEEP\Emberwatch`.**
Not a typo fix, not a comment, not a doc update. If you find something worth
changing, describe the change — do not make it.

Three commands would break that rule, so never run them:

- `node variants/build-variants.js` — overwrites the six variant HTML files
- `node tools/make-icon.js` and `node tools/make-ico.js` — overwrite `app/build/`
- `npm run dist` (or any `electron-builder` invocation) — writes `app/dist/`

Everything else in `tools/` is read-only and safe to run. `cd app && npm start`
and the smoke test are also fine — they run the app, they do not edit it.

There is **no git here**, so there is no undo. The archived files in
`revisions/` are the only history. This is why the constraint is absolute
rather than a preference.

## Your workspace

Create your own folder and work in it:

    D:\_KEEP\Emberwatch-audit\<today's date>\

**Experiment freely in there and make as many mistakes as you like.** Copy
whatever you need into it — `app/renderer/index.html`, a variant, a tool — and
hack the copies apart to test a theory. Deleting a function from *your copy* to
see what breaks is exactly the right move; deleting it from the real one is not.
Put your scratch scripts, probe files, notes and the final report there too.

## Phase 1 — understand it before you judge it

Read in this order. Do not skim, and do not start forming findings until you
have finished this phase.

1. `PROJECT.md` — the full rundown. Architecture, conventions, traps, how to
   ship. This is the map.
2. `CLAUDE.md` — the five rules that must never be missed.
3. `RESUME-AFTER-REINSTALL.md` — the *why* behind the load-bearing decisions.
   Most of them exist because something broke once. This is the file that stops
   you "fixing" something into a bug that already happened.
4. `CATALOG.md` — the folder map and the full revision timeline, from r04 to
   whichever revision is marked `<- current`.
5. `docs/dr-dabber-switch2-frames.md` — the device protocol, fully decoded.
6. `NIGHT-LOG.md` — recent unattended work, newest first.
7. `app/main.js` and `app/preload.js` — small, and they explain why Electron is
   here at all.
8. `app/renderer/index.html` — the game. ~1.38 MB, two `<script>` blocks. The
   first is the generated three.js r186 engine bundle; **skip it**, but read
   `tools/three-vendor/entry.js` and its history note (the r128-look layer it
   once carried was retired in r111). Read the gameplay block (the second
   `<script>`; `node tools/check-parse.js` prints its line) properly.

Things worth holding in your head while you read the gameplay block:

- It is **one IIFE under `'use strict'`**. Nothing is on `window` but `EMBER`.
  A call to a function that no longer exists is a *runtime* error the parser
  never sees, so the file parses perfectly while a feature is silently dead.
  That has happened three times in this project.
- Static geometry goes through a merge batcher (`collect`, `aBox`, `aCyl`,
  `aCone`, `aRoof`, `mergeAll`). Loose meshes are only for things that move.
- Two walls: `CITY_RADIUS = 240` and `OUTER_WALL_R = 380`. Anything describing
  physical size must be in metres, not degrees — a gate width in degrees is a
  different gate on a different radius, and that shipped once.
- Roads carry no colliders. `onRoad(x,z,pad)` tests a **point**; a building is
  not a point.
- `surfaceAt(x,z)` is what makes anything above y=0 walkable.

When you finish Phase 1, write `understanding.md` in your folder: the
architecture in your own words, the data flow from world-build to render, and
the five things you are least sure about. If you cannot explain how a resident
decides where to walk, you are not done reading.

## Phase 2 — run what already exists

These all run against the real tree and write nothing:

```bash
node tools/check-parse.js
node tools/audit-source.js
node tools/audit-dom.js
node tools/audit-dead.js
node tools/test-switch-frames.js
node tools/test-switch-b9.js
```

Then the runtime audit, through the Electron harness in `tools/harness`:

```bash
app/node_modules/.bin/electron tools/harness <path-to-html> <path-to-probe.js> <seconds> [shotsDir]
```

If your probe returns `{ shots: [{ name, x, z, yaw, pitch }] }` and you pass a
`shotsDir` inside your own folder, it saves a screenshot at each — use it to
look at what you are auditing. `node tools/check-variants.js` boots all six
variants the same way and is also read-only.

`tools/audit-runtime.js` is the big one — world diagnostics, panels, every
dialogue branch in every ward, resident movement and clustering. Write your own
probes into your folder and run them the same way.

Two things that will mislead you:

- **`backgroundThrottling` is off in that harness for a reason.** A hidden
  browser pane does not run rAF, so every input reads as doing nothing. That is
  the pane, not the code.
- **Parsing is not evidence, and neither is a passing audit.** Drive the thing.

Record what each tool reported. If a tool disagrees with a doc, that is itself a
finding.

## Phase 3 — audit independently

The existing tools cover what has already gone wrong. Your value is in what
they do not check. Some directions worth taking, not a checklist:

- **Dead paths.** Is anything reachable only from a condition that can no longer
  be true? Section B/C of `audit-source.js` catch the easy cases; a function
  called only from inside another dead branch is not caught.
- **Docs against reality.** Every number in `PROJECT.md` and `CATALOG.md` claims
  to have been measured. Measure them again. Report anything that has drifted —
  this project has published a wrong number before and had to retract it.
- **Invariants that are enforced in one place but not another.** The doorway
  rule, the road-footprint rule, and the metres-not-degrees rule are each
  enforced at some call sites. Are they enforced at all of them?
- **The seed.** The world is seeded. Does anything behave differently across
  seeds in a way that suggests a latent placement bug? You can set a seed and
  rebuild in your own copy.
- **Error handling.** What happens when the Bluetooth device disappears
  mid-cycle, when WebGL context is lost, when localStorage is unavailable?
- **The variants.** They are generated by injection. Does every layer still
  attach to a hook that exists in the current base?
- **Performance claims.** LOD swap at 46/41 units, the tiered light budget, the
  shadow restamp. Measure whether they still do what they claim.

## Known non-issues — do not report these

These are already understood. Reporting them tells me you did not read.

- **The 2026-09-14 audit and what came of it.** Its report is in
  `D:\_KEEP\Emberwatch-audit\2026-09-14\`. r115 fixed F1–F9, F11–F14 and F16;
  r116 answered F15 (the reload now restores your position), S3 and S4. F10
  (the lane into the cathedral) is known and left for the owner. Check that the
  fixes hold, but do not report F10 again as new, and do not report the
  context-recovery reload itself as a bug. Since r117–r118 up to four
  residents a day walk out of the city and back on purpose — two mourners to
  the Old Graveyard, one to the Fallen Hall, one to Foxglove Pond; a resident
  outside the walls is not a navigation escape.
- `audit-source.js` **section A** lists ~64 false positives: GLSL builtins
  (`vec2`, `mix`, `fbm`, `smoothstep`, `sin`, `exp`) and ordinary words followed
  by a bracket in comments and strain text.
  Sections B and C are the real ones and are currently at zero.
- `audit-dom.js` **section B** lists three `<details>` ids — `switchPanel`,
  `swRaw`, `puffProbe` — that nothing in the app reads. They are deliberate
  handles for probe scripts.
- **About 150 props intrude near carriageways** (it depends on the seed). Zero
  are in the road itself. All are under 4 units of reach. Known and accepted.
- **`app/dist/` holds every installer ever built** (40, about 4.3 GB, at r112).
  Known. Not to be deleted.
- **r106 has no installers** — a filesystem lock blocked `npm run dist` until a
  reboot. Known; r107 built normally.
- **The terrain is one mesh and is never frustum-culled.** Deliberate and
  measured (PROJECT.md §4). Report it only with a measurement that says it
  matters.
- **The lighting is physically based since r111, on purpose.** Point lights are
  made through `lampLight()` from "lamp units" and animated through
  `userData.lampScale`; that conversion is intended, not a leftover. Report a
  lamp whose `.intensity` is written without the scale — that one is a bug.
- **Residents' own meshes sit on layer 1 on purpose (r113)**: one `BatchedMesh`
  draws them. **Walk-in homes stay solid until `activateHomes()`** so the
  seeded build never sees them open. **F acting on the second thing in reach**
  is intended.
- **Bloom is hand-rolled over the finished frame on purpose (r112)**, not
  three's `EffectComposer`, and keyed on red and violet so the aurora does not bloom.
  Do not recommend the composer without accounting for tone mapping being
  skipped inside render targets (PROJECT.md §2 "Bloom").
- **Some textures and roads look softer than `NearestFilter` suggests** — they
  are `LinearFilter` on purpose (PROJECT.md §9).
- **The Dr. Dabber preset index is unresolved and shelved by the owner**, and
  deliberately blocks writing temperatures. Do not "solve" it by reasoning — it
  needs a hardware capture — and do not list it as a finding.

## What a finding must contain

Rank by severity, most severe first. For each:

- **What is wrong**, in one sentence.
- **Where** — `file:line`.
- **How you know.** Command output, probe result, or measured number. Not "this
  looks like it could". If you could not verify it, say so explicitly and label
  it a suspicion rather than a finding.
- **A concrete failure** — the inputs or state that produce the wrong result.
- **What you would change**, described, not applied.

Separate confirmed findings from suspicions. A short list of things you actually
proved beats a long list of things that look off. If you find nothing in a
category, say so — that is a real result.

## Deliverable

`D:\_KEEP\Emberwatch-audit\<date>\AUDIT.md`, containing:

1. **Summary** — the three things most worth acting on.
2. **Confirmed findings**, ranked.
3. **Suspicions** — worth a look, not verified.
4. **Doc drift** — every claim in the docs that no longer matches reality.
5. **What I checked and found clean** — so the next audit does not repeat it.
6. **What I could not check**, and why.

Keep `understanding.md` alongside it.

Report back with the summary in chat. Do not modify `D:\_KEEP\Emberwatch`.
