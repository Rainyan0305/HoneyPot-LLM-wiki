# Honeypot（蜜罐）LLM Wiki — 目錄

> 📽 教學簡報：[slides/](slides/)｜📄 作業說明：[workflow.md](workflow.md)｜🧪 檢查紀錄：[reports/run-2026-11-23.md](reports/run-2026-11-23.md)

> Query 時 LLM 先讀這頁，找到相關頁再深入。讀者設定：完全沒學過資安的人。

## Wiki 頁面
| 頁面 | 一句話 | 主要來源 |
|---|---|---|
| [01-definition](wiki/01-definition.md) | 蜜罐是故意做得很誘人的假系統或假資料，用來引誘、觀察攻擊者 | S1 S2 S3 S7 S8 |
| [02-history](wiki/02-history.md) | 從 1991 年 Berferd 事件到 LLM 動態蜜罐 | S2 S4 S8 S9 |
| [03-how-it-works](wiki/03-how-it-works.md) | 擺誘餌 → 留破綻 → 全程記錄 → 分析 → 回饋 | S2 S3 S5 S7 |
| [04-types](wiki/04-types.md) | 用途、互動程度、目標三種分法 | S2 S3 S4 S5 |
| [05-honeynet-honeytoken](wiki/05-honeynet-honeytoken.md) | 蜜網＝假網路、蜜標＝假資料 | S1 S2 S3 S6 S8 |
| [06-pros-risks-detection](wiki/06-pros-risks-detection.md) | 誤報少、情報準；但可能變跳板、會被識破 | S2 S3 S4 |
| [07-deployment](wiki/07-deployment.md) | 定目的、隔離、做得像、接警報、持續維護 | S2 S3 S4 S6 |

## 原始資料（raw/，共 9 篇）
| ID | 來源 | 類型 |
|---|---|---|
| S1 | NIST CSRC Glossary | 官方定義 |
| S2 | Splunk — Why Honeypots Work | 廠商教學 |
| S3 | CrowdStrike — What Is a Honeypot? | 廠商教學 |
| S4 | Honeynet Project — Low Interaction Honeypots Revisited | 一手研究組織 |
| S5 | Cowrie 官方 README + Wikipedia | 開源專案文件 |
| S6 | CyberDefenders — Honeytokens | 教育平台 |
| S7 | Kaspersky Encyclopedia | 資安百科 |
| S8 | Honeynet Project 歷史（Wikipedia + SANS GIAC） | 百科 + 實務論文 |
| S9 | Cheswick〈An Evening with Berferd〉+ Spitzner 專書時間軸 | 一手論文 + 專書（lint 時補抓） |
