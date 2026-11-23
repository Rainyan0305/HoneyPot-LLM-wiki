---
id: S4
title: The Honeynet Project — Low Interaction Honeypots Revisited (2015)
url: https://honeynet.org/2015/08/06/low-interaction-honeypots-revisited/
type: 一手研究組織部落格
ingested: 2026-11-23
reliability: 高（蜜罐領域最重要的非營利研究組織）
---

# 摘要（改寫）
- Honeynet Project 於 1999 年成立時，外界對攻擊者的動機和工具所知很少。
- 主題：攻擊者如何「認出」蜜罐，以及防守方該學到什麼。
- 偵測與反偵測的歷史：
  - 2003 Phrack 刊出偵測、利用蜜罐的文章。
  - 2004 BlackHat「NoSEBrEak」演講示範如何偵測 Honeynet Project 的 Sebek 元件；2005 Sebek 改版；講者後來加入 Project。
  - Nmap 能指紋辨識 Dionaea（2012 年部落格提到）；約 2013 年出現辨識 Kippo（SSH 蜜罐）的技巧。
  - Shodan 有 honeyscore，可以查出疑似蜜罐。
- 給防守方的教訓：
  - 低互動蜜罐只是模擬服務，幾乎一定能被指紋辨識 → 主要適合抓自動化、基本攻擊。
  - 進階攻擊者不會被低互動蜜罐拖住太久；要觀察高手需調校過的高互動蜜罐。
  - 改掉預設設定、持續更新與監控，蜜罐不是「裝了就不用管」。
  - 接受「被識破 → 修補 → 改進」的循環；搭配其他偵測（縱深防禦）。

# claims
- C4.1 低互動蜜罐可被指紋辨識（Nmap、Shodan honeyscore）。
- C4.2 必須改預設值並持續維護。
- C4.3 蜜罐應搭配縱深防禦。
