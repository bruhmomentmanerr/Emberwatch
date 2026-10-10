// Renders the game's makeTex environment textures headlessly, using the real
// code extracted from app/renderer/index.html, so texture work can be seen
// without the Electron harness. Usage: node tools/tex-preview.js [outdir]
// Writes one PNG per texture in TX (256px).
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const outDir = process.argv[2] || path.join(__dirname, '..', 'workspace', 'tex-preview');
fs.mkdirSync(outDir, { recursive: true });

const html = fs.readFileSync(path.join(__dirname, '..', 'app', 'renderer', 'index.html'), 'utf8');

// ---- minimal 2d canvas -------------------------------------------------
function parseRgb(s) {
  const m = /rgb\((\d+),(\d+),(\d+)\)/.exec(s);
  return m ? [ +m[1], +m[2], +m[3] ] : [0, 0, 0];
}
function makeCanvas(w, h) {
  const buf = Buffer.alloc(w * h * 4, 255);
  const ctx = {
    imageSmoothingEnabled: false,
    _fill: [0, 0, 0],
    set fillStyle(v) { this._fill = parseRgb(v); },
    get fillStyle() { return ''; },
    fillRect(x, y, w2, h2) {
      const [r, g, b] = this._fill;
      const x0 = Math.max(0, Math.floor(x)), y0 = Math.max(0, Math.floor(y));
      const x1 = Math.min(w, Math.ceil(x + w2)), y1 = Math.min(h, Math.ceil(y + h2));
      for (let yy = y0; yy < y1; yy++)
        for (let xx = x0; xx < x1; xx++) {
          const o = (yy * w + xx) * 4;
          buf[o] = r; buf[o + 1] = g; buf[o + 2] = b; buf[o + 3] = 255;
        }
    },
    getImageData(sx, sy, w2, h2) {
      const data = new Uint8ClampedArray(w2 * h2 * 4);
      for (let yy = 0; yy < h2; yy++)
        for (let xx = 0; xx < w2; xx++) {
          const so = ((sy + yy) * w + (sx + xx)) * 4, o = (yy * w2 + xx) * 4;
          data[o] = buf[so]; data[o + 1] = buf[so + 1]; data[o + 2] = buf[so + 2]; data[o + 3] = 255;
        }
      return { width: w2, height: h2, data };
    },
    putImageData(img, dx, dy) {
      const { width: w2, height: h2, data } = img;
      for (let yy = 0; yy < h2; yy++)
        for (let xx = 0; xx < w2; xx++) {
          const o = (yy * w2 + xx) * 4, so = ((dy + yy) * w + (dx + xx)) * 4;
          buf[so] = data[o]; buf[so + 1] = data[o + 1]; buf[so + 2] = data[o + 2];
        }
    },
  };
  return { width: w, height: h, _buf: buf, getContext: () => ctx };
}
function writePng(canvas, file) {
  const { width: w, height: h, _buf } = canvas;
  const raw = Buffer.alloc((w * 3 + 1) * h);
  for (let y = 0; y < h; y++) {
    raw[y * (w * 3 + 1)] = 0;
    for (let x = 0; x < w; x++) {
      const si = (y * w + x) * 4, di = y * (w * 3 + 1) + 1 + x * 3;
      raw[di] = _buf[si]; raw[di + 1] = _buf[si + 1]; raw[di + 2] = _buf[si + 2];
    }
  }
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(w, 0); ihdr.writeUInt32BE(h, 4);
  ihdr[8] = 8; ihdr[9] = 2;
  const chunk = (type, data) => {
    const len = Buffer.alloc(4); len.writeUInt32BE(data.length, 0);
    const td = Buffer.concat([Buffer.from(type), data]);
    const crc = Buffer.alloc(4); crc.writeUInt32BE(zlib.crc32 ? zlib.crc32(td) : crc32(td), 0);
    return Buffer.concat([len, td, crc]);
  };
  const sig = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
  fs.writeFileSync(file, Buffer.concat([sig, chunk('IHDR', ihdr), chunk('IDAT', zlib.deflateSync(raw)), chunk('IEND', Buffer.alloc(0))]));
}
// node < 20 lacks zlib.crc32; tiny fallback
function crc32(buf) {
  let t = crc32.t;
  if (!t) {
    t = crc32.t = new Int32Array(256);
    for (let n = 0; n < 256; n++) {
      let c = n;
      for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
      t[n] = c;
    }
  }
  let c = 0xffffffff;
  for (let i = 0; i < buf.length; i++) c = t[(c ^ buf[i]) & 255] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}

// ---- shims for the extracted game code ---------------------------------
let worldRngState = 0x5eeda11;
function worldRandom() { let v = worldRngState += 0x6D2B79F5; v = Math.imul(v ^ v >>> 15, v | 1); v ^= v + Math.imul(v ^ v >>> 7, v | 61); return ((v ^ v >>> 14) >>> 0) / 4294967296; }
const rand = (a, b) => a + worldRandom() * (b - a);
function shade(hex, d) { const c = v => Math.max(0, Math.min(255, v | 0)); return 'rgb(' + c((hex >> 16 & 255) + d) + ',' + c((hex >> 8 & 255) + d) + ',' + c((hex & 255) + d) + ')'; }
const document = { createElement: () => { throw new Error('use makeCanvas'); } };
const THREE = {
  CanvasTexture: class { constructor(cvs) { this.image = cvs; this.repeat = { set() {} }; } },
  NearestFilter: 1, LinearFilter: 2, LinearMipmapLinearFilter: 3,
  RepeatWrapping: 4, SRGBColorSpace: 5,
};
const renderer = { capabilities: { getMaxAnisotropy: () => 8 } };
const CONFIG = { mapSize: 512 };

