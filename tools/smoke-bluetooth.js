// Run with Electron: electron tools/smoke-bluetooth.js
// Loads the real desktop app/preload/renderer and exercises chooser IPC and
// the registered pairing handler using synthetic discovery and native-dialog
// answers. No radio, GATT connection, heater command or device write is used.
'use strict';
const { app, BrowserWindow, session, dialog } = require('electron');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const expectedRevision = 'r' + (100 + Number(require('../app/package.json').version.split('.')[1]));

app.disableHardwareAcceleration();
if (process.env.HARNESS_SWIFTSHADER) {
  app.commandLine.appendSwitch('use-gl', 'angle');
  app.commandLine.appendSwitch('use-angle', 'swiftshader');
  app.commandLine.appendSwitch('enable-unsafe-swiftshader');
}
app.setPath('userData', path.join(app.getPath('temp'), 'emberwatch-bluetooth-smoke'));
const timeout = setTimeout(() => { console.error('SMOKE-PAIRING timeout'); app.exit(1); }, 120000);

app.whenReady().then(async () => {
  let handler;
  const pairingSession = session.defaultSession;
  const register = pairingSession.setBluetoothPairingHandler;
  assert.equal(typeof register, 'function', 'run this pairing smoke on Windows or Linux');
  pairingSession.setBluetoothPairingHandler = function (next) {
    handler = next;
    return register.call(this, next);
  };
  const dialogs = [];
  dialog.showMessageBox = async (_window, options) => {
    dialogs.push(options);
    return { response: 0 }; // deterministic test answer, not a real user prompt
  };
  // main.js schedules createWindow from app.whenReady().
  await Promise.resolve();
  const win = BrowserWindow.getAllWindows()[0];
  assert.ok(win);
  // Keep software rendering bounded; the production window size is unchanged.
  win.setSize(900, 600);
  await new Promise((resolve, reject) => {
    win.webContents.once('did-finish-load', resolve);
    win.webContents.once('did-fail-load', (_event, code, description) => reject(new Error(code + ': ' + description)));
  });
  assert.equal(typeof handler, 'function', 'the real desktop registered the handler');
  const wc = win.webContents;
  const js = code => wc.executeJavaScript(code, true);
  await js('window.EMBER?.setPixel(.4)');
  assert.equal(await js('window.emberBluetoothChooser'), 'installed');
  let selected;
  wc.emit('select-bluetooth-device', { preventDefault() {} },
    [{ deviceId: 'smoke-device', deviceName: 'Test device (simulated)' }], id => { selected = id; });
  await js("new Promise(resolve => setTimeout(resolve, 100))");
  assert.equal(await js("document.getElementById('btChooser').classList.contains('open')"), true);
  assert.equal(await js("document.querySelectorAll('#btcList button').length"), 1);
  if (process.env.EMBERWATCH_BT_SHOT) {
    const shot = await wc.capturePage();
    fs.writeFileSync(path.resolve(process.env.EMBERWATCH_BT_SHOT), shot.toPNG());
  }
  await js("document.querySelector('#btcList button').click()");
  await new Promise(resolve => setTimeout(resolve, 100));
  assert.equal(selected, 'smoke-device', 'renderer selection reached the real main process');
  const answers = [];
  await handler({ deviceId: selected, frame: wc.mainFrame, pairingKind: 'confirm' }, answer => answers.push(answer));
  assert.deepEqual(answers, [{ confirmed: true }]);
  assert.equal(dialogs.length, 1);
  assert.equal(dialogs[0].cancelId, 1);
  let cancelled;
  wc.emit('select-bluetooth-device', { preventDefault() {} }, [], id => { cancelled = id; });
  // The chooser suppresses discovery updates for 1.5s after selection.
  await new Promise(resolve => setTimeout(resolve, 1600));
  wc.emit('select-bluetooth-device', { preventDefault() {} }, [], id => { cancelled = id; });
  await js("new Promise(resolve => setTimeout(resolve, 100))");
  assert.equal(await js("document.getElementById('btChooser').classList.contains('open')"), true);
  await js("document.getElementById('btcCancel').click()");
  await new Promise(resolve => setTimeout(resolve, 100));
  assert.equal(cancelled, '');
  assert.equal(await js("document.getElementById('btChooser').classList.contains('open')"), false);
  const state = await js('({ gameBooted: !!window.EMBER, revision: window.EMBER?.diagnostics().revision, secureContext: window.isSecureContext, hasBluetooth: !!navigator.bluetooth, contextLost: window.EMBER?.diagnostics().runtime.contextLost })');
  assert.equal(state.gameBooted, true);
  assert.equal(state.revision, expectedRevision);
  assert.equal(state.secureContext, true);
  assert.equal(state.hasBluetooth, true, 'Linux smoke needs --enable-features=WebBluetooth');
  assert.equal(state.contextLost, false, 'WebGL context must remain healthy through the chooser flow');
  console.log('SMOKE-PAIRING ' + JSON.stringify({ ...state, handlerRegistered: true,
    chooserSelection: true, chooserCancel: true, pairingConfirmed: true, simulated: true }));
  clearTimeout(timeout); app.exit(0);
}).catch(error => { console.error(error); clearTimeout(timeout); app.exit(1); });

// Register the custom scheme before app ready; our ready callback above runs
// before the main process creates its window and installs its session handler.
require('../app/main.js');
