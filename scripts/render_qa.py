"""Render a Beamer PDF and report content outside page bounds; no source edits."""
from pathlib import Path
import sys,json,pymupdf
from PIL import Image,ImageDraw
pdf=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
doc=pymupdf.open(pdf);issues=[];previews=[]
for i,p in enumerate(doc):
    pix=p.get_pixmap(matrix=pymupdf.Matrix(1.65,1.65),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.save(out/f'slide-{i+1:03}.png')
    thumb=im.resize((600,338));previews.append(thumb)
    for block in p.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for s in line['spans']:
                x0,y0,x1,y1=s['bbox']
                if x0<-.5 or x1>p.rect.width+.5 or y0<-.5 or y1>p.rect.height+.5:
                    issues.append({'slide':i+1,'text':s['text'],'bbox':s['bbox']})
for start in range(0,len(previews),9):
    sheet=Image.new('RGB',(1800,1095),'#ddd');draw=ImageDraw.Draw(sheet)
    for j,im in enumerate(previews[start:start+9]):
        x=(j%3)*600;y=(j//3)*365;sheet.paste(im,(x,y+22));draw.text((x+6,y+4),str(start+j+1),fill='black')
    sheet.save(out/f'contact-{start+1:03}-{min(start+9,len(previews)):03}.jpg',quality=85)
(out/'bounds.json').write_text(json.dumps(issues,indent=2)+'\n')
print(f'{len(doc)} slides rendered; {len(issues)} out-of-page text spans; {len(list(out.glob("contact-*.jpg")))} contact sheets')
