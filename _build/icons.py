# -*- coding: utf-8 -*-
# 八王子オリジナルのイラスト集（56x56 viewBox）
def _hotel():
    w=""
    for y in (15,25,35):
        for x in (14,25,36):
            w+=f'<rect x="{x}" y="{y}" width="6" height="6" fill="#F7E1A8"/>'
    return '<rect x="10" y="10" width="36" height="40" fill="#fff" stroke="#204A67" stroke-width="2"/>'+w+'<rect x="23" y="42" width="10" height="8" fill="#8B5E3C"/><rect x="16" y="3" width="24" height="6" rx="1" fill="#B14C5D"/>'
def _city():
    w=""
    for x,y in [(9,26),(14,26),(9,33),(14,33),(25,16),(30,16),(25,23),(30,23),(25,30),(30,30),(41,30),(45,30),(41,37),(45,37)]:
        w+=f'<rect x="{x}" y="{y}" width="3" height="4" fill="#fff"/>'
    return '<rect x="6" y="22" width="14" height="28" fill="#6E8CA6"/><rect x="22" y="12" width="14" height="38" fill="#3E7CA6"/><rect x="38" y="26" width="12" height="24" fill="#8FB0C8"/>'+w+'<path d="M2 50 H54" stroke="#204A67" stroke-width="2"/>'

