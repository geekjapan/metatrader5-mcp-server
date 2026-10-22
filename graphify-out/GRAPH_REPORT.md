# Graph Report - metatrader5-mcp-server  (2026-10-23)

## Corpus Check
- 2 semantic source files; AST status: extracted. Exclusions and reuse evidence: build-audit.json.

## Summary
- 171 nodes · 283 edges · 12 communities (8 shown, 4 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.92)
- Token usage: per-project usage unavailable (native Codex semantic extraction).

## Graph Freshness
- Built from commit: `ec1005aa`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- MT5Client
- MT5Connection
- MT5Client
- exceptions.py
- metatrader_mcp/server.py
- MT5Market
- history.py
- MetaTrader5 AI integration
- Flask, FastAPI, uvicorn, websockets, typer, pydantic-settings and MetaTrader5

## God Nodes (most connected - your core abstractions)
1. `MT5Connection` - 24 edges
2. `MT5Client` - 22 edges
3. `MT5Client` - 13 edges
4. `MT5Account` - 13 edges
5. `MT5Market` - 11 edges
6. `MT5Order` - 9 edges
7. `MT5History` - 8 edges
8. `MT5Error` - 8 edges
9. `OrderType` - 7 edges
10. `MCPServer` - 7 edges

## Surprising Connections (you probably didn't know these)
- `MT5Client` --uses--> `MT5Account`  [INFERRED]
  src/metatrader_client/client.py → src/metatrader_client/client_account.py
- `MT5Connection` --uses--> `MT5ConnectionError`  [INFERRED]
  src/metatrader_client/client_connection.py → src/metatrader_client/exceptions.py
- `MT5Market` --uses--> `MT5Connection`  [INFERRED]
  src/metatrader_client/client_market.py → src/metatrader_client/client_connection.py
- `MT5Client` --uses--> `MT5Connection`  [INFERRED]
  src/metatrader_client/client.py → src/metatrader_client/client_connection.py
- `MT5Client` --uses--> `MT5History`  [INFERRED]
  src/metatrader_client/client.py → src/metatrader_client/client_history.py

## Import Cycles
- None detected.

## Communities (12 total, 4 thin omitted)

### Community 0 - "MT5Client"
Cohesion: 0.11
Nodes (10): MT5Client, MT5Config, Config, get_client(), account_info(), get_client(), get_client(), symbols() (+2 more)

### Community 1 - "MT5Connection"
Cohesion: 0.09
Nodes (4): MT5Account, MT5Connection, MT5History, MT5Order

### Community 2 - "MT5Client"
Cohesion: 0.09
Nodes (5): MT5Client, account(), connect(), ping(), place_order()

### Community 3 - "exceptions.py"
Cohesion: 0.13
Nodes (6): MT5ConnectionError, MT5Error, MT5NotConnectedError, MT5SymbolError, MT5TimeframeError, MT5TradeError

### Community 4 - "metatrader_mcp/server.py"
Cohesion: 0.16
Nodes (3): serve(), MCPServer, Tool

### Community 6 - "MT5Market"
Cohesion: 0.13
Nodes (5): MT5Market, OrderType, Timeframe, get_client(), market_order()

### Community 7 - "history.py"
Cohesion: 0.52
Nodes (3): deals(), get_client(), orders()

### Community 8 - "MetaTrader5 AI integration"
Cohesion: 0.50
Nodes (4): MetaTrader5 AI integration, WebSocket MCP server, FastAPI REST API, Running MetaTrader 5 terminal

## Knowledge Gaps
- **4 isolated node(s):** `WebSocket MCP server`, `FastAPI REST API`, `Running MetaTrader 5 terminal`, `Flask, FastAPI, uvicorn, websockets, typer, pydantic-settings and MetaTrader5`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 76 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MT5Client` connect `MT5Client` to `MT5Connection`, `exceptions.py`, `metatrader_mcp/server.py`, `client.py`, `MT5Market`, `history.py`?**
  _High betweenness centrality (0.339) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `MT5Connection` (e.g. with `MT5Account` and `MT5ConnectionError`) actually correct?**
  _`MT5Connection` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `WebSocket MCP server`, `FastAPI REST API`, `Running MetaTrader 5 terminal` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `MT5Client` be split into smaller, more focused modules?**
  _Cohesion score 0.10887096774193548 - nodes in this community are weakly interconnected._
- **Why does `MT5Connection` connect `MT5Connection` to `MT5Client`, `exceptions.py`, `client.py`, `MT5Market`?**
  _High betweenness centrality (0.180) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `MT5Client` (e.g. with `MT5Account` and `MT5Connection`) actually correct?**
  _`MT5Client` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Should `MT5Connection` be split into smaller, more focused modules?**
  _Cohesion score 0.09401709401709402 - nodes in this community are weakly interconnected._