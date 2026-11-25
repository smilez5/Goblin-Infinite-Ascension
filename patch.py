from pathlib import Path
import sys
p=Path(sys.argv[1]); s=p.read_text(); edits=[('function vrHands(dt){','function validSwing(dt,distance){return Number.isFinite(dt)&&Number.isFinite(distance)&&dt>=.004&&dt<=.05&&distance>=0&&distance<=.35&&distance/dt>1.25&&distance/dt<=12;}\nfunction vrHands(dt,trackingDt=dt){'),('if(h.prev&&dt>0&&local.distanceTo(h.prev)/dt>1.25&&h.cool===0)','if(h.prev&&validSwing(trackingDt,local.distanceTo(h.prev))&&h.cool===0)'),('let dt=frameDelta(now,last);last=now;','let trackingDt=(now-last)/1000;let dt=frameDelta(now,last);last=now;'),('vrHands(dt)}else','vrHands(dt,trackingDt)}else')];
for a,b in edits:
 if s.count(a)!=1: raise SystemExit('Incompatible source or already applied: '+a)
 s=s.replace(a,b)
p.write_text(s)