ICONS = {
"takao":'<path d="M2 50 L22 16 L32 31 L39 23 L54 50Z" fill="#3C7A52"/><path d="M2 50 L22 16 L29 27 L19 50Z" fill="#2B5E3E"/><path d="M22 16V7" stroke="#204A67" stroke-width="1.6"/><path d="M22 7L31 9.5L22 12Z" fill="#B14C5D"/><path d="M5 45 L35 27" stroke="#6b6b6b" stroke-width="1.2"/><rect x="17" y="34" width="9" height="6" rx="1.2" fill="#C1892E" transform="rotate(-30 21.5 37)"/><circle cx="46" cy="10" r="5" fill="#E8B923"/>',
"yakuoin":'<rect x="9" y="30" width="38" height="18" fill="#fff" stroke="#8B5E3C" stroke-width="1.5"/><rect x="13" y="30" width="3" height="18" fill="#B14C5D"/><rect x="26.5" y="30" width="3" height="18" fill="#B14C5D"/><rect x="40" y="30" width="3" height="18" fill="#B14C5D"/><path d="M3 31 Q28 25 53 31 L45 19 L11 19Z" fill="#4A5560"/><path d="M15 19 Q28 13 41 19 L37 10 L19 10Z" fill="#5A6672"/><rect x="22" y="36" width="12" height="12" fill="#8B5E3C"/><circle cx="28" cy="6" r="2" fill="#C1892E"/>',
"joseki":'<path d="M5 50 L9 27 H47 L51 50Z" fill="#9AA3A8"/><path d="M8 34 H48 M10 41 H46 M20 27 V34 M34 27 V34 M14 34 V41 M28 34 V41 M40 34 V41 M14 41 V50 M40 41 V50" stroke="#6E777C" stroke-width="1"/><path d="M22 50 V42 Q28 34 34 42 V50Z" fill="#3A3F44"/><path d="M44 27 V8" stroke="#8B5E3C" stroke-width="2"/><path d="M44 8 L54 11 L44 15Z" fill="#B14C5D"/>',
"jinba":'<path d="M0 50 Q28 10 56 50Z" fill="#7FB37A"/><path d="M0 50 Q20 22 34 50Z" fill="#5E9E6E" opacity=".6"/><ellipse cx="27" cy="25" rx="7" ry="3.6" fill="#fff" stroke="#8a97a0"/><path d="M32 23 L36 15 L39 16 L37 22Z" fill="#fff" stroke="#8a97a0"/><path d="M22 28 V34 M25 28.5 V34 M30 28.5 V34 M33 28 V34" stroke="#8a97a0" stroke-width="1.6"/><circle cx="46" cy="12" r="5" fill="#E8B923"/>',
"museum599":'<path d="M5 24 L28 10 L51 24Z" fill="#8B5E3C"/><rect x="9" y="25" width="38" height="3" fill="#C9B79C"/><rect x="11" y="28" width="5" height="16" fill="#fff" stroke="#8B5E3C"/><rect x="20" y="28" width="5" height="16" fill="#fff" stroke="#8B5E3C"/><rect x="31" y="28" width="5" height="16" fill="#fff" stroke="#8B5E3C"/><rect x="40" y="28" width="5" height="16" fill="#fff" stroke="#8B5E3C"/><rect x="7" y="44" width="42" height="5" fill="#C9B79C"/><path d="M28 14 q6 2 4 8 q-6 -1 -4 -8Z" fill="#5E9E6E"/>',
"sakura":'<path d="M28 50 V30 M28 38 L19 30 M28 34 L37 27" stroke="#8B5E3C" stroke-width="3" stroke-linecap="round" fill="none"/><circle cx="18" cy="22" r="9" fill="#F7C6D0"/><circle cx="30" cy="15" r="10" fill="#F4B6C2"/><circle cx="40" cy="24" r="8" fill="#F7C6D0"/><circle cx="28" cy="26" r="7" fill="#F4B6C2"/><circle cx="12" cy="44" r="2" fill="#F4B6C2"/><circle cx="44" cy="46" r="2" fill="#F4B6C2"/><circle cx="36" cy="50" r="1.6" fill="#F4B6C2"/>',
"artmuseum":'<rect x="6" y="8" width="44" height="32" rx="2" fill="#C1892E"/><rect x="10" y="12" width="36" height="24" fill="#BFE0F0"/><path d="M10 36 L22 22 L30 30 L36 24 L46 36Z" fill="#5E9E6E"/><circle cx="38" cy="18" r="3.5" fill="#E8B923"/><path d="M16 40 L12 52 M40 40 L44 52 M28 40 V52" stroke="#8B5E3C" stroke-width="2.5"/>',
"takiyama":'<path d="M0 44 L16 22 L30 44Z" fill="#7FB37A"/><path d="M20 44 L36 26 L56 44Z" fill="#5E9E6E"/><path d="M0 44 H56 V52 H0Z" fill="#6FB1D6"/><path d="M4 48 q6 -3 12 0 q6 3 12 0 q6 -3 12 0 q6 3 12 0" stroke="#fff" stroke-width="1.2" fill="none"/><path d="M16 22V8" stroke="#8B5E3C" stroke-width="2"/><path d="M16 8 L26 11 L16 15Z" fill="#B14C5D"/>',
"ramen":'<path d="M6 28 H50 Q48 48 28 48 Q8 48 6 28Z" fill="#B14C5D"/><ellipse cx="28" cy="28" rx="22" ry="5.5" fill="#B5702E"/><path d="M12 28 q4 -4 8 0 t8 0 t8 0 t8 0" stroke="#F3DFA2" stroke-width="2" fill="none"/><circle cx="20" cy="27" r="1.2" fill="#fff"/><circle cx="26" cy="29" r="1.2" fill="#fff"/><circle cx="33" cy="27" r="1.2" fill="#fff"/><circle cx="38" cy="29" r="1.2" fill="#fff"/><circle cx="31" cy="26" r="3.6" fill="#fff" stroke="#E58EA0"/><path d="M42 6 L30 26 M46 8 L34 27" stroke="#8B5E3C" stroke-width="1.8" stroke-linecap="round"/><path d="M16 14 q-3 -4 0 -8 M24 14 q-3 -4 0 -8" stroke="#8a97a0" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
"napolitan":'<ellipse cx="28" cy="40" rx="24" ry="9" fill="#fff" stroke="#8a97a0" stroke-width="1.5"/><path d="M10 38 Q12 18 28 18 Q44 18 46 38 Q28 46 10 38Z" fill="#D9541E"/><path d="M16 30 q6 -6 12 0 M24 26 q6 -6 12 0 M20 35 q8 -5 16 0" stroke="#F08A4B" stroke-width="2" fill="none"/><rect x="22" y="22" width="4" height="4" fill="#5E9E6E"/><rect x="33" y="29" width="4" height="4" fill="#5E9E6E"/><circle cx="18" cy="34" r="2.5" fill="#F3D27A"/><path d="M48 6 V26 M45 6 V14 M51 6 V14" stroke="#8a97a0" stroke-width="1.6"/>',
"soba":'<path d="M6 26 H50 Q48 48 28 48 Q8 48 6 26Z" fill="#8B5E3C"/><ellipse cx="28" cy="26" rx="22" ry="5" fill="#D9C9A6"/><path d="M10 26 q18 -7 36 0 M12 24 q16 -5 32 0" stroke="#A89878" stroke-width="1.2" fill="none"/><path d="M14 27 Q28 10 42 27Z" fill="#fff" stroke="#e6e0d0"/><circle cx="26" cy="20" r="1.4" fill="#5E9E6E"/><circle cx="31" cy="22" r="1.4" fill="#5E9E6E"/><rect x="24" y="12" width="8" height="6" fill="#1f3a33"/>',
"tengu":'<circle cx="28" cy="30" r="19" fill="#C8453B"/><path d="M10 20 Q28 2 46 20 Q38 12 28 12 Q18 12 10 20Z" fill="#fff"/><path d="M14 24 L24 28 M42 24 L32 28" stroke="#3a1a16" stroke-width="3" stroke-linecap="round"/><circle cx="20" cy="31" r="3" fill="#fff"/><circle cx="36" cy="31" r="3" fill="#fff"/><circle cx="20" cy="31" r="1.3" fill="#222"/><circle cx="36" cy="31" r="1.3" fill="#222"/><path d="M28 32 L48 38 L28 44Z" fill="#E8634F"/><path d="M20 47 Q28 50 36 47" stroke="#3a1a16" stroke-width="2" fill="none" stroke-linecap="round"/>',
"tamaori":'<rect x="8" y="10" width="40" height="34" rx="2" fill="#F7F1E2" stroke="#8B5E3C"/><path d="M14 10 V44 M22 10 V44 M30 10 V44 M38 10 V44" stroke="#B14C5D" stroke-width="3"/><path d="M8 18 H48 M8 28 H48 M8 38 H48" stroke="#204A67" stroke-width="3" opacity=".75"/><path d="M18 14 H26 M34 24 H42 M18 34 H26" stroke="#E8B923" stroke-width="3"/><path d="M6 52 H50" stroke="#8B5E3C" stroke-width="3" stroke-linecap="round"/>',
"shojin":'<path d="M4 26 H28 Q27 42 16 42 Q5 42 4 26Z" fill="#B14C5D"/><ellipse cx="16" cy="26" rx="12" ry="3" fill="#F7E1A8"/><path d="M28 30 H52 Q51 46 40 46 Q29 46 28 30Z" fill="#2B5E3E"/><ellipse cx="40" cy="30" rx="12" ry="3" fill="#E89B3C"/><circle cx="13" cy="25" r="2.5" fill="#E89B3C"/><circle cx="19" cy="24.5" r="2" fill="#5E9E6E"/><circle cx="37" cy="29" r="2" fill="#fff"/><path d="M8 16 q3 -6 0 -10 M20 16 q3 -6 0 -10" stroke="#8a97a0" stroke-width="1.5" fill="none"/>',
"train":'<rect x="8" y="14" width="40" height="28" rx="8" fill="#fff" stroke="#204A67" stroke-width="2"/><rect x="8" y="30" width="40" height="5" fill="#B14C5D"/><rect x="13" y="19" width="12" height="9" rx="2" fill="#BFE0F0"/><rect x="31" y="19" width="12" height="9" rx="2" fill="#BFE0F0"/><circle cx="18" cy="38" r="2" fill="#F7E1A8"/><circle cx="38" cy="38" r="2" fill="#F7E1A8"/><path d="M12 46 L8 52 M44 46 L48 52 M6 52 H50" stroke="#555" stroke-width="2"/>',
"bag":'<path d="M10 20 H46 L44 50 H12Z" fill="#B14C5D"/><path d="M20 20 V15 Q28 6 36 15 V20" stroke="#8B2F3F" stroke-width="3" fill="none"/><circle cx="28" cy="34" r="6" fill="#fff" opacity=".9"/><path d="M25 34 L27.5 36.5 L31.5 31.5" stroke="#B14C5D" stroke-width="2" fill="none"/>',
"farm":'<path d="M8 50 L8 30 L28 14 L48 30 L48 50Z" fill="#fff" stroke="#8B5E3C" stroke-width="2"/><path d="M4 32 L28 11 L52 32" stroke="#B5702E" stroke-width="5" fill="none" stroke-linejoin="round"/><rect x="22" y="36" width="12" height="14" fill="#8B5E3C"/><rect x="11" y="34" width="8" height="7" fill="#BFE0F0"/>',
"fire":'<path d="M28 4 Q44 20 42 34 Q42 48 28 50 Q14 48 14 34 Q14 24 22 18 Q22 28 28 28 Q34 20 28 4Z" fill="#E8563A"/><path d="M28 22 Q38 32 36 40 Q36 48 28 48 Q20 48 20 40 Q20 34 28 22Z" fill="#F5A623"/><path d="M28 34 Q33 38 32 43 Q32 47 28 47 Q24 47 24 43 Q24 38 28 34Z" fill="#FCE38A"/>',
"beer":'<rect x="10" y="18" width="26" height="30" rx="3" fill="#F5C242" stroke="#B5802E" stroke-width="1.5"/><path d="M36 24 H44 Q50 24 50 31 V34 Q50 41 44 41 H36" fill="none" stroke="#B5802E" stroke-width="3"/><path d="M8 18 Q8 8 16 10 Q20 4 26 9 Q34 6 38 14 Q40 18 36 18Z" fill="#fff" stroke="#dde3e8"/><path d="M16 26 V42 M23 26 V42 M30 26 V42" stroke="#fff" stroke-width="1.5" opacity=".6"/>',
"dashi":'<rect x="10" y="36" width="36" height="8" fill="#8B5E3C"/><rect x="14" y="22" width="28" height="14" fill="#B14C5D"/><path d="M8 22 H48 L42 14 H14Z" fill="#4A5560"/><path d="M12 14 L28 4 L44 14Z" fill="#6A7580"/><circle cx="20" cy="29" r="3" fill="#F7E1A8"/><circle cx="28" cy="29" r="3" fill="#F7E1A8"/><circle cx="36" cy="29" r="3" fill="#F7E1A8"/><circle cx="16" cy="48" r="5" fill="#3a2a1f"/><circle cx="40" cy="48" r="5" fill="#3a2a1f"/><circle cx="16" cy="48" r="2" fill="#C1892E"/><circle cx="40" cy="48" r="2" fill="#C1892E"/>',
"maple":'<path d="M28 6 L32 16 L40 12 L38 22 L48 22 L41 30 L46 36 L35 36 L36 44 L28 40 L20 44 L21 36 L10 36 L15 30 L8 22 L18 22 L16 12 L24 16Z" fill="#D9472B"/><path d="M28 40 V52" stroke="#8B3A1F" stroke-width="3"/>',
"ginkgo":'<path d="M28 50 V33" stroke="#8B6A2F" stroke-width="3" stroke-linecap="round"/><path d="M28 33 C12 34 5 20 9 11 C15 17 22 15 28 11 C34 15 41 17 47 11 C51 20 44 34 28 33Z" fill="#E8B923"/><path d="M28 33 V16 M28 33 L16 18 M28 33 L40 18" stroke="#C1892E" stroke-width="1" fill="none"/>',
"sunrise":'<circle cx="28" cy="34" r="14" fill="#F08A3C"/><path d="M28 6 V14 M8 14 L14 20 M48 14 L42 20 M2 30 H10 M46 30 H54" stroke="#F5A623" stroke-width="3" stroke-linecap="round"/><path d="M0 50 L14 32 L24 44 L34 30 L56 50Z" fill="#2B5E3E"/>',
"city":_city(),
"mall":'<rect x="6" y="18" width="44" height="30" fill="#BFE0F0" stroke="#3E7CA6" stroke-width="2"/><path d="M6 28 H50 M6 38 H50 M17 18 V48 M28 18 V48 M39 18 V48" stroke="#3E7CA6"/><rect x="4" y="12" width="48" height="6" fill="#3E7CA6"/>',
"hotel":_hotel(),
"bed":'<rect x="6" y="36" width="44" height="8" fill="#204A67"/><rect x="6" y="22" width="4" height="26" fill="#8B5E3C"/><rect x="46" y="30" width="4" height="18" fill="#8B5E3C"/><rect x="10" y="28" width="36" height="9" rx="2" fill="#fff" stroke="#204A67"/><rect x="12" y="23" width="12" height="6" rx="3" fill="#BFE0F0"/><path d="M44 6 a6 6 0 1 0 6 6 a4 4 0 1 1 -6 -6Z" fill="#E8B923"/>',
"onsen":'<path d="M8 36 H48 Q46 50 28 50 Q10 50 8 36Z" fill="#6FB1D6"/><ellipse cx="28" cy="36" rx="20" ry="4" fill="#9DD0EA"/><circle cx="22" cy="31" r="5" fill="#F7D9B8"/><path d="M14 22 q3 -6 0 -12 M28 20 q3 -6 0 -12 M42 22 q3 -6 0 -12" stroke="#b9c7d1" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
"mail":'<rect x="6" y="14" width="44" height="30" rx="3" fill="#fff" stroke="#204A67" stroke-width="2"/><path d="M6 16 L28 34 L50 16" stroke="#204A67" stroke-width="2" fill="none"/><circle cx="44" cy="40" r="7" fill="#B14C5D"/><path d="M41 40 L43.5 42.5 L47.5 37.5" stroke="#fff" stroke-width="2" fill="none"/>',
"pin":'<path d="M28 52 C16 38 12 30 12 22 A16 16 0 0 1 44 22 C44 30 40 38 28 52Z" fill="#B14C5D"/><circle cx="28" cy="22" r="6" fill="#fff"/>',
}

