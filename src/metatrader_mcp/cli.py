"""Command line interface to run MCP server."""

import asyncio
from typing import Optional

import typer

from metatrader_client import MT5Client
from .server import MCPServer

app = typer.Typer()


@app.command()
def serve(
    host: str = "127.0.0.1",
    port: int = 8765,
    login: int = typer.Option(...),
    password: str = typer.Option(...),
    server: str = typer.Option(...),
):
    """Start MCP server."""
    client = MT5Client(login, password, server)
    client.connect()
    server_obj = MCPServer(host, port, client)

    # register simple tools using docstrings
    server_obj.register_tool("account_info", client.account.get_account_info, "Return account info")
    server_obj.register_tool("positions", client.order.get_all_positions, "Return open positions")

    asyncio.run(server_obj.run())


if __name__ == "__main__":
    app()
