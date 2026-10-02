/* Build the Emberwatch variant editions.
   Each is a full standalone copy of the live build with one self-contained
   layer injected before </body>. The base file is never modified, so a variant
   is always regenerable from whatever the current revision is.

   Most variants are purely additive: the layer runs after the world is built
   and adds to it. r0 is the exception. A layer cannot un-build a city, because
   by the time it runs every static mesh has been merged into batches by
   material, so r0 also carries a `transform` that edits the source before the
   world stages run. */
const fs = require('fs'), path = require('path');

const ROOT = path.join(__dirname, '..');
const BASE = path.join(ROOT, 'app', 'renderer', 'index.html');
const SRC  = path.join(ROOT, 'variants', 'src');
const OUT  = path.join(ROOT, 'variants');

const VARIANTS = [
  { file: 'wardens.js',   out: 'emberwatch_wardens.html',
    title: 'Emberwatch — Wardens',        sub: 'the ledger of the black city' },
  { file: 'longnight.js', out: 'emberwatch_long-night.html',
    title: 'Emberwatch — The Long Night', sub: 'what the dark left behind' },
  { file: 'emberhour.js', out: 'emberwatch_ember-hour.html',
    title: 'Emberwatch — Ember Hour',    sub: 'the session is the clock' },
  { file: 'heatline.js',  out: 'emberwatch_heatline.html',
    title: 'Emberwatch — Heatline',      sub: 'temperature is the dial' },
  { file: 'emberfall.js', out: 'emberwatch_emberfall.html',
    title: 'Emberwatch — Emberfall',      sub: 'carry the last light' },
  // Not a step in the revision chain. The chain run backwards.
  { file: 'barebones.js', out: 'emberwatch_r0_barebones.html',
    title: 'Emberwatch r0', sub: 'tech demo', transform: bareWorld }
];

