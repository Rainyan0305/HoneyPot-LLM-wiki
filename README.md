# 用 LLM Wiki 做教學 HTML 簡報：蜜罐（Honeypot）是什麼？

先建立「蜜罐」主題的 LLM Wiki（ingest 9 篇資料），再只用這個 Wiki 當知識來源，製作一份給資安新手看的教學 HTML 簡報。

## 🔗 成果連結

| 項目 | 連結 |
|---|---|
| 📽 教學 HTML 簡報（線上瀏覽） | https://YOUR_USERNAME.github.io/honeypot-llm-wiki/slides/ |
| 📚 LLM Wiki 目錄 | [index.md](index.md) |
| 📄 Wiki 頁面（7 頁） | [wiki/](wiki/) |
| 🗂 原始資料摘要（9 篇） | [raw/](raw/) |
| 🔁 loop / graph 設計＋反思 | [workflow.md](workflow.md) |
| 🧪 實際執行的檢查紀錄 | [reports/run-2026-11-23.md](reports/run-2026-11-23.md) |
| 📝 操作日誌 | [log.md](log.md) |

> 簡報操作：← → 鍵或空白鍵換頁，手機可以左右滑。

## 📁 資料夾結構

```
honeypot-llm-wiki/
├── README.md          ← 你正在看的這頁
├── SCHEMA.md          ← Wiki 的維護規則與術語表（給 LLM 看）
├── index.md           ← Wiki 目錄（Query 的入口）
├── log.md             ← 每一步操作的日誌（append-only）
├── workflow.md        ← 作業步驟三、四：graph 設計與反思
├── raw/               ← 第 1 層：9 篇來源的改寫摘要＋claims（S1–S9）
├── wiki/              ← 第 2 層：7 頁主題頁，每個事實句都標 [S#]
├── slides/index.html  ← 教學 HTML 簡報（20 頁，每頁標出依據的 Wiki 頁）
├── tools/
│   ├── lint_wiki.py      ← 檢查 B／C-1：來源標註、斷鏈、術語、投影片對應
│   └── render_check.py   ← 檢查 C-2：用無頭瀏覽器逐頁渲染
└── reports/           ← 一次實際執行的檢查紀錄＋20 頁截圖
```

## 🔁 工作流程（簡版）

```
① 討論選題(人) → ② 搜尋 → ③ Ingest → [檢查 A] → ④ 討論結構(人) → ⑤ 生成 Wiki → [檢查 B]
→ ⑥ 簡報大綱 → ⑦ 逐頁 Query Wiki → ⑧ 生成投影片 → [檢查 C] → ⑨ 發佈
```
- 檢查 A 不過 → 回 ② 找一手來源；檢查 B 不過 → 回 ⑤ 修 Wiki；檢查 C 不過 → 回 ⑧ 重做，若是 Wiki 缺內容就回 ② 重新取得。
- 簡報只能用 Wiki 裡有的內容，Wiki 是唯一的事實來源。

完整說明見 [workflow.md](workflow.md)。

## ▶ 自己重跑檢查

```bash
python3 tools/lint_wiki.py                              # 檢查 Wiki
python3 tools/lint_wiki.py --slides slides/index.html   # 檢查簡報原始碼
python3 tools/render_check.py slides/index.html         # 逐頁渲染（需要 Playwright＋Chrome，並修改腳本中的 Chrome 路徑）
```

## 📖 資料來源
NIST CSRC Glossary、Splunk、CrowdStrike、The Honeynet Project、Cowrie（GitHub）、CyberDefenders、Kaspersky Encyclopedia、SANS GIAC、Bill Cheswick〈An Evening with Berferd〉、Lance Spitzner《Honeypots: Tracking Hackers》。完整連結請見 `raw/` 裡每個檔案的開頭。
`raw/` 中的內容是用自己的話改寫的摘要，並非原文。
