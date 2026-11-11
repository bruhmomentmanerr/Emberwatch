// Drive the shipped Peak client with simulated GATT, never a real radio.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { webcrypto } = require('node:crypto');
const source = fs.readFileSync(path.join(__dirname, '../app/renderer/index.html'), 'utf8');
const start = source.indexOf('const PUFF=(function(){');
const end = source.indexOf('\n})();', start);
assert.ok(start >= 0 && end > start);
const uuids = {
  service: 'e276967f-ea8a-478a-a92e-d78f5dd15dd5', version: '05434bca-cc7f-4ef6-bbb3-b1c520b9800c',
  command: '60133d5c-5727-4f2c-9697-d842c5292a3c', reply: '8dc5ec05-8f7d-45ad-99db-3fbde65dbd9c',
  pup: '420b9b40-457d-4abe-a3bf-71609d79581b', pupVersion: '58b0a7aa-d89f-4bf2-961d-0d892d7439d8'
};
function simulated(mode) {
  const commands = [], requests = [], listeners = new Map();
  let bonded = false;
  const reply = { uuid: uuids.reply, startNotifications: async () => {},
    addEventListener: (_event, callback) => listeners.set('reply', callback) };
  const command = { uuid: uuids.command, properties: { writeWithoutResponse: true },
    writeValueWithoutResponse: async packet => {
      commands.push(packet[2]);
      assert.ok(bonded, 'bond read precedes commands');
      if (mode === 'hung-write') return new Promise(() => {});
      if (mode === 'silent') return;
      if (mode === 'write-error') throw new Error('GATT write failed');
      const payload = packet[2] === 0 ? new Uint8Array(16).fill(7) : new Uint8Array();
      const response = Uint8Array.from([packet[0], packet[1], 0, ...payload]);
      listeners.get('reply')({ target: { value: new DataView(response.buffer) } });
      if (mode === 'reply-before-write') return new Promise(() => {});
    }
  };
  if (mode === 'with-response') {
    command.properties = { write: true, writeWithoutResponse: false };
    command.writeValueWithResponse = command.writeValueWithoutResponse;
    command.writeValueWithoutResponse = async () => { throw new Error('Unsupported write without response'); };
  }
  const services = [
    { uuid: uuids.service, getCharacteristics: async () => [
      { uuid: uuids.version, readValue: async () => new DataView(new Uint8Array([0, 0]).buffer) }, command, reply
    ] },
    { uuid: uuids.pup, getCharacteristics: async () => [
      { uuid: uuids.pupVersion, readValue: async () => { bonded = true; return new DataView(new ArrayBuffer(1)); } }
    ] }
  ];
  const device = { name: 'Simulated Plasma', addEventListener() {},
    gatt: { connected: false, connect: async () => { device.gatt.connected = true; return { getPrimaryServices: async () => services }; },
      disconnect: () => { device.gatt.connected = false; } } };
  const client = vm.runInNewContext(source.slice(start, end + 6) + '\nPUFF;', {
    window: { isSecureContext: true }, document: { getElementById: () => ({ checked: false }) },
    navigator: { bluetooth: { requestDevice: async options => { requests.push(options); return device; } } },
    performance, crypto: webcrypto, TextEncoder, TextDecoder, Uint8Array, DataView, atob,
    setTimeout: (callback, ms) => setTimeout(callback, Math.min(ms, 25)), clearTimeout
  });
  return { client, commands, requests, device };
}
(async () => {
  const unhandled = [];
  const onUnhandled = error => unhandled.push(error);
  process.on('unhandledRejection', onUnhandled);
  try {
    for (const mode of ['success', 'silent', 'hung-write', 'reply-before-write', 'write-error', 'with-response']) {
      const sim = simulated(mode);
      let deadline;
      const outcome = await Promise.race([
        sim.client.connect().then(value => ({ value }), error => ({ error })),
        new Promise(resolve => { deadline = setTimeout(() => resolve({ hung: true }), 350); })
      ]);
      clearTimeout(deadline);
      assert.equal(outcome.hung, undefined, mode + ': connection must settle even if a GATT write never does');
      if (mode === 'success' || mode === 'reply-before-write' || mode === 'with-response') {
        assert.equal(outcome.value?.protocol, 'Lorax');
        assert.deepEqual(sim.commands, [2, 0, 1, 16], 'limits, seed, unlock, firmware read; no heating commands');
      } else {
        assert.match(outcome.error.message, mode === 'write-error' ? /GATT write failed/ : /did not answer the limits request/);
        assert.equal(sim.device.gatt.connected, false, 'failed setup releases the connection');
        assert.deepEqual(sim.commands, mode === 'write-error' ? [2, 0, 0] : [2], 'setup command sequence stays bounded');
      }
      console.log('ok Lorax ' + mode);
    }
    await new Promise(resolve => setTimeout(resolve, 30));
    assert.equal(unhandled.length, 0, 'timeouts must not create unhandled rejections');
  } finally { process.removeListener('unhandledRejection', onUnhandled); }
})().catch(error => { console.error(error); process.exitCode = 1; });
