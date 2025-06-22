# MetaTrader5 MCP Server

This repository provides a minimal template for building a MetaTrader 5 MCP server using Python and Flask.

## Requirements

- Python 3.12 or later
- Dependencies listed in `requirements.txt`

## Setup

```bash
pip install -r requirements.txt
python -m mcp_server.server
```

## Endpoints

- `GET /api/v1/ping` – health check endpoint.
- `POST /api/v1/orders` – placeholder for order handling; echoes the request payload.

Feel free to extend these handlers with your own logic.
