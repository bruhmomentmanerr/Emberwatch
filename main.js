'use strict';
const { app, BrowserWindow, ipcMain, protocol, net, shell } = require('electron');
const path = require('path');
const { pathToFileURL } = require('url');

// A custom scheme rather than file://. It gives the page a real, stable origin
// that counts as a secure context (so Web Bluetooth is allowed) and supports
// fetch/CORS, which file:// does not — the strain archive lookups and any
// future .glb loading both need that.
protocol.registerSchemesAsPrivileged([
  {
    scheme: 'app',
    privileges: { standard: true, secure: true, supportFetchAPI: true, corsEnabled: true, stream: true }
  }
]);

// Bump this whenever renderer/index.html is replaced with a newer revision.
// It shows in the window title and taskbar so a running build is identifiable
// at a glance without opening the Puffco panel to read its header.
const BUILD_REVISION = 'r137';

let mainWindow = null;
// Electron hands us a callback to pick a device with. We hold it while the
// renderer shows its own chooser.
let bluetoothCallback = null;

function resolveBluetooth(deviceId) {
  if (!bluetoothCallback) return;
  const callback = bluetoothCallback;
  bluetoothCallback = null;
  callback(deviceId || '');
}

function createWindow() {
  // EMBERWATCH_WINDOW_X/_Y are for the smoke test only — they let it open off
  // the primary display while it's in use for something else. Unset, the
  // window opens wherever the OS puts it, same as any ordinary player sees.
  const winPos = {};
  if (process.env.EMBERWATCH_WINDOW_X) winPos.x = Number(process.env.EMBERWATCH_WINDOW_X);
  if (process.env.EMBERWATCH_WINDOW_Y) winPos.y = Number(process.env.EMBERWATCH_WINDOW_Y);
  mainWindow = new BrowserWindow({
    ...winPos,
    width: 1440,
    height: 900,
    minWidth: 900,
    minHeight: 600,
    backgroundColor: '#0a0710',
    // Also set at runtime so the taskbar and the window itself carry it, not
    // just the packaged executable.
    icon: path.join(__dirname, 'build', 'icon.ico'),
    autoHideMenuBar: true,
    title: 'Emberwatch — '+BUILD_REVISION,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
      // The Puffco panel keeps polling the Peak while you play; without this
      // Chromium throttles timers and rAF whenever the window loses focus.
      backgroundThrottling: false
    }
  });

  // THE critical piece for Web Bluetooth in Electron. There is no built-in
  // device chooser: if this event is not handled, navigator.bluetooth
  // .requestDevice() simply never settles and the Connect button hangs
  // forever with no error. We forward the list to the renderer, which draws
  // its own picker in the game's own style.
  mainWindow.webContents.on('select-bluetooth-device', (event, deviceList, callback) => {
    event.preventDefault();
    bluetoothCallback = callback;
    mainWindow.webContents.send(
      'ember:bluetooth-devices',
      deviceList.map(device => ({
        deviceId: device.deviceId,
        deviceName: device.deviceName || 'unnamed device'
      }))
    );
  });

  // Grant the permissions the game legitimately needs and refuse the rest.
  // pointerLock is the important one: mouse look calls requestPointerLock(),
  // and in Electron that is a *permission*. Omitting it silently denied the
  // lock, so the camera could not be steered at all — the browser build works
  // only because Chrome grants pointer lock on a user gesture without asking.
  const ALLOWED_PERMISSIONS = new Set([
    'pointerLock',
    'fullscreen',
    'bluetooth',
    'clipboard-sanitized-write'
  ]);
  mainWindow.webContents.session.setPermissionRequestHandler((_wc, permission, done) => {
    done(ALLOWED_PERMISSIONS.has(permission));
  });
  // Some Chromium builds route pointer lock through the *check* handler rather
  // than the async request handler, so both have to agree or the lock is
  // granted once and then revoked on the next frame.
  mainWindow.webContents.session.setPermissionCheckHandler((_wc, permission) =>
    ALLOWED_PERMISSIONS.has(permission)
  );

  // The page carries its own <title>, which Chromium would apply the moment it
  // loads and quietly wipe out the revision marker. Hold our own title instead.
  mainWindow.on('page-title-updated', event => {
    event.preventDefault();
    mainWindow.setTitle('Emberwatch — ' + BUILD_REVISION);
  });

  // Any external link opens in the real browser, never inside the app shell.
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    if (/^https?:/i.test(url)) shell.openExternal(url);
    return { action: 'deny' };
  });

  mainWindow.on('closed', () => {
    resolveBluetooth('');
    mainWindow = null;
  });

  // Headless-ish self check: `set EMBERWATCH_SMOKE=1 && npm start` loads the
  // app, reports whether the page and its WebGL/Bluetooth surfaces came up,
  // then exits. Lets the shell be verified without a human watching a window.
  if (process.env.EMBERWATCH_SMOKE) {
    mainWindow.hide();
    mainWindow.webContents.once('did-finish-load', async () => {
      try {
        const report = await mainWindow.webContents.executeJavaScript(`(() => ({
          title: document.title,
          secureContext: window.isSecureContext,
          hasBluetooth: !!navigator.bluetooth,
          bridge: !!window.emberBluetooth,
          webgl: !!document.createElement('canvas').getContext('webgl'),
          gameBooted: !!window.EMBER,
          bluetoothChooser: window.emberBluetoothChooser || null,
          colliders: window.EMBER ? window.EMBER.colliders.length : 0,
          diagnostics: window.EMBER?.diagnostics?.() || null,
          pointerLockApi: !!document.documentElement.requestPointerLock,
          loaderMessage: (document.getElementById('lmsg') || {}).textContent || ''
        }))()`);
        report.windowTitle = mainWindow.getTitle();
        console.log('SMOKE ' + JSON.stringify(report));
        // `set EMBERWATCH_SMOKE=bluetooth` additionally proves the chooser
        // handshake completes. Until r76 the renderer never answered
        // select-bluetooth-device, so requestDevice() never settled and Connect
        // hung with no error — a failure no amount of staring at the panel
        // reveals. This asserts the promise settles, whatever the answer is.
        // executeJavaScript's second argument supplies the user activation
        // requestDevice() requires.
        if (process.env.EMBERWATCH_SMOKE === 'bluetooth') {
          try {
            const chooser = await mainWindow.webContents.executeJavaScript(`(async () => {
              const overlay = document.getElementById('btChooser');
              const pending = navigator.bluetooth
                .requestDevice({ acceptAllDevices: true, optionalServices: [] })
                .then(d => 'device: ' + (d.name || d.id), e => 'rejected: ' + e.name);
              await new Promise(r => setTimeout(r, 2000));
              const openedWhileScanning = overlay.classList.contains('open');
              document.getElementById('btcCancel').click();
              const settled = await Promise.race([
                pending,
                new Promise(r => setTimeout(() => r('HUNG — never settled'), 4000))
              ]);
              return { openedWhileScanning, settled, closedAfterCancel: !overlay.classList.contains('open') };
            })()`, true);
            console.log('SMOKE-BT ' + JSON.stringify(chooser));
          } catch (error) {
            console.log('SMOKE-BT ' + JSON.stringify({ error: String(error && error.message || error) }));
          }
        }
      } catch (error) {
        console.log('SMOKE ' + JSON.stringify({ error: String(error && error.message || error) }));
      }
      app.exit(0);
    });
    mainWindow.webContents.once('did-fail-load', (_e, code, desc) => {
      console.log('SMOKE ' + JSON.stringify({ failed: true, code, desc }));
      app.exit(1);
    });
  }

  mainWindow.loadURL('app://emberwatch/index.html');
}

ipcMain.on('ember:bluetooth-select', (_event, deviceId) => resolveBluetooth(deviceId));
ipcMain.on('ember:bluetooth-cancel', () => resolveBluetooth(''));

app.whenReady().then(() => {
  protocol.handle('app', request => {
    const { pathname } = new URL(request.url);
    const relative = decodeURIComponent(pathname).replace(/^\/+/, '');
    const target = path.join(__dirname, 'renderer', relative || 'index.html');
    // Refuse anything that escapes the renderer directory.
    const rendererRoot = path.join(__dirname, 'renderer');
    const relativeToRoot = path.relative(rendererRoot, target);
    if (relativeToRoot.startsWith('..') || path.isAbsolute(relativeToRoot)) {
      return new Response('Forbidden', { status: 403 });
    }
    return net.fetch(pathToFileURL(target).toString());
  });

  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
