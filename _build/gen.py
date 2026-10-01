# -*- coding: utf-8 -*-
import html, os
from data import *
from icons import *
OUT = "/mnt/user-data/outputs/hachioji"
E = html.escape

def header(active):
    links = "".join(f'<a href="{h}"{" class=\"active\"" if h==active else ""}>{t}</a>' for h,t in NAV)
    return f'''<header class="site-header">
<div class="wrap">
<div class="brand">
{BRAND_SVG}
<span>{SITE_NAME}<span class="brand-sub">{SITE_SUB}</span></span>
</div>
<nav class="main-nav">
{links}
</nav>
</div>
</header>'''

DISCLAIMER = "当サイトはアフィリエイト（広告）を掲載しており、掲載する広告・リンクを経由した商品購入等によって収益を得る場合があります。広告掲載商品の内容、品質、価格、在庫状況、取引条件等については各広告主・販売元の情報をご確認ください。広告のご利用によって生じたいかなる損害・不利益についても、当サイト運営者は一切の責任を負いかねますので、あらかじめご了承ください。また、当サイトに掲載する観光・特産品・施設情報は作成時点のものであり、内容の正確性・最新性を保証するものではありません。情報に誤りが含まれる場合もございますので、あらかじめご容赦いただくとともに、実際のご利用の際は各施設・自治体の公式情報を必ずご確認ください。"

PRIVACY = f'当サイトが独自に取得・保存する個人情報はありません。「<a href="unei.html">運営者情報・連絡先</a>」ページのフォームからお送りいただいた内容（お名前・メールアドレス・連絡の表題・内容）は、フォーム送信サービス「Formspree」を経由して運営者宛のメールに転送されます。送信の際、IPアドレスやブラウザの種類等の情報がFormspree社によって取得される場合があります。詳細は<a href="https://formspree.io/legal/privacy-policy/" target="_blank" rel="noopener noreferrer">Formspreeのプライバシーポリシー</a>をご確認ください。恐れ入りますが、パスワードやマイナンバーなど機微な情報の送信はお控えください。また、当サイトはWebフォント表示のためGoogle Fonts等の外部サービスに接続しており、その際にアクセス情報が当該サービスに送信される場合があります。加えて、当サイトに掲載するアフィリエイト（広告）のリンクを経由した場合、各広告サービス・提供元によってクッキー等を用いたアクセス情報の取得が行われることがあります。詳細は各サービスが公開するプライバシーポリシーをご確認ください。本ポリシーの内容は、必要に応じて予告なく変更することがあります。'

def footer():
    items = "".join(f'<li><a href="{h}">{t if h!="areas.html" else "地区紹介"}</a></li>' for h,t in NAV)
    return SKYLINE + f'''
<footer class="site-footer">
<div class="wrap">
<div class="footer-grid">
<div>
<h4>{SITE_NAME}について</h4>
<p>東京都八王子市の観光地・特産品・祭り・宿泊情報を、個人の視点でまとめた非公式の情報サイトです。掲載内容は公開情報をもとに作成しており、最新情報は各施設・自治体の公式情報をご確認ください。</p>
</div>
<div>
<h4>サイト内リンク</h4>
<ul>
{items}
</ul>
</div>
<div>
<h4>運営者情報</h4>
<p>サイトの運営者情報・連絡先フォームは専用ページに掲載しています。</p>
<ul>
<li><a href="unei.html">運営者情報・連絡先&rarr;</a></li>
</ul>
</div>
</div>
<div class="disclaimer">
{DISCLAIMER}
</div>
<div class="disclaimer" id="privacy" style="margin-top:14px;">
<strong>プライバシーポリシー</strong><br>
{PRIVACY}
</div>
<div class="copyright"><span id="copyright-text">© {START_YEAR} {SITE_NAME}</span></div>
</div>
</footer>
<script>
(function(){{
var startYear = {START_YEAR};
var currentYear = new Date().getFullYear();
var yearText = currentYear > startYear ? (startYear + '-' + currentYear) : String(startYear);
var el = document.getElementById('copyright-text');
if (el) {{ el.textContent = '\\u00A9 ' + yearText + ' {SITE_NAME}'; }}
}})();
</script>'''

