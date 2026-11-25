// Records explicitly surveyed sectors, not every sector traversed.
function recordSurveySector(snapshot,id){
 if(typeof id!=='string'||!/^([0-3]|-[1-3]),([0-3]|-[1-3])$/.test(id))return null;
 const raw=snapshot.surveyedSectors;
 const ids=Array.isArray(raw)?[...new Set(raw.filter(v=>typeof v==='string'&&/^([0-3]|-[1-3]),([0-3]|-[1-3])$/.test(v)))]:[];
 const fresh=!ids.includes(id);if(fresh)ids.push(id);
 snapshot.surveyedSectors=ids;
 return {fresh,count:ids.length};
}
function showSageTerritory(p){
 const t=sageTerritory(state.seed,player.position.x,player.position.z);
 const result=recordSurveySector(state,t.id);if(result?.fresh)save();
 const h=document.createElement('h3');h.textContent='Territory survey';
 const d=document.createElement('p');d.textContent=t.name+' — 15-unit survey sector. Region designation only; terrain and inhabitants are unchanged.';p.append(h,d);
 if(result){const progress=document.createElement('p');progress.textContent=(result.fresh?'New sector surveyed. ':'Previously surveyed. ')+result.count+' of 49 sectors surveyed.';p.append(progress);}
}
