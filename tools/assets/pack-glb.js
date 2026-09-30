// Shrink a landmark .glb before it is inlined (r143).
//
//   node tools/assets/pack-glb.js assets/<name>.glb [out.glb]
//
// The game is one HTML file, and a modelled landmark exported plainly from
// Blender carries float positions, float normals and 16-bit colour for every
// vertex — the Fallen Hall came out at 223 KB, over inline-glb.js's limit on
// its own. This rewrites it as a smaller but equivalent GLB:
//   - normals dropped: landmarks are flat-shaded, and the game recomputes a
//     face normal per triangle anyway (placeLandmark de-indexes first);
//   - positions quantised to normalised 16-bit integers under
//     KHR_mesh_quantization, with the node's translation and scale restoring
//     them — three.js's GLTFLoader reads this natively, and placeLandmark
//     applies the node transform before merging;
//   - vertex colour as normalised 8-bit RGBA (core glTF);
//   - vertices welded where position and colour agree, indices 16-bit.
// Precision: 16 bits over a 40 m model is 0.6 mm.
const fs = require('fs');
const [src, dst = src] = process.argv.slice(2);
if (!src) { console.error('usage: pack-glb.js <in.glb> [out.glb]'); process.exit(2); }
const buf = fs.readFileSync(src);
if (buf.readUInt32LE(0) !== 0x46546c67) { console.error('not a GLB'); process.exit(1); }
const jsonLen = buf.readUInt32LE(12), json = JSON.parse(buf.toString('utf8', 20, 20 + jsonLen));
const binStart = 20 + jsonLen + 8, bin = buf.subarray(binStart);
if (json.meshes.length !== 1 || json.meshes[0].primitives.length !== 1) { console.error('expected one mesh with one primitive'); process.exit(1); }
const prim = json.meshes[0].primitives[0];
const COMPONENTS = { SCALAR: 1, VEC2: 2, VEC3: 3, VEC4: 4 };
function read(accIndex) {
  const acc = json.accessors[accIndex], view = json.bufferViews[acc.bufferView], n = COMPONENTS[acc.type];
  const base = (view.byteOffset || 0) + (acc.byteOffset || 0), out = new Float64Array(acc.count * n);
  const size = { 5126: 4, 5123: 2, 5125: 4, 5121: 1 }[acc.componentType], stride = view.byteStride || size * n;
  for (let i = 0; i < acc.count; i++) for (let c = 0; c < n; c++) {
    const at = base + i * stride + c * size;
    let v = acc.componentType === 5126 ? bin.readFloatLE(at) : acc.componentType === 5123 ? bin.readUInt16LE(at) : acc.componentType === 5125 ? bin.readUInt32LE(at) : bin.readUInt8(at);
    if (acc.normalized) v /= acc.componentType === 5123 ? 65535 : 255;
    out[i * n + c] = v;
  }
  return { data: out, n, count: acc.count };
}
const pos = read(prim.attributes.POSITION);
const col = prim.attributes.COLOR_0 !== undefined ? read(prim.attributes.COLOR_0) : null;
const idx = read(prim.indices);
// weld
const key = new Map(), remap = new Uint32Array(pos.count), P = [], C = [];
for (let i = 0; i < pos.count; i++) {
  const p = [pos.data[i * 3], pos.data[i * 3 + 1], pos.data[i * 3 + 2]];
  const c = col ? [0, 1, 2, 3].map(k => k < col.n ? Math.round(col.data[i * col.n + k] * 255) : 255) : [255, 255, 255, 255];
  const k = p.map(v => v.toFixed(4)).join(',') + '|' + c.join(',');
  if (!key.has(k)) { key.set(k, P.length / 3); P.push(...p); C.push(...c); }
  remap[i] = key.get(k);
}
const verts = P.length / 3;
if (verts > 65535) { console.error('too many vertices for 16-bit indices: ' + verts); process.exit(1); }
const min = [0, 1, 2].map(c => Math.min(...P.filter((_, i) => i % 3 === c)));
const max = [0, 1, 2].map(c => Math.max(...P.filter((_, i) => i % 3 === c)));
const centre = min.map((m, c) => (m + max[c]) / 2), half = min.map((m, c) => Math.max(1e-6, (max[c] - m) / 2));
// positions: int16 normalised, padded to 8 bytes per vertex for alignment
const posBuf = Buffer.alloc(verts * 8), colBuf = Buffer.alloc(verts * 4), tris = idx.count;
for (let i = 0; i < verts; i++) {
  for (let c = 0; c < 3; c++) posBuf.writeInt16LE(Math.max(-32767, Math.min(32767, Math.round((P[i * 3 + c] - centre[c]) / half[c] * 32767))), i * 8 + c * 2);
  for (let c = 0; c < 4; c++) colBuf.writeUInt8(C[i * 4 + c], i * 4 + c);
}
const idxBuf = Buffer.alloc(Math.ceil(tris * 2 / 4) * 4);
for (let i = 0; i < tris; i++) idxBuf.writeUInt16LE(remap[idx.data[i]], i * 2);
const bodyParts = [posBuf, colBuf, idxBuf], offsets = [];
let off = 0; for (const b of bodyParts) { offsets.push(off); off += b.length; }
const body = Buffer.concat(bodyParts);
const q = {
  asset: { version: '2.0', generator: 'Emberwatch pack-glb (r143) from ' + (json.asset.generator || 'unknown') },
  extensionsUsed: ['KHR_mesh_quantization'], extensionsRequired: ['KHR_mesh_quantization'],
  scene: 0, scenes: [{ nodes: [0] }],
  nodes: [{ mesh: 0, name: json.nodes[0].name, translation: centre, scale: half }],
  meshes: [{ name: json.meshes[0].name, primitives: [{ attributes: { POSITION: 0, COLOR_0: 1 }, indices: 2 }] }],
  accessors: [
    { bufferView: 0, componentType: 5122, normalized: true, count: verts, type: 'VEC3', min: [-32767, -32767, -32767].map((v, c) => Math.round((min[c] - centre[c]) / half[c] * 32767)), max: [0, 1, 2].map(c => Math.round((max[c] - centre[c]) / half[c] * 32767)) },
    { bufferView: 1, componentType: 5121, normalized: true, count: verts, type: 'VEC4' },
    { bufferView: 2, componentType: 5123, count: tris, type: 'SCALAR' }
  ],
  bufferViews: [
    { buffer: 0, byteOffset: offsets[0], byteLength: posBuf.length, byteStride: 8, target: 34962 },
    { buffer: 0, byteOffset: offsets[1], byteLength: colBuf.length, byteStride: 4, target: 34962 },
    { buffer: 0, byteOffset: offsets[2], byteLength: tris * 2, target: 34963 }
  ],
  buffers: [{ byteLength: body.length }]
};
let jsonText = JSON.stringify(q); while (jsonText.length % 4) jsonText += ' ';
const jsonBuf = Buffer.from(jsonText, 'utf8');
const header = Buffer.alloc(12), jh = Buffer.alloc(8), bh = Buffer.alloc(8);
header.writeUInt32LE(0x46546c67, 0); header.writeUInt32LE(2, 4); header.writeUInt32LE(12 + 8 + jsonBuf.length + 8 + body.length, 8);
jh.writeUInt32LE(jsonBuf.length, 0); jh.writeUInt32LE(0x4e4f534a, 4); bh.writeUInt32LE(body.length, 0); bh.writeUInt32LE(0x004e4942, 4);
fs.writeFileSync(dst, Buffer.concat([header, jh, jsonBuf, bh, body]));
console.log('packed ' + src + ': ' + pos.count + ' -> ' + verts + ' vertices, ' + tris / 3 + ' triangles, ' +
  Math.round(buf.length / 1024) + ' KB -> ' + Math.round(fs.statSync(dst).size / 1024) + ' KB; bounds y ' + min[1].toFixed(2) + '..' + max[1].toFixed(2));
