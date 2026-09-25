(async()=>{
  const E=window.EMBER, wait=ms=>new Promise(r=>setTimeout(r,ms));
  const out={errors:[],phases:[]};
  addEventListener('error',e=>out.errors.push(String(e.message)));
  async function ride(id,seconds){
    E.setWatch(id);
    await wait(seconds*1000);
    out.phases.push({
      asked:id, actual:E.watch().id,
      indoors:E.villagers.filter(n=>n.indoors).length,
      visible:E.villagers.filter(n=>n.g.visible).length,
      meeting:E.villagers.filter(n=>n.meetingWith).length,
      calls:E.renderer.info.render.calls
    });
  }
  E.player.x=0; E.player.z=120;
  await ride('labour',26);
  await ride('market',26);
  await ride('still',46);
  await ride('ember',40);
  await ride('labour',24);
  out.residents=E.villagers.length;
  return out;
})()
