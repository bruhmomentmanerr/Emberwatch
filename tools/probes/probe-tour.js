// A look at the whole of Vaneth in one run: every ward, both walls, the four
// gates, the quarters between the walls, and the four places in the wilds.
// probe-look has seven fixed standpoints for comparing two builds; this one is
// for reading the world itself — geometry standing where it should not,
// buildings in the road, a door with no house.
//
//   app/node_modules/.bin/electron tools/harness app/renderer/index.html tools/probes/probe-tour.js 20 <shotsDir>
//
// HARNESS_PROFILE=<dir> gives it a fresh world, which is the point: the city is
// seeded, so a fault can be in one world and not the next.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2000);
  E.setWatch('labour'); await wait(600);
  const face = (x, z, tx, tz) => Math.atan2(-(tx - x), -(tz - z));
  const at = (name, x, z, tx, tz, pitch = -0.04, y) => ({ name, x, z, y, yaw: face(x, z, tx, tz), pitch });
  const d = E.diagnostics();
  return {
    revision: d.revision, seed: d.world.seed, homes: d.world.homes,
    shots: [
      at('01-north-gate-outside', 0, 410, 0, 300, 0.01),
      at('02-north-gate-inside', 0, 350, 0, 240),
      at('03-market', 0, 136, 0, 108, -0.06),
      at('04-citadel', 0, 62, 0, 14, -0.02),
      at('05-old-vaneth-street', -120, 130, -40, 60),
      at('06-east-ward', 180, 60, 60, 20),
      at('07-west-works', -168, -103, -60, -40),
      at('08-south-road', -62, -190, 0, -60),
      at('09-new-quarters-ne', 250, 250, 120, 120),
      at('10-new-quarters-sw', -250, -250, -120, -120),
      at('11-outer-wall-south', 0, -360, 0, -260),
      at('12-rampart', 60, 372, 0, 100, -0.2, 14.9),
      at('13-track-crossroads', 0, 440, 0, 520, -0.02),
      at('14-pond', -329, 310, -340, 320, -0.14),
      at('15-stones', 318, 318, 330, 330, 0),
      at('16-graveyard', -315, -323, -326, -334, -0.05),
      at('17-fallen-hall', 327, -315, 338, -326, -0.05),
      at('18-wilds-east', 470, 0, 380, 0, -0.02)
    ]
  };
})()
