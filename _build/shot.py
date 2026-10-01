from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1000,"height":900})
    for n in ["index","map","matsuri"]:
        pg.goto(f"file:///mnt/user-data/outputs/hachioji/{n}.html"); pg.screenshot(path=f"/home/claude/build/{n}.png",full_page=(n!="index"))
    pg.goto("file:///mnt/user-data/outputs/hachioji/index.html"); pg.screenshot(path="/home/claude/build/index_full.png",full_page=True)
    b.close()
