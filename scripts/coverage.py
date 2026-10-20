"""Inventory thesis graphics and locate every use in the active presentation."""
from pathlib import Path
import re, json, hashlib
ROOT=Path(__file__).resolve().parents[1]
THESIS=ROOT.parent/'Lattice-QCD-calculations-of-x-dependence-of-Sivers-TMD-Hariprashad-Ravikumar-NMSU-PhD-Thesis'
def clean(t): return re.sub(r'(?<!\\)%[^\n]*','',t)
def expand(p):
    t=clean(p.read_text())
    return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(ROOT/(m[1]+('' if m[1].endswith('.tex') else '.tex'))),t)
t=expand(ROOT/'main.tex').split(r'\appendix')[0]
frames=re.findall(r'\\begin\{frame\}(.*?)\\end\{frame\}',t,re.S)
used={}
for i,f in enumerate(frames,1):
    for m in re.finditer(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',f):
        used.setdefault(Path(m[1]).name,[]).append(i)
# Cropped copies retain an explicit source-to-asset manifest.
manifest=ROOT/'figures/thesis/fitting/coverage.json'
derived={}
if manifest.exists():
    for entry in json.loads(manifest.read_text()):
        key=Path(entry['source']).stem
        derived.setdefault(key,set()).update(used.get(Path(entry['asset']).name,[]))
native=ROOT/'audit/native_path_tables.json'
if native.exists():
    for entry in json.loads(native.read_text()):
        indices={i for i,f in enumerate(frames,1) if any(
            r'\label{'+label+'}' in f for label in entry['labels'])}
        derived.setdefault(Path(entry['source']).stem,set()).update(indices)
rows=[]
for chapter in sorted((THESIS/'Chapters').glob('*.tex')):
    text=clean(chapter.read_text());pl=''
    pattern=r'\\(?:re)?newcommand\{\\PLval\}\{([^}]+)\}|\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}'
    for m in re.finditer(pattern,text):
        if m[1]: pl=m[1];continue
        src=m[2].replace(r'\PLval',pl)
        slides=sorted(set(used.get(Path(src).name,[])) | derived.get(Path(src).stem,set()))
        rows.append({'chapter':chapter.stem,'source':src,'slides':slides,'source_exists':(THESIS/src).is_file()})
(ROOT/'audit'/'figure_coverage.json').write_text(json.dumps(rows,indent=2)+'\n')
lines=['# Thesis figure coverage','',f'{len(frames)} active main-talk frames.','', '| Chapter | Source asset | Main-talk slides |','|---|---|---|']
for r in rows:lines.append(f"| {r['chapter']} | `{r['source']}` | {', '.join(map(str,r['slides'])) or '**MISSING**'} |")
(ROOT/'audit'/'figure_coverage.md').write_text('\n'.join(lines)+'\n')
missing=[r for r in rows if not r['slides']]
print(f'{len(rows)} thesis graphics references; {len(missing)} missing; {len(frames)} main-talk frames')
for r in missing: print(r['chapter']+': '+r['source'])
