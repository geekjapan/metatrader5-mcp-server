"""WebSocket MCP server implementation."""

from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass
from typing import Callable, Dict

import websockets

from metatrader_client import MT5Client


@dataclass
class Tool:
    func: Callable
    description: str


class MCPServer:
    def __init__(self, host: str, port: int, client: MT5Client) -> None:
        self.host = host
        self.port = port
        self.client = client
        self.tools: Dict[str, Tool] = {}

    def register_tool(self, name: str, func: Callable, description: str) -> None:
        self.tools[name] = Tool(func, description)

    async def handler(self, websocket):
        async for message in websocket:
            data = json.loads(message)
            name = data.get("tool")
            args = data.get("args", {})
            if name not in self.tools:
                await websocket.send(json.dumps({"error": "unknown tool"}))
                continue
            result = self.tools[name].func(**args)
            await websocket.send(json.dumps({"result": result}))

    async def run(self):
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()  # run forever
