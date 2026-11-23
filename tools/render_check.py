"""檢查 C 的第二半：用無頭瀏覽器逐頁「實看」簡報。
- 先確認換頁本身可用（不然後面全是假性通過——這次真的發生過）
- 每頁：內容是否壓到頁尾、SVG 方框內文字是否超出方框
- 每頁存截圖到 shots/
用法：python3 tools/render_check.py slides/index.html
"""
import asyncio, sys, pathlib
from playwright.async_api import async_playwright

JS = """()=>{const s=document.querySelector('.slide.on');const f=s.querySelector('.foot').getBoundingClientRect();
 const out=[];
 s.querySelectorAll('*').forEach(el=>{if(el.closest('.foot')||el.closest('svg'))return;const r=el.getBoundingClientRect();
   if(r.height&&r.bottom>f.top+1)out.push('壓到頁尾:'+(el.textContent||'').trim().slice(0,16))});
 s.querySelectorAll('svg g:not(.legend)').forEach(g=>{const rect=g.querySelector(':scope>rect');if(!rect)return;const R=rect.getBoundingClientRect();
   g.querySelectorAll(':scope>text').forEach(t=>{const T=t.getBoundingClientRect();if(T.left<R.left-1||T.right>R.right+1)out.push('字超出方框:'+t.textContent)})});
 return [s.querySelector('.foot span:last-child').textContent,out]}"""

async def main(path):
    url = pathlib.Path(path).resolve().as_uri()
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1280, "height": 780})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto(url + "#s3"); await pg.wait_for_timeout(1000)
        first = await pg.evaluate("document.querySelector('.slide.on .foot span:last-child').textContent")
        if not first.startswith("3 "):
            print("❌ 換頁失敗：開 #s3 卻顯示", first); return
        await pg.evaluate("location.hash='#s1'"); await pg.wait_for_timeout(300)
        n = await pg.evaluate("document.querySelectorAll('.slide').length")
        out = pathlib.Path("shots"); out.mkdir(exist_ok=True)
        total = 0
        for i in range(n):
            if i:
                await pg.keyboard.press("ArrowRight"); await pg.wait_for_timeout(420)
            page, probs = await pg.evaluate(JS)
            if not page.startswith(f"{i+1} "):
                print(f"❌ 第 {i+1} 次換頁失敗，顯示 {page}"); break
            for pr in probs: print(f"slide {i+1}: {pr}")
            total += len(probs)
            await pg.screenshot(path=str(out / f"s{i+1:02d}.png"))
        print(f"渲染 {n} 頁，問題 {total} 個；JS 錯誤：{errs or '無'}")
        await b.close()

asyncio.run(main(sys.argv[1]))
