(async () => {
  const E = window.EMBER, THREE = window.THREE, R = E.renderer;
  const out = { renderer: {}, lights: {}, shadows: {}, frame: {} };

  out.renderer = {
    pixelRatio: R.getPixelRatio(),
    size: (() => { const v = new THREE.Vector2(); R.getSize(v); return [v.x, v.y]; })(),
    drawingBuffer: [R.domElement.width, R.domElement.height],
    cssSize: [R.domElement.clientWidth, R.domElement.clientHeight],
    shadowsEnabled: R.shadowMap.enabled,
    shadowType: R.shadowMap.type,
    shadowAutoUpdate: R.shadowMap.autoUpdate,
    renderScale: E.CONFIG.renderScale
  };

  const kinds = {};
  let shadowCasters = 0, castingLights = 0, shadowMapPixels = 0;
  E.scene.traverse(o => {
    if (o.isLight) {
      kinds[o.type] = (kinds[o.type] || 0) + 1;
      if (o.castShadow) {
        castingLights++;
        shadowMapPixels += (o.shadow.mapSize.width || 0) * (o.shadow.mapSize.height || 0);
        out.shadows[o.type] = { mapSize: [o.shadow.mapSize.width, o.shadow.mapSize.height] };
      }
    }
    if (o.isMesh && o.castShadow) shadowCasters++;
  });
  out.lights = { byType: kinds, castingShadow: castingLights, shadowMapPixels, meshesCastingShadow: shadowCasters };

  // how expensive is one frame, really
  const gl = R.getContext();
  const times = [];
  for (let i = 0; i < 40; i++) {
    const t0 = performance.now();
    R.render(E.scene, E.camera);
    gl.finish();
    times.push(performance.now() - t0);
  }
  times.sort((a, b) => a - b);
  out.frame.medianRenderMs = +times[Math.floor(times.length / 2)].toFixed(2);
  out.frame.worstRenderMs = +times[times.length - 1].toFixed(2);

  // same again with shadows off, to price them
  const wasShadow = R.shadowMap.enabled;
  R.shadowMap.enabled = false;
  E.scene.traverse(o => { if (o.isMesh) o.material && (o.material.needsUpdate = true); });
  R.render(E.scene, E.camera); gl.finish();
  const noShadow = [];
  for (let i = 0; i < 30; i++) {
    const t0 = performance.now(); R.render(E.scene, E.camera); gl.finish();
    noShadow.push(performance.now() - t0);
  }
  noShadow.sort((a, b) => a - b);
  out.frame.medianWithoutShadowsMs = +noShadow[Math.floor(noShadow.length / 2)].toFixed(2);
  R.shadowMap.enabled = wasShadow;

  out.frame.info = JSON.parse(JSON.stringify(R.info.render));
  return out;
})()
