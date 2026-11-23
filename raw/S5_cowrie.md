---
id: S5
title: Cowrie SSH/Telnet Honeypot（GitHub 官方 README + Wikipedia 條目）
url: https://github.com/cowrie/cowrie ; https://en.wikipedia.org/wiki/Cowrie_(honeypot)
type: 開源專案文件
ingested: 2026-11-23
reliability: 高（一手專案文件）
---

# 摘要（改寫）
- Cowrie 是中互動的 SSH 與 Telnet 蜜罐，用來記錄暴力破解登入與攻擊者登入後的 shell 操作；由 Michel Oosterhof 維護，以 Python 撰寫，BSD 授權。
- 前身是 Kippo（Upi Tamminen 開發）。
- 兩種模式：模擬 shell（中互動，用 Python 模擬一個 UNIX 系統），或 proxy 模式（把連線轉到真實系統觀察，接近高互動）。
- 功能：假檔案系統（仿 Debian 5.0）、可放假的 /etc/passwd 內容；攻擊者用 wget/curl 下載或 SFTP/scp 上傳的檔案會被保存供分析；連線紀錄可用 playlog 依原始節奏重播；JSON 格式日誌方便丟進日誌分析系統；有 Docker 版本。
- Deutsche Telekom 開發的多蜜罐平台 T-Pot 於 2016 年 3 月以 Cowrie 取代 Kippo。

# claims
- C5.1 Cowrie = 中互動 SSH/Telnet 蜜罐。
- C5.2 記錄登入嘗試、指令、下載的惡意檔案。
- C5.3 T-Pot 是整合多個蜜罐的平台。
