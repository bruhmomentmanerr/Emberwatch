const {app,BrowserWindow}=require('electron');
const assert=require('node:assert/strict'),path=require('node:path'),os=require('node:os'),fs=require('node:fs');
app.setPath('userData',fs.mkdtempSync(path.join(os.tmpdir(),'emberwatch-fez-')));
app.disableHardwareAcceleration();
app.whenReady().then(async()=>{
 const win=new BrowserWindow({show:true,width:1100,height:800,webPreferences:{backgroundThrottling:false,preload:path.join(__dirname,'harness/preload.js'),contextIsolation:false,sandbox:false}});
 const run=code=>win.webContents.executeJavaScript(code,true);
 const ready=async()=>{for(let i=0;i<120;i++){if(await run('!!window.EMBER'))return;await new Promise(r=>setTimeout(r,200));}throw Error('Game did not boot');};
 const key='emberwatch.personal-strains.v1';
 try{
  await win.loadFile(path.join(__dirname,'../app/renderer/index.html'));await ready();
  const first=await run(`JSON.parse(localStorage.getItem('${key}'))`);
  const jars=first.records.filter(r=>r.name==='Fez');assert.equal(jars.length,1);assert.equal(jars[0].form,'unspecified');assert.equal(jars[0].reference.lineage,'Rainbow Belts × Moroccan Peaches');assert.deepEqual(jars[0].reference.effects,[]);
  await run(`document.getElementById('strainBtn').click()`);
  assert.ok(await run(`document.getElementById('strainList').textContent.includes('Rainbow Belts × Moroccan Peaches')`),'lineage visible in journal');
  await win.loadFile(path.join(__dirname,'../app/renderer/index.html'));await ready();
  assert.equal(await run(`JSON.parse(localStorage.getItem('${key}')).records.filter(r=>r.name==='Fez').length`),1,'no duplicate on reload');
  await run(`(()=>{const j=JSON.parse(localStorage.getItem('${key}'));j.records=j.records.filter(r=>r.name!=='Fez');localStorage.setItem('${key}',JSON.stringify(j));})()`);
  await win.loadFile(path.join(__dirname,'../app/renderer/index.html'));await ready();
  assert.equal(await run(`JSON.parse(localStorage.getItem('${key}')).records.filter(r=>r.name==='Fez').length`),0,'removed jar stays removed');
  const audit=await run(`(()=>{const n=EMBER.villagers.find(n=>n.name==='Dunna Wex');return {revision:EMBER.diagnostics().revision,dunnaSculpt:!!n?.sculptBody,sculptParts:n?.g.children.filter(p=>p.name.startsWith('dunna-wex-sculpt')).length};})()`);
  console.log('PASS Fez arrival, lineage rendering, reload deduplication, removal persistence. '+JSON.stringify(audit));app.exit(0);
 }catch(e){console.error(e);app.exit(1);}
});
