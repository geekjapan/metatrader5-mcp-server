# MetaTrader5 MCP Server

This repository provides a minimal template for building a MetaTrader 5 MCP server using Python and Flask. It demonstrates how to connect to a local MetaTrader 5 terminal and execute basic operations through simple REST APIs.

## Requirements

- Python 3.12 or later
- Dependencies listed in `requirements.txt`
- A running MetaTrader 5 terminal

## Setup

```bash
pip install -r requirements.txt
python -m mcp_server.server
```

## Endpoints

- `GET /api/v1/ping` – health check endpoint.
- `POST /api/v1/connect` – initialize connection to MetaTrader 5.
- `GET /api/v1/account` – fetch account information.
- `POST /api/v1/orders` – send a market order using connected terminal.

## 日本語での説明

このリポジトリは、Python と Flask を使用して MetaTrader 5 MCP サーバーを構築するための最小限のテンプレートです。ローカルの MetaTrader 5 ターミナルに接続し、簡潔な REST API を通じて基本的な操作を実行する方法を示しています。

### 主な機能

- `GET /api/v1/ping` – サーバーの稼働確認を行います。
- `POST /api/v1/connect` – MetaTrader 5 への接続を初期化します。
- `GET /api/v1/account` – 口座情報を取得します。
- `POST /api/v1/orders` – 市場注文を送信します。

### セットアップ方法

1. `requirements.txt` に記載された依存パッケージをインストールします。
2. `python -m mcp_server.server` を実行してサーバーを起動します。

