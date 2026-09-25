// A 512x512 PNG app icon, written with nothing but zlib. Vaneth at night: the
// aurora, the wall, and the ember the whole project is named for.
// electron-builder converts this to .ico via tools/make-ico.js.
//
// Composed for 32px first, not 512. A taskbar icon is read at a glance and at a
// glance the only thing that survives is one bright warm mark against something
// dark — so the ember is large, the gate it sits in is a wide clear notch, and
// the wall is a silhouette rather than masonry. The 512 version is the same
// picture with room to breathe, not a more detailed one.
const fs = require('fs');
const zlib = require('zlib');
const path = require('path');

const S = 512;
const px = Buffer.alloc(S * S * 4);

const clamp = v => Math.max(0, Math.min(255, Math.round(v)));
function set(x, y, r, g, b, a = 255) {
  if (x < 0 || y < 0 || x >= S || y >= S) return;
  const i = (y * S + x) * 4;
  const sa = a / 255, da = px[i + 3] / 255, oa = sa + da * (1 - sa);
  if (oa <= 0) return;
  px[i] = clamp((r * sa + px[i] * da * (1 - sa)) / oa);
  px[i + 1] = clamp((g * sa + px[i + 1] * da * (1 - sa)) / oa);
  px[i + 2] = clamp((b * sa + px[i + 2] * da * (1 - sa)) / oa);
  px[i + 3] = clamp(oa * 255);
}

const R = S / 2, cx = S / 2, cy = S / 2;

// --- sky -------------------------------------------------------------------
for (let y = 0; y < S; y++) {
  for (let x = 0; x < S; x++) {
    const d = Math.hypot(x - cx + 0.5, y - cy + 0.5);
    if (d > R - 1) continue;
    const edge = Math.min(1, (R - d) / 1.5);
    const t = y / S;
    let r = 18 + 10 * (1 - t), g = 14 + 10 * (1 - t), b = 44 + 26 * (1 - t);
    // One broad aurora band, brighter than the game's, so the disc does not go
    // to mud when it is thirty pixels wide.
    const band = Math.exp(-Math.pow((t - 0.28) / 0.15, 2));
    const ripple = 0.6 + 0.4 * Math.sin(x / 52 + Math.sin(x / 130) * 2);
    r += 16 * band * ripple; g += 178 * band * ripple; b += 150 * band * ripple;
    set(x, y, r, g, b, 255 * edge);
  }
}

// --- wall, as one silhouette with a gate cut out of it ---------------------
const wallTop = Math.round(S * 0.56), gateW = Math.round(S * 0.30);
const gateTop = Math.round(S * 0.60), gateArch = gateW * 0.5;
for (let y = wallTop; y < S; y++) {
  for (let x = 0; x < S; x++) {
    if (Math.hypot(x - cx + 0.5, y - cy + 0.5) > R - 2) continue;
    const dx = Math.abs(x - cx);
    // an arched opening: a rectangle below, a half-round on top
    const inGate = dx < gateW / 2 &&
      (y > gateTop + gateArch || Math.hypot(dx, y - (gateTop + gateArch)) < gateArch);
    if (inGate) continue;                          // leave the sky, the ember fills it
    const v = 30 + (Math.floor(y / 26) % 2 ? 5 : 0) + (Math.floor((x + (Math.floor(y / 26) % 2) * 20) / 40) % 2 ? 4 : 0);
    set(x, y, v, v - 3, v + 12, 255);
  }
}
// two merlon blocks either side, just enough to say "wall" and not "floor"
for (const side of [-1, 1]) {
  const tx = cx + side * (gateW / 2 + S * 0.11);
  for (let y = Math.round(S * 0.47); y < wallTop; y++)
    for (let x = Math.round(tx - S * 0.055); x < tx + S * 0.055; x++) {
      if (Math.hypot(x - cx + 0.5, y - cy + 0.5) > R - 2) continue;
      set(x, y, 36, 33, 50, 255);
    }
}

// --- the ember, filling the gate ------------------------------------------
const ex = cx, ey = Math.round(S * 0.755);
for (let y = 0; y < S; y++) {
  for (let x = 0; x < S; x++) {
    const d = Math.hypot(x - ex, y - ey);
    if (d > S * 0.30) continue;
    if (Math.hypot(x - cx + 0.5, y - cy + 0.5) > R - 2) continue;
    const core = Math.max(0, 1 - d / (S * 0.062));
    const glow = Math.exp(-Math.pow(d / (S * 0.115), 2));
    const a = Math.min(1, core * 1.1 + glow * 0.9);
    if (a <= 0.004) continue;
    set(x, y, 255, 168 + 70 * core, 70 + 140 * core, 255 * a);
  }
}

// --- PNG -------------------------------------------------------------------
let table = null;
function crc32(buf) {
  if (!table) {
    table = new Int32Array(256);
    for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; table[n] = c; }
  }
  let c = -1;
  for (let i = 0; i < buf.length; i++) c = table[(c ^ buf[i]) & 0xFF] ^ (c >>> 8);
  return c ^ -1;
}
function chunk(type, data) {
  const len = Buffer.alloc(4); len.writeUInt32BE(data.length);
  const body = Buffer.concat([Buffer.from(type, 'ascii'), data]);
  const crcBuf = Buffer.alloc(4); crcBuf.writeUInt32BE(crc32(body) >>> 0);
  return Buffer.concat([len, body, crcBuf]);
}
const raw = Buffer.alloc((S * 4 + 1) * S);
for (let y = 0; y < S; y++) {
  raw[y * (S * 4 + 1)] = 0;
  px.copy(raw, y * (S * 4 + 1) + 1, y * S * 4, (y + 1) * S * 4);
}
const ihdr = Buffer.alloc(13);
ihdr.writeUInt32BE(S, 0); ihdr.writeUInt32BE(S, 4);
ihdr[8] = 8; ihdr[9] = 6;
const png = Buffer.concat([
  Buffer.from([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
  chunk('IHDR', ihdr),
  chunk('IDAT', zlib.deflateSync(raw, { level: 9 })),
  chunk('IEND', Buffer.alloc(0))
]);
const out = process.argv[2] || 'icon.png';
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, png);
console.log('wrote ' + out + '  ' + S + 'x' + S + '  ' + png.length + ' bytes');
