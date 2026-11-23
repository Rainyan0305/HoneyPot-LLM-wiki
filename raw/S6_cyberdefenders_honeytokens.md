---
id: S6
title: CyberDefenders Glossary — Honeytokens
url: https://cyberdefenders.org/cybersecurity-glossary/honeytokens/
type: 資安教育平台術語文章
ingested: 2026-11-23
reliability: 中高
---

# 摘要（改寫）
- 蜜標（honeytoken）：放在真實資產之間的假資料（假帳密、檔案、資料列、金鑰），沒有任何正當用途，只要有人碰到就發出警報。
- 與蜜罐的差別：蜜罐是「假系統」，需要自己的基礎設施、隔離和監控，回答「攻擊者進來後做什麼」；蜜標是「假資料」，放在既有系統裡，成本很低，回答「有沒有人碰了不該碰的東西」。
- 類型：假帳密、canary token / API 金鑰、誘餌文件（打開就回報）、資料庫假資料列。
- 偵測迴圈：部署（放在攻擊者會找、正常使用者不會碰的地方）→ 偵測（接上 SIEM/EDR/雲端警報）→ 回應（當作入侵處理）。
- 常見錯誤：警報沒接上；命名太明顯（如 honeypot.txt）；放在沒人會去的地方；備份或掃描程式誤觸造成誤報；沒有回應計畫。

# claims
- C6.1 蜜標 = 假資料；蜜罐 = 假系統。
- C6.2 偵測迴圈：部署 → 偵測 → 回應。
- C6.3 命名要像真的、要避開正常流程誤觸。