SPOT_ICON={"高尾山":"takao","高尾山薬王院":"yakuoin","八王子城跡":"joseki","陣馬山":"jinba","高尾599ミュージアム":"museum599","多摩森林科学園":"sakura","東京富士美術館":"artmuseum","滝山城跡":"takiyama"}
TOKUSAN_ICON={"八王子ラーメン":"ramen","八王子ナポリタン":"napolitan","高尾山のとろろそば":"soba","天狗焼き":"tengu","多摩織（八王子織物）":"tamaori","薬王院の精進料理":"shojin"}
GOURMET_ICON={"高尾山・高尾エリア":"soba","八王子駅周辺":"train","南大沢エリア":"bag","恩方・陣馬エリア":"farm"}
AREA_ICON={"中心市街地":"city","高尾":"takao","元八王子・川口":"joseki","恩方・陣馬":"jinba","南大沢・由木":"mall","滝山・北部":"takiyama"}
HOTEL_ICON={"京王プラザホテル八王子":"hotel","駅周辺のビジネスホテル":"bed","京王高尾山温泉 極楽湯":"onsen","南大沢駅周辺の宿泊施設":"mall"}
EVENT_ICONS=["fire","sakura","beer","dashi","maple","ginkgo","sunrise"]

def icon_svg(key, cls="icon"):
    return f'<svg class="{cls}" viewBox="0 0 56 56" aria-hidden="true">{ICONS[key]}</svg>'

