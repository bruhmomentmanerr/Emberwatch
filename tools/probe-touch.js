(async()=>{
  const wait=ms=>new Promise(r=>setTimeout(r,ms));
  const out={errors:[]};
  addEventListener('error',e=>out.errors.push(String(e.message)));
  const E=window.EMBER;
  const f0=E.renderer.info.render.frame; await wait(800);
  out.loopRunning=E.renderer.info.render.frame>f0;
  const stick=document.getElementById('stick');
  out.stick=!!stick; out.talkButton=!!document.getElementById('interactBtn');
  if(!stick)return out;
  const rect=stick.getBoundingClientRect();
  const cx=rect.left+rect.width/2, cy=rect.top+rect.height/2;
  const mk=(type,x,y)=>{ const t=new Touch({identifier:7,target:stick,clientX:x,clientY:y});
    return new TouchEvent(type,{touches:type==='touchend'?[]:[t],changedTouches:[t],bubbles:true,cancelable:true}); };
  const before=[E.player.x,E.player.z];
  stick.dispatchEvent(mk('touchstart',cx,cy));
  for(let i=0;i<40;i++){ stick.dispatchEvent(mk('touchmove',cx,cy-42)); await wait(60); }
  stick.dispatchEvent(mk('touchend',cx,cy-42));
  await wait(400);
  out.movedByStick=+Math.hypot(E.player.x-before[0],E.player.z-before[1]).toFixed(2);
  // and the look drag on the canvas
  const canvas=E.renderer.domElement;
  const yaw0=E.camera.rotation.y;
  const mkc=(type,x,y)=>{ const t=new Touch({identifier:9,target:canvas,clientX:x,clientY:y});
    return new TouchEvent(type,{touches:type==='touchend'?[]:[t],changedTouches:[t],bubbles:true,cancelable:true}); };
  canvas.dispatchEvent(mkc('touchstart',400,300));
  for(let i=0;i<12;i++){ canvas.dispatchEvent(mkc('touchmove',400+i*10,300)); await wait(50); }
  canvas.dispatchEvent(mkc('touchend',520,300));
  await wait(300);
  out.lookTurned=+Math.abs(E.camera.rotation.y-yaw0).toFixed(3);
  // the touch interact button
  const talk=document.getElementById('interactBtn');
  out.talkClickable=!!(talk&&talk.onclick||talk);
  return out;
})()
