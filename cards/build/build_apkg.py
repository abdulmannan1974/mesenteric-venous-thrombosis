import json, os, genanki, html
HERE=os.path.dirname(os.path.abspath(__file__))
D=json.load(open(os.path.join(HERE,'..','cards.json'),encoding='utf-8'))
DECK=[d for d in D['decks']]; BY={d['id']:(i+1,d) for i,d in enumerate(DECK)}

CSS = """
.card{font-family:-apple-system,'Inter','Segoe UI',Helvetica,Arial,sans-serif;background:#eef3fb;color:#0f1c2e;margin:0;padding:18px;text-align:left}
.nightMode.card,.card.nightMode{background:#0a1220;color:#eaf2fc}
.wrap{max-width:760px;margin:0 auto}
.front{border-radius:24px;padding:26px 30px 22px;min-height:260px;display:flex;flex-direction:column;box-shadow:0 18px 44px rgba(15,28,46,.18)}
.tag{font-size:13px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;opacity:.9}
.q{font-size:32px;font-weight:800;line-height:1.25;letter-spacing:-.02em;margin:auto 0;padding:22px 0}
.q u{text-decoration-thickness:3px;text-underline-offset:5px}
.backc{margin-top:16px;border-radius:24px;overflow:hidden;background:#fff;border:1px solid #d6e1ee;box-shadow:0 18px 44px rgba(15,28,46,.12)}
.nightMode .backc{background:#131f33;border-color:#243851}
.band{height:12px}
.bb{padding:22px 30px 24px}
.a{font-size:29px;font-weight:700;line-height:1.32;letter-spacing:-.015em}
.a b,.x b{font-weight:850;padding:0 2px}
.x{font-size:20px;line-height:1.5;margin-top:16px;padding:12px 16px;border-radius:12px;background:#f5f8fd;border-left:5px solid #999;color:#43566e}
.nightMode .x{background:#182740;color:#aec2da}
.rt{font-family:Georgia,'Times New Roman',serif;font-size:26px;line-height:1.4;margin-top:16px}
.bd{display:inline-block;font-size:17px;font-weight:900;padding:6px 13px;border-radius:10px;margin:0 8px 8px 0}
.c-I{background:#dcfce7;color:#14532d}.c-IIa{background:#fef9c3;color:#713f12}.c-IIb{background:#ffedd5;color:#7c2d12}
.l-B{background:#dbeafe;color:#1e3a8a}.l-C{background:#e0e7ff;color:#3730a3}.l-x{background:#eef2f7;color:#64748b}
.s-New{background:#fee2e2;color:#991b1b}.s-Changed{background:#fef3c7;color:#92400e}.s-Unchanged{background:#eef2f7;color:#43566e}
.src{margin-top:18px;font-size:14px;font-weight:700;color:#7489a3}
@media (max-width:600px){.q{font-size:25px}.a{font-size:23px}.rt{font-size:21px}.x{font-size:17px}.front,.bb{padding-left:20px;padding-right:20px}}
"""

FRONT = """<div class="wrap"><div class="front" style="background:linear-gradient(145deg,{{G1}},{{G2}});color:{{Ink}}">
<div class="tag">{{Topic}}</div><div class="q">{{Question}}</div></div></div>"""
BACK = """<div class="wrap"><div class="front" style="background:linear-gradient(145deg,{{G1}},{{G2}});color:{{Ink}};min-height:0">
<div class="tag">{{Topic}}</div><div class="q" style="font-size:22px;padding:12px 0 4px">{{Question}}</div></div>
<div class="backc" id="answer"><div class="band" style="background:linear-gradient(90deg,{{G1}},{{G2}})"></div><div class="bb">
{{#Badges}}<div>{{Badges}}</div>{{/Badges}}
{{#Verbatim}}<div class="rt">&ldquo;{{Verbatim}}&rdquo;</div>{{/Verbatim}}
{{#Answer}}<div class="a" style="--hl:{{G2}}">{{Answer}}</div>{{/Answer}}
{{#Extra}}<div class="x" style="border-left-color:{{G2}}">{{Extra}}</div>{{/Extra}}
<div class="src">{{Source}}</div></div></div></div>"""

model = genanki.Model(
  1771623401, 'Blood Doctor · MVT flashcard (colour)',
  fields=[{'name':n} for n in ['Question','Answer','Verbatim','Badges','Extra','Source','Topic','G1','G2','Ink','CardID']],
  templates=[{'name':'Card 1','qfmt':FRONT,'afmt':BACK}], css=CSS, sort_field_index=0)

class Note(genanki.Note):
    @property
    def guid(self): return genanki.guid_for('bd-mvt-esvs2025', self.fields[10])

root='MVT · ESVS 2025 flashcards'
decks={}
for i,d in enumerate(DECK):
    decks[d['id']]=genanki.Deck(1771623500+i, f"{root}::{i+1:02d} {d['name']}")

def hl(s,colour):
    # highlighter underline on <b>, readable on light cards
    return s.replace('<b>',f'<b style="background:linear-gradient(transparent 56%,{colour}55 56%)">')

for c in D['cards']:
    n,d=BY[c['d']]
    badges=verb=ans=''
    if c['d']=='rec':
        lvl = '<span class="bd l-x">Level not graded here</span>' if c['lvl']=='—' else f'<span class="bd l-{c["lvl"]}">Level {c["lvl"]}</span>'
        st = 'New in 2025' if c['st']=='New' else c['st']
        badges=f'<span class="bd c-{c["cls"]}">Class {c["cls"]}</span>{lvl}<span class="bd s-{c["st"]}">{st}</span>'
        verb=c['a']
    else:
        ans=hl(c['a'],d['g2'])
    tags=['ESVS2025','MVT',c['d']]+([f"class_{c['cls']}",f"rec_{c['n']}"] if c['d']=='rec' else [])
    decks[c['d']].add_note(Note(model=model, tags=tags, fields=[
        c['q'], ans, verb, badges, hl(c['x'],d['g2']) if c['x'] else '', c['s'], d['name'],
        d['g1'], d['g2'], d['ink'], c['id']]))

out=os.path.join(HERE,'..','mvt-esvs-2025.apkg')
genanki.Package(list(decks.values())).write_to_file(out)
print('wrote',out,'notes:',sum(len(x.notes) for x in decks.values()),'subdecks:',len(decks))