def ad_slot(slot_id, label="広告"):
    """アフィリエイトコード貼り付け枠。<!-- ここから --> 〜 <!-- ここまで --> の間を差し替える"""
    return f'''<div class="ad-slot" data-slot="{slot_id}">
<span class="ad-label">広告</span>
<span class="ad-note">{label}</span>
<!-- ▼ {slot_id}：アフィリエイトのリンクコードをここに貼り付け（a タグには rel="nofollow sponsored noopener" target="_blank" を付ける） -->
<div class="slot-placeholder">広告枠（{slot_id}）</div>
<!-- ▲ {slot_id} ここまで -->
</div>'''

def furusato(block_id, label, slots):
    inner = "\n".join(f'<div class="furusato-slot" data-slot="{s}"><span class="slot-title">返礼品広告 {n}</span>\n<!-- ▼ {s}：ふるさと納税（八王子市）のアフィリエイトコードを貼り付け -->\n<div class="slot-placeholder">広告枠（{s}）</div>\n<!-- ▲ {s} ここまで -->\n</div>' for s,n in slots)
    return f'''<div class="furusato-block" id="{block_id}">
<span class="furusato-label">{label}</span>
<div class="furusato-grid">
{inner}
</div>
</div>'''

def bottom_ad(page_key):
    return f'''<section class="section alt-lavender">
<div class="wrap">
<div class="section-head">
<span class="tag">PR</span>
<h2>広告</h2>
</div>
<div class="ad-row">
{ad_slot("ad-"+page_key+"-1","広告 1")}
</div>
</div>
</section>'''

BANNER_KIND={'map.html':'map','matsuri.html':'matsuri','areas.html':'areas','shukuhaku.html':'shukuhaku','unei.html':'unei'}
def page(fname, title, desc, active, body):
    if fname in BANNER_KIND: body = banner(BANNER_KIND[fname]) + '\n' + body
    canonical = SITE_URL + ("" if fname=="index.html" else fname)
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="stylesheet" href="style.css">
</head>
<body>
{header(active)}
{body}
{footer()}
</body>
</html>
'''

def head(tag, h2, p=""):
    return f'<div class="section-head">\n<span class="tag">{tag}</span>\n<h2>{h2}</h2>\n{ORN}\n' + (f'<p>{p}</p>\n' if p else '') + '</div>'

# ---------------- index ----------------
def build_index():
    cards = "\n".join(f'<div class="card">\n{icon_svg(SPOT_ICON[s[0]])}\n<span class="place">{E(s[1])}</span>\n<h3>{E(s[0])}</h3>\n<p>{E(s[3])}</p>\n</div>' for i,s in enumerate(SPOTS))
    tok = "\n".join(f'<div class="card">\n{icon_svg(TOKUSAN_ICON[n])}\n<h3>{E(n)}</h3>\n<p>{E(d)}</p>\n</div>' for n,d in TOKUSAN)
    gm = "\n".join('<div class="card">\n%s\n<h3>%s</h3>\n<p>%s</p>\n</div>' % (icon_svg(GOURMET_ICON[a]), E(a), "<br>\n".join(f"<strong>{E(n)}</strong>：{E(d)}" for n,d in items)) for a,items in GOURMET)
    hero_svg = HERO
    body = f'''<section class="hero">
<div class="wrap">
<div class="hero-copy">
<span class="eyebrow">都心から約50分、山と歴史のまち</span>
<h1>いつもの週末を、<br>山のほうへ。</h1>
<p>東京都の西部に広がる八王子市。標高599mの高尾山、戦国の山城・八王子城跡、織物で栄えた「桑都」の街並み——都心から近いのに、驚くほど多彩な旅が待っています。</p>
<a href="#kanko" class="btn">観光地をみる</a>
<a href="matsuri.html" class="btn btn-outline">祭り・行事をみる</a>
</div>
<div class="hero-art">
{hero_svg}
</div>
</div>
</section>

<!-- ===================== 観光地 ===================== -->
<section class="section" id="kanko">
<div class="wrap">
{head("Sightseeing","まず訪れたい、八王子の観光地","山、城跡、美術館、桜の名所——市内に点在する定番スポットをご紹介します。それぞれの位置関係は<a href=\"map.html\" style=\"text-decoration:underline;\">観光マップ</a>でご覧いただけます。")}
<div class="grid">
{cards}
</div>
<!-- ふるさと納税広告枠：観光地セクション -->
{furusato("furusato-kanko","ふるさと納税で応援する（八王子市の返礼品）",[("furusato-1",1),("furusato-2",2)])}
</div>
</section>

