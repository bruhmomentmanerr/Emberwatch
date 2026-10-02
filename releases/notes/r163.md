**r163 — modelled masses** · 1.63.0 · 2026-10-02 · phase 5, world depth

### Summary

Modelled masses. The residents fuller (thicker, bent arms with shoulder caps, a deeper torso with a posture, calves, bigger hands and feet) with shading painted into their colours; the trades' staffs, spears, shields, mallets, baskets, hammers and the reference roles' staff and bow modelled in the kit instead of primitives. villager() 2.2 s to 1.6-1.7 s over a boot. The game times its own load in the menu. Verified: audits clean; in-game lineup r162 against r163; variants 6/6; smoke.

### Patch notes

**State: r163 / 1.63.0, sealed 2026-10-02 ("Modelled masses").** The owner,
on r162: "the html file takes forever to load as well" and "start pushing
that npc work" — the residents, which "still sort of look like geometric. I
would like to just have them as like modeled masses or something".

**Next:** the owner's look at the residents, and the load line from their
own machine (menu → Display, under fullscreen; also in the console). Then,
for the residents, one of the two things below that this revision did not
do, whichever the owner's eye says matters more.

### The residents, as masses

Shot side by side in the game (six market people pinned in a row by the
hearth, r162 against r163) and in a studio page built from the kit alone,
the r159 figures read as mannequins: arms of thin tube hanging dead
straight into the hips, a flat shelf for shoulders, a torso about twice
as wide as it is deep, legs of uniform pipe, and every surface lit evenly.
And the most geometric things in any frame were not bodies at all: the
trades' props were still r158 primitives, five-sided black sticks for
staffs and spears, boxes for a mallet and a basket, an eight-sided disc for
a shield. r163:

- **Fuller forms.** Sleeves about a quarter thicker, swelling at the
  shoulder and biceps, the elbow a little back and the forearm forward, and
  hanging slightly out from the body; a rounded shoulder cap that closes
  the top of every sleeve, so an arm grows out of the shoulder; larger
  hands that follow the forearm. The torso deeper and rounder, with a
  posture (chest forward, shoulder blades and seat back) and a sloped
  trapezius in place of the shelf; a thicker neck. Thighs fuller, a calf in
  every shin, chunkier boots and feet; tall boots' cuffs turned, not
  flared.
- **Shading painted in**, as the PS2-era figures in the references carried
  it in their textures: a surface turned down is darker than one turned up,
  the lower a point stands on the figure the darker, and an arm darkens on
  its inner side toward the armpit. It rides in the colour bytes every
  vertex already has (`NpcMesh(ox, oy, inner)`, `vert`); no attribute and no
  shader change.
- **The props modelled in the kit's own way** (`npcProp*`, "what they
  carry"): a turned staff with a crook and a leather grip, an ash spear with
  a leaf-shaped head and a socket, a round shield with a dome, an iron rim
  and boss painted in the resident's colour, a mallet, a woven basket held
  by its handle, a smith's hammer; and for the reference roles a plain
  pole under the staff's crown and a bow with a tapered limb, a grip and a
  string. Each is centred and sized as the primitive it replaces. The book,
  the pipe and the glowing lantern are unchanged.

What it is not yet: the figures are still rigid segments on the rig, so a
joint is hidden by overlap, not shared by one surface. Two ways on from
here, not started: one continuous body per resident bent by its pivots in
the shader (each resident's pivot matrices in a texture the resident batch
reads, two-bone blending at shoulders, hips and knees), which is what
"modelled masses" most literally means; or heavier stylisation of the
pieces themselves. The owner's look decides.

### The load

The browser load was measured in stages in the harness (software
rendering, one boot each): page and engine 0.15 s; world 3.1 s, the largest
pieces the city's merge (275 ms), the street graph (207 ms) and the
residents' mask atlas (490 ms); the residents 2.7 s; the lamps' shaders
0.45 s; the first frame 2.1 s. The residents were the largest piece of
script, and two things in the kit made them cost more than they should:
`loft` worked out each Catmull-Rom ring once per vertex instead of once per
row, and the far version is a second full build. The first is fixed. Over
two boots each, `villager()` came to 2,183 and 2,201 ms on r162 and 1,749 and
1,597 ms on r163 (the rigs alone 1,577 and 1,580 against 1,163 and 1,059),
with the fuller figures and modelled props included.

**The game now times its own load** and says where it went: a line in the
menu under Display ("loaded in … s · page · world · people · lamps · first
frame"), the same in the console, and `EMBER.diagnostics().world.loadTimes`.
One harness boot read "loaded in 9.0 s · page 0.5 · world 3.1 · people 2.7 ·
lamps 0.5 · first frame 2.2". The owner's minute was never seen here; this
line is how it will be.

Found and not fixed, for the next session that touches load: this three.js
puts the light counts into every shader program's key, lit or not, so with
three light tiers the unlit materials are compiled three times over for
nothing. Of the 129 programs on one boot, 69 were lit standard materials,
27 basic, 12 points, 18 custom shaders and 3 depth. On Windows each program
is a Direct3D compile. The clean fix is a patch applied by
`tools/build-three.js` (never by hand in the engine block).

### Verified

- `check-parse`, `audit-source` (A 229 as on r162, B and C 0), `audit-dom`,
  `audit-dead` (682, 0 dead), `audit-comments`, `test-switch-frames`,
  `test-switch-b9`, `test-bluetooth-pairing`: clean.
- In-game screenshots: the market lineup r162 against r163, wide, close and
  side; the reference roles with the new staff and bow.
- Variants 6/6 built, 6/6 booted. Bluetooth smoke passed, r163 in the title.
- Not run: the runtime audit; a Windows launch.

### In the code

- 4.98 MB (+8,737 bytes on r162).
- 13 functions added: `loadTimes`, `npcPropBasket`, `npcPropBow`, `npcPropHammerHead`, `npcPropHammerShaft`, `npcPropMallet`, `npcPropMesh`, `npcPropPole`, `npcPropShield`, `npcPropSpear`, `npcPropStaff`, `npcShaft`, `reportLoadTime`.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
