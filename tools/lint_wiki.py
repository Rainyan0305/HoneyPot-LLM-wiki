"""Wiki lint：檢查來源標註、來源是否存在、單一來源關鍵事實、斷鏈、術語一致。
用法：python3 tools/lint_wiki.py [wiki_dir] [raw_dir]
也可用來檢查簡報：python3 tools/lint_wiki.py --slides slides.html
"""
import re, sys, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
BAD_TERMS = {"蜂蜜罐": "蜜罐", "誘捕系統": "蜜罐", "honey token": "蜜標", "蜜糖罐": "蜜罐"}
CITE = re.compile(r"\[S(\d+)\]")
YEAR = re.compile(r"(19|20)\d{2}")


def raw_ids():
    return {int(re.match(r"S(\d+)", p.name).group(1)) for p in (ROOT / "raw").glob("S*.md")}


def lint_wiki():
    issues = []
    ids = raw_ids()
    pages = {p.stem: p for p in (ROOT / "wiki").glob("*.md")}
    for name, p in sorted(pages.items()):
        text = p.read_text(encoding="utf-8")
        body = text.split("---", 2)[2]
        in_analogy = False
        for i, line in enumerate(body.splitlines(), 1):
            s = line.strip()
            if s.startswith("## 給新手的比喻"):
                in_analogy = True
            elif s.startswith("## "):
                in_analogy = False
            # (a) 事實句（條列/表格列/編號）沒有來源
            is_fact = (s.startswith("- ") or re.match(r"^\d+\.", s) or (s.startswith("|") and not set(s) <= set("|- ")))
            if is_fact and not in_analogy and not CITE.search(s) and "來源" not in s and "⚠" not in s:
                if s.startswith("|") and re.match(r"^\|\s*(\||年份|誰在用|是什麼)", s):
                    continue  # 表頭
                if "[[" in s:
                    continue
                issues.append((name, i, "無來源", s[:60]))
            # (b) 引用不存在的來源
            for m in CITE.finditer(s):
                if int(m.group(1)) not in ids:
                    issues.append((name, i, "來源不存在", m.group(0)))
            # (c) 年份只靠單一來源
            if YEAR.search(s) and len(set(CITE.findall(s))) == 1 and not in_analogy and "<!--ok" not in s:
                issues.append((name, i, "年份僅單一來源(提醒)", s[:60]))
            # (e) 術語
            for bad, good in BAD_TERMS.items():
                if bad in s:
                    issues.append((name, i, f"術語「{bad}」應改「{good}」", s[:40]))
        # (d) 斷鏈
        for link in re.findall(r"\[\[([^\]]+)\]\]", text):
            if link not in pages:
                issues.append((name, 0, "斷鏈", link))
    # 孤兒頁
    linked = set()
    for p in pages.values():
        linked |= set(re.findall(r"\[\[([^\]]+)\]\]", p.read_text(encoding="utf-8")))
    for name in pages:
        if name not in linked:
            issues.append((name, 0, "孤兒頁(沒被其他頁連到)", ""))
    return issues


def lint_slides(path):
    """簡報檢查：每張內容投影片都要有 data-wiki 來源，且來源頁存在；術語一致。"""
    html = pathlib.Path(path).read_text(encoding="utf-8")
    pages = {p.stem for p in (ROOT / "wiki").glob("*.md")}
    issues = []
    slides = re.findall(r'<section class="slide([^"]*)"([^>]*)>(.*?)</section>', html, re.S)
    for n, (cls, attrs, inner) in enumerate(slides, 1):
        m = re.search(r'data-wiki="([^"]*)"', attrs)
        if "no-source" in cls:
            continue
        if not m:
            issues.append((f"slide{n}", 0, "缺 data-wiki 來源", ""))
            continue
        for w in m.group(1).split():
            if w not in pages:
                issues.append((f"slide{n}", 0, "來源 Wiki 頁不存在", w))
        text = re.sub(r"<[^>]+>", " ", inner)
        for bad, good in BAD_TERMS.items():
            if bad in text:
                issues.append((f"slide{n}", 0, f"術語「{bad}」應改「{good}」", ""))
        if len(text.split()) > 0 and len(re.sub(r"\s", "", text)) > 420:
            issues.append((f"slide{n}", 0, "字太多(>420字)，新手讀不完", ""))
    return len(slides), issues


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--slides":
        n, issues = lint_slides(sys.argv[2])
        print(f"檢查 {n} 張投影片")
    else:
        issues = lint_wiki()
    for it in issues:
        print(" | ".join(map(str, it)))
    print(f"共 {len(issues)} 個問題")
