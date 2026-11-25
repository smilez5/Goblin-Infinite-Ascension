from pathlib import Path
import sys
p=Path(sys.argv[1]); s=p.read_text(); marker='function showSageTerritory(p){'; end='function showSageAdvice(p)'
if 'function recordSurveySector(' in s or s.count(marker)!=1 or s.count(end)!=1 or 'function sageTerritory(seed,x,z)' not in s or 'showSageTerritory(p);' not in s: raise SystemExit('Incompatible or already patched source; no changes written')
a=s.index(marker); b=s.index(end,a)
old=s[a:b]
if 'Region designation only; terrain and inhabitants are unchanged.' not in old: raise SystemExit('Unexpected survey implementation; no changes written')
new=Path(__file__).with_name('survey.js').read_text()+'\n'
p.write_text(s[:a]+new+s[b:])
