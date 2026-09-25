# Dr. Dabber BLE — what the official web app actually uses

Extracted 2026-09-01 from the Dr. Dabber web app bundle at
`https://drdabber.app/_expo/static/js/web/AppEntry-<hash>.js` (an Expo /
React-Native-Web build, ~4.5 MB). The app drives the device with **Web
Bluetooth** — `navigator.bluetooth`, `requestDevice`, `getPrimaryService`,
`startNotifications`, `writeValue` — which is why the whole map is legible
client-side rather than needing packet captures.

This is the same situation that made the Puffco panel possible. It is *not*
guesswork: every UUID below is copied verbatim out of the app's own
`BluetoothConfig` object.

## How the app scans

```js
const filters = deviceType === 'Switch2'
  ? [{ services: ['0000fee7-0000-1000-8000-00805f9b34fb'] }]
  : [{ services: ['000055e4-0000-1000-8000-00805f9b34fb'] }];
navigator.bluetooth.requestDevice({ filters, optionalServices: [...] })
```

So a **Switch 2 advertises `0000fee7`**. The other branch (`000055e4`) is the
non-Switch2 device type. Note the app filters on the *demo* service, then talks
over the primary service once connected.

## Switch2 config

    demoService              0000fee7-0000-1000-8000-00805f9b34fb   <- advertised
    demoReadCharacteristic   0000fec2-0000-1000-8000-00805f9b34fb
    demoWriteCharacteristic  0000fec1-0000-1000-8000-00805f9b34fb

    primaryService           f56598fa-3ffa-41a7-9726-3fc69baeca1d   <- control
    readCharacteristic       744c98ff-83c6-45d5-bd0c-52a50589215b
    writeCharacteristic      2c759c29-a73c-45ab-a799-31d6a032f6af

    otaService               e5c7a653-7e52-4b06-af32-960455084ae3
    otaReadCharacteristic    739cb17a-1aec-4232-a01a-a250d4c35f0d
    otaWriteCharacteristic   4cbbd40d-f1fa-4dbd-9bb5-36ec99d99a08

## SwitchGo config

Plain Microchip/ISSC transparent UART — a serial bridge over BLE, not a custom
GATT layout. Primary and demo are the same service here.

    primaryService           55535343-fe7d-4ae5-8fa9-9fafd205e455
    readCharacteristic       49535343-1e4d-4bd9-ba61-23c647249616
    writeCharacteristic      49535343-8841-43f4-a8d4-ecbe34729bb3

    otaService               5833ff01-9b8b-5191-6142-22a4536ef123
    otaReadCharacteristic    5833ff03-9b8b-5191-6142-22a4536ef123
    otaWriteCharacteristic   5833ff02-9b8b-5191-6142-22a4536ef123

## Shared by both (standard SIG services)

    deviceInfoService              0000180a-0000-1000-8000-00805f9b34fb
      nameCharacteristic           00002a00-...
      modelCharacteristic          00002a24-...
      serialCharacteristic         00002a25-...
      hardwareRevisionCharacteristic 00002a27-...
      softwareRevisionCharacteristic 00002a28-...
      manufacturerCharacteristic   00002a29-...
    batteryService                 0000180f-0000-1000-8000-00805f9b34fb
      batteryLevelCharacteristic   00002a19-...

## What this means for Emberwatch

The hard question — "does the device expose a controllable BLE interface at
all" — is answered: **yes**. Control is a single write characteristic and a
single read/notify characteristic on `f56598fa`. There is no Puffco-style
hardcoded auth key anywhere in the bundle, so the Lorax challenge-response
handshake has no equivalent here.

> **Superseded in part.** A real Switch 2 was captured on 2026-09-06 and the
> notification frame is decoded in `dr-dabber-switch2-frames.md`. The section
> below was written before that and is kept for the reasoning; where the two
> disagree, the capture wins.

## What is still unknown

- **The packet format.** The UUIDs say *where* to write; they do not say
  *what*. The app writes with `writeValueWithoutResponse` and there is a
  `bluetoothDeviceAuthenticatedAtom` plus an `initialPacketStackReceivedAtom`,
  which together suggest a handshake or a startup packet exchange before the
  device accepts commands. That sequence has not been read out yet.
- Atoms named `tempSettingPreset0Atom`, `tempSettingPreset1Atom`, … exist, so
  temperature presets are part of the protocol surface.
- Nothing here has been tested against real hardware. These are the app's
  declared constants, not observed traffic.

## Next step

Point the r76+ device probe at a Switch 2. The probe now ships every UUID above
in its default request list, so the device should enumerate without anything
being pasted in by hand. Compare what comes back against this table; then the
remaining work is reading the command encoder out of the same bundle.
