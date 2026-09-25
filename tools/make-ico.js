// A real multi-size .ico. electron-builder will happily convert a PNG for the
// executable, but makensis will not: it rejects a PNG handed to MUI_ICON with
// "invalid icon file", which is what broke the installer build. So the icon is
// written as classic DIB entries, which every Windows consumer accepts.
const fs = require('fs');
const { execFileSync } = require('child_process');
const zlib = require('zlib');

const SRC = process.argv[2];
const OUT = process.argv[3];
const SIZES = [16, 24, 32, 48, 64, 128, 256];

// --- read back the PNG we generated (no filters other than 0, RGBA8) --------
const png = fs.readFileSync(SRC);
let p = 8, W = 0, H = 0, idat = [];
while (p < png.length) {
  const len = png.readUInt32BE(p), type = png.toString('ascii', p + 4, p + 8);
  const data = png.slice(p + 8, p + 8 + len);
  if (type === 'IHDR') { W = data.readUInt32BE(0); H = data.readUInt32BE(4); }
  if (type === 'IDAT') idat.push(data);
  p += 12 + len;
}
const raw = zlib.inflateSync(Buffer.concat(idat));
const src = Buffer.alloc(W * H * 4);
for (let y = 0; y < H; y++) {
  const off = y * (W * 4 + 1);
  if (raw[off] !== 0) throw new Error('unexpected PNG filter ' + raw[off]);
  raw.copy(src, y * W * 4, off + 1, off + 1 + W * 4);
}

// --- box-filter downscale, so the small sizes do not alias to mush ----------
function resize(size) {
  const out = Buffer.alloc(size * size * 4);
  const step = W / size;
  for (let y = 0; y < size; y++) {
    for (let x = 0; x < size; x++) {
      let r = 0, g = 0, b = 0, a = 0, n = 0;
      const x0 = Math.floor(x * step), x1 = Math.max(x0 + 1, Math.floor((x + 1) * step));
      const y0 = Math.floor(y * step), y1 = Math.max(y0 + 1, Math.floor((y + 1) * step));
      for (let sy = y0; sy < y1 && sy < H; sy++)
        for (let sx = x0; sx < x1 && sx < W; sx++) {
          const i = (sy * W + sx) * 4, sa = src[i + 3] / 255;
          r += src[i] * sa; g += src[i + 1] * sa; b += src[i + 2] * sa; a += src[i + 3]; n++;
        }
      if (!n) continue;
      // r/g/b were accumulated premultiplied by alpha, so the mean colour is
      // (r/n) and the mean alpha is (a/n); un-premultiplying gives r*255/a.
      // This had an extra factor of n in it, which is at least 4x on every size
      // and saturated the whole icon to white — the app icon was a white circle.
      const aa = a / n, k = a > 0 ? 255 / a : 0;
      const o = (y * size + x) * 4;
      out[o] = Math.min(255, Math.round(r * k)); out[o + 1] = Math.min(255, Math.round(g * k));
      out[o + 2] = Math.min(255, Math.round(b * k)); out[o + 3] = Math.round(aa);
    }
  }
  return out;
}

// --- one DIB image, bottom-up BGRA plus the legacy AND mask -----------------
function dib(size, rgba) {
  const header = Buffer.alloc(40);
  header.writeUInt32LE(40, 0);
  header.writeInt32LE(size, 4);
  header.writeInt32LE(size * 2, 8);          // height counts colour + mask
  header.writeUInt16LE(1, 12);
  header.writeUInt16LE(32, 14);
  header.writeUInt32LE(0, 16);
  header.writeUInt32LE(size * size * 4, 20);
  const body = Buffer.alloc(size * size * 4);
  for (let y = 0; y < size; y++)
    for (let x = 0; x < size; x++) {
      const s = ((size - 1 - y) * size + x) * 4, d = (y * size + x) * 4;
      body[d] = rgba[s + 2]; body[d + 1] = rgba[s + 1]; body[d + 2] = rgba[s]; body[d + 3] = rgba[s + 3];
    }
  const maskRow = Math.ceil(size / 32) * 4;
  const mask = Buffer.alloc(maskRow * size);  // all zero: nothing masked out
  return Buffer.concat([header, body, mask]);
}

const images = SIZES.map(s => ({ size: s, buf: dib(s, resize(s)) }));
const dir = Buffer.alloc(6 + 16 * images.length);
dir.writeUInt16LE(0, 0); dir.writeUInt16LE(1, 2); dir.writeUInt16LE(images.length, 4);
let offset = dir.length;
images.forEach((img, i) => {
  const e = 6 + i * 16;
  dir[e] = img.size >= 256 ? 0 : img.size;
  dir[e + 1] = img.size >= 256 ? 0 : img.size;
  dir[e + 2] = 0; dir[e + 3] = 0;
  dir.writeUInt16LE(1, e + 4); dir.writeUInt16LE(32, e + 6);
  dir.writeUInt32LE(img.buf.length, e + 8);
  dir.writeUInt32LE(offset, e + 12);
  offset += img.buf.length;
});
fs.writeFileSync(OUT, Buffer.concat([dir, ...images.map(i => i.buf)]));
console.log('wrote ' + OUT + '  sizes ' + SIZES.join(',') + '  ' + fs.statSync(OUT).size + ' bytes');