// makeTex references document.createElement('canvas'); route it to makeCanvas
const docProxy = { createElement: (tag) => { if (tag === 'canvas') { const c = makeCanvas(1, 1); return { get width() { return c.width; }, set width(v) { const n = makeCanvas(v, c.height); c.width = v; c._buf = n._buf; }, get height() { return c.height; }, set height(v) { const n = makeCanvas(c.width, v); c.height = v; c._buf = n._buf; }, getContext: () => c.getContext(), _c: c }; } throw new Error('bad tag ' + tag); } };

// extract makeTex verbatim
const startMark = 'function makeTex(base,opt={})';
const endMark = "t.colorSpace=THREE.SRGBColorSpace;if(opt.repeat)t.repeat.set(opt.repeat[0],opt.repeat[1]);return t;}";
const si = html.indexOf(startMark), ei = html.indexOf(endMark);
if (si < 0 || ei < 0) { console.error('makeTex not found'); process.exit(1); }
const src = html.slice(si, ei + endMark.length);

// grimeTex verbatim (defined just after makeTex in the game)
const gStart = html.indexOf('function grimeTex(');
const gEndMark = 'x.putImageData(img,0,0);\n}';
const gEnd = html.indexOf(gEndMark, gStart);
if (gStart < 0 || gEnd < 0) { console.error('grimeTex not found'); process.exit(1); }
const grimeSrc = html.slice(gStart, gEnd + gEndMark.length);

// TX literal: copy the game's list verbatim so the preview tracks it
const txStart = html.indexOf('const TX={', si);
let depth = 0, txEnd = -1;
for (let i = txStart; i < html.length; i++) {
  if (html[i] === '{') depth++;
  else if (html[i] === '}') { depth--; if (depth === 0) { txEnd = i; break; } }
}
const txSrc = html.slice(txStart, txEnd + 1);

// npcHash/npcNoise are used by the grime pass; copied verbatim from the game
function npcHash(x, y, s) { let h = (Math.imul(x | 0, 374761393) + Math.imul(y | 0, 668265263) + Math.imul(s | 0, 1442695041)) | 0; h = Math.imul(h ^ (h >>> 13), 1274126177); return ((h ^ (h >>> 16)) >>> 0) / 4294967296; }
function npcNoise(u, v, f, s) {
  const x = u * f, y = v * f, x0 = Math.floor(x), y0 = Math.floor(y), fx = x - x0, fy = y - y0, sx = fx * fx * (3 - 2 * fx), sy = fy * fy * (3 - 2 * fy), m = k => ((k % f) + f) % f;
  const a = npcHash(m(x0), m(y0), s), b = npcHash(m(x0 + 1), m(y0), s), c = npcHash(m(x0), m(y0 + 1), s), d = npcHash(m(x0 + 1), m(y0 + 1), s);
  return a + (b - a) * sx + (c - a) * sy + (a - b - c + d) * sx * sy;
}
const runner = new Function('document', 'THREE', 'renderer', 'CONFIG', 'worldRandom', 'rand', 'shade', 'npcHash', 'npcNoise', 'makeCanvas',
  src + '\n' + grimeSrc + '\n' + txSrc + '\n' + `
  const out = {};
  for (const [k, v] of Object.entries(TX)) out[k] = v.image._c ? v.image._c : v.image;
  return out;`);

// The TX literal uses size 128 default; render bigger for inspection by
// re-running makeTex per entry is complex, so instead render at 128 and
// upscale 2x with nearest for viewing.
const docShim = { createElement: (tag) => {
  if (tag !== 'canvas') throw new Error('bad tag');
  let c = makeCanvas(1, 1);
  return {
    get width() { return c.width; }, set width(v) { c = makeCanvas(v, c.height); },
    get height() { return c.height; }, set height(v) { c = makeCanvas(c.width, v); },
    getContext: () => c.getContext(),
    get _c() { return c; },
  };
} };
const textures = runner(docShim, THREE, renderer, CONFIG, worldRandom, rand, shade, npcHash, npcNoise, makeCanvas);
for (const [name, cvs] of Object.entries(textures)) {
  // upscale 2x nearest for easier inspection
  const big = makeCanvas(cvs.width * 2, cvs.height * 2);
  const s = cvs._buf, d = big._buf;
  for (let y = 0; y < big.height; y++)
    for (let x = 0; x < big.width; x++) {
      const so = (((y >> 1) * cvs.width + (x >> 1)) * 4), o = (y * big.width + x) * 4;
      d[o] = s[so]; d[o + 1] = s[so + 1]; d[o + 2] = s[so + 2]; d[o + 3] = 255;
    }
  writePng(big, path.join(outDir, name + '.png'));
  console.log('wrote', name + '.png');
}
