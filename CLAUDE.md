# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Python 課堂練習專案（NCUT），依章節整理練習程式碼。無 build system；
`project/` 底下的作業採 **TDD（測試先行）**，測試框架為 pytest。

## 執行方式

```bash
# 執行任意 Python 檔案
python <filename>.py

# 使用虛擬環境（.venv 已存在）
source .venv/bin/activate
python <filename>.py
```

```bash
# 跑測試（在專案根目錄執行）
pytest project/test_maze_spec.py -x    # 第一個失敗就停，TDD 預設用這個
pytest project/test_maze_spec.py -v    # 逐條列出
pytest                                 # 跑全部
```

## 專案結構

- `book/` — 課本各章節練習（c4.py、c5.py、c6.py、c6Practice.py、C7.py、C7Array.py）
- `book/example/` — 課堂範例（DataTypes.py、test1.py、c6P.py）
- `project/` — 作業繳交檔與其規格檔（spec）
- `w3c/` — W3Schools 相關練習
- `test1_toBinary_9B417004.py` — 作業繳交檔，命名格式為 `test<題號>_<題目>_<學號>.py`
- `main.py` — 進入點（通常只是測試用）

## TDD 工作流程（`project/` 的作業）

作業採測試先行。規格檔（`test_<主題>_spec.py`）先寫好，作業檔只留函式空殼
（`raise NotImplementedError`），由使用者自己實作。

節奏：**紅 → 綠 → 重構**

1. 跑測試，親眼看它失敗（沒看過它紅，就不知道這個測試有沒有在檢查東西）
2. 寫「剛好能讓它變綠」的最少程式碼，不要多寫
3. 全綠之後才能重構；重構期間必須維持全綠

規格檔用 `@pytest.mark.skip(reason="Step N：...")` 把後面的關卡鎖住，
一次只開一個 Step。前一個 Step 全綠，才刪掉下一個 Step 的 skip 那行。

### ⚠️ 重要：不要直接給答案

使用者是為了練習才用 TDD。協助時：

- **可以**：寫規格 / 測試、設計函式介面與骨架、解釋演算法概念與比喻、
  指出踩到哪個坑、跑測試並解讀失敗訊息
- **不可以**：直接把實作寫出來，除非使用者明確開口要答案
- 需要驗證測試裡的預期值時，把驗證用的腳本寫在 scratchpad，用完刪掉，
  不要把參考解答留在專案裡

## 回答風格

使用者正在學習 Python，回答問題時請使用**教學模式**：
- 逐步解說，從基本概念出發
- 用比喻或生活例子輔助理解
- 說明「為什麼」而不只是「怎麼做」
- 適時提問確認理解

## 檔案命名慣例

- 課本章節練習：`c<章節號>.py` 或 `C<章節號><主題>.py`（如 `C7Array.py`）
- 作業：`test<題號>_<描述>_<學號>.py`
- 規格（測試）檔：`test_<主題>_spec.py`

pytest 只收集符合 `test_*.py` 的檔案（`test` 後面要有底線），
所以 `test5_Mouse_9B417004.py`、`Test4_maxSP_9B417004.py` 這類作業檔**不會**被誤當成測試收集。