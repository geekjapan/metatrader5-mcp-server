"""Connection management for MetaTrader 5 terminal."""

from __future__ import annotations

from typing import Optional

import MetaTrader5 as mt5

from .exceptions import MT5ConnectionError


class MT5Connection:
    """Handle initialize and shutdown of MetaTrader 5 terminal."""

    def __init__(self, login: int, password: str, server: str) -> None:
        self.login = login
        self.password = password
        self.server = server
        self._connected = False

    def connect(self, timeout: int = 30) -> bool:
        """Initialize connection to the terminal."""
        self._connected = mt5.initialize(
            login=self.login, password=self.password, server=self.server
        )
        if not self._connected:
            raise MT5ConnectionError("failed to connect to terminal")
        return True

    def disconnect(self) -> None:
        """Shutdown connection."""
        if self._connected:
            mt5.shutdown()
            self._connected = False

    def is_connected(self) -> bool:
        return self._connected and mt5.terminal_info() is not None

    def get_terminal_info(self) -> Optional[dict]:
        info = mt5.terminal_info()
        return info._asdict() if info else None
