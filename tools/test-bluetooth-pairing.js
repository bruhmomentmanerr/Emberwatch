// Exercise the desktop main process without a radio or a device write.
// Pairing is separate from discovery; check answers, cancellation and races.
//
// The details are shaped as Chromium and Electron really send them (r164):
// deviceId is the device's display name in Unicode isolation marks
// (WebBluetoothPairingManagerImpl passes device->GetNameForDisplay() through
// ContainStringForDisplay, and ElectronBluetoothDelegate sets it as deviceId),
// never the address-like id the chooser used. Until r164 this test passed the
// chooser's id there, and so did not catch a handler that refused every real
// pairing request.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { EventEmitter } = require('node:events');

async function desktop(pairingSupported = true) {
  let win, handler;
  const dialogs = [], answers = [], reports = [], ipcMain = new EventEmitter();
  class BrowserWindow extends EventEmitter {
    constructor() {
      super(); win = this;
      this.webContents = new EventEmitter();
      this.webContents.mainFrame = { processId: 7, routingId: 1 };
      this.webContents.send = (channel, report) => { if (channel === 'ember:bluetooth-pairing') reports.push(report); };
      this.webContents.setWindowOpenHandler = () => {};
      this.webContents.session = {
        setPermissionRequestHandler() {}, setPermissionCheckHandler() {}
      };
      if (pairingSupported) this.webContents.session.setBluetoothPairingHandler = h => { handler = h; };
    }
    isDestroyed() { return !!this.destroyed; }
    loadURL() {}
    static getAllWindows() { return [win]; }
  }
  const electron = {
    app: Object.assign(new EventEmitter(), { whenReady: () => Promise.resolve(), quit() {} }),
    BrowserWindow, ipcMain,
    protocol: { registerSchemesAsPrivileged() {}, handle() {} }, net: {}, shell: {},
    dialog: { showMessageBox: (_win, options) => { dialogs.push(options); return answers.shift() || Promise.resolve({ response: 1 }); } }
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../app/main.js'), 'utf8'), {
    require: name => name === 'electron' ? electron : require(name),
    __dirname: path.join(__dirname, '../app'), process: { env: {}, platform: 'win32' },
    URL, Response, console
  });
  await Promise.resolve();
  const select = () => {
    let selected;
    win.webContents.emit('select-bluetooth-device', { preventDefault() {} },
      [{ deviceId: 'AA:BB:CC:DD:EE:FF', deviceName: 'Peak Pro' }], id => { selected = id; });
    ipcMain.emit('ember:bluetooth-select', {}, 'AA:BB:CC:DD:EE:FF');
    assert.equal(selected, 'AA:BB:CC:DD:EE:FF');
  };
  const pair = (overrides = {}) => {
    assert.equal(typeof handler, 'function', 'desktop must register its pairing handler');
    const responses = [];
    const pending = handler({ deviceId: '\u2068Peak Pro\u2069', frame: win.webContents.mainFrame, pairingKind: 'confirm', ...overrides },
      response => responses.push({ ...response }));
    return { responses, pending };
  };
  return { get win() { return win; }, get handler() { return handler; }, dialogs, answers, reports, select, pair };
}

(async () => {
  const app = await desktop();
  let request = app.pair(); await request.pending;
  assert.deepEqual(request.responses, [{ confirmed: false }], 'no selection cannot pair');
  app.select();
  app.answers.push(Promise.resolve({ response: 0 }));
  request = app.pair(); await request.pending;
  assert.deepEqual(request.responses, [{ confirmed: true }], 'Pair accepts a request that names the device, as Chromium sends it');
  assert.ok(app.dialogs.at(-1).message.includes('Peak Pro'), 'the dialog names the device');
  assert.equal(app.reports[0].result, 'refused'); assert.equal(app.reports[0].reason, 'no device chosen');
  assert.ok(!/[\u2066-\u2069]/.test(app.dialogs.at(-1).message), 'isolation marks are stripped from the name');
  assert.deepEqual(app.reports.slice(-2).map(r => r.result), ['asked', 'confirmed'], 'the panel hears the question and the answer');
  app.answers.push(Promise.resolve({ response: 0 }));
  request = app.pair({ frame: { processId: 7, routingId: 1 } }); await request.pending;
  assert.deepEqual(request.responses, [{ confirmed: true }], 'the same frame as another wrapper object is still this window');
  assert.equal(app.dialogs.at(-1).cancelId, 1);
  assert.equal(app.dialogs.at(-1).defaultId, 1);
  request = app.pair(); await request.pending;
  assert.deepEqual(request.responses, [{ confirmed: false }], 'Cancel rejects pairing');
  app.answers.push(Promise.resolve({ response: 0 }));
  request = app.pair({ pairingKind: 'confirmPin', pin: '001234' }); await request.pending;
  assert.deepEqual(request.responses, [{ confirmed: true }]);
  assert.ok(app.dialogs.at(-1).message.includes('001234'), 'PIN prompt preserves leading zeroes');
  for (const details of [{ frame: null }, { frame: {} }, { frame: { processId: 8, routingId: 1 } },
    { pairingKind: 'unknown' }, { pairingKind: 'confirmPin' }]) {
    const before = app.dialogs.length;
    request = app.pair(details); await request.pending;
    assert.deepEqual(request.responses, [{ confirmed: false }]);
    assert.equal(app.dialogs.length, before);
  }
  request = app.pair({ pairingKind: 'providePin' }); await request.pending;
  assert.deepEqual(request.responses, [{ confirmed: false }], 'PIN-entry request settles instead of hanging');
  assert.ok(app.dialogs.at(-1).message.includes('system Bluetooth settings'));
  app.answers.push(Promise.reject(new Error('dialog failed')));
  request = app.pair(); await request.pending;
  assert.deepEqual(request.responses, [{ confirmed: false }], 'dialog failure settles pairing');
  let finishOld;
  app.answers.push(new Promise(resolve => { finishOld = resolve; }));
  const old = app.pair();
  let finishNew;
  app.answers.push(new Promise(resolve => { finishNew = resolve; }));
  const next = app.pair();
  assert.deepEqual(old.responses, [{ confirmed: false }], 'superseded request is cancelled');
  finishOld({ response: 0 }); await old.pending;
  assert.deepEqual(next.responses, [], 'old prompt cannot accept a newer request');
  finishNew({ response: 1 }); await next.pending;
  assert.deepEqual(next.responses, [{ confirmed: false }]);
  let finishClosed;
  app.answers.push(new Promise(resolve => { finishClosed = resolve; }));
  request = app.pair();
  app.win.destroyed = true; app.win.emit('closed');
  assert.deepEqual(request.responses, [{ confirmed: false }], 'window close cancels pairing');
  finishClosed({ response: 0 }); await request.pending;
  assert.equal(request.responses.length, 1, 'each callback receives exactly one answer');
  assert.equal((await desktop(false)).handler, undefined, 'platform without this API still boots');
  console.log('Bluetooth pairing checks passed: confirmation, PIN display, cancel, failure, frame/device scope, races, close, unsupported platform. No device writes.');
})().catch(error => { console.error(error); process.exitCode = 1; });