<!-- ===================== 特産品 ===================== -->
<section class="section alt-cream" id="tokusan">
<div class="wrap">
{head("Local Specialties","八王子でしか出会えない、特産品とご当地グルメ","宿場町・織物の町として栄えた歴史と、高尾山の参道文化が生んだ味をご紹介します。")}
<div class="grid">
{tok}
</div>
<!-- ふるさと納税広告枠：特産品セクション -->
{furusato("furusato-tokusan","ふるさと納税で取り寄せる（八王子市の特産品）",[("furusato-3",3)])}
</div>
</section>

<!-- ===================== 飲食店 ===================== -->
<section class="section" id="gourmet">
<div class="wrap">
{head("Restaurants","エリアごとに味わう、八王子のグルメ","高尾・八王子駅周辺・南大沢・恩方——それぞれの街で異なる味に出会えます。店名は代表的な例で、営業日・メニューは事前にご確認ください。")}
<div class="grid">
{gm}
</div>
</div>
</section>

{bottom_ad("index")}'''
    return page("index.html", f"{SITE_NAME}｜東京都八王子市 観光・特産品・グルメ案内",
        "東京都八王子市の観光地・特産品・飲食店・祭り・宿泊情報をまとめた非公式ファンサイト「はちおうじ往来」。高尾山、八王子城跡、八王子まつりなど、八王子の魅力をご紹介します。","index.html",body)

# ---------------- map ----------------
def _g(k,x,y,sc): return f'<g transform="translate({x} {y}) scale({sc})">{ICONS[k]}</g>'
def build_map():
    pts = ""
    for i,s in enumerate(SPOTS,1):
        x,y = s[5]
        pts += f'<g><circle cx="{x}" cy="{y}" r="11" fill="#B14C5D" stroke="#fff" stroke-width="2"/><text x="{x}" y="{y+4}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{i}</text></g>\n'
    deco = (_g("takao",24,300,0.6)+_g("jinba",16,150,0.9)+_g("sakura",186,292,0.7)+_g("ginkgo",296,252,0.6)+_g("ginkgo",212,110,0.6)
            +'<path d="M150 330 q60 -40 120 -20 q60 20 140 -40" stroke="#6FB1D6" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/><text x="300" y="318" font-size="11" fill="#3E7CA6" font-style="italic">浅川</text>'
            +'<g transform="translate(440 40)"><circle r="14" fill="#fff" stroke="#2F6690"/><path d="M0 -10 L4 4 L0 1 L-4 4Z" fill="#B14C5D"/><text y="26" font-size="10" text-anchor="middle" fill="#2F6690">N</text></g>')
    svg = f'''<svg class="map-svg" viewBox="0 0 480 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="八王子市の主な観光スポットの位置関係を示した略図">
<rect width="480" height="380" rx="14" fill="#EAF4E7"/>
<path d="M30 200 L70 130 L150 110 L210 60 L320 50 L400 90 L450 170 L420 250 L360 300 L260 330 L160 340 L80 320 L40 260 Z" fill="#fff" stroke="#2F6690" stroke-width="2.5" stroke-linejoin="round"/>
<text x="270" y="200" font-size="13" fill="#204A67" text-anchor="middle" font-weight="700">中心市街地</text>
<text x="100" y="330" font-size="12" fill="#204A67" text-anchor="middle">高尾</text>
<text x="390" y="230" font-size="12" fill="#204A67" text-anchor="middle">南大沢・由木</text>
<text x="60" y="220" font-size="12" fill="#204A67" text-anchor="middle">恩方・陣馬</text>
<text x="245" y="80" font-size="12" fill="#204A67" text-anchor="middle">滝山・北部</text>
{deco}
{pts}
<text x="240" y="366" font-size="11" fill="#555" text-anchor="middle">※位置関係のイメージ略図です（縮尺・形状は正確ではありません）</text>
</svg>'''
    lst = "\n".join(f'<li><span class="num">{i}</span><div><strong>{E(s[0])}</strong><span class="place">{E(s[1])}</span><br>{E(s[2])}<br><span class="access">アクセス：{E(s[4])}</span></div></li>' for i,s in enumerate(SPOTS,1))
    body = f'''<section class="section">