// r0's world: no Vaneth at all, just a clearing with a fire in it. Written into
// the source rather than the layer so it can use the game's own aBox/aCyl/aCone
// helpers, which means it lands in the batched meshes and gets real colliders.
// A layer can only add loose meshes with no collision.
const CAMPSITE = `
function campsite(){
  // ---- materials -----------------------------------------------------------
  // Everything in this camp used to be drawn with the city's 'wood': a red-brown
  // plank texture. Planks are right for a bench, wrong for bark, and wrong again
  // for tent canvas, so a trunk, a tarpaulin and a crate all came out the same
  // shade of sawn timber. And MATS.foliage carries an emissive green, which is
  // why a forest at night glowed like moulded plastic instead of sitting dark
  // under the sky.
  //
  // These are r0's own, registered before anything is built and left out of the
  // city entirely. UV_TILED_KEYS is what makes a texture repeat over a surface
  // rather than stretch one copy across it, so every tiled key joins it.
  const mat=(key,m,tiled)=>{ MATS[key]=m; if(tiled)UV_TILED_KEYS.add(key); };
  mat('bark',   sm(makeTex(0x352a1e,{pattern:'wood',  density:.013,jitter:7})), true);
  mat('canvas', sm(makeTex(0x9a8c72,{pattern:'cloth', density:.007,jitter:5})), true);
  mat('ash',    sm(makeTex(0x33302c,{pattern:'ground',density:.030,jitter:6,repeat:[3,3]})), true);
  // Dark on purpose. A mid-grey stone sitting a metre from an open fire is
  // driven to pale tan by it, and the ring came out looking like sawn logs.
  mat('rock',   sm(makeTex(0x39373f,{pattern:'stone', density:.006,jitter:5})), true);
  // Forest floor: needle litter and dark earth, laid over the base ground so
  // the camp is not standing on an orange plain.
  mat('floor',  sm(makeTex(0x2a2a20,{pattern:'ground',density:.034,jitter:7,repeat:[30,30]})), true);
  mat('iron',   new THREE.MeshStandardMaterial({color:0x2b2b33,roughness:.62,metalness:.35,flatShading:true}));
  // Two needle tones, neither of them emissive. A stand of trees in one flat
  // green reads as one object; two tones a little apart give it depth at no
  // cost, because they are still only two merged meshes.
  mat('needle', new THREE.MeshStandardMaterial({color:0x22402e,roughness:1,flatShading:true}));
  mat('needle2',new THREE.MeshStandardMaterial({color:0x2c4a33,roughness:1,flatShading:true}));

  const CLEAR=20;

  // ---- the clearing floor --------------------------------------------------
  // One unbroken sheet of ground is the flattest thing in any of these scenes.
  // A scorched patch under the fire, a trodden ring round it where people walk,
  // then grass and stones breaking up everything outside that.
  const floor=new THREE.Mesh(tileFlatUV(new THREE.CircleGeometry(CLEAR+30,48).rotateX(-Math.PI/2),30),MATS.floor);
  floor.position.y=.012; floor.receiveShadow=true; scene.add(floor);
  const scorch=new THREE.Mesh(tileFlatUV(new THREE.CircleGeometry(3.1,24).rotateX(-Math.PI/2),3),MATS.ash);
  scorch.position.y=.025; scorch.receiveShadow=true; scene.add(scorch);
  const worn=new THREE.Mesh(tileFlatUV(new THREE.RingGeometry(3.0,6.6,28).rotateX(-Math.PI/2),5),MATS.dirt);
  worn.position.y=.02; worn.receiveShadow=true; scene.add(worn);
  for(let i=0;i<120;i++){
    const a=rand(0,Math.PI*2), r=rand(4.2,CLEAR+9);
    const x=Math.cos(a)*r, z=Math.sin(a)*r;
    if(Math.hypot(x,z)<4.2)continue;
    aCone(rand(.16,.34),rand(.28,.62),4,x,.16,z,i%3?'needle':'needle2',rand(0,3));
  }
  for(let i=0;i<26;i++){
    const a=rand(0,Math.PI*2), r=rand(5,CLEAR+7);
    const x=Math.cos(a)*r, z=Math.sin(a)*r, s=rand(.22,.62);
    aCyl(s*.8,s,s*rand(.5,.9),5,x,s*.3,z,'rock',rand(0,3));
    if(s>.45)addCollider(x,z,s*.9);
  }

  // ---- the fire ------------------------------------------------------------
  // Ring of stones in rock rather than the city's cut masonry, an ash bed, and
  // logs laid across it.
  for(let i=0;i<13;i++){ const a=(i/13)*Math.PI*2+rand(-.06,.06), r=1.55+rand(-.06,.06);
    aCyl(.28,.33,.3,5,Math.cos(a)*r,.15,Math.sin(a)*r,'rock',a); }
  aCyl(1.35,1.45,.1,12,0,.05,0,'ash');
  for(const a of[0.5,2.6,4.7])
    aBox(.24,.24,1.9,Math.cos(a)*.25,.24,Math.sin(a)*.25,'bark',a);
  addCollider(0,0,1.7);

  // Several small tongues rather than one cone. A single cone scaled up reads
  // as a lit shape sitting in the camp; overlapping tongues at different sizes
  // and phases read as fire even at this polygon count. Unlit materials, so
  // the flame is exactly the colour it is set to and never washes out to white
  // however hard the Peak is driving it.
  //
  // The names and userData below are the layer's handles on the fire: it finds
  // r0-flame, r0-fire and r0-embers by name and drives them from the device.
  // Do not rename them.
  const flame=new THREE.Group(); flame.name='r0-flame'; flame.position.y=.18;
  const outerMat=new THREE.MeshBasicMaterial({color:0xff7a24,fog:false});
  const coreMat =new THREE.MeshBasicMaterial({color:0xffd166,fog:false});
  flame.userData.mats={outer:outerMat,core:coreMat};
  const tongue=(r,h,x,z,m,ph)=>{
    const mesh=new THREE.Mesh(new THREE.ConeGeometry(r,h,5),m);
    mesh.position.set(x,h/2,z); mesh.userData.ph=ph; flame.add(mesh); return mesh;
  };
  tongue(.40,1.10, 0.00, 0.00,outerMat,0.0);
  tongue(.24,0.74,-0.26, 0.14,outerMat,1.7);
  tongue(.21,0.62, 0.24,-0.16,outerMat,3.4);
  tongue(.15,0.46, 0.02, 0.22,outerMat,5.0);
  tongue(.19,0.56, 0.00, 0.00,coreMat, 2.5);
  scene.add(flame);

  // Not pushed into lights[] with a base flicker: the layer owns this one.
  const fire=lampLight(0xff8a3c,1.4,18); fire.position.set(0,1.0,0);
  fire.name='r0-fire'; scene.add(fire);
  lights.push({light:fire,base:1.4,phase:0,fire:true});
  const emberGeo=new THREE.BufferGeometry(); const EN=40, ep=new Float32Array(EN*3);
  for(let i=0;i<EN;i++){ ep[i*3]=rand(-.5,.5); ep[i*3+1]=rand(.4,3.2); ep[i*3+2]=rand(-.5,.5); }
  emberGeo.setAttribute('position',new THREE.BufferAttribute(ep,3));
  const embers=new THREE.Points(emberGeo,new THREE.PointsMaterial({color:0xffa84c,size:.09,transparent:true,opacity:.85,fog:false}));
  embers.name='r0-embers'; scene.add(embers);

  // A spit over the fire, because a fire with nothing on it reads as decoration
  // rather than a camp. It is a spit and not a tripod on purpose: aBox only
  // takes a Y rotation, so three "tripod" legs come out as three vertical posts
  // that never meet, which looked like scaffolding with a boulder on it.
  for(const ux of[-1.6,1.6]){ aBox(.13,2.0,.13,ux,1.0,0,'bark'); addCollider(ux,0,.2); }
  aBox(3.4,.07,.07,0,1.97,0,'iron');
  aBox(.04,.46,.04,.55,1.73,0,'iron');
  aCyl(.3,.26,.42,8,.55,1.29,0,'iron');
  aBox(.04,.32,.04,-.6,1.8,0,'iron');
  aBox(.46,.05,.3,-.6,1.62,0,'iron');

  // ---- tents ---------------------------------------------------------------
  // Canvas over a ridge pole, mouth to the fire: a pale weathered sheet, a dark
  // opening, a bark ridge and pegged guy lines.
  // Sized off the people who sleep in them, not off the clearing: at 3.0 across
  // and 2.9 tall these stood higher than the tree line behind them and made the
  // fire look like a candle.
  const tent=(tx,tz,ry)=>{
    aCone(2.25,2.35,4,tx,1.18,tz,'canvas',ry+Math.PI/4);
    aBox(.1,.1,3.5,tx,2.32,tz,'bark',ry);
    aBox(.95,1.2,.06,tx+Math.sin(ry)*1.08,.6,tz+Math.cos(ry)*1.08,'dark',ry);
    for(const g of[-1,1]){
      const px=tx+Math.cos(ry)*g*1.6, pz=tz-Math.sin(ry)*g*1.6;
      aBox(.045,.045,1.2,px,.38,pz,'bark',ry+.7);
      aCyl(.045,.055,.26,4,px+Math.cos(ry)*g*.4,.13,pz-Math.sin(ry)*g*.4,'bark');
    }
    addBoxCollider(tx,tz,2.6,2.6,ry);
  };
  tent(-6.6,-4.6,0.5); tent(6.2,-5.6,-0.7); tent(-7.8,3.0,1.9);

  // ---- somewhere to sit ----------------------------------------------------
  // Split logs round the fire at 30, 150 and 270 degrees, which leaves the
  // approach you actually walk in along open.
  for(const seat of [[-3.64,2.10,-4.189],[0,-4.20,0],[3.64,2.10,-2.094]]){
    aCyl(.28,.28,3.0,7,seat[0],.28,seat[1],'bark',seat[2]+Math.PI/2);
    aBox(2.9,.12,.5,seat[0],.42,seat[1],'bark',seat[2]);
    addBoxCollider(seat[0],seat[1],3.0,.6,seat[2]); }
  for(const stump of [[-3.2,-4.4],[3.6,-3.9],[5.2,1.4]]){
    aCyl(.46,.54,.6,7,stump[0],.3,stump[1],'bark'); aCyl(.44,.44,.05,7,stump[0],.62,stump[1],'wood');
    addCollider(stump[0],stump[1],.58); }

  // ---- stores --------------------------------------------------------------
  // Crates are sawn boards, so these keep the plank texture; everything round
  // them is bark or canvas, which is the whole point of separating them.
  for(const crate of [[8.6,2.4],[-9.2,-.6],[8.2,4.0]]){
    aBox(1.0,.9,1.0,crate[0],.45,crate[1],'wood',rand(0,3));
    aBox(1.04,.08,1.04,crate[0],.92,crate[1],'iron',rand(0,3));
    addCollider(crate[0],crate[1],.75); }
  for(let i=0;i<8;i++) aCyl(.1,.11,1.6,6,-6.0+(i%4)*.25,.12+Math.floor(i/4)*.22,6.2,'bark',Math.PI/2);
  for(let i=0;i<5;i++){ const a=rand(0,6.28),r=rand(3.4,7);
    aCyl(.08,.09,1.2,5,Math.cos(a)*r,.09,Math.sin(a)*r,'bark',a+Math.PI/2); }
  addCollider(-6.0,6.2,1.1);
  aBox(.8,.66,.56,-2.6,.33,-5.1,'canvas',.3); addCollider(-2.6,-5.1,.6);
  aCyl(.28,.34,.58,7,4.4,.29,-5.6,'canvas'); addCollider(4.4,-5.6,.4);

  // ---- a drying line -------------------------------------------------------
  for(const px of[-10.5,-4.2]){ aCyl(.07,.09,2.5,5,px,1.25,-8.8,'bark'); addCollider(px,-8.8,.3); }
  aBox(6.3,.04,.04,-7.35,2.4,-8.8,'iron');
  for(let i=0;i<3;i++) aBox(.86,.95,.03,-9.6+i*2.2,1.88,-8.8,'canvas');

  // ---- a lantern, so the clearing has a second, steadier light -------------
  aCyl(.08,.11,3.3,5,3.5,1.65,7.4,'bark');
  aBox(.34,.1,.34,3.5,3.28,7.4,'iron');
  aBox(.3,.34,.3,3.5,3.5,7.4,'amber');
  aCone(.3,.22,4,3.5,3.78,7.4,'iron');
  addCollider(3.5,7.4,.3);
  const lamp=lampLight(0xffaf64,1.1,16); lamp.position.set(3.5,3.5,7.4);
  scene.add(lamp); lights.push({light:lamp,base:1.1,phase:rand(0,6)});

  // ---- the trees -----------------------------------------------------------
  // Three tiers of needles on a bark trunk, sizes and tones varied so the ring
  // does not read as one cut-and-pasted tree. The near ring you can walk up to;
  // a denser far ring closes the view so the camp feels enclosed rather than
  // standing on an empty plain.
  const tree=(x,z,h,w,tone)=>{
    aCyl(.15*w,.27*w,h,6,x,h/2,z,'bark');
    aCone(1.85*w,3.0,7,x,h*.66,z,tone);
    aCone(1.45*w,2.5,7,x,h*.84,z,tone==='needle'?'needle2':'needle');
    aCone(.95*w,1.9,6,x,h*1.0,z,tone);
  };
  for(let i=0;i<58;i++){
    const a=(i/58)*Math.PI*2+rand(-.07,.07), r=CLEAR+rand(1,14);
    const x=Math.cos(a)*r, z=Math.sin(a)*r;
    tree(x,z,rand(4.5,8.5),rand(.75,1.3),i%2?'needle':'needle2');
    if(i%2===0)addCollider(x,z,.8);
  }
  for(let i=0;i<80;i++){
    const a=rand(0,Math.PI*2), r=CLEAR+15+rand(0,26);
    tree(Math.cos(a)*r,Math.sin(a)*r,rand(5,9.5),rand(.8,1.2),i%3?'needle':'needle2');
  }
  // Two fallen trunks at the edge, because a forest floor is not swept.
  for(const log of [[-13.5,9.5,.7],[12.8,-11,2.4]]){
    aCyl(.34,.4,5.2,6,log[0],.36,log[1],'bark',log[2]);
    addBoxCollider(log[0],log[1],5.2,.8,log[2]);
  }
}
`;

