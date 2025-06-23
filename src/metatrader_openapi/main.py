"""FastAPI server exposing REST endpoints."""

from fastapi import Depends, FastAPI

from metatrader_client import MT5Client
from .config import MT5Config
from .routers import accounts, market, orders, positions, history

app = FastAPI(title="MetaTrader OpenAPI")


def get_client() -> MT5Client:
    config = MT5Config()
    client = MT5Client(config.login, config.password, config.server)
    client.connect()
    return client


app.include_router(accounts.router, dependencies=[Depends(get_client)])
app.include_router(market.router, dependencies=[Depends(get_client)])
app.include_router(orders.router, dependencies=[Depends(get_client)])
app.include_router(positions.router, dependencies=[Depends(get_client)])
app.include_router(history.router, dependencies=[Depends(get_client)])
