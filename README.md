# MetaTrader5 AI Integration

This repository provides tools to integrate MetaTrader 5 terminals with AI applications. It includes a Python client library, a WebSocket MCP server, and a REST API based on FastAPI.

## Requirements

- Python 3.12 or later
- Dependencies listed in `requirements.txt`
- A running MetaTrader 5 terminal

## Setup

```bash
pip install -r requirements.txt
```

### MCP Server

```bash
python -m metatrader_mcp.cli serve --login <LOGIN> --password <PASS> --server <SERVER>
```

### OpenAPI Server

```bash
uvicorn metatrader_openapi.main:app
```

## 日本語

このリポジトリは MetaTrader 5 ターミナルを AI アプリケーションと統合するためのツールを提供します。Python クライアントライブラリ、WebSocket MCP サーバー、FastAPI ベースの REST API を含みます。

### 必要条件

- Python 3.12 以上
- `requirements.txt` に記載された依存関係
- 実行中の MetaTrader 5 ターミナル

### セットアップ

```bash
pip install -r requirements.txt
```

#### MCP サーバー

```bash
python -m metatrader_mcp.cli serve --login <LOGIN> --password <PASS> --server <SERVER>
```

#### OpenAPI サーバー

```bash
uvicorn metatrader_openapi.main:app
```
