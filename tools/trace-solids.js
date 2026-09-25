'use strict';
// Build a copy of the game that records every solid it puts in the world.
// aBox/aCyl/aCone merge their geometry into one mesh per material, so nothing
// downstream can tell one solid from another — which is why a scene-graph
// audit cannot see the city's props at all. Tapping the constructors gives the
// exact inventory. Cylinders and cones matter as much as boxes: leave them out
// and everything standing on a tower drum, a barrel or a post reads as
// floating, which is the false positive this project has already chased once.
const fs = require('fs');
let t = fs.readFileSync('app/renderer/index.html', 'utf8');

const EDITS = [
  ['function aBox(w,h,d,x,y,z,k,ry=0){ const g=new THREE.BoxGeometry(w,h,d);',
   'function aBox(w,h,d,x,y,z,k,ry=0){ (window.__BOXES=window.__BOXES||[]).push([w,h,d,x,y,z,k,ry]); const g=new THREE.BoxGeometry(w,h,d);'],
  ['function aCone(r,h,s,x,y,z,k,ry=0){ const g=new THREE.ConeGeometry(r,h,s);',
   'function aCone(r,h,s,x,y,z,k,ry=0){ (window.__BOXES=window.__BOXES||[]).push([r*2,h,r*2,x,y,z,k,0]); const g=new THREE.ConeGeometry(r,h,s);'],
  ['function aCyl(rt,rb,h,s,x,y,z,k,ry=0){ const g=new THREE.CylinderGeometry(rt,rb,h,s);',
   'function aCyl(rt,rb,h,s,x,y,z,k,ry=0){ (window.__BOXES=window.__BOXES||[]).push([Math.max(rt,rb)*2,h,Math.max(rt,rb)*2,x,y,z,k,0]); const g=new THREE.CylinderGeometry(rt,rb,h,s);']
];
const bad = EDITS.filter(([a]) => t.split(a).length - 1 !== 1);
if (bad.length) { console.error('FAILED:\n  ' + bad.map(b => b[0].slice(0, 50)).join('\n  ')); process.exit(1); }
for (const [a, b] of EDITS) t = t.replace(a, b);
fs.writeFileSync(process.argv[2], t);
console.log('ok — solid-tracing copy written (boxes, cylinders, cones)');