BRAND_SVG_INNER='<rect width="64" height="64" rx="14" fill="#E8F4FA"/><path d="M2 56 L22 22 L32 38 L40 28 L62 56Z" fill="#3C7A52"/><path d="M2 56 L22 22 L30 35 L20 56Z" fill="#2B5E3E"/><g transform="translate(30 4) scale(.5)"><path d="M28 33 C12 34 5 20 9 11 C15 17 22 15 28 11 C34 15 41 17 47 11 C51 20 44 34 28 33Z" fill="#E8B923"/><path d="M28 50 V33" stroke="#C1892E" stroke-width="3"/></g>'
BRAND_SVG=f'<svg class="brand-icon" viewBox="0 0 64 64" aria-hidden="true">{BRAND_SVG_INNER}</svg>'
FAVICON=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{BRAND_SVG_INNER}</svg>\n'

def _g(key,x,y,s): return f'<g transform="translate({x} {y}) scale({s})">{ICONS[key]}</g>'

HERO = '''<svg viewBox="0 0 480 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="高尾山とイチョウ並木、京王線の電車を描いた八王子のイラスト">
<defs><g id="gk"><path d="M0 12 L-14 -10 Q0 -16 14 -10Z" fill="#E8B923"/><path d="M0 12 V-8" stroke="#C1892E" stroke-width="1.2"/></g></defs>
<circle cx="392" cy="58" r="30" fill="#F2B94B"/>
<g fill="#fff" opacity=".95"><ellipse cx="90" cy="60" rx="34" ry="11"/><ellipse cx="114" cy="52" rx="22" ry="11"/><ellipse cx="300" cy="44" rx="28" ry="9"/><ellipse cx="320" cy="38" rx="16" ry="9"/></g>
<path d="M0 210 L70 160 L120 190 L200 130 L280 185 L340 150 L420 200 L480 175 V340 H0Z" fill="#BFD9E8"/>
<path d="M40 304 L170 124 L232 72 L300 142 L332 122 L456 304Z" fill="#3C7A52"/>
<path d="M40 304 L170 124 L232 72 L254 112 L206 304Z" fill="#2B5E3E"/>
<path d="M232 72 V48" stroke="#204A67" stroke-width="3"/><path d="M232 48 L256 55 L232 63Z" fill="#B14C5D"/>
<path d="M90 280 L212 112" stroke="#555" stroke-width="2"/>
<rect x="138" y="190" width="22" height="15" rx="3" fill="#C1892E" transform="rotate(-54 149 197)"/>
<g fill="#5E9E6E"><circle cx="250" cy="180" r="9"/><circle cx="270" cy="200" r="11"/><circle cx="290" cy="170" r="8"/><circle cx="310" cy="210" r="10"/><circle cx="350" cy="230" r="11"/></g>
<path d="M0 300 Q120 268 240 290 T480 284 V340 H0Z" fill="#9CCB8B"/>
<path d="M310 300 L316 262 H374 L380 300Z" fill="#9AA3A8"/><path d="M314 272 H376 M312 284 H378 M330 262 V272 M350 272 V284 M338 284 V300" stroke="#6E777C" stroke-width="1.5"/><path d="M336 300 V290 Q345 278 354 290 V300Z" fill="#3A3F44"/><path d="M372 262 V236" stroke="#8B5E3C" stroke-width="3"/><path d="M372 236 L390 242 L372 249Z" fill="#B14C5D"/>
<rect x="96" y="284" width="118" height="24" rx="8" fill="#fff" stroke="#204A67" stroke-width="2"/><rect x="96" y="297" width="118" height="5" fill="#B14C5D"/>
<g fill="#BFE0F0"><rect x="104" y="288" width="16" height="9" rx="2"/><rect x="126" y="288" width="16" height="9" rx="2"/><rect x="148" y="288" width="16" height="9" rx="2"/><rect x="170" y="288" width="16" height="9" rx="2"/></g>
<path d="M0 322 Q120 304 240 322 T480 316 V340 H0Z" fill="#6FB1D6"/>
<path d="M20 330 q12 -5 24 0 t24 0 M200 332 q12 -5 24 0 t24 0 M380 330 q12 -5 24 0 t24 0" stroke="#fff" stroke-width="2" fill="none" opacity=".8"/>
<rect x="40" y="236" width="9" height="66" fill="#8B5E3C"/><ellipse cx="44" cy="212" rx="36" ry="42" fill="#E8B923"/><ellipse cx="34" cy="204" rx="18" ry="22" fill="#F3CB4E"/>
<rect x="432" y="254" width="7" height="50" fill="#8B5E3C"/><ellipse cx="436" cy="236" rx="27" ry="32" fill="#E8B923"/><ellipse cx="428" cy="230" rx="13" ry="17" fill="#F3CB4E"/>
<g transform="translate(24 76) scale(.7)">''' + ICONS["tengu"] + '''</g>
<path d="M300 112 L346 100 L362 120 L334 126Z" fill="#B5702E"/><circle cx="296" cy="112" r="6" fill="#B5702E"/><circle cx="294" cy="110" r="1.3" fill="#222"/>
<use href="#gk" x="120" y="110" transform="rotate(20 120 110)"/><use href="#gk" x="80" y="170" transform="rotate(-30 80 170)"/><use href="#gk" x="400" y="150" transform="rotate(40 400 150)"/><use href="#gk" x="460" y="200" transform="rotate(-15 460 200)"/><use href="#gk" x="18" y="260" transform="scale(.8) rotate(10)"/>
</svg>'''

