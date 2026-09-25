// Feed GLTFLoader a minimal glTF (one triangle, embedded buffer) through the
// game's own loadGLB, and check the model lands in the scene.
(async () => {
  const E = window.EMBER, wait = ms => new Promise(r => setTimeout(r, ms));
  await wait(2500);
  const pos = new Float32Array([0, 0, 0, 4, 0, 0, 0, 4, 0]);
  let bin = ''; new Uint8Array(pos.buffer).forEach(b => bin += String.fromCharCode(b));
  const gltf = { asset: { version: '2.0' }, scene: 0, scenes: [{ nodes: [0] }], nodes: [{ mesh: 0 }],
    meshes: [{ primitives: [{ attributes: { POSITION: 0 } }] }],
    buffers: [{ byteLength: 36, uri: 'data:application/octet-stream;base64,' + btoa(bin) }],
    bufferViews: [{ buffer: 0, byteLength: 36 }],
    accessors: [{ bufferView: 0, componentType: 5126, count: 3, type: 'VEC3', min: [0, 0, 0], max: [4, 4, 0] }] };
  const url = 'data:model/gltf+json;base64,' + btoa(JSON.stringify(gltf));
  const before = E.scene.children.length;
  E.loadGLB(url, 'probe triangle');
  await wait(2500);
  let found = null;
  E.scene.traverse(o => { if (o.isMesh && o.geometry && o.geometry.attributes.position && o.geometry.attributes.position.count === 3 && !found) found = o; });
  return { sceneChildrenBefore: before, after: E.scene.children.length, triangleMeshInScene: !!found };
})()
