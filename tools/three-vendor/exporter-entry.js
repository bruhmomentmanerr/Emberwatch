// A tools-only bundle: three's glTF exporter, as a classic script that hangs
// itself on window.THREE_EXPORT. It is deliberately NOT part of entry.js — the
// game ships the engine inlined in one HTML file, and nothing that only a probe
// needs belongs in the file the player downloads. tools/probes/probe-export-city.js
// injects this at runtime to write the city out for Blender.
import { GLTFExporter } from 'three/addons/exporters/GLTFExporter.js';
window.THREE_EXPORT = { GLTFExporter };