<div class="wrap">
{head("Map","八王子 観光マップ","トップページで紹介した観光地の位置関係を、略図で確認できます。番号は下のスポット一覧と対応しています。")}
<div class="map-wrap">
{svg}
</div>
<ol class="spot-list">
{lst}
</ol>
<p class="note">詳しい道順は、<a href="https://www.google.com/maps/search/%E5%85%AB%E7%8E%8B%E5%AD%90%E5%B8%82+%E8%A6%B3%E5%85%89" target="_blank" rel="noopener noreferrer">Googleマップ</a>などの地図アプリでご確認ください。各エリアの特徴は<a href="areas.html">地区紹介</a>に、宿泊は<a href="shukuhaku.html">宿泊施設</a>にまとめています。</p>
</div>
</section>
{bottom_ad("map")}'''
    return page("map.html", f"観光マップ｜{SITE_NAME}","東京都八王子市の主な観光スポットの位置関係を略図で紹介。高尾山、八王子城跡、陣馬山、滝山城跡など。","map.html",body)

# ---------------- matsuri ----------------
def build_matsuri():
    rows = "\n".join(f'<tr><th>{icon_svg(EVENT_ICONS[k],'icon sm')}<br>{E(m)}</th><td><strong>{E(n)}</strong><br><span class="place">{E(p)}</span></td><td>{E(d)}</td></tr>' for k,(m,n,p,d) in enumerate(EVENTS))
    body = f'''<section class="section">
<div class="wrap">
{head("Festivals","八王子の祭り・年間行事","山伏の火渡りから山車の巡行まで、季節ごとの行事をカレンダー形式でまとめました。")}
<div class="table-wrap">
<table class="event-table">
<thead><tr><th>時期</th><th>行事名・場所</th><th>内容</th></tr></thead>
<tbody>
{rows}
</tbody>
</table>
</div>
<p class="note">開催日・内容は年によって変わることがあります。お出かけ前に、<a href="https://www.city.hachioji.tokyo.jp/" target="_blank" rel="noopener noreferrer">八王子市公式サイト</a>や主催者の情報をご確認ください。会場の位置は<a href="map.html">観光マップ</a>、エリアの特徴は<a href="areas.html">地区紹介</a>をご覧ください。</p>
</div>
</section>
{bottom_ad("matsuri")}'''
    return page("matsuri.html", f"祭り・行事｜{SITE_NAME}","東京都八王子市の祭り・年間行事一覧。高尾山火渡り祭、八王子まつり、八王子いちょう祭り、高尾山の紅葉など。","matsuri.html",body)

# ---------------- areas ----------------
def build_areas():
    cards = "\n".join(f'<div class="card">\n{icon_svg(AREA_ICON[a[0]])}\n<span class="place">{E(a[1])}</span>\n<h3>{E(a[0])}</h3>\n<p>{E(a[2])}</p>\n<ul class="tags">' + "".join(f"<li>{E(t)}</li>" for t in a[3]) + '</ul>\n</div>' for a in AREAS)
    body = f'''<section class="section">
<div class="wrap">
{head("Areas","地区紹介","八王子市は東西に長い市域に、個性の異なる街が広がっています。エリアごとの特徴をご紹介します。")}
<div class="grid">
{cards}
</div>
<p class="note">各エリアの観光地は<a href="index.html#kanko">トップページ</a>・<a href="map.html">観光マップ</a>、泊まる場所は<a href="shukuhaku.html">宿泊施設</a>もあわせてご覧ください。</p>
</div>
</section>
{bottom_ad("areas")}'''
    return page("areas.html", f"地区紹介｜{SITE_NAME}","東京都八王子市のエリア別ガイド。中心市街地、高尾、元八王子・川口、恩方・陣馬、南大沢・由木、滝山・北部の特徴を紹介。","areas.html",body)

# ---------------- shukuhaku ----------------
def build_shukuhaku():
    cards = "\n".join(f'<div class="card">\n{icon_svg(HOTEL_ICON[n])}\n<span class="place">{E(a)}</span>\n<h3>{E(n)}</h3>\n<p><span class="access">場所：{E(loc)}</span><br>{E(d)}</p>\n</div>' for a,n,loc,d in HOTELS)
    body = f'''<section class="section">
