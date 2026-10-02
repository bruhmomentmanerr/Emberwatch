'use strict';
const { contextBridge, ipcRenderer } = require('electron');

// The only bridge across the isolation boundary. The renderer gets no Node
// access at all — just the calls the Bluetooth chooser and pairing need.
contextBridge.exposeInMainWorld('emberBluetooth', {
  // Electron re-fires the device event as more devices are discovered, so the
  // renderer should treat each call as a fresh, complete list.
  onDevices(handler) {
    ipcRenderer.on('ember:bluetooth-devices', (_event, devices) => handler(devices));
  },
  select(deviceId) {
    ipcRenderer.send('ember:bluetooth-select', String(deviceId || ''));
  },
  cancel() {
    ipcRenderer.send('ember:bluetooth-cancel');
  },
  // (r164) What became of a pairing request Windows raised for the chosen
  // device: asked, confirmed, cancelled, or refused (with the reason).
  onPairing(handler) {
    ipcRenderer.on('ember:bluetooth-pairing', (_event, report) => handler(report));
  }
});
