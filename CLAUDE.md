# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Python 課堂練習專案（NCUT），依章節整理練習程式碼，無 build system 或測試框架。

## 執行方式

```bash
# 執行任意 Python 檔案
python <filename>.py

# 使用虛擬環境（.venv 已存在）
source .venv/bin/activate
python <filename>.py
```

## 專案結構

- `book/` — 課本各章節練習（c4.py、c5.py、c6.py、c6Practice.py、C7.py、C7Array.py）
- `book/example/` — 課堂範例（DataTypes.py、test1.py、c6P.py）
- `w3c/` — W3Schools 相關練習
- `test1_toBinary_9B417004.py` — 作業繳交檔，命名格式為 `test<題號>_<題目>_<學號>.py`
- `main.py` — 進入點（通常只是測試用）

## 回答風格

使用者正在學習 Python，回答問題時請使用**教學模式**：
- 逐步解說，從基本概念出發
- 用比喻或生活例子輔助理解
- 說明「為什麼」而不只是「怎麼做」
- 適時提問確認理解

## 檔案命名慣例

- 課本章節練習：`c<章節號>.py` 或 `C<章節號><主題>.py`（如 `C7Array.py`）
- 作業：`test<題號>_<描述>_<學號>.py`