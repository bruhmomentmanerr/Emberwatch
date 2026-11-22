---
name: style-match
description: Make a place, character, interior or sky in Emberwatch look like the owner's references (the PS2-era dark-fantasy style study in tools/video-frames/reference/). Use for any visual work judged against a reference image, for Blender-baked assets, for tuning a place's sky, fog or colour, or when the user says "match", "make it look like", "style", "reference" or invokes /style-match.
---

# Style match

The full guide, with the reasons and every trap, is `docs/STYLE-PLAYBOOK.md`.
Read its sections 1 (the style), 5 (traps) and 7 (recipe) before starting.
This page is the procedure.

## The style in one breath

Low-poly but smooth-shaded and painted, with the paint baked; one saturated
light colour per scene; deep blue or violet night, never black; high-contrast
ground and rock texture; soft local glows that keep their colour; mist at the
foot of things; big simple silhouettes with detail in the texture.

## Procedure

1. **Shoot the current state** at the reference's frame shape, through the
   harness (`tools/harness`, wrapper as in PROJECT.md §3). Hold the clouds
   (`EMBER.sky.hold(120)`), throw the first shot away, and hide the UI.
   `tools/probes/probe-orren-vista.js` is the model probe.
2. **Measure:**
   - `python tools/match-score.py <ref> <shot> --mask ...` for one number;
   - `python tools/region-audit.py <ref> <shot> --sheet out.png` for the
     worst region. Set its `REGIONS` for a new reference.
3. **Frame first:** camera place, lens and pitch. Put the camera in a
   function, so anything placed for the frame can use it.
4. **Fix the worst region next.** Try several variants in one boot with
   harness `before` scripts. `EMBER.moods` (live mood values), `EMBER.scene`
   (move, scale or tint objects) and direct light intensities are the levers.
   Keep the best by score *and* by eye. Histogram-style fits score high and
   look garish.
5. **New geometry goes through Blender:**
   - characters: copy the pattern of `tools/assets/orren.py`;
   - rock and stone: `tools/assets/_bake.py` `finish_baked(..., shape=...,
     style='rock'|'masonry', normals=True)`;
   - then `gltf-transform quantize ... --quantize-normal 8`, then
     `node tools/assets/inline-glb.js <glb> app/renderer/index.html NAME <KB>`;
   - place it with `placeBakedLandmark` or `attachSculpt`, never
     `placeLandmark`;
   - keep colliders separate from the model.
6. **Send the owner a preview** of the reference beside the before and
   after, at every meaningful step.
7. **Verify** (CLAUDE.md's list plus playbook section 6):
   - diagnostics against the last release;
   - every new or moved collider against the walk's route, 2 m clear;
   - boot time, three runs each;
   - variants and smoke;
   - the change looked at from other sides.
8. **Ship** as a revision. Record every number read off a run in PROJECT.md
   §0, and add any new trap to the playbook's section 5.

## Never

- Copy watermarks, handles, captions or exact characters from a reference.
- Let an emissive burn white. Use a modest strength plus a halo sprite.
- Put a point lamp inside the geometry it lights.
- Trust a Blender-saved JPEG's colours or quality, or an alpha-only colour
  attribute. Both are traps with fixes in the playbook.
- Ship a model whose colliders cross a route without checking it.
