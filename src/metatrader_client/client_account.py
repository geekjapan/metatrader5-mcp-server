"""Account related helpers for MT5."""

from __future__ import annotations

from typing import Optional, Dict

import MetaTrader5 as mt5

from .client_connection import MT5Connection


class MT5Account:
    def __init__(self, connection: MT5Connection) -> None:
        self._connection = connection

    def get_account_info(self) -> Optional[Dict]:
        info = mt5.account_info()
        return info._asdict() if info else None

    def get_balance(self) -> Optional[float]:
        info = mt5.account_info()
        return info.balance if info else None

    def get_equity(self) -> Optional[float]:
        info = mt5.account_info()
        return info.equity if info else None

    def get_margin(self) -> Optional[float]:
        info = mt5.account_info()
        return info.margin if info else None

    def get_free_margin(self) -> Optional[float]:
        info = mt5.account_info()
        return info.margin_free if info else None

    def get_margin_level(self) -> Optional[float]:
        info = mt5.account_info()
        return info.margin_level if info else None

    def is_trade_allowed(self) -> Optional[bool]:
        info = mt5.account_info()
        return info.trade_allowed if info else None
