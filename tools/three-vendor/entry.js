// The Three.js engine as Emberwatch inlines it: the library and the two addons
// the game uses. Bundled to a single classic script by tools/build-three.js,
// which sets window.THREE exactly as the old r128 build did.
//
// The engine is stock three.js, lighting included. History, because the game's
// light values only make sense with it:
//
//   r110 moved from r128 to r186 behind a compatibility layer, which lived in
//   this file. It turned colour management off, patched r128's π and linear
//   light falloff back into ShaderChunk.lights_pars_begin, and defaulted point
//   and spot lights to decay 1, so the city looked exactly as it had on r128.
//
//   r111 retired that layer on purpose and retuned the game for physically
//   based light: sRGB colours converted to linear, inverse-square falloff, no π.
//   The conversion from the old light values lives in the game, in
//   lampLight() and lampPower() — see the "lights" section of index.html.
//
// Do not bring the layer back to fix a brightness problem: every light in the
// game and its variants is now tuned for physical light, and the layer would
// make the city several times too bright. The r110 archive in revisions/ has the
// last build that used it.

import * as THREE_NS from 'three';
import * as BufferGeometryUtils from 'three/addons/utils/BufferGeometryUtils.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// A module namespace is frozen, so the global is a copy of it with the addons
// attached where the old examples/js scripts put them.
const THREE = { ...THREE_NS, BufferGeometryUtils, GLTFLoader };

// Read by the game's diagnostics() and checked by tools/build-three.js.
THREE.EMBERWATCH_LIGHTS = 'physical';
globalThis.THREE = THREE;
