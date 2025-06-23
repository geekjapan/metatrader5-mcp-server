"""Facade class providing access to MetaTrader 5 terminal features."""

from __future__ import annotations

from .client_connection import MT5Connection
from .client_account import MT5Account
from .client_market import MT5Market
from .client_order import MT5Order
from .client_history import MT5History


class MT5Client:
    """Entry point for interacting with MetaTrader 5 terminal."""

    def __init__(self, login: int, password: str, server: str) -> None:
        self._connection = MT5Connection(login, password, server)
        self.account = MT5Account(self._connection)
        self.market = MT5Market(self._connection)
        self.order = MT5Order(self._connection)
        self.history = MT5History(self._connection)

    def connect(self) -> bool:
        """Connect to the terminal using provided credentials."""
        return self._connection.connect()

    def disconnect(self) -> None:
        """Disconnect from terminal."""
        self._connection.disconnect()

    @property
    def connection(self) -> MT5Connection:
        return self._connection
