// How different do two sets of screenshots look?
//
// Built for the Three.js upgrade, where "it looks the same" had to be a number.
// Compares every PNG that exists in both folders and reports, per shot:
//
//   mean    average absolute difference per channel, 0-255, over every pixel
//   blocks  the same over a 32x18 grid of block averages — ignores the small
//           things that move between frames (flames, residents, the aurora)
//           and keeps what a person would call "the look"
//   light   mean luminance of each, so "darker" and "brighter" have a sign
//
// The sky, water and fires animate, so two captures of the same build never
// match exactly. Diff a build against itself first; that is the noise floor.
//
//   node tools/diff-shots.js <dirA> <dirB>
// Needs pngjs from tools/three-vendor (npm install there).

const fs = require('fs');
const path = require('path');
const { PNG } = require(path.join(__dirname, 'three-vendor', 'node_modules', 'pngjs'));

const [dirA, dirB] = process.argv.slice(2);
if (!dirA || !dirB) { console.error('usage: node tools/diff-shots.js <dirA> <dirB>'); process.exit(2); }

const read = f => PNG.sync.read(fs.readFileSync(f));
const lum = (d, i) => .2126 * d[i] + .7152 * d[i + 1] + .0722 * d[i + 2];
const GX = 32, GY = 18;

function blocks(img) {
  const out = new Float64Array(GX * GY * 3), count = new Float64Array(GX * GY);
  for (let y = 0; y < img.height; y++) for (let x = 0; x < img.width; x++) {
    const b = Math.min(GY - 1, Math.floor(y * GY / img.height)) * GX + Math.min(GX - 1, Math.floor(x * GX / img.width));
    const i = (y * img.width + x) * 4;
    out[b * 3] += img.data[i]; out[b * 3 + 1] += img.data[i + 1]; out[b * 3 + 2] += img.data[i + 2]; count[b]++;
  }
  for (let b = 0; b < GX * GY; b++) for (let c = 0; c < 3; c++) out[b * 3 + c] /= count[b] || 1;
  return out;
}

const names = fs.readdirSync(dirA).filter(f => f.endsWith('.png') && fs.existsSync(path.join(dirB, f))).sort();
if (!names.length) { console.error('no PNGs in common'); process.exit(1); }
let totalMean = 0, totalBlocks = 0;
console.log('shot'.padEnd(24) + 'mean'.padStart(7) + 'blocks'.padStart(8) + '   light A → B');
for (const name of names) {
  const a = read(path.join(dirA, name)), b = read(path.join(dirB, name));
  if (a.width !== b.width || a.height !== b.height) { console.log(name.padEnd(24) + '  size differs'); continue; }
  let sum = 0, la = 0, lb = 0;
  for (let i = 0; i < a.data.length; i += 4) {
    sum += Math.abs(a.data[i] - b.data[i]) + Math.abs(a.data[i + 1] - b.data[i + 1]) + Math.abs(a.data[i + 2] - b.data[i + 2]);
    la += lum(a.data, i); lb += lum(b.data, i);
  }
  const px = a.data.length / 4, mean = sum / (px * 3);
  const ba = blocks(a), bb = blocks(b);
  let bsum = 0; for (let i = 0; i < ba.length; i++) bsum += Math.abs(ba[i] - bb[i]);
  const blockMean = bsum / ba.length;
  totalMean += mean; totalBlocks += blockMean;
  console.log(name.replace('.png', '').padEnd(24) + mean.toFixed(2).padStart(7) + blockMean.toFixed(2).padStart(8) +
    '   ' + (la / px).toFixed(1) + ' → ' + (lb / px).toFixed(1));
}
console.log('-'.repeat(52));
console.log('average'.padEnd(24) + (totalMean / names.length).toFixed(2).padStart(7) + (totalBlocks / names.length).toFixed(2).padStart(8));