function bareWorld(html) {
  const swap = (from, to, what) => {
    const n = html.split(from).length - 1;
    if (n !== 1) throw new Error('bareWorld: ' + what + ' matched ' + n + ' times');
    html = html.replace(from, to);
  };

  // r0 gets its own save keys. Sharing them would mean opening the demo
  // overwrites the real game's saved position and world seed, and reading them
  // would drop you at whatever coordinate the last real session ended on —
  // which, in a world with no city, is empty ground.
  swap("const GAME_SAVE_KEY='emberwatch.game-state.v3'",
       "const GAME_SAVE_KEY='emberwatch.r0.game-state.v3'", 'save key');
  swap("const WORLD_SEED_KEY='emberwatch.vaneth.world-seed.v2'",
       "const WORLD_SEED_KEY='emberwatch.r0.world-seed.v2'", 'seed key');

  // Everything from the first world stage to the last is replaced. Spliced by
  // index and anchored on line content, because the stage lines are long and
  // their leading whitespace is not worth depending on.
  const from = html.indexOf("LMSG.textContent='planning the avenues");
  const tailMark = 'makeVanethLively();';
  const tail = html.indexOf(tailMark);
  if (from < 0 || tail < 0 || tail < from) throw new Error('bareWorld: world stages not found');
  const lineStart = html.lastIndexOf('\n', from) + 1;

  // outerBuilt and innerBuilt survive as stubs: EMBER exposes both and the
  // diagnostics read outerBuilt.features.length and outerBuilt.colliders. This
  // stub had to follow r106's change to wilderness() and did not, so r0's
  // diagnostics() threw on every call from r106 until r107 — the builder only
  // transforms text and never runs what it builds. tools/check-variants.js now
  // boots every variant and calls diagnostics, which is what would have caught it.
  const stages = [
    '  // r0 builds no city. The ground, sky, moon and starfield are made at',
    '  // module level and survive; every stage that would have raised Vaneth is',
    '  // gone, and a campsite stands at the origin instead. The geometry audit',
    '  // will warn about having no interior doors, which is correct and expected.',
    CAMPSITE.trim().split('\n').map(l => '  ' + l).join('\n'),
    "  LMSG.textContent='setting a fire\\u2026'; useWorldStream('campsite'); campsite();",
    '  const outerBuilt={features:[],colliders:0};',
    '  const innerBuilt={built:0};'
  ].join('\n');

  html = html.slice(0, lineStart) + stages + html.slice(tail + tailMark.length);

  // r0 has nowhere for anyone to live, and the resident spawners run after the
  // world stages so cutting those did not stop them: 58 were still being made
  // and updated every frame against an empty nav grid. Neutering villager()
  // itself is one edit and stops all of them, wherever they are called from.
  // (r143 gave villager() an optional look parameter; the match follows it.)
  swap('function villager(name,x,z,robe,line,route=[],districtOverride,look=null){',
       'function villager(){ return; }\nfunction villagerDisabledForR0(name,x,z,robe,line,route=[],districtOverride,look=null){',
       'villager');

  // r0 is a campfire at night. The base restores whatever lighting mode was
  // last saved, and a profile that happens to hold 'dusk' lights the clearing
  // with an orange sky at 1.5 and a warm sun at 1.86 — under an aurora, which
  // is the night sky. The camp came out orange and the fire had nothing to
  // stand out against. The demo pins itself to night; the four watches still
  // turn, they just no longer drag the sky with them.
  swap("setLighting(savedGameState?.lighting||'night');",
       "setLighting('night');", 'night lighting');

  // Spawn just south of the fire, looking at it.
  // The base spawn has moved twice: to the north gate of the one remaining wall
  // in r85, and out to the new outer wall's north gate in r94.
  swap('const SPAWN_A=90*Math.PI/180, SPAWN_R=OUTER_WALL_R+26;',
       'const SPAWN_A=Math.PI/2, SPAWN_R=12;', 'spawn');

  return html;
}

