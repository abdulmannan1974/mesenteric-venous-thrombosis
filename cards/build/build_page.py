import io, json, os
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.join(HERE,'..')
data=json.dumps(json.load(open(os.path.join(ROOT,'cards.json'),encoding='utf-8')),ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
t=io.open(os.path.join(HERE,'template.html'),encoding='utf-8').read()
io.open(os.path.join(ROOT,'index.html'),'w',encoding='utf-8').write(t.replace('__DATA__',data))
print('built index.html')
