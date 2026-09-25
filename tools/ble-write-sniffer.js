// ===========================================================================
//  Web Bluetooth write sniffer
//
//  Paste this into the DevTools console on https://drdabber.app BEFORE you
//  press connect, then use the app normally. Every write the app makes to the
//  device is logged with its bytes, and every notification that comes back is
//  logged next to it, so a command and the device's answer sit together.
//
//  This is how the command encoding gets read. Emberwatch can decode what the
//  Switch 2 *says* because it can listen to it; it cannot write to the device
//  because nothing has ever observed what the vendor app sends. The app itself
//  is the only thing that knows, and it is ordinary JavaScript calling
//  navigator.bluetooth in a browser tab, so wrapping the two write methods
//  catches every command it issues.
//
//  Nothing is modified or blocked. Each call is logged and forwarded unchanged.
//
//  When you are done:  copy(BLESNIFF.report())  and send the text.
// ===========================================================================
(() => {
  if (globalThis.BLESNIFF) { console.log('%csniffer already installed', 'color:#c90'); return; }

  const t0 = performance.now();
  const log = [];
  const stamp = () => ((performance.now() - t0) / 1000).toFixed(2).padStart(7) + 's';
  const hex = view => {
    const b = new Uint8Array(view.buffer ? view.buffer.slice(view.byteOffset || 0, (view.byteOffset || 0) + view.byteLength) : view);
    return [...b].map(v => v.toString(16).padStart(2, '0')).join(' ');
  };
  const short = uuid => String(uuid).slice(0, 8);

  function note(kind, uuid, bytes, extra) {
    const row = { t: stamp(), kind, uuid: short(uuid), bytes, extra: extra || '' };
    log.push(row);
    const colour = kind === 'WRITE' ? 'color:#e08a2e;font-weight:600' : 'color:#5aa9e6';
    console.log('%c' + row.t + '  ' + kind.padEnd(6) + ' ' + row.uuid + '  ' + bytes + (extra ? '   ' + extra : ''), colour);
  }

  const proto = BluetoothRemoteGATTCharacteristic.prototype;

  for (const method of ['writeValue', 'writeValueWithResponse', 'writeValueWithoutResponse']) {
    const original = proto[method];
    if (typeof original !== 'function') continue;
    proto[method] = function (value) {
      try { note('WRITE', this.uuid, hex(value), '(' + method + ')'); } catch (e) { console.warn('sniff failed', e); }
      return original.call(this, value);
    };
  }

  // Notifications: wrap startNotifications so every characteristic the app
  // subscribes to is also reported here, in the same timeline as the writes.
  const startOriginal = proto.startNotifications;
  proto.startNotifications = async function () {
    const result = await startOriginal.call(this);
    this.addEventListener('characteristicvaluechanged', event => {
      try { note('notify', event.target.uuid, hex(event.target.value)); } catch (e) { }
    });
    note('sub', this.uuid, '(subscribed)');
    return result;
  };

  // readValue too — the app reads device information and possibly state.
  const readOriginal = proto.readValue;
  proto.readValue = async function () {
    const view = await readOriginal.call(this);
    try { note('read', this.uuid, hex(view)); } catch (e) { }
    return view;
  };

  globalThis.BLESNIFF = {
    log,
    // Only the writes, deduplicated, which is usually what you actually want to
    // read: the notification stream is two frames a second of mostly the same
    // twenty bytes and it buries them.
    writes: () => log.filter(r => r.kind === 'WRITE'),
    mark(label) { note('MARK', '--------', '', label); },
    report() {
      const lines = ['Dr. Dabber write capture — ' + new Date().toISOString(), ''];
      for (const r of log) lines.push(r.t + '  ' + r.kind.padEnd(6) + ' ' + r.uuid + '  ' + r.bytes + (r.extra ? '   ' + r.extra : ''));
      return lines.join('\n');
    },
    writesOnly() {
      const lines = ['Dr. Dabber writes only — ' + new Date().toISOString(), ''];
      for (const r of log) if (r.kind === 'WRITE' || r.kind === 'MARK') lines.push(r.t + '  ' + r.kind.padEnd(6) + ' ' + r.uuid + '  ' + r.bytes + (r.extra ? '   ' + r.extra : ''));
      return lines.join('\n');
    }
  };

  console.log('%cBLE write sniffer installed. Connect the device now.', 'color:#4caf50;font-weight:600');
  console.log('%cBLESNIFF.mark("pressed preset 2")  labels the next thing you do.', 'color:#888');
  console.log('%ccopy(BLESNIFF.writesOnly())  when you are finished.', 'color:#888');
})();