<div class="wrap">
{head("Stay","八王子の宿泊施設","早朝から高尾山へ向かう、買い物と組み合わせる——目的に合わせて、エリアで宿を選べます。")}
<div class="grid">
{cards}
</div>
<p class="note">施設名・設備・料金・空室状況は変更される場合があります。ご予約の際は各施設・予約サイトの最新情報をご確認ください。エリアごとの雰囲気は<a href="areas.html">地区紹介</a>をご覧ください。</p>
<div class="furusato-block" id="travel-ad">
<span class="furusato-label">宿泊予約サイトで探す（PR）</span>
<div class="furusato-grid">
{ad_slot("ad-shukuhaku-travel","宿泊予約サイト")}
</div>
</div>
</div>
</section>
{bottom_ad("shukuhaku")}'''
    return page("shukuhaku.html", f"宿泊施設｜{SITE_NAME}","東京都八王子市の宿泊エリアガイド。八王子駅周辺、高尾、南大沢のホテル・温泉施設を紹介。","shukuhaku.html",body)

# ---------------- unei ----------------
def build_unei():
    body = f'''<section class="section">
<div class="wrap narrow unei-box">
{head("About","運営者情報・連絡先")}
<table class="info-table">
<tr><th>サイト名</th><td>{SITE_NAME}（{SITE_SUB}）</td></tr>
<tr><th>運営者</th><td>（運営者名・ハンドルネームを入力）</td></tr>
<tr><th>サイトの目的</th><td>東京都八王子市の観光地・特産品・祭り・宿泊情報を、個人の視点でまとめて紹介すること。</td></tr>
<tr><th>広告について</th><td>当サイトはアフィリエイトプログラム（広告）に参加しており、広告リンク経由の購入・予約等で収益を得る場合があります。広告であることは「広告」「PR」の表示で明記しています。</td></tr>
<tr><th>免責事項</th><td>掲載情報は作成時点のものであり、正確性・最新性を保証するものではありません。実際のご利用の際は、各施設・自治体の公式情報を必ずご確認ください。当サイトの情報を利用して生じた損害について、運営者は責任を負いかねます。</td></tr>
<tr><th>非公式について</th><td>当サイトは八王子市および各施設・団体とは関係のない、個人運営の非公式サイトです。</td></tr>
<tr><th>リンク・転載</th><td>リンクは自由です。文章・画像・イラストの無断転載はお断りします。</td></tr>
</table>

<h3 class="sub-h" id="contact">連絡先フォーム</h3>
<p>ご連絡は下記のフォームをご利用ください。</p>
<form class="contact-form" action="{FORMSPREE}" method="POST">
<input type="hidden" name="site" value="{SITE_NAME}">
<label>お名前<input type="text" name="name" autocomplete="name"></label>
<label>あなたのメールアドレス<input type="email" name="email" required autocomplete="email"></label>
<label>連絡の表題（○○について）<input type="text" name="subject" required placeholder="例：掲載内容について"></label>
<label>内容<textarea name="message" rows="6" required></textarea></label>
<p class="form-note">この連絡を利用しての各種の勧誘はご遠慮ください。</p>
<button type="submit" class="btn">送信する</button>
</form>
<p class="note">送信内容の取り扱いは、<a href="#privacy-unei">プライバシーポリシー</a>をご覧ください。</p>

<h3 class="sub-h" id="privacy-unei">プライバシーポリシー</h3>
<p>{PRIVACY}</p>

<h3 class="sub-h">広告（アフィリエイト）に関する表記</h3>
<p>{DISCLAIMER}</p>
<p class="note"><a href="index.html">&larr; トップページへ戻る</a></p>
</div>
</section>'''
    return page("unei.html", f"運営者情報・連絡先｜{SITE_NAME}","「はちおうじ往来」の運営者情報、連絡先フォーム、プライバシーポリシー、広告（アフィリエイト）に関する表記。","unei.html",body)

PAGES = {"index.html":build_index,"map.html":build_map,"matsuri.html":build_matsuri,
         "areas.html":build_areas,"shukuhaku.html":build_shukuhaku,"unei.html":build_unei}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f,fn in PAGES.items():
        open(os.path.join(OUT,f),"w",encoding="utf-8").write(fn())
    urls = "".join(f"<url><loc>{SITE_URL}{'' if f=='index.html' else f}</loc></url>\n" for f in PAGES)
    open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    open(os.path.join(OUT,"favicon.svg"),"w").write(FAVICON)
    print("generated", list(PAGES))
