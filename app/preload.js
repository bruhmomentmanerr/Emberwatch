'use strict';
const { contextBridge, ipcRenderer } = require('electron');

// The only bridge across the isolation boundary. The renderer gets no Node
// access at all — just the three calls the Bluetooth chooser needs.
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
  }
});
