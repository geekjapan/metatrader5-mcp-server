"""History retrieval helpers."""

from __future__ import annotations

from datetime import datetime
from typing import List, Dict

import MetaTrader5 as mt5

from .client_connection import MT5Connection


class MT5History:
    def __init__(self, connection: MT5Connection) -> None:
        self._connection = connection

    def get_deals(self, from_date: datetime, to_date: datetime, symbol: str = "") -> List[Dict]:
        deals = mt5.history_deals_get(from_date, to_date, group=symbol or None)
        return [d._asdict() for d in deals] if deals else []

    def get_orders(self, from_date: datetime, to_date: datetime, symbol: str = "") -> List[Dict]:
        orders = mt5.history_orders_get(from_date, to_date, group=symbol or None)
        return [o._asdict() for o in orders] if orders else []
