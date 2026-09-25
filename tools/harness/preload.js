// Edge on file:// is not a secure context, so these simply do not exist there.
// Electron's file:// is treated as secure, which is why the app looked fine.
// Removing them here means a probe can never reach a real Bluetooth device.
try { delete navigator.bluetooth; } catch (e) {}
try { Object.defineProperty(navigator, 'bluetooth', { get: () => undefined, configurable: true }); } catch (e) {}
try { Object.defineProperty(window, 'crypto', { value: Object.assign(Object.create(Object.getPrototypeOf(window.crypto)), { subtle: undefined, getRandomValues: window.crypto.getRandomValues.bind(window.crypto) }), configurable: true }); } catch (e) {}
try { Object.defineProperty(navigator, 'clipboard', { get: () => undefined, configurable: true }); } catch (e) {}

// A probe can hand a file back: window.__harnessSave(name, ArrayBuffer|Uint8Array)
// writes it under HARNESS_SAVE_DIR (default the working directory) and returns
// the path. Added for exporting the city as glTF, where the payload is tens of
// megabytes and has no business travelling back as JSON over the IPC channel.
try {
  const fs = require('fs'), path = require('path');
  window.__harnessSave = (name, data) => {
    const dir = process.env.HARNESS_SAVE_DIR || process.cwd();
    const safe = String(name).replace(/[^A-Za-z0-9._-]/g, '_');
    const file = path.join(dir, safe);
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(file, Buffer.from(data instanceof ArrayBuffer ? new Uint8Array(data) : data));
    return { file, bytes: fs.statSync(file).size };
  };
} catch (err) { /* no node here: probes that need it will say so */ }

// A couple of env vars a probe may need to be told rather than guess. Added for
// the video frame extractor (tools/video-frames), which has to be pointed at a
// file outside the project and told how many stills to take.
try {
  window.__HARNESS_VIDEO = process.env.HARNESS_VIDEO || null;
  window.__HARNESS_FRAMES = process.env.HARNESS_FRAMES || null;
  window.__HARNESS_LOOK = process.env.HARNESS_LOOK || null;
} catch (err) { /* same */ }

// Read a local file into the page. The frame extractor needs this because a
// video loaded straight off file:// taints the canvas it is drawn to, and a
// tainted canvas returns null from toBlob — so the bytes come in this way and
// go back out as a same-origin blob: URL instead.
try {
  const fs = require('fs');
  window.__harnessRead = file => new Uint8Array(fs.readFileSync(file));
} catch (err) { /* same */ }
