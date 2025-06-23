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
