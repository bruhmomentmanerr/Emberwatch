# Emberwatch — build catalog

Consolidated 2026-08-25 from files that were scattered across Downloads.
Current home: `D:\_KEEP\Emberwatch`

## What this is

Emberwatch — retro first-person dark-fantasy game set in the black city of
Vaneth. Daggerfall-style chunky-pixel look, three.js (inlined), the whole game
in one self-contained HTML file. It ships as an Electron desktop app so the
in-game Puffco Peak Pro Bluetooth panel gets a real secure origin — Web
Bluetooth will not run from `file://`.

Current sealed source: **1.52.0 / build r152 ("the forest at night")**,
2026-10-01. Archived, smoke-tested, six variants boot-check. Not packaged
yet (nor are r143 to r151): the latest packaged pair is 1.42.0 (r142). r121 was never packaged; r122
carries it. 1.31.0 was never issued — r131 shipped without a version
stamp, so the version skips from 1.30.0 to 1.32.0. **r136-r139 ("reference
build") were never archived** — the live file carried their stamp but
`revisions/` jumps straight from r135 to r140. That work (the visual-canon
layer, resident pose/role additions) survives inside r140's own archive, just
without its own intermediate checkpoints; nothing has been reconstructed or
guessed at.

> **PROJECT.md** is the single-file rundown of everything here — architecture,
> conventions, traps, how to ship. Start there; this file is the timeline.

## Folder map

    app/            The live Electron project — this is the thing you work in
      main.js         Electron main process. Registers a custom app:// scheme
                      (standard + secure + fetch/CORS) so Web Bluetooth and
                      the strain-archive lookups work. BUILD_REVISION = 'r152'
      preload.js      Bridge for the Bluetooth device chooser
      renderer/
        index.html    THE GAME. About 3.0 MB. Byte-identical to
                      revisions/phase 5 - world depth (r70-)/
                      emberwatch_3_r152-the-forest-at-night.html
      package.json    electron ^43.4.1, electron-builder ^26.15.3
      package-lock.json
      node_modules/   224 packages — DO NOT BACK UP, `npm install` rebuilds it
      dist/           Build output — DO NOT BACK UP, `npm run dist` rebuilds it
                        Latest sealed pair is 1.21.0 (r122).
                        r106 (1.5.1) never got installers: dist/win-unpacked
                        stayed locked until a reboot on Sep 11. r107 built clean.
                        56 installers in all, about 5.5 GB — never cleared, because
                        nobody has said which are worth keeping
                        win-unpacked/                   (loose Emberwatch.exe)
                      `npm run dist` now builds both the NSIS installer and a
                      single-file portable exe. They are both .exe, so each
                      target carries its own artifactName in package.json —
                      with one shared name they overwrite each other.

    revisions/      The full development history, 2026-08-17 to 2026-09-14.
                    Each file is a complete, playable single-file build, named
                    by what changed. Split into the four phases below:
                      phase 1 - Puffco BLE panel (r04-r19)            16 files
                      phase 2 - Vaneth city + strain archive (r20-r35) 16 files
                      phase 3 - NPCs, collision, city compiler (r36-r52) 17
                      phase 4 - streets, crowds, inner city (r53-r69)  15 files
                      phase 5 - world depth (r70-)                       active
                      test plans/   EMBERWATCH_R51 and R52 test plans
                    Phase 5 currently contains r70-r152, minus the revisions
                    that lived under an hour, were never played, and were folded
                    into their successor rather than left as links nobody can
                    reach (r87, r89-r92, r102), and r136-r139, which were never
                    archived (see above). The live build:
                    emberwatch_3_r152-the-forest-at-night.html

    variants/       Six alternate editions built on the current base, each a complete
                    standalone HTML file. Not forks — each is the live build
                    with one self-contained layer injected before </body>, so
                    `node variants/build-variants.js` regenerates all six
                    against whatever revision is current.
                      emberwatch_wardens.html      objectives, as a commission
                                                   ledger rather than a checklist
                      emberwatch_long-night.html   combat; wraiths, and lamplight
                                                   that actually burns them
                      emberwatch_emberfall.html    survival; one ember, sixteen
                                                   braziers, permanent progress
                      src/                         the layers — edit these
                      README.md                    what each one is and why
                    Each keeps its own localStorage key and edits no world
                    geometry, so they all describe the same Vaneth.

    snapshots/      The earliest loose builds from 2026-08-17, kept for history
                      wizard_1.html      08:34  third-person v1 (624 KB)
                      wizard_1_1.html    08:36  third-person v1, tweaked
                      emberwatch.html    08:37  first named build (728 KB)
                      emberwatch_2.html  09:19  (758 KB)
                      emberwatch_3.html  20:11  (771 KB) — the base the whole
                                                r04-r69 chain builds on
                    (emberwatch_1.html and a second copy of emberwatch_3.html
                    were byte-identical duplicates — both moved to
                    Downloads\To Delete\Duplicates.)

    assets/         emberwatch-medieval-ui-concept-r45.png and
                    emberwatch-oblivion-dark-fantasy-ui-concept-r45.png — the
                    two UI concept images from the r45 design pass.
                    75.glb was moved to
                    `_KEEP\BIG - decide before copying\` because it is 435 MB.
                    It is a glTF asset downloaded 2026-08-17 08:52, mid-session
                    between emberwatch_1 and _2. The engine loads .glb via
                    drag-drop or the gear menu. Verify it actually opens before
                    you decide it is worth 435 MB of backup space.

    docs/           bt (Puffco BLE protocol writeup).pdf — the Peak Pro
                    reverse-engineering reference the Bluetooth panel is
                    built from (Firmware-X auth handshake, Lorax protocol).
                    dr-dabber-ble-notes.md — the Switch 2 / Switch Go service
                    and characteristic map, lifted verbatim from the official
                    drdabber.app web app's own BluetoothConfig. It is a Web
                    Bluetooth app, so the whole layout is legible client-side.
                    The probe ships every UUID in that file.

## Version timeline

    Aug 17  wizard_1 -> emberwatch_3        first-person, Daggerfall look, city
    Aug 17-18  r04-r19    Puffco BLE panel: diagnostics, autodetect, reconnect,
                          auth retry, single-bond, Fahrenheit profiles
    Aug 18-19  r20-r35    Vaneth citadel + city; strain journal, terp codex,
                          smoke-note archive with autocomplete
    Aug 19-20  r36-r52    NPC conversations, city collision, seeded city
                          compiler, test plans
    Aug 20-21  r53-r69    doors, castle, pathfinding, crowds, NPC schedules,
                          street layout, inner city
    Aug 31     r70        district-specific civic courts and outer-quarter
                          landmarks; corrected South Road/Citadel frontage
                          directions; repaired and expanded world audits
    Aug 31     r71        full-world doorstep repair; zero blocked anchors;
                          safer app:// containment; leaner permissions; WebGL
                          context recovery; reduced-motion and diagnostics
    Aug 31     r72        district atmosphere, forge smoke and ward arrival
                          prose in two batched particle draw calls
    Aug 31     r73        persistent, non-checklist Vaneth Chronicle; wards,
                          interiors and residents remembered; eight reachable
                          world-detail interactions
    Aug 31     r74        coherent world-scale paving, calmer outer-road warp,
                          cleaner street density, rebuilt resident faces and
                          silhouettes, nearby acknowledgement
    Sep 1      r75        the four outer-gate approaches paved end to end as
                          lamplit avenues; country tracks on out to the
                          wilderness landmarks through carved mountain passes;
                          frayed forest edge; road-absence audit
    Sep 1      r76        wired the Electron Bluetooth chooser — the renderer
                          had never answered select-bluetooth-device, so
                          requestDevice() never settled and Connect hung in the
                          desktop app; read-only BLE device probe; chooser
                          handshake now covered by the smoke test
    Sep 1      r77        ward streets get kerbs so a carriageway has an edge;
                          forest edge becomes a density gradient instead of one
                          evenly spaced row; ward residents moved off four
                          invisible concentric rings onto the actual street
                          network and raised 96 -> 150; probe learns the
                          Dr. Dabber UUIDs
    Sep 1      r78        kerbs stop at junctions instead of crossing through
                          them; wall colliders flagged so the new road
                          obstruction audit stops counting the city's own gates
                          as obstructions; props nudged to the verge
    Sep 1      r79        residents merged to 6 meshes from 16.1 — draw calls
                          3,386 -> 1,425 at the spawn; interior counters, the
                          Great Hall dais and lectern, the shrine altar given
                          the footprints they never had; a lintel above every
                          interior door, which had all been open to the sky;
                          Fawwk added to the strain library
    Sep 1      r80        inner-city avenues and grid lines stop at the citadel
                          curtain instead of crossing the bailey, which is what
                          put barracks and the keep itself in the middle of a
                          road; the keep's plinth given a real footprint so you
                          can no longer walk into the motte
    Sep 1      r81        keep moved to the centre of the bailey and the Great
                          Hall rebuilt against its south face as one connected
                          mass (32x22, was 26x18 stranded behind the keep, its
                          door facing the keep's back across six units); royal
                          walls take the keep's stone so the join reads as one
                          building; the bailey gets its own roads — a
                          processional way from the gatehouse to the hall door
                          plus lanes routed clear of the ranges; porch clutter
                          (crates, barrels, firewood, benches, handcarts)
                          tested against the road network, which is what put
                          loose boxes on open paving
    Sep 1      r82        the keep IS the Great Hall — one square great tower
                          whose ground floor is the walk-in hall, tower mass and
                          four corner turrets rising off the same footprint.
                          r81's separate hall block is gone; so is the cylinder
                          keep. Avenue monuments walked out to the verge: they
                          are 6.0 across the street and sat 2.0 off the centre
                          line, which put 22 of them in the carriageway
    Sep 2      r83        compiler lots slide along their row instead of being
                          dropped when their one fixed spot is dirty, which made
                          it affordable to test them against the authored road
                          grid as well as the compiler's own lanes. Buildings
                          standing on a carriageway: 8 -> 0, at a cost of four
                          facade parcels. Fawwk entry corrected — Kaya Extracts
                          / Kaya Farms is a confirmed hand-washed live rosin
                          house; the drop itself is still unlisted
    Sep 3      r84        interior dressing: a prop vocabulary and a pass that
                          scales with the room and seeds off its name (the
                          Great Hall went 12 -> 58 colliders); continuous NPC
                          separation, since the old unstick only ran while a
                          resident was walking and never for one standing at
                          its stop; a wall-aware road layer, roads through
                          walls 232 -> 0; K copies a resident flow report
    Sep 4      r85        **the generated greater city is gone.** outerWards()
                          laid 2,460 buildings on a warped grid out to radius
                          540 and almost every placement fault this project
                          chased came from it. Vaneth is one walled city inside
                          radius 240 with wilderness beyond. The Chronicle is
                          removed, as is the saved-position restore and the
                          ?spawn debug hook. Dead generators deleted outright.
    Sep 4      r86        the city stands on earth, not pavement: cityFloor()
                          used to lay the whole disc in the same cobble as the
                          roads one shade darker, so no street read as a
                          street. Second phantom wall removed from the road
                          clipper, which had been cutting a four unit hole out
                          of every gate approach
    Sep 4      r88        **r85 had deleted the settings and strain block whole.**
                          The Chronicle removal took the two hundred lines around
                          it as well, so openSettings, toggleStrains, currentStrain
                          and the smoke-session helpers were undefined: every
                          conversation threw on the first line of the greeting and
                          left an empty panel with the markup's placeholder name,
                          and because dialogueOpen was then stuck true, M, J and P
                          did nothing either. Restored, with a runtime test that
                          opens each panel and holds a conversation.
                          Also: the south gate had a twenty-unit tavern built
                          across it, so the south road ran under a floor and
                          stopped at a back wall; wardRoof laid a second eaves
                          course over the one wardHouse already laid and stacked
                          two pitches on houses too narrow for one, which is what
                          read as "more than one roof"; the wilderness ruins took
                          their height and their centre height from separate rolls
                          and floated; the mountains were plain six-sided cones and
                          read as pyramids. Roads on the carriageway 73 -> 28, and
                          26 of the 28 are furniture inside buildings.
                          The Windows key no longer snaps the camera
    Sep 4      r89        **a pyramid is not a roof.** Every house in Vaneth was
                          capped with a four-sided cone, which on the rectangles
                          houses are actually built on either overhangs the narrow
                          walls by metres or leaves the long ones bare, and comes
                          to a point where a roof has a ridge. Cones were reached
                          for because aBox cannot tilt — so aRoof() builds the
                          roof out of its own triangles instead: four eaves
                          corners, a ridge of the right length, hip or gable, a
                          real overhang and a closed soffit. Cheaper than the
                          cones it replaced (1,145 -> 1,131 calls, 500k -> 486k
                          triangles). Also: facadeWindows and four other fittings
                          positioned themselves with the opposite rotation to the
                          one aBox applies, so on any building that is not
                          axis-aligned the windows sat off their own wall; and
                          half of building()'s outbuildings were capped with a
                          flat slate slab and no roof at all
    Sep 4      r90        an audit pass, and what it turned up. A source sweep
                          (called-but-never-defined, defined-but-never-called)
                          found askForDirection calling pointWayfinderAt() and
                          reading wayfinderState.discovered, neither of which has
                          existed since the objective arrow was removed — so "ask
                          for a place worth finding" threw every time it was
                          clicked. It gives a compass bearing now. The same sweep
                          removed 30 dead functions in four rounds, 121 lines,
                          most of them the superseded legacy dialogue system.
                          Roads no longer run through the authored walk-in
                          landmarks: the ward grid is drawn wall to wall and had a
                          lane down the long axis of the Moon Archive, so layRoad
                          now walks off a landmark lot the same way it walks off a
                          wall. Colliders on a carriageway 73 -> 5, and the five
                          are door leaves and one noticeboard.
                          The app has an icon.
    Sep 4      r91        **the frame cost less than half what it did.** Measured,
                          not guessed: 37.2ms a frame, of which 18.8ms was Three
                          rebuilding a 2048x2048 shadow map every single frame for
                          33 casters, in a world where the moon is fixed and the
                          city is a static batch. shadowMap.autoUpdate is off; the
                          map is stamped once when the city is built and again
                          only when a door leaf actually moves. 16.4ms now.
                          Also: 83 point lights, every one of them walked by every
                          lit fragment shader — the nearest 14 stay lit and the
                          rest switch off, on a fixed count so Three compiles one
                          program instead of recompiling as the count drifts. And
                          rAF draws at the panel's refresh rate, so a 144Hz
                          monitor was rendering 144 frames a second of a walking
                          game; the draw is capped at 60 with the skipped slices
                          carried into the next dt, so nothing moves at half speed.
                          Interiors: hearths burn. A flickering light and a plume
                          that rises and recycles, over an ember bed with logs laid
                          across it — the mouth used to be two slabs of emissive
                          amber that read as a glowing white brick. Interior floors
                          lifted clear of the tallest paving in the world, every
                          walk-in landmark got a paved doorstep out from its own
                          door, and court furniture is skipped rather than built in
                          a carriageway. Colliders on a road 5 -> 2
    Sep 4      r92        **a resident you are not standing next to costs one draw
                          call.** 1,002 of the city's 1,155 meshes were residents:
                          a merged body, a merged head and four limb pivots that
                          have to stay separate so they can swing — six calls each,
                          at any distance, for a figure four pixels tall at the far
                          end of a ward. Every resident now also carries a
                          single-mesh copy of itself, baked in a neutral pose at
                          build time, swapped in past 46 units and back at 41 so a
                          resident walking the boundary cannot flicker between
                          them. The gait is skipped for anyone on the far side of
                          that line too. At the north gate: 1,152 calls -> 320.
                          Standing in the market: 213. Standing next to someone:
                          176, and that one keeps all six of its parts.
                          Also: colliders standing on a road are now **zero** —
                          the court furniture is five pieces, not one point, and
                          nudging on any single one of them put another in a
                          different road; and the light budget snaps to tiers
                          (0/5/14) so the wilderness runs on none rather than
                          lighting fourteen lanterns that cannot reach you

    Sep 5      r93        residents use the streets. The nav grid treated every
                          walkable cell as identical, so a resident crossing a
                          ward took the shortest line over the dirt and the
                          streets stayed empty. Paving is the cheap surface now
                          (1 against 3 for open ground) and string-pulling may no
                          longer shortcut off it. The ward grid was also drawn at
                          4.6 and 5.4 wide in streets whose building lines are
                          eighteen apart — a ribbon of cobble with a wide dirt
                          verge, which is where people were walking; no lane is
                          narrower than 7. Residents on paving 76% -> 85%.
                          The app icon was a white circle: make-ico's downscale
                          un-premultiplied with an extra factor of n in it, which
                          is at least 4x on every size and saturated everything.
    Sep 5      r94        **Vaneth outgrew its wall.** r85 deleted a generated
                          outer city because it was laid on a warped grid that
                          knew nothing of the authored passes. The lesson was not
                          "keep the city small", it was "one street plan, one set
                          of rules" — so the city grows the way a real one does.
                          The wall at 240 stays exactly where it is with
                          everything inside it untouched and becomes the *old*
                          wall; new quarters go up outside it, on the same
                          compiler, behind a new wall at 380. Three ring streets,
                          four diagonal avenues, the gate roads run the whole way
                          through. Map 900 -> 1500, wilderness pushed out past the
                          new wall. 162 residents -> 326.
    Sep 5      r95        watches, haunts and ties. Vaneth is permanently night —
                          the aurora is the identity of the place — so the clock
                          is the watch bell rather than the sun: four named
                          watches of about three minutes that change where people
                          are without touching the sky. Every resident has a home,
                          a workplace drawn from their own ward's business, and
                          one to three people they know, taken from their nearest
                          neighbours so the graph is a neighbourhood and not a
                          scatter. The bell turns and 56 of them cross more than
                          twenty-five units of city to be somewhere else. A new
                          dialogue topic asks after their people and answers with
                          names, relations and bearings.
    Sep 5      r96        the still hours empty the streets. When the bell turns
                          to still, a resident who reaches their own door goes
                          through it — 200 of 326 off the street, and the draw
                          drops with them. Roughly a quarter never go in, always
                          the same quarter by name, so the faces you learn to
                          expect on a corner are still there at the worst hour.
                          The ember watch is the other half: 137 residents stop
                          and turn to face somebody off their own tie list. It is
                          the only visible payoff of the relationship graph and it
                          costs a pause and a facing.
                          The new quarters were terraces and nothing else — every
                          lamp, bench and planter in Vaneth comes off a
                          hand-authored coordinate list written against the old
                          circle, and none of them reach past 240. The outer
                          dressing reads the street network instead: it walks
                          every carriageway beyond the old wall and lights it,
                          and puts a well or a shrine where a diagonal avenue
                          meets a ring street. 274 lamps in the world now; the
                          tier culling still lights eight.
                          EMBER.setWatch(id) jumps the bell, because a watch is
                          nearly three minutes and waiting one out is not a test
    Sep 5      r97        somewhere to go, and somebody to be. Every one of the
                          old city's eight walk-in landmarks is inside the 240
                          wall, so the new quarters were bigger without being
                          anywhere: a resident out there could name a place worth
                          finding and every answer pointed back through the gate.
                          Six new halls — the Lamplighters' Hall, the Wayhouse,
                          the Cold Assay, the Drovers' Rest, the New Chapel and
                          Ferrier's Yard — sited on the bearings halfway between
                          the gate avenues and the diagonals, at radii that fall
                          between ring streets, so no lot touches a carriageway.
                          Doors 9 -> 15.
                          And households. The first tie pass was one-directional:
                          you could be somebody's kin without them being yours,
                          and nothing in the world said so. People who live on the
                          same few metres of street now take one name between them
                          — 39 households, two or three each, from their own
                          surname pool — and every tie is answered from the other
                          end with the relation that matches it (972 of 1,089
                          edges). Rivals exist. Nobody spends the ember watch at a
                          rival's door.
                          All five gameplay variants retargeted: arches, braziers
                          and warden commissions now reach the new quarters, and
                          the hall targets aim at the paving outside the door
                          rather than at the middle of the building
    Sep 5      r98        word travels, and the gates were wrong. **The gate
                          opening was measured in degrees.** 3.3 degrees is
                          fourteen metres of arc at the old wall's 240 and
                          twenty-two at the new wall's 380, so generalising
                          citadelWall to take a radius quietly made the outer
                          gates half again as wide — a forty-four metre hole with
                          no masonry in it — while the flanking towers stayed
                          pinned six metres off the centre line, which put them
                          *inside* the opening. Four free-standing pillars in a
                          gap. A gate is now a fixed thirteen metres either side
                          whatever circle it is cut into, the towers stand on the
                          jambs, and there is a gatehouse across the top.
                          Ties do something now: sharing your jar puts it into
                          the mouths of everyone on that resident's list, so the
                          next door you knock on has already heard — warmly, or
                          from a rival, who will not take the jar from you at all.
                          Residents go in at a door rather than evaporating in
                          the road: 320 of 326 have a doorway, the street face of
                          the nearest house, and they arrive within 2.3 metres of
                          it before they step out of sight.
                          The wayfinder said "The Northern Wilds - the Working
                          Watch" to somebody who had never been told there was a
                          clock. It names the hour on its own line now and says
                          what the hour means.
    Sep 5      r99        the probe listens. The Dr. Dabber notes settled where to
                          write on a Switch 2 and left one question open — what
                          the device says first, since drdabber.app has both an
                          initialPacketStackReceivedAtom and a
                          bluetoothDeviceAuthenticatedAtom. After its survey the
                          probe now subscribes to everything that can notify and
                          prints twenty seconds of traffic, timestamped. That is
                          the read-out the notes ask for, and it is the honest
                          limit of what can be built without the hardware: the
                          UUIDs are the app's own constants, the packet format is
                          not in the bundle, and this project has no Switch 2 to
                          watch.
    Sep 5      r100       four quarters, not one repeated four times. innerInfill
                          drew every terrace beyond the old wall from one palette
                          of four materials and one range of heights, so the New
                          North, Eastreach, Westreach and the Long Southing were
                          the same street going round a circle. Each has its own
                          palette, its own height and depth, and a trade it leaves
                          out in the street: loading beams and shutters on the
                          grain lofts, awnings and sign boards and a counter in
                          Eastreach, a chimney with a red mouth at its foot the
                          length of Westreach, and fences and troughs for the
                          Southing's yards. A third of the terraces carry it —
                          all of them would read as a theme park.
                          WARD_ATMOSPHERE had four keys naming wards wardAt has
                          not returned since r94 and was missing eleven that it
                          does, so most of the city was walked into in silence.
                          And the audit now names the doors it finds blocked
                          rather than reporting false: a terrace had gone up
                          across the Drovers' Rest doorstep, because the infill
                          checked carriageways and other buildings but never
                          asked whether it was standing in a doorway.

    Sep 6      r101       **a second device.** A real Switch 2 capture came back
                          from the listening probe and the frame decoded: twenty
                          bytes, a9 either end, 0x14 for the length, byte 7 is
                          0xaa for exactly the length of a heat cycle and byte 11
                          is the heat — identifiable because it goes on climbing
                          with a decreasing slope for three seconds after byte 7
                          clears, which is thermal lag in a heater that has just
                          switched off and nothing else in the frame does it.
                          Note the device answers on the *demo* service, 0000fee7;
                          the primary control service the vendor app declares did
                          not enumerate at all on firmware V2.0.0.
                          Emberwatch reads it and does not write to it. The
                          command encoding is still unobserved and inventing bytes
                          to send a heater is not a thing to do.
                          The Switch publishes the same session signals the Puffco
                          bridge does, so Ember Hour opens its arches and Heatline
                          moves its fog on a Switch without either of them knowing
                          which device is attached.
    Sep 6      r102       **the Switch is writeable.** A labelled write capture
                          from the vendor app decoded in one pass: the envelope
                          is <opcode> <total length> <payload> <opcode>, and the
                          state frame b9 has exactly two bytes that ever move —
                          payload[1] is the preset index and payload[8] is the run
                          flag. Six labelled samples, one byte of difference each
                          time. Emberwatch sends b9 and the b1 clock and nothing
                          else; b5, which writes a value into a heater profile,
                          has one unlabelled sample and is not sent.
                          Confirmed on hardware the same day: presets differentiate
                          and cycles start and stop on command.
                          The units were called for Celsius here, on a cycle that
                          reached 201 still climbing. That was wrong — see r104.
                          The temperature is sixteen bits across bytes 10-11 and
                          Fahrenheit; an eight-bit read cannot see byte 10, which
                          is why 201 looked like a plausible Celsius climb.
    Sep 6      r103       the panel became the bench. A byte grid for the whole
                          frame with the changed cells lit and every field named on
                          click; a log that collapses repeats and prints any frame
                          that *differs* with the changed bytes named; inline marks
                          so a label sits beside the traffic it describes; copy-all
                          and copy-changes; a raw write behind an arm switch, which
                          is the only way b5 gets decoded; and a replay box that
                          pushes a captured log through the same decode with no
                          device present.
                          A standalone page was built for this first and scrapped —
                          the panel is where the device already is
    Sep 6      r104       ramparts. Both walls walkable: surfaceAt() gives the world
                          surfaces above y=0, gravity lands on them, street-level
                          colliders stop applying once you stand on top of them.
                          Climbed 0->12.9 and 0->14.9, walked 65 and 67 units of
                          circuit. Curved ramparts need solid edges — a tangent
                          leaves a 4 m walkway inside thirty paces.
                          Also: downloaded the vendor bundle and replaced the
                          guessed a9 field map with their parser. Temperature is
                          16-bit Fahrenheit across bytes 10-11; the reported
                          "drops to zero then climbs" was the low byte wrapping
                          at 256 F. b5 is the heating profile, not a temperature.
    Sep 6      r105       the whole Switch 2 protocol. All thirteen notification
                          handlers and all thirteen command builders read out of
                          the vendor bundle: the target temperature lives in a3,
                          statistics in a2, custom profile points in aa/ab, and a
                          write is always its read plus 0x10.
                          Which exposed a real bug — the b9 frame is the entire
                          settings block, and Emberwatch had been sending a body
                          frozen from one capture, writing that evening's light
                          mode, brightness, auto-shut-off, haptics and temperature
                          unit over the owner's own every time a preset was
                          pressed. It builds from the live state frame now.
                          The panel names every frame type instead of shouting
                          UNEXPECTED, and the raw-write preview names the opcode —
                          b8 is a four-byte factory reset one nibble from b9.
    Sep 6      r106       the diagnostics stopped lying. outerWards() was removed
                          back at r85 but the three fields it fed were left wired
                          to a stub returning hardcoded zeros, so
                          diagnostics().city reported outerBuildings:0,
                          outerSquares:0 and outerYardDetails:0 — three numbers
                          naming a system that no longer exists, which read as
                          "the outer city is empty" to anything trusting them.
                          EMBER.wards pointed at the same stub.
                          wilderness() now counts what each pass actually leaves:
                          8 features, 1,096 colliders (forest 840, graveyard 130,
                          ruined ring 84). EMBER.wards is now EMBER.wilderness.
                          Also new: tools/check-parse.js and tools/audit-dom.js,
                          which cross-checks markup ids against script lookups in
                          both directions — the audit that would have caught r85's
                          dead settings panel. And PROJECT.md, the single-file
                          rundown of the whole project.
    Sep 13     r107       hills and water, and a way out to them. Past radius
                          404 the ground now rolls into hills rising to about 25 m
                          under the peaks; the city inside stays flat. terrainAt()
                          reads the same triangles the mesh draws, so feet stay on
                          the visible surface — a walk uphill measured a worst gap
                          of 0 between the player and the ground. Foxglove Pond is
                          real water in a 1.16 m basin, fed by a brook off the
                          western peaks whose water only runs downhill.
                          The four gate avenues used to stop at 426 with the
                          landmarks at 467 and no path to any of them. An earth
                          ring track at 440 now joins every gate road to every
                          landmark, with signposts, lanterns and cairns.
                          Found on the way: trees growing in the pond (5), the
                          graveyard (5) and the ruins (3), because the forest was
                          still avoiding where the landmarks stood before the
                          rescale. Now 0. "Aloft" was y > 3.2, which on a hill
                          would have switched off collision with every tree on it.
                          r0's diagnostics had thrown on every call since r106 —
                          the variant builder never runs what it builds — so
                          tools/check-variants.js now boots all six. The harness
                          moved into tools/harness and can take screenshots.
                          Tree Flip (Lemon Tree × Wedding Cake, rosin) joined the
                          strain ledger. Cost: +1 draw call, +100k triangles,
                          about +1.5 ms a frame in the software harness.
    Sep 13     r108       places beyond the wall. Each landmark now does something,
                          and none of them keeps score. Strike the standing stones
                          with spells until every one holds a colour and the ring
                          answers with a pillar of light the city can see. Skim
                          stones on Foxglove Pond. Read the headstones — their
                          names are the city's own households, and the living
                          family knows when you have been. Sift one fragment of
                          the Fallen Hall's end from its ash each watch. Read the
                          waymarks at the crossroads.
                          Found on the way: no one had ever been able to enter the
                          graveyard. Its wall was 128 colliders and no geometry —
                          an invisible ring with gaps too narrow to pass. It is a
                          dry-stone wall with a gate now, and its mausoleum is a
                          mausoleum instead of a house with lit windows. The
                          standing stones floated up to half a metre and the
                          headstones 20 cm. "Watch the foxglove water" sat 149
                          units from the pond; it is placed from the pond itself.
                          audit-source.js read `...fn()` as a property access and
                          called a live function dead; fixed.
    Sep 13     r109       every ward keeps shop. The only shopfronts had been a
                          third of Eastreach; the old city had none, and the
                          compiler's eleven "shop" buildings on the Cinder Market
                          were an awning strip with nothing under it. About 115
                          shops now, mostly on gate roads, avenues and the ring
                          boulevard, each selling what its ward would — bakers
                          and chandlers by the market, booksellers by the archive,
                          ironmongers in the west, saddlers on the south road.
                          Shutters come down for the Still Hours and the Ember
                          Watch. The nearest resident keeps each shop and stands
                          at its counter through the working day; look over the
                          counter and they talk. Chosen by a hash of position, so
                          no building in the seeded city moved.
                          Caught before shipping: a `let` one line below its first
                          use stopped the city building. Cost: +2 draw calls,
                          about +25k triangles.
    Sep 13     r110       three.js r128 → r186. The engine is one generated block
                          now, built by tools/build-three.js from pinned packages,
                          replacing three hand-inlined r128 blocks. r186 changed
                          colour management and light maths; unshimmed, the city
                          rendered at half its brightness (22.7/255 average
                          difference from r109). A compatibility layer restores
                          r128's colour handling, π and point-light falloff, and
                          the difference fell to 0.55-0.78 against a 0.32 noise
                          floor. Also: NearestFilter textures had been smoothed by
                          r128's anisotropy all along, so they are Linear now to
                          keep that look; Clock → Timer; mergeBufferGeometries →
                          mergeGeometries; PCFSoft → PCF. Same draw calls, ~62k
                          fewer triangles, frame time level. Every probe from
                          r107-r109, the runtime audit, all six variants and the
                          Bluetooth smoke test pass on r186.
    Sep 13     r111       physical light. The owner asked for a lighting
                          upgrade, so the r128-look layer r110 had kept alive
                          was retired and the city relit for physically based
                          light: colour management on, inverse-square lamps, no
                          π. The ~300 lamps keep their tuned numbers as "lamp
                          units" through lampLight()/lampPower(), which convert
                          to candela and stretch each lamp's reach 2.2×, so
                          light lands on the street in warm pools. Night fill
                          went from violet to deep blue (the violet turned every
                          street purple under real light), the moon from
                          lavender to pale cool blue, windows from white cards
                          to amber (emissive ×0.7), moon shadows soft (radius
                          3). Ember mode desaturated; dusk kept. The aurora sky
                          keeps r110's colour maths. All six variants' lights
                          converted; Emberfall's carried ember and r0's campfire
                          at a fixed range so they do not blow out at the
                          player's feet. Tried and dropped: AgX tone mapping,
                          physical lights on unconverted hex, the old violet
                          scaled up. Measured against r110 (harness, software
                          rendering): 16.6/255 average block difference over
                          nine standpoints, the hearth 53 → 62 luminance, the
                          lantern street 47 → 43; same draw calls and
                          triangles; +1.9 ms at the north gate and +2.7 ms at
                          the market, because the longer reach keeps more
                          lamps lit (market 5 → 14). Probes r107-r109, reach,
                          the runtime audit (same result as r110 on this
                          harness), six variants and the smoke test pass.
                          New: tools/probes/probe-light-tune.js, reference-r111
                          shots, build-three.js --entry/--html.
    Sep 13     r112       bloom. A glow round lamps, windows, fire, crystals and
                          the moon. Laid over the finished frame (copied, blurred
                          at five sizes, screen-blended back) instead of three's
                          HDR composer, which would have skipped tone mapping on
                          the fog, sky and water r111 was tuned with. Keyed
                          toward red and violet, because the aurora's teal is
                          brighter by luminance than a lit window and a
                          luminance key turned the sky to milk; cyan and green
                          spells do not glow as a result. Menu toggle, saved. Cost on the
                          harness +1.1 to +1.8 ms and 12 draw calls.
                          renderer.info now resets once a frame, so calls count
                          the bloom passes and frame still counts frames. A
                          tuning run that switched bloom off persisted through
                          the harness's localStorage and made the next four
                          screenshot sets bloomless — caught by reading
                          EMBER.bloom, and probe-bloom now leaves it on.
    Sep 14     r113       walk-in homes. Fifty to seventy ordinary ward houses are
                          hollow now, each with a real door onto its street and a
                          furnished room behind it; chosen by hash and kept solid
                          to every build stage until the residents are settled,
                          so the seeded city matches r112 exactly (a first try
                          that opened them early moved a resident's home). Every
                          resident draws in one BatchedMesh: north gate 551 → 322
                          draw calls, market 323 → 193, frame time level on the
                          harness. F takes the second thing
                          in reach (a keeper behind their counter). Long Night's
                          wraiths share four lamps instead of carrying one each,
                          which had compiled 120 shader programs in the first
                          waves. The market braziers are converted at a nearer
                          range, so their foot is an orange pool, not a white
                          disc. The runtime audit's North Ward "failure" was the
                          audit standing inside a shop. probe-soak played the
                          base and all six variants for four minutes each.
                          Dr. Dabber preset work shelved by the owner.
    Sep 14     r114       people at home. Up to three residents live in each
                          walk-in home, those whose address is nearest its
                          door, and in the still hours they walk to that door
                          and stand inside at the hearth, the table or the bed
                          instead of vanishing; you can talk to them there, not
                          through the wall. 35 residents in 18 homes on the
                          harness seed. Talking to someone at home re-anchored
                          their route inside, so at the bell they walked back
                          in: now re-anchored from the doorstep, only when a
                          conversation moved it. Shader warm-up while loading:
                          no new programs compile during a four-minute soak,
                          and the 1.9-3.5 s first-use stalls in Ember Hour and
                          Long Night are gone. The read-only audit was rerun by
                          a background agent against r113.
    Sep 14     r115       the audit's fixes. The 2026-09-14 audit (run by a
                          background agent on r113) found 16 things; this fixes
                          13. Switch 2: Start and Stop sent a remembered preset
                          of 3, and a half-failed connect could still write the
                          frozen capture body over the owner's settings — both
                          gone; writes wait for the device's state; raw writes
                          parse one byte at a time, so "-48" is no longer a
                          disguised factory reset. Residents: 144 were parked on
                          one-point routes and never pathed; now none, and those
                          moving 25 m in two minutes went 94 → 229; the path
                          queue served 11,749 requests a minute saturated, 18
                          residents never, and now 5,927 with none left out.
                          Lights: one budget, exactly 5 or 14 lit at the gate
                          and market in the base and every variant (Emberfall
                          had 46); the light pool retired; homes no longer lit
                          from the street. Moon shadows follow the player (84%
                          of the city had none). Late-blocked homes stay shut.
                          Long Night stopped firing on menu clicks; variant
                          hotkeys stopped firing while typing; Ember Hour counts
                          12 arches; Wardens stopped sending you to door hinges.
                          Door leaves cast no shadow: walking residents had set
                          the Cinder and Keg's door swinging and restamping the
                          shadow map. Cost against r114: market level, gate and
                          pond about 1.2 ms slower on the harness.
                          Seven dead functions deleted; tools/audit-dead.js;
                          the Switch frame test now reads the real decode.
    Sep 14     r116       settled in. Residents at home are posed: crouched at
                          the hearth with their hands to it, sat at the table,
                          asleep on their backs in the bed. A lost WebGL context
                          still reloads the page but puts you back where you
                          stood (audit F15), tested by a probe that loses and
                          restores the context through the harness, which now
                          follows a reload. Wardens' hall commissions aim at
                          each hall's real doorstep; Ferrier's Yard's had been
                          behind its back wall (audit S4). probe-bloom proves the
                          glow: +74 luminance just outside a white card with
                          bloom on, +5 in empty sky (audit S3; the old
                          whole-frame average once read darker with bloom on).
    Sep 14     r117       the mourners. Somebody does go out to the Old
                          Graveyard now: at the Working Watch bell two residents
                          whose family has a legible stone walk out through the
                          nearest gate, stand at the stone through the Still
                          Hours with their head bowed, and walk home at the
                          Ember Watch. The stone names whoever is standing at
                          it; they tell you whose it is. Residents can carry a
                          list of legs for a long walk, and walk on the terrain
                          outside the wall. After a context-recovery reload the
                          ward's welcome line no longer buries "The renderer
                          recovered". The harness takes HARNESS_TIMEOUT
                          for long probes; probe-soak-spikes records long-
                          animation frames: none over 150 ms in three soaks,
                          but three 306-345 ms frames in the next three soaks
                          without it. Still open.
    Sep 15     r118       past the wall. The places outside the city that were
                          waiting for somebody get somebody: a lamplighter
                          kneels sifting at the Fallen Hall (its last fragment
                          says someone still comes back to it), an angler fishes
                          Foxglove Pond, and r117's mourners go on. One outing
                          system for all three, with poses that hold — bowed,
                          kneeling, rod out over the water. Sift or skim with
                          them there and they notice. The long frames: three
                          caught just before r118, no heap change and no script
                          time named; r118's six soaks had none, and the spike
                          probe now times the game's own frame callbacks for
                          the next one.
    Sep 16     r119       the long frames. The 300 ms hitches the soaks had been
                          catching since r116 are found and gone. The game now
                          says where a frame went (FRAME_COST, EMBER.frameCost),
                          and with that, seven instrumented Wardens soaks caught
                          four and named three causes: npcObstructed testing all
                          326 residents for every moving resident (now the nine
                          cells of the resident grid), the path queue running
                          seven long searches with no time limit (8 ms a frame
                          now), and a bell re-anchoring every resident at once
                          with a line-of-sight test sampled every 1.1 m (40
                          samples maximum, three re-anchors a frame). Six soaks
                          after: none. Frames 2-3 ms faster at every standpoint.
                          Two probes that play a variant rather than soak it,
                          for the balance nobody has measured.
    Sep 16     r120       measured variants. The balance probes played: The Long
                          Night cannot hurt you if you fight back at all (five
                          minutes, vitality never below 100) and the dark is
                          better than the lit street, which is the opposite of
                          its own design; Emberfall's ember read 100% at every
                          brazier it lit, 24 of 32 in fifteen minutes. Both
                          verdicts are the owner's to act on. EMBER.findPath
                          lets a probe walk the streets like someone who knows
                          them. The resident grid stopped rebuilding a few
                          hundred arrays a frame, which took The Long Night's
                          last hitches with it: four soaks, none.
    Sep 20     r121       the city takes shape. The generator now dresses its
                          existing façades with authored stone surrounds,
                          shutters, upper timber, hooded lanterns and rare
                          verdigris panes. Rendering moves from a deliberately
                          pixel/purple default to a glossy saturated low-poly
                          cobalt night; mixed-stature residents smoke pipes.
                          The city keeps its
                          seed, nav, doors, collision and routes; the balance
                          work first measured at r120 ships alongside it.
    Sep 22     r131       the plan redrawn. A Blender top-down of the exported
                          city showed what screenshots never had: Vaneth was a
                          bullseye. Concentric rings, four dead-straight
                          avenues, every block a rectangle, every house the
                          same footprint, every block interior a void, and the
                          four quadrants mirroring each other. The lot table
                          is rebuilt against that. Nine hand-placed quarters
                          give character by nearest seed rather than by angle,
                          so no quarter is another's mirror; building width
                          spread goes from 2.8 m to 10.9 m, sheds through
                          halls; 1,054 buildings now stand inside the blocks
                          that used to be empty; and 95 segments of crooked
                          lane cut through the lattice, two or three to a
                          block, by pattern — spine, court, fork or left
                          solid. 1,513 lots, up from 1,325, denser in every
                          ring. Two latent crashes found on the way: sync()
                          read a const still in its dead zone, and the
                          function it read had a `node` out of scope, so it
                          had never once run successfully. Verified: nothing
                          floating, nothing buried, no building in a road, no
                          blocked anchor, 149 walk-in doors all clear.
    Sep 22     r132       streets that bend. The roads were the last part of
                          the city still drawn with a ruler: two dead-straight
                          cardinal avenues and a symmetric grid. Both
                          cardinals and all eight lattice lines now keep their
                          exact endpoints — every gate and frontage authored
                          against them still lines up — and kink two to four
                          times in between; the ring roads are polygons rather
                          than circles; the lattice offsets are uneven, so the
                          quadrants stop mirroring. Three seed-dependence bugs
                          came out of it. The bends were drawn with the world
                          seed, so on any other profile the roads moved and
                          the baked city did not: the smoke run had 244
                          colliders standing in a carriageway while the
                          harness showed none. The plan is now drawn by
                          planHash, with the seed left out, and is identical
                          on every profile. The citadel's four corner
                          bastions, at radius 69, had always sat outside the
                          54 clearance disc and were missed by luck; side
                          streets now clear a 78 precinct. And a lattice line
                          crossing an authored ward cannot thread a 7 m
                          carriageway between rowhouses spaced 14.3, so a
                          street now stops at a ward and picks up beyond it,
                          the same way it already stopped at a landmark hall —
                          the ward is authored, the cross-street is new, so
                          the street gives way rather than the buildings. The
                          lot table was regenerated against the final network:
                          1,801 lots, up from 1,513. Verified: compiler lots
                          in a road 7 to 0, inRoad 244 to 1, no road overlap,
                          no blocked anchor, gate approaches whole, 303 of 326
                          residents walking.
    Sep 22     r133       nothing hangs on nothing. A walk round the city for
                          clutter that makes no sense and residents that are
                          broken. The residents turned out to be fine — nobody
                          wedged in geometry, nobody permanently stuck, no
                          clump that lasts longer than two people passing each
                          other — but the clutter audit had been looking at
                          the wrong thing for its whole life. aBox, aCyl and
                          aCone merge into one mesh per material, so there is
                          no individual prop left in the scene to test, and
                          every scene-graph audit of the city's props has been
                          inspecting a handful of giant meshes. Tapping the
                          three constructors gives the first true inventory of
                          Vaneth: 39,417 solids. It found 42 trade signs whose
                          bracket never touched the board it was supposed to
                          carry, hanging at eye level on every shopfront; the
                          tavern light the owner reported by name, floating a
                          metre above the bar; the same fault in the refuge's
                          tool shelf; and 33 boxes built with no material at
                          all, because compileDistrict never copied the
                          accent colour off its spec and so every lot in all
                          six authored wards drew its sign board with an
                          undefined key. Gable ends also got windows: facade
                          windows only ever did front and back, so any
                          building standing side-on to its street showed a
                          blank slab. Three false trails on the way, all
                          recorded in PROJECT.md so they are not walked
                          again — the largest being a stuck-NPC test that did
                          not exclude residents who were indoors at home.
    Sep 22     r134       people in the square. The owner's note on r133 was
                          that the residents look weird, and that r133 had
                          been thinking functionally where they were thinking
                          aesthetically. Both were true: the residents walked
                          and pathed and did not clip, and they still looked
                          wrong. Portraits of one resident per species showed
                          why. The head was a quarter of the figure and sat
                          straight on the collar — there was a neck mesh, but
                          it was 0.2 tall centred on headY while the head's
                          underside reaches headY-0.12, so it had spent its
                          whole life inside the head. Long-ear ears used a
                          rotation of exactly ninety degrees, so a 0.43 cone
                          starting 0.30 out reached 0.73 from the centre on a
                          figure with 0.32 shoulders: wings. And every leg
                          ended in a bare cylinder with no foot. All three
                          fixed, the feet merged into the leg mesh so the
                          draw calls are unchanged at 27,806. Aiming the
                          portrait camera also caught a convention error that
                          had quietly spoiled every look-at screenshot of the
                          session: the camera's forward vector is the
                          negation of the one residents face along. The
                          market was thickened at the owner's request — it
                          had twenty stalls and bays with counters, awnings,
                          stock and lanterns, and nobody at a single one of
                          them. Sixteen market people later the plaza holds
                          24.6 on average instead of 11.1. Two residents were
                          found standing inside walls, having walked in: the
                          shove that unsticks a stalled resident only pushed
                          away from other bodies, so anyone stuck in geometry
                          alone had no escape. Wedged 2 to 0, clumps 0, 319
                          of 342 walking.
    Sep 23     r135       the crowd parts. The owner went AFK in the market and
                          came back unable to move in any direction: npcBlocked
                          made a resident exactly as solid as masonry, tested
                          per axis, so a crowd that closes around you is a
                          cage. Reproduced by ringing the player with twelve
                          bodies — on r134 the player moves 0.00 m. Bodies are
                          soft now: anyone the player is standing in steps to
                          the nearest clear spot just outside arm's reach, and
                          the same test walks 5.6 m straight out. An open
                          doorway also stopped asking to be opened; a door
                          whose leaves have swung wide is just a doorway. Then
                          the interiors, where two faults had been hiding each
                          other. A HemisphereLight has no occlusion, so every
                          room was flooded with 2.25 of open night sky; and
                          the great tower's crown beacon, measured from inside
                          the Great Hall, was a violet point light of
                          intensity 7368 at two metres against 83 for a lit
                          hearth, reaching sixty units down through the keep.
                          That was the flat violet wash, not the sky. Indoors
                          the sky eases to a fifth, the beacon lights the
                          tower instead of the ward, and no light outside the
                          room you stand in gets a slot. The Great Hall itself
                          was rebuilt: 950 square metres that held a
                          twenty-metre slab, a throne and two tables shoved
                          against it now has a dais, trestle tables with
                          benches, two hearths, banners and wall sconces.
    Sep 25     r140       modelled not assembled. r136-r139 ("reference
                          build", never archived) added a "visual canon"
                          layer — ten vista sites scattered at the map's
                          edges, each built around one preset camera angle —
                          entirely as aBox/aCyl/aCone calls with hand-tuned
                          rotations, the exact pattern this project moved away
                          from for the city itself back at r121. The owner
                          found it on foot: two motionless figures sitting on
                          their own walkway outside a gate, eleven lamps where
                          four belonged, and — worst — a bridge over no water
                          at all, waterDepthAt() there returning a flat 0. The
                          ruins turned out to have three separate,
                          uncoordinated generators drawing overlapping stone
                          in the same 16 m patch: the base game's own scatter,
                          plus two new "rib" loops, plus an 18-rod ring, none
                          aware the others existed. Every one of these was
                          invisible to every audit this project owns — they
                          parse, and audit-dead doesn't know a kneeling knight
                          from a standing one. Fixed in place (the lamps
                          thinned, the redundant ribs removed, the skywatch
                          pair moved 11 m off their own path), and the bridge
                          and three of the four posed figures rebuilt as
                          actual Blender models: tools/assets/foxglove-
                          bridge.py, oath-knight.py, hooded-watcher.py — each
                          rendered to a PNG and looked at before it ever
                          touched the game, which is the entire point. The
                          first oath-knight render scattered across the frame
                          from a wrong rotation axis; caught in the preview,
                          fixed, re-rendered, confirmed, only then exported.
                          The bridge now has a real river under it, built the
                          same way Saltmere's was. PROJECT.md's "Making
                          assets" section now states this as the standing
                          rule for any posed figure or one-off landmark:
                          model it, do not assemble it from primitives in
                          the source file.
                          Verified: 0 dead functions, 0 new road obstructions,
                          352 residents, 6/6 variants, smoke clean.
    Sep 27     r141       quiet road. The owner: "in your screenshot alone,
                          I'm seeing nonsense in the road." Three wrong
                          answers before the right one. Not the standing-
                          stones ring 26 m off — its crystal and hidden light
                          pillar were both exactly where they were meant to
                          be. Not ruinedRing()'s loose wall-rubble, though
                          that had the same unchecked-scatter bug already
                          fixed twice this session elsewhere (its rubble
                          skipped the road/clearing check its own wall stub
                          used, and six of this session's own new sites were
                          never in WILD_CLEARINGS for it to check against) —
                          a pixel diff against the pre-fix screenshot proved
                          that fix changed nothing at this site. What it was:
                          nine rain-oath-ring-stone paving nodes, added
                          earlier this session as ring dressing, 5.4 m out,
                          no rotation, 3.8 m apart — far enough apart that
                          they never read as a ring, only as litter. Found by
                          projecting all nine world positions through the
                          exact screenshot camera and landing, pixel for
                          pixel, on the nine visible discs; removed. Also
                          rebuilt tools/assets/oath-knight.py's kneeling pose
                          around a limb(a,b) helper — every jointed piece now
                          derives its own length and rotation from the two
                          joints it spans, after the hand-guessed version put
                          the down leg's thigh and shin rotations on the
                          wrong leg and the figure read as a scattered pile
                          with a floating helmet.
                          Verified: 0 dead functions, parse/audit/dom clean,
                          6/6 variants, smoke clean (bluetooth chooser
                          installed, r141 in the window title).
    Sep 28     r142       walkaround. Instruction: visit every visual-canon
                          site in person and check it against what the code
                          claims, because "the code can say something and
                          eyes can say otherwise." Visited all 8 stored
                          VISUAL_CANON.captures cameras and read each frame
                          against its own one-line target description. Four
                          real bugs, none visible in any diagnostic. Biggest:
                          r141's own WILD_CLEARINGS fix turned out to also
                          feed a wilderness-cairn placer and two signpost
                          pickers, not just the rubble check it was written
                          for — registering the four new canon sites there
                          silently planted a cairn 2m from the rain-oath
                          knight, inside the very shot r141 had just cleaned.
                          Split into a second array, CANON_SITE_CLEARINGS,
                          read only by the rubble/tree check. Also found: the
                          same sparse-ring-reads-as-litter shape from r141
                          repeated at the ruins (fallen-hall-outer-circle-
                          stone, removed); a "frame the vista with bare
                          branches" tree at three sites sized like a full
                          background tree at 7-11m from its own camera,
                          reading as a solid black wall across the frame at
                          the overlook (cut to ~1/3 scale at all three);
                          and the skywatch companion's optional wing pair
                          rendering as two blade shapes nearly a metre long,
                          burying the seated figure it was meant to accent
                          (cut down, tilt narrowed). Checked and confirmed
                          NOT broken: the foxglove river mesh (present,
                          correctly placed, just dark at night), the ruins'
                          waterfall veil color (#8fb7ff confirmed — a
                          magenta read was ambient bleed), and three
                          reference NPCs absent from their site's wide vista
                          shot but present and correctly posed on direct
                          approach — a camera-framing gap, not a missing NPC.
                          Verified: parse/audit/dead clean, 6/6 variants,
                          smoke clean (bluetooth chooser installed, r142 in
                          the window title).
    Sep 30     r143       places under the moon. Instruction: "design
                          landmarks and places to explore … match that visual
                          canon as close as possible, fix the npcs, populate
                          the world, continue and fix the city rebuild." Every
                          reference place is now somewhere you walk into,
                          climb and look out from, each laid out in its own
                          frame (mostly on the moon's bearing, so its proof
                          shot holds the moon), the climbs with walk proofs:
                          the Fallen Hall and the Veilscar falls (nave 5/5,
                          stair to 15.05 m); the Oathfield (56 planted
                          oath-blades, a lychgate, the winged angel; 10/10);
                          the Watcher's Bluff over Lowmere (a 21 m crag above
                          a lit hamlet, a watchtower beyond; 10/10); the
                          Foxglove crossing (a humpbacked arch over the real
                          brook, a gate tower); the Rain Oath (a causeway over
                          a mere to a ring of stones, the knight remodelled);
                          the Skywatch knoll (an armillary on its crown). New
                          beyond the seven: Foxglove Mill, whose overshot
                          wheel turns under its flume; the Lantern Grove, a
                          bare oak hung with thirty lanterns; the High Step, a
                          real climb up the inner wall by the south gate
                          (8/8). New machinery: terrain landforms, walkable
                          stairs and decks, a Blender kit (tube, leaf) and a
                          vertex-alpha glow mask, landmark movers. Eleven
                          residents live out there; role residents keep their
                          pose and only glance at you; faces read at play
                          distance and every role wears its part; talk and
                          directions for every new place. Night sky rebuilt
                          to the canon (cobalt/violet, one moon direction for
                          disc, light and glint, staged meteor showers and
                          omen, rain). One lane that ran into the back of a
                          house rerouted: road obstructions 0. Removed the
                          r138 stand-ins these replace. Installers not built
                          (no Windows toolchain in the container).
                          Verified: parse/audit/dead clean; runtime audit
                          against the r142 archive, 16 wards / 96 dialogue
                          branches none broken, draw calls 449 -> 436; walk
                          proofs above; all 12 captures looked at (three
                          reframed); 6/6 variants built and booted; smoke
                          clean (r143 in the window title).
    Sep 30     r144       market and cathedral. The city itself, after r143's
                          places outside it. The Cinder Market re-authored as
                          a table (tools/plan-market.py): 34 modelled stalls
                          (draper, grocer, potter) in six rows along the
                          avenue, lantern strings on poles across the avenue
                          and two aisles, the hearth moved off the avenue's
                          kerb into a court, the well its interaction always
                          pointed at, sixteen keepers behind their counters.
                          It replaces a ring of stalls laid by trigonometry
                          and bays nudged by offRoad(), one of them into the
                          tavern's wall. Lots fronting the main avenues and
                          the market stand two to four storeys (74 raised).
                          The cathedral - a box with two cylinders - is now
                          the Cathedral of Hours, a modelled gothic church
                          you walk into: aisles on an arcade, flying
                          buttresses, twin 44 m spires with lit belfries, a
                          rose over the portal, the apse, pews, the altar,
                          its verger, a kneeler and a pilgrim; walk proof
                          9/9.
                          Verified: parse/audit/dead clean; runtime audit
                          against r143, 17 wards / 102 dialogue branches
                          none broken, road obstructions 0, draw calls
                          436 -> 442; market probe 34/34 stalls, 16 keepers;
                          all 14 captures looked at; 6/6 variants built and
                          booted; smoke clean (r144 in the window title).
    Sep 30     r145       halls and crossings. The eleven landmark halls,
                          boxes under a flat four-sided cone, get steep roofs
                          whose gables stand over their doors, buttresses,
                          tall lit windows and a feature by kind (a chimney
                          and timbered gable for a tavern, a lantern turret
                          for an archive, a tower for a guild, a bell-cote
                          for the shrine and chapel); rooms untouched. Lamps
                          on two corners of each of the main avenues' 23
                          crossings, baked from the live street plan by
                          tools/plan-crossings.py (45 of 46 fit). Walking the
                          Rain Oath, which r143 had only photographed, found
                          its causeway half a metre under the mere: it is a
                          stone embankment walked as a deck now (13/13), and
                          the Skywatch knoll walks 8/8.
                          Verified: parse/audit/dead clean; runtime audit
                          against r144, no errors, 102 dialogue branches
                          none broken, road obstructions 0, draw calls
                          unchanged; 14 captures looked at; 6/6 variants
                          built and booted; smoke clean (r145 in the title).
    Sep 30     r146       the avenues at night. Lit windows are leaded;
                          warm pools of light on the paving under every lit
                          ground-floor window, hall window and door lantern
                          (one additive mesh); door lanterns' glass lit.
                          Chimney stacks on three houses in five, sized to
                          their roofs, modelled crowns and pots; the forty
                          nearest smoke, leaning with the wind. The four old
                          fixed smoke columns, which drifted off their
                          sources, removed. The avenues: 25 houses facing
                          them from the gaps and 14 lantern festoons across
                          them, baked by tools/plan-avenues.py; lit windows
                          in every back or side wall that faces a street.
                          Verified: parse/audit/dead clean; runtime audit
                          against r145, no errors, 102 dialogue branches
                          none broken, road obstructions 0, six new draw
                          calls; 14 captures looked at; 6/6 variants built
                          and booted (r0 after a fix); smoke clean (r146 in
                          the title).
    Sep 30     r147       signs and lamps. Every shop's sign, a coloured
                          board on a wooden arm, is its trade hung from a
                          wrought-iron bracket: pretzel, cask, candles,
                          shears, key, horseshoe, book, bottle
                          (tools/assets/shop-signs.py), 143 of them, clear
                          of the awnings. The street lamps, a pole with a
                          glowing cube, are cast-iron lamp posts with
                          four-paned lanterns (tools/assets/street-lamp.py),
                          each lit one with a pool of light under it. The
                          Cinder Market's strings sag as one tube and carry
                          the festoon lanterns.
                          Verified: parse/audit/dead clean; runtime audit
                          against r146, no errors, 102 dialogue branches
                          none broken, road obstructions 0; 14 captures
                          looked at; 6/6 variants built and booted; smoke
                          clean (r147 in the title).
    Sep 30     r148       torchlit walls. Both town walls were unlit stone
                          between the gates and their towers dark drums: a
                          torch in an iron sconce three times between each
                          pair of towers on the outer faces and once on the
                          inner wall's inner face (tools/assets/wall-
                          sconce.py), a pool at the foot and a wash up the
                          stone, the middle one of each span a real light;
                          arrow slits lit up every tower. Light washes up
                          the wall are a second kind of light pool, used by
                          the houses' door lanterns too.
                          Verified: parse/audit/dead clean; runtime audit
                          against r147, no errors, 102 dialogue branches
                          none broken, road obstructions 0; 14 captures
                          looked at; 6/6 variants built and booted; smoke
                          clean (r148 in the title).
    Sep 30     r149       the bell tower. The Cathedral of Hours' east tower,
                          a solid block, is hollow and climbable: a door from
                          the east aisle, a stone newel stair of ten flights
                          to a belfry at 19 m, open arches, two bells, a
                          lantern; a new capture from the belfry over the
                          roofs. Walkable surfaces can be stacked: one marked
                          so counts only within 1.5 m of the walker, so a
                          stair can pass over itself.
                          Verified: parse/audit/dead clean; walked door to
                          belfry 14/14; runtime audit against r148, no
                          errors, 102 dialogue branches none broken, road
                          obstructions 0; all captures looked at; 6/6
                          variants built and booted; smoke clean (r149 in
                          the title).
    Oct 1      r150       the bells ring the watch in. The cathedral's two
                          bells are their own model (cathedral-bell) and
                          swing when the watch turns: rung up, full, dying
                          away, over 27 s. A landmark mover can swing as well
                          as spin. Sixteen doves on the nave ridge and the
                          spire drums go up when the bells ring, wheel over
                          the church, and land back where they sat: one mesh
                          for the flock, rewritten only while it flies.
                          Verified: parse/audit/dead clean; a full ring read
                          off at runtime, every dove back on its perch;
                          runtime audit against r149, no errors, 102
                          dialogue branches none broken, road obstructions
                          0; all captures looked at; 6/6 variants built
                          and booted; smoke clean (r150 in the title).
    Oct 1      r151       the city heard. World sound, all of it synthesized
                          in the page: the bells struck from a church bell's
                          partials, wind rising with height, rain, the two
                          nearest fires crackling (hearths, forges, wall
                          torches), crickets beyond the walls, footsteps, the
                          doves' wings. Positional, one shared reverb; a Sound
                          section in the settings, kept in the browser.
                          Verified: parse/audit/dead clean; a bell strike
                          rendered offline and its spectrum read; levels read
                          off the running context; runtime audit against
                          r150, no errors, 102 dialogue branches none broken,
                          road obstructions 0; all captures looked at; 6/6
                          variants built and booted; smoke clean (r151 in the
                          title).
    Oct 1      r152       the forest at night. The 4,200 cone trees outside
                          the walls are modelled (tools/assets/trees.py):
                          pines, firs, broadleaves, dead pines, and shrubs
                          along the edge; one BatchedMesh, culled per tree,
                          trees past the fog's reach hidden; same world
                          stream and colliders. Fireflies at the forest's
                          edge and along the brook.
                          Verified: parse/audit/dead clean; five standpoints
                          before and after; frame time against r151, faster
                          at all four standpoints; runtime audit against
                          r151, no errors, 102 dialogue branches none
                          broken, road obstructions 0; all captures
                          looked at; 6/6 variants built and booted; smoke
                          clean (r152 in the title).
    Sep 22     r130       props & porters. Every held prop now uses its
                          corresponding wrist grip; the guard shield is a
                          forearm item, and the far LOD does not leave nested
                          props visible. Eight living carts remain, with
                          unencumbered porters, 2.45 m trail, 2.25 m hard
                          clearance and a pull pose. Forge/artisan aprons,
                          scholar book/coat and watch armour were reshaped to
                          remove dark board silhouettes. The QA harness now
                          ignores benign closed-pipe EPIPE errors. Full
                          runtime audit clean. <- current
    Sep 22     r129       resident hands. A reported close-up of Jarek Quarrier
                          showed sleeves ending bluntly and a hammer hiding
                          the wrist. Every animated arm now includes a
                          low-poly species-toned palm and thumb, merged into
                          its existing limb mesh; held props sit behind the
                          grip. Scholar books now show a page face and sit
                          below the chest. City/interior work untouched.
    Sep 22     r128       rooms you can see. The owner: "there's weird
                          clipping in all the interiors." Not clipping — one
                          point lamp per room, physical falloff, so the shelf
                          beside it blew out and the floor three metres away
                          was black. Every walk-in room gets a second light
                          now: dim, wide, cool, high, budgeted exactly like
                          the first and only alive while you are inside.
                          Warm pool against cold fill, which is the grammar
                          the owner's reference clips use. Found while fixing
                          it: the street kit's glTF callback could reach
                          shaderWarmMs before that `let` had been evaluated,
                          killing every kit piece — door surrounds, frames,
                          banners, the lot — with nothing but a console
                          warning. Declared early now. That race means some
                          sessions have been running with the kit missing.
    Sep 21     r127       one shop, everywhere. The owner's own screenshots,
                          fixed: the Great Hall's generic wall-and-floor
                          clutter pass (barrels, crates, sacks — the same set
                          any tavern gets) is skipped now that the hall has
                          its own composed furniture, and the district
                          compiler's 20 solid-box stalls ("a bell hangs on a
                          string", forever, nobody behind the counter) are now
                          the same walk-in room every other shop is — 13 of
                          20 open, the rest stay shut the same way a blocked
                          terrace shop does. Caught and fixed in the same
                          pass: one shop's own interior shelf was standing in
                          a road at the end of a tightly packed compiler row;
                          checked directly now, the same rule r125 wrote for
                          street lanterns. Shops 113, shop sum 669314 — a real
                          change, not drift; parcels and resident addresses
                          untouched, and both numbers repeat exactly across
                          two runs and a fresh seed.
    Sep 21     r126       nothing left to roll. The owner: "I don't even want
                          any part generated." The two remaining systems that
                          move where anything stands — 268 outer residents
                          walked down every arterial street, and the district
                          compiler's 126 attempted lots — are baked the same
                          way r125 baked the terrace walk. Proven with two
                          fresh, never-used seeds: both give the exact city
                          the fixed seed always has (shops 115, parcels 98,
                          same shop sum, same resident-address sum).
                          WORLD_SEED no longer moves a building, a shop or a
                          resident anywhere. About fifteen worldRandom() calls
                          remain, all decorative (texture dither, a ruin's
                          rubble, which good sits on a counter) and none of
                          them move a single fingerprint number — left as is,
                          documented, not hidden.
    Sep 21     r125       the city holds still. innerInfill's live terrace walk
                          — worldRandom() rolls for every house and shop's
                          width, depth, storeys, material, accent and whether
                          it became a shop, one after another down every
                          street — is retired. The walk was run once and its
                          exact output frozen into a table (CITY_LOTS_BUILT /
                          CITY_LOTS_VACANT); innerInfill replays it. Same city,
                          verified house-for-house and shop-for-shop against
                          the live build it replaced, but it can no longer
                          reshuffle when something else changes, and any one
                          lot is now a line in a table instead of a hash to
                          reverse-engineer. First step of a larger, explicit
                          move away from procedural generation toward one
                          hand-finished map; the rest — residents, wilderness,
                          clutter, the roads and districts themselves — is
                          still generated and is the next phase, not this one.
    Sep 21     r124       material & resident pass. Structured 128 px painted
                          building materials, 82% balanced rendering (98%
                          clear / 62% performance), tight warm bloom and the
                          existing FXAA finish. Five peoples now have three
                          build axes and eight job silhouettes; hooded people
                          are rare, and props are fixed to animated arm pivots
                          rather than clipping through bodies. City layout,
                          road and collision generation untouched.
    Sep 21     r123       clean-poly polish. 72% balanced render scale with
                          clear and performance alternatives, post-grade FXAA
                          and smooth hard-surface/NPC kit normals. Trees,
                          grass and their low-side-count silhouette stay
                          faceted. The same seal carries a geometry pass: a
                          fix for kit pieces that were exporting into the walls
                          (surrounds, frames, timber, lanterns, leadlights now
                          stand proud), roof dormers with lit windows, and 221
                          wall banners. Seed, doors, collision and residents
                          untouched; the homes fingerprint matches r122.
    Sep 21     r122       street dressing. Stone quoins up the street corners of
                          half the taller homes, a scalloped teal valance on
                          the awning of every frame shop (100 of them), and
                          paving that keeps crisp texels up close instead of
                          smearing into streaks. Seed, doors, collision and
                          residents untouched: the homes fingerprint matches
                          r121.

## Known gaps

- No collider stands in a carriageway any more (`inRoad: 0` at r107). About
  150 props intrude near one, depending on seed; all under 4 units of reach.
- Residents draw in one BatchedMesh since r113, but each is still a group of
  animated objects on the CPU. Since r115 most of them actually walk (229 of
  326 moved 25 m in two minutes, against 94 before).
- The places beyond the wall respond only to the player (r108). Nobody else
  walks out to them, and no resident visits the graveyard they talk about.
- 15 landmark interiors and, since r113, 50–72 walk-in homes in a city of
  roughly 1,400 buildings. Shops and workshops are still facades.
- The inlined Three.js runtime is r186 (since r110), physically lit (r111).
- The z = −42 lane runs into the cathedral (2026-09-14 audit, F10): the fix
  reshuffles the seeded city, so it waits for the owner.
- **r85/r86 changed the scale of the world.** Measured at the north gate spawn:

        r84   ~2,800 calls   ~940,000 tris   ~10,000 colliders   208 residents
        r86    1,130 calls    493,000 tris    4,413 colliders   162 residents
        r88    1,145 calls    500,000 tris    4,421 colliders   162 residents
        r89    1,131 calls    486,000 tris    4,421 colliders   162 residents
        r90    1,152 calls    488,000 tris    4,436 colliders   162 residents
        r91    1,136 calls    484,000 tris    4,377 colliders   162 residents
        r92      320 calls    488,000 tris    4,431 colliders   162 residents

  Draw calls by where you stand, at r92 — the number moves now, which is the
  whole point:

        north gate      320   (all 162 residents on their one-mesh copy)
        cinder market   213   (146 far, 16 near)
        beside someone  176

  And at r95, with the city doubled in radius and the population doubled:

        residents            326
        draw calls (gate)    491
        triangles            643,000
        colliders            6,631
        walking at any moment  36%  (~117 people), ~24 units each per 30s

  And by watch, at r96 — the number that says the city is being lived in:

        labour / market   326 out,   0 indoors
        still             126 out, 200 indoors,  241 draw calls
        ember             326 out, 137 of them stopped talking to each other

  r97: 326 residents, 15 walk-in interiors, 39 households, 1,089 tie edges of
  which 972 are answered from the other end. 539 draw calls, 663k triangles,
  7,521 colliders. Colliders standing on a road: 0.

  Verified at r99, both of which had never been exercised end to end:

  - **the music player.** A generated WAV pushed through the file input as a
    real File: the track label updates, it plays without a user gesture in
    Electron, and pause, resume, volume, next and previous all drive the same
    element.
  - **touch.** The stick moved the player 28 units and a canvas drag turned the
    camera 0.55 radians. Note that this cannot be tested in a hidden browser
    pane — rAF does not fire there, so the game loop never runs and every input
    reads as doing nothing. That is the pane, not the controls.

  r100: 326 residents, 15 walk-in interiors, 533 draw calls, 666k triangles,
  7,599 colliders. Doors clear 15/15, buildings in road 0, colliders on a
  carriageway 0, gates 4/4.

  The Switch 2 decode is checked against the capture itself rather than against
  my reading of it — `node tools/test-switch-frames.js` replays the twenty-three
  frames through the same decode the panel uses and asserts twelve properties of
  them, including the one that identifies the heat byte. The panel's own replay
  box does the same thing interactively: paste a log, watch it decode.

  Frame time matters more than any of those. Measured in the Electron harness,
  which runs software GL, so read the ratio and not the absolute:

        r90    37.2ms median   (18.4ms with shadows disabled)
        r91    16.4ms median   (13.8ms with shadows disabled)

  87% of the draw calls are residents: 1,002 of 1,155 meshes, 6.2 per villager.
  The whole authored city — walls, roads, roofs, interiors, forest, mountains —
  is 153 meshes. Any future work on resident count or resident detail runs into
  that number first.

  Roughly half the triangles and well under half the colliders, because the
  greater city no longer exists. Everything below this line predates that cut
  and was measured at the old outer-gate spawn.

- Render telemetry, measured at the old spawn (408,408) facing the centre:

        r74   2,540 calls    811,325 tris   2,392 geometries   154 residents
        r75   2,539 calls    814,605 tris   2,391 geometries   154 residents
        r76   2,539 calls    814,605 tris   2,391 geometries   154 residents
        r77   3,302 calls  1,015,543 tris   3,107 geometries   208 residents
        r79   1,425 calls  1,018,123 tris   1,425 geometries   208 residents

  r79 is the residents batching pass. They were 3,208 of 3,386 draw calls —
  208 of them at 16.1 meshes each. Everything static inside a resident is now
  merged into one vertex-coloured mesh per moving part: one head, one torso,
  four limbs. Six meshes, identical appearance. Triangles are unchanged (the
  merge drops the index, which costs a little), but draw calls fell 58%.

  r75 was effectively free and r76 changed no world geometry at all. r77 costs
  **+30% draw calls and +25% triangles** — the triangles are the forest going
  2,100 -> 5,200 trees, the calls are the ward population going 96 -> 150,
  since each resident is several meshes and instancing does not apply to them.
  This is by far the largest single jump in the project and it crosses a
  million triangles. **The shadow/light and material batching pass is now
  overdue** — treat it as the next engine revision rather than adding more
  geometry. Note that both figures swing widely with camera position AND with
  frame aspect, so only compare readings taken the same way; an earlier
  published figure of 2,644 / 817k for r76 was never actually measured and was
  wrong.
- Live Peak Pro pairing now works against real hardware and has been confirmed
  by the owner: pairing, authentication, profile writes and heat cycles all
  exercised on an actual Peak Pro (2026-09-02). Note this was impossible before
  r76 — main.js called preventDefault() on select-bluetooth-device and nothing
  in the renderer ever answered the callback, so requestDevice() never settled
  and Connect hung silently in the desktop app, for any device. The handshake is
  now asserted by `set EMBERWATCH_SMOKE=bluetooth && npm start`, which fails
  loudly if the promise ever hangs again.
- Whether any non-Puffco device can be driven at all is unknown. The r76 probe
  (Puffco panel -> "device probe") surveys services, characteristics,
  properties and readable values without writing anything, which is the way to
  find out. Web Bluetooth hides services not named before the chooser opens,
  so a genuinely unknown device needs its UUIDs read off
  chrome://bluetooth-internals and pasted in first.
- The r75 installer and portable exe are built and the portable one passes an
  Electron smoke test (window title reads "Emberwatch — r75"). Both still use
  Electron’s default icon, and the package has no author or publisher
  metadata — electron-builder warns "author is missed" on every run, and the
  binaries are unsigned. Treat signing, icon artwork, and release branding as
  a dedicated packaging pass rather than inventing those identity choices
  automatically.

- `mushroom_forest.html` (the bioluminescent infinite-terrain build) is NOT on
  this machine's Downloads or Desktop. If you want it, find it before the wipe.
- The old `START-Windows.bat` / `START-Mac.command` localhost launchers are
  gone and no longer needed — the app:// scheme in the Electron build replaced
  the localhost-server workaround.
