// The runtime harness: load the game in an Electron window, let it run, then
// evaluate a probe file inside the page and print what it returns.
//
//   app/node_modules/.bin/electron tools/harness <html> [probe.js] [waitSeconds] [shotsDir]
//
// Why it exists. A hidden browser pane never fires requestAnimationFrame, so
// nothing that unfolds over time can be observed there — residents walking,
// session timers, the water moving, anything on the game loop. This window
// keeps rendering while nobody looks at it (backgroundThrottling off), which is
// the only way to test those.
//
// Two properties to know before trusting a number from it:
//   - Hardware acceleration is off. WebGL runs in software, so frame times are
//     good for comparing one build with another and meaningless as a figure
//     for real hardware.
//   - The preload removes navigator.bluetooth, crypto.subtle and the clipboard,
//     the way Edge on file:// does. Nothing here can reach a device.
//
// Screenshots. If the probe's result has a `shots` array of
// { name, x, z, yaw, pitch, y? }, and a shotsDir is given, the harness stands
// the player at each, waits for a few frames, and saves <shotsDir>/<name>.png.
// Shots are taken at full render scale so they are legible.
//
// This used to live in a temporary folder from one session. It is part of the
// project now because PROJECT.md, the audit prompt and the night-shift skill
// all depend on it.
const { app, BrowserWindow } = require('electron');
const fs = require('fs');
const path = require('path');

// A harness is often launched by an editor or a short-lived test runner. If
// that runner has already collected its output, Electron's later console logs
// can hit a closed pipe. This is a normal end-of-run condition, not a game
// failure, and must not surface as a frightening main-process dialog.
for (const stream of [process.stdout, process.stderr]) stream.on('error', error => {
  if (error && error.code === 'EPIPE') return;
  throw error;
});

const target = process.argv[2];
const probePath = process.argv[3];
const waitSeconds = Number(process.argv[4] || 12);
const shotsDir = process.argv[5];
if (!target) { console.log('usage: electron tools/harness <html-or-url> [probe.js] [waitSeconds] [shotsDir]'); app.exit(2); }

app.disableHardwareAcceleration();

// HARNESS_PROFILE=<dir> runs with its own storage: its own localStorage, so its
// own world seed and settings, and no lock clash with a harness already
// running. Without it every run shares one profile, which is what keeps seeds
// and screenshots comparable from run to run.
if (process.env.HARNESS_PROFILE) app.setPath('userData', path.resolve(process.env.HARNESS_PROFILE));

app.whenReady().then(() => {
  // HARNESS_WINDOW_X/_Y push the window off the primary display while the
  // owner is using it for something else. Unset, it opens at the old 40,40.
  const winX = process.env.HARNESS_WINDOW_X ? Number(process.env.HARNESS_WINDOW_X) : 40;
  const winY = process.env.HARNESS_WINDOW_Y ? Number(process.env.HARNESS_WINDOW_Y) : 40;
  const win = new BrowserWindow({
    show: true, width: 1280, height: 720, x: winX, y: winY,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: false, sandbox: false,
      // The whole point: keep rAF running in a window nobody is looking at.
      backgroundThrottling: false
    }
  });
  win.webContents.setBackgroundThrottling(false);

  win.webContents.on('console-message', (event) => {
    const { level, message } = event;
    if (/Security Warning|unsafe-eval|electronjs.org/.test(message)) return;
    console.log('[' + String(level).toUpperCase() + '] ' + String(message).slice(0, 300));
  });
  win.webContents.on('did-fail-load', (_e, code, desc) => console.log('[FAIL-LOAD] ' + code + ' ' + desc));
  win.webContents.on('render-process-gone', (_e, d) => console.log('[RENDERER GONE] ' + JSON.stringify(d)));

  const load = /^https?:/.test(target) ? win.loadURL(target) : win.loadFile(path.resolve(target));
  load.catch(err => console.log('[LOAD THREW] ' + err.message));

  // HARNESS_FOLLOW_RELOAD=1: a probe that makes the page reload (the WebGL
  // context-recovery test does) is run again on the reloaded page, with
  // window.__harnessPass counting the loads, instead of the run ending on the
  // navigation. At most three passes. Without it, only the first load counts.
  const follow = !!process.env.HARNESS_FOLLOW_RELOAD;
  let pass = 0;
  win.webContents.on('did-finish-load', async () => {
    pass++;
    if (pass > 1 && !follow) return;
    if (pass > 3) return;
    await new Promise(r => setTimeout(r, waitSeconds * 1000));
    let result;
    try {
      const probe = probePath
        ? fs.readFileSync(probePath, 'utf8')
        : `(async()=>({booted:!!window.EMBER, frames:window.EMBER?window.EMBER.renderer.info.render.frame:null}))()`;
      await win.webContents.executeJavaScript('window.__harnessPass=' + pass, true);
      result = await win.webContents.executeJavaScript(probe, true);
      console.log('RESULT' + (follow ? ' pass ' + pass : '') + ' ' + JSON.stringify(result && result.shots ? { ...result, shots: result.shots.map(s => s.name) } : result, null, 1));
    } catch (err) {
      console.log('[PROBE THREW] ' + err.message);
      if (follow) return;          // the page went away under the probe; wait for the next load
    }
    if (follow && result && result.reloading) return;

    if (shotsDir && result && Array.isArray(result.shots)) {
      fs.mkdirSync(shotsDir, { recursive: true });
      await win.webContents.executeJavaScript('window.EMBER&&EMBER.setPixel(1)', true);
      for (const shot of result.shots) {
        await win.webContents.executeJavaScript(`(()=>{const E=window.EMBER,s=${JSON.stringify(shot)};
          E.player.x=s.x;E.player.z=s.z;E.player.vy=0;E.player.onGround=true;
          E.player.y=s.y!==undefined?s.y:(E.terrainAt?E.terrainAt(s.x,s.z):0);
          E.look(s.yaw,s.pitch||0);})()`, true);
        await new Promise(r => setTimeout(r, 1500));
        const image = await win.webContents.capturePage();
        const file = path.join(shotsDir, shot.name + '.png');
        fs.writeFileSync(file, image.toPNG());
        console.log('SHOT ' + file);
      }
    }
    app.exit(0);
  });

  // HARNESS_TIMEOUT=<seconds> gives a long probe more than the default 300 s
  // after its wait (probe-mourners follows residents on a walk of several minutes).
  setTimeout(() => { console.log('[TIMEOUT]'); app.exit(1); }, (waitSeconds + Number(process.env.HARNESS_TIMEOUT || 300)) * 1000);
});
