// A normal, playable Electron window for a standalone branch file — the
// harness (tools/harness/main.js) exists for automated probes: it disables
// hardware acceleration, strips Bluetooth, and force-quits after a timeout.
// None of that belongs here. This just opens the file and stays open.
//
//   app/node_modules/.bin/electron tools/play-branch.js <html-file>
//
const { app, BrowserWindow } = require('electron');
const path = require('path');

const target = process.argv[2];
if (!target) { console.log('usage: electron tools/play-branch.js <html-file>'); app.exit(2); }

app.whenReady().then(() => {
  const win = new BrowserWindow({
    width: 1400, height: 900,
    webPreferences: { contextIsolation: false, sandbox: false }
  });
  win.loadFile(path.resolve(target));
});

app.on('window-all-closed', () => app.quit());