def banner(kind):
    sets={
     "map":["takao","joseki","pin","jinba","takiyama","pin","artmuseum","sakura","pin","yakuoin"],
     "matsuri":["fire","sakura","beer","dashi","dashi","maple","ginkgo","sunrise","tengu","fire"],
     "areas":["city","takao","joseki","jinba","mall","takiyama","city","yakuoin","sakura","mall"],
     "shukuhaku":["hotel","onsen","bed","takao","hotel","mall","bed","onsen","hotel","sunrise"],
     "unei":["mail","ginkgo","takao","tengu","maple","sakura","mail","yakuoin","ginkgo","takao"],
    }[kind]
    items="".join(_g(k,10+i*104,14,1.6) for i,k in enumerate(sets))
    return f'''<div class="banner"><svg viewBox="0 0 1040 120" preserveAspectRatio="xMidYMax slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<rect width="1040" height="120" fill="#E8F4FA"/>
<path d="M0 92 Q130 60 260 88 T520 84 T780 88 T1040 80 V120 H0Z" fill="#CFE6D2"/>
{items}
<path d="M0 108 Q130 96 260 108 T520 106 T780 108 T1040 104 V120 H0Z" fill="#9CCB8B"/>
</svg></div>'''

ORN='<svg class="orn" viewBox="0 0 120 20" aria-hidden="true"><path d="M4 10 H46 M74 10 H116" stroke="#9cc3da" stroke-width="2" stroke-linecap="round"/><g transform="translate(50 -1) scale(.38)">'+ICONS["ginkgo"]+'</g></svg>'

SKYLINE='''<div class="skyline" aria-hidden="true"><svg viewBox="0 0 1200 70" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<g fill="#E8B923"><ellipse cx="90" cy="26" rx="18" ry="20"/><ellipse cx="330" cy="30" rx="14" ry="16"/><ellipse cx="640" cy="24" rx="18" ry="20"/><ellipse cx="930" cy="30" rx="15" ry="17"/><ellipse cx="1120" cy="26" rx="17" ry="19"/></g>
<g fill="#8B5E3C"><rect x="88" y="44" width="4" height="26"/><rect x="328" y="44" width="4" height="26"/><rect x="638" y="44" width="4" height="26"/><rect x="928" y="46" width="4" height="24"/><rect x="1118" y="44" width="4" height="26"/></g>
<path d="M0 70 V50 L120 34 L200 52 L330 22 L430 50 L560 30 L700 54 L820 28 L960 52 L1080 36 L1200 50 V70Z" fill="#204A67"/>
</svg></div>'''
