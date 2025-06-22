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
