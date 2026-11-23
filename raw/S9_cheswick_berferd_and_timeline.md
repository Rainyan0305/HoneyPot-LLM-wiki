---
id: S9
title: Bill Cheswick — An Evening with Berferd（一手論文）+ Spitzner《Honeypots: Tracking Hackers》歷史時間軸
url: https://www.cerias.purdue.edu/apps/reports_and_papers/view/1007 ; https://www.oreilly.com/library/view/honeypots-tracking-hackers/0321108957/0321108957_ch03lev1sec1.html
type: 一手論文 + 專書
ingested: 2026-11-23（lint 階段補抓，用來核對 S2 的「1990」年份）
reliability: 高
---

# 為什麼補抓這篇
lint 時發現 S2 寫「1990 年 AT&T 貝爾實驗室」，但只有單一來源。查一手論文後發現事件日期是 1991 年 1 月 7 日 → 以一手來源為準，S2 的年份標記為「與一手來源不一致」。

# 摘要（改寫）
- 1991 年 1 月 7 日，一名入侵者以為找到 AT&T 貝爾實驗室網際網路閘道上的 sendmail DEBUG 漏洞，想偷密碼檔；Cheswick 故意寄給他一份假的密碼檔，接著建立一個「監獄（jail）」環境觀察他的行為，並寫成論文。
- Spitzner 專書的時間軸把 1990/1991 年的兩份作品視為最早公開記錄蜜罐概念的文獻：Clifford Stoll《The Cuckoo's Egg》與 Cheswick〈An Evening With Berferd〉。
- 1997：Fred Cohen 的 Deception Toolkit 0.1 釋出，是最早可供社群使用的蜜罐方案之一。
- 1998：CyberCop Sting 開始開發，是最早公開販售的商用蜜罐之一。

# claims
- C9.1 Berferd 事件發生在 1991 年 1 月（修正 S2 的 1990）。
- C9.2 Stoll 與 Cheswick 是最早記錄蜜罐概念的公開作品。
- C9.3 1997 Deception Toolkit；1998 CyberCop Sting。
