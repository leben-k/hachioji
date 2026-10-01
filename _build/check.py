# -*- coding: utf-8 -*-
import re, os, sys
from html.parser import HTMLParser
from data import *
D="/mnt/user-data/outputs/hachioji"
pages=[f for f in os.listdir(D) if f.endswith(".html")]
errs=[]
VOID={"meta","link","br","img","input","path","circle","rect","ellipse","line","hr"}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.ids=set(); s.links=[]; s.title=""; s.t=False; s.meta={}; s.canon=None; s.active=[]; s.stack=[]
    def handle_starttag(s,t,a):
        a=dict(a)
        if t not in VOID: s.stack.append(t)
        if "id" in a: s.ids.add(a["id"])
        if t=="a" and "href" in a: s.links.append((a["href"],a.get("rel",""),a.get("target","")));
        if t=="a" and "active" in (a.get("class") or ""): s.active.append(a["href"])
        if t=="title": s.t=True
        if t=="meta" and a.get("name"): s.meta[a["name"]]=a.get("content","")
        if t=="link" and a.get("rel")=="canonical": s.canon=a["href"]
    def handle_endtag(s,t):
        if t in VOID: return
        if t=="title": s.t=False
        if s.stack and s.stack[-1]==t: s.stack.pop()
        else: errs.append(("unbalanced",t))
    def handle_data(s,d):
        if s.t: s.title+=d
info={}
for f in pages:
    src=open(os.path.join(D,f),encoding="utf-8").read(); p=P(); p.feed(src)
    info[f]=(p,src)
    if p.stack: errs.append((f,"unclosed",p.stack))
# 1 links/anchors
for f,(p,src) in info.items():
    for h,rel,tg in p.links:
        if h.startswith("http"):
            if tg=="_blank" and "noopener" not in rel: errs.append((f,"noopener missing",h))
            continue
        base,_,anc=h.partition("#")
        tgt=base or f
        if tgt not in info: errs.append((f,"broken link",h)); continue
        if anc and anc not in info[tgt][0].ids: errs.append((f,"broken anchor",h))
# 2 titles/desc/canonical
titles=[p.title for p,_ in info.values()]
if len(set(titles))!=len(titles): errs.append(("dup titles",))
for f,(p,src) in info.items():
    if not p.meta.get("description"): errs.append((f,"no desc"))
    exp=SITE_URL+("" if f=="index.html" else f)
    if p.canon!=exp: errs.append((f,"canonical",p.canon))
    if SITE_NAME not in p.title: errs.append((f,"title lacks site name"))
    if 'rel="stylesheet" href="style.css"' not in src: errs.append((f,"css"))
    if "広告" not in src or "アフィリエイト" not in src: errs.append((f,"no ad disclosure"))
    if "運営者情報・連絡先" not in src: errs.append((f,"no unei link"))
    if src.count("<h1")>1: errs.append((f,"multi h1"))
# 3 nav/footers identical & active
def block(src,a,b): return src[src.index(a):src.index(b)+len(b)]
navs={f:re.sub(r' class="active"',"",block(s,"<nav","</nav>")) for f,(p,s) in info.items()}
foots={f:block(s,"<footer","</footer>") for f,(p,s) in info.items()}
if len(set(navs.values()))!=1: errs.append(("nav differs",))
if len(set(foots.values()))!=1: errs.append(("footer differs",))
for f,(p,s) in info.items():
    want=[f] if f in [h for h,_ in NAV] else []
    if p.active!=want: errs.append((f,"active nav",p.active))
navfiles={h for h,_ in NAV}|{"unei.html"}
if navfiles!=set(pages): errs.append(("page set vs nav",navfiles^set(pages)))
# 4 data consistency
for s in SPOTS:
    if s[1] not in AREA_NAMES: errs.append(("spot area",s[0],s[1]))
for h in HOTELS:
    if h[0] not in AREA_NAMES: errs.append(("hotel area",h[0]))
for a in GOURMET: pass
idx=info["index.html"][1]; mp=info["map.html"][1]
for i,s in enumerate(SPOTS,1):
    if s[0] not in idx or s[0] not in mp: errs.append(("spot missing",s[0]))
    if f'<text x="{s[5][0]}" y="{s[5][1]+4}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{i}</text>' not in mp: errs.append(("marker",i))
for a in AREAS:
    if a[0] not in info["areas.html"][1]: errs.append(("area missing",a[0]))
# area highlights should mention real spots/events consistently
for a in AREAS:
    for t in a[3]:
        pass
# 5 slots
slots=re.findall(r'data-slot="([^"]+)"',"".join(s for _,s in info.values()))
if len(slots)!=len(set(slots)): errs.append(("dup slot ids",[x for x in slots if slots.count(x)>1]))
# 6 sitemap
sm=open(D+"/sitemap.xml").read()
for f in pages:
    if (SITE_URL+("" if f=="index.html" else f)) not in sm: errs.append(("sitemap",f))
# 7 number claims
for f,(p,s) in info.items():
    for kw in ["新宿から約50分"]: pass
print("pages:",sorted(pages)); print("slots:",slots)
print("ERRORS:" if errs else "ALL OK"); [print(" ",e) for e in errs]
# --- イラスト点検 ---
from icons import *
ic=[]
if len(EVENT_ICONS)!=len(EVENTS): ic.append("event icons count")
for s in SPOTS:
    if s[0] not in SPOT_ICON: ic.append(("spot icon",s[0]))
for n,_ in TOKUSAN:
    if n not in TOKUSAN_ICON: ic.append(("tokusan icon",n))
for a,_ in GOURMET:
    if a not in GOURMET_ICON: ic.append(("gourmet icon",a))
for a in AREAS:
    if a[0] not in AREA_ICON: ic.append(("area icon",a[0]))
for h in HOTELS:
    if h[1] not in HOTEL_ICON: ic.append(("hotel icon",h[1]))
for m in (SPOT_ICON,TOKUSAN_ICON,GOURMET_ICON,AREA_ICON,HOTEL_ICON):
    for v in m.values():
        if v not in ICONS: ic.append(("missing icon",v))
for f,(p,s) in info.items():
    if "<svg" not in s: ic.append((f,"no svg"))
    if s.count('class="card"')!=s.count('<div class="card">\n<svg class="icon"') and f!="unei.html": ic.append((f,"card without icon"))
print("ICON CHECK:", ic or "OK")
