---
title: 蜜罐的歷史
sources: [S2, S4, S8, S9]
related: [01-definition, 05-honeynet-honeytoken, 06-pros-risks-detection]
updated: 2026-11-23
---

# 蜜罐的歷史

**一句話：蜜罐從「工程師臨時起意把駭客留下來觀察」，發展成有開源工具、研究組織和商業產品的一門技術。**

## 時間軸
| 年份 | 事件 | 來源 |
|---|---|---|
| 1990/1991 | Clifford Stoll《The Cuckoo's Egg》與 Bill Cheswick〈An Evening with Berferd〉被視為最早公開記錄蜜罐概念的作品 | [S9] <!--ok:一手專書-->|
| 1991 年 1 月 | AT&T 貝爾實驗室的 Cheswick 發現有人想偷密碼檔，故意寄給對方假密碼檔，再用「監獄」環境觀察他 | [S9][S8] |
| 1997 | Fred Cohen 的 Deception Toolkit 0.1 釋出，最早給社群使用的蜜罐方案之一 | [S9] <!--ok:一手專書-->|
| 1998 | CyberCop Sting 開發，最早的商用蜜罐之一 | [S9] <!--ok:一手專書-->|
| 1999 | Lance Spitzner 創立 The Honeynet Project（2000 年 6 月正式命名） | [S8][S4] |
| 2003–2013 | 攻擊者開始研究「怎麼認出蜜罐」：Phrack 文章、BlackHat 演講、Nmap 能辨識 Dionaea 等 | [S4] <!--ok:一手組織-->|
| 近年 | 用 LLM 動態產生假檔案與終端回應的「動態蜜罐」 | [S2] |

## ⚠ 來源差異（lint 紀錄）
- S2（Splunk）寫 AT&T 事件在 **1990 年**；一手論文 S9 寫明是 **1991 年 1 月 7 日**。本 Wiki 以一手來源為準，採用 1991。

## 給新手的比喻
> 一開始像是「警察發現小偷，先不抓，偷偷跟著看他去哪」；後來變成「專門設計的誘捕行動」，再後來有了整套的器材和訓練。

## 相關頁面
[[01-definition]] · [[06-pros-risks-detection]]