// The light pool (src/lightpool.js) was injected into every variant until r115.
// It was a fix for r86, and the base's own light budget (cullLights, r91-r92)
// replaced it, but the two kept fighting over the same lamps: the nearest ones
// were lit twice, and Emberfall ran 46 lights at the gate against the base
// game's 8 (r114 audit). Variant lamps now join the base budget through
// EMBER.addLamp, and nothing is injected but the layer itself.

const base = fs.readFileSync(BASE, 'utf8');
const rev = (base.match(/revision:'(r\d+)'/) || [])[1] || 'unknown';
let built = 0;

for (const v of VARIANTS) {
  const layer = fs.readFileSync(path.join(SRC, v.file), 'utf8');
  if (layer.includes('</script')) { console.error('FAIL ' + v.file + ' contains a closing script tag'); process.exitCode = 1; continue; }

  let html;
  try { html = v.transform ? v.transform(base) : base; }
  catch (err) { console.error('FAIL ' + v.out + ': ' + err.message); process.exitCode = 1; continue; }

  const t0 = html.split('<title>Emberwatch</title>').length - 1;
  if (t0 !== 1) { console.error('FAIL title anchor in ' + v.out + ' (' + t0 + ')'); process.exitCode = 1; continue; }
  html = html.replace('<title>Emberwatch</title>', '<title>' + v.title + '</title>');

  const subRe = /(<div id="gameTitle"[^>]*>[\s\S]{0,200}?<span class="u">)([^<]*)(<\/span>)/;
  if (subRe.test(html)) html = html.replace(subRe, (_m, a, _b, c) => a + v.sub + c);

  const inject = '\n<!-- ' + v.title + ' — variant layer over base ' + rev + ' -->\n<script>\n' + layer + '\n</scr' + 'ipt>\n';
  const b0 = html.split('</body>').length - 1;
  if (b0 !== 1) { console.error('FAIL body anchor in ' + v.out + ' (' + b0 + ')'); process.exitCode = 1; continue; }
  html = html.replace('</body>', inject + '</body>');

  fs.writeFileSync(path.join(OUT, v.out), html);
  console.log('built ' + v.out + '  (' + (html.length / 1048576).toFixed(2) + ' MB, base ' + rev + ')');
  built++;
}
console.log(built + '/' + VARIANTS.length + ' variants built from base ' + rev);
