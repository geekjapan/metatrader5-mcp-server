"""Market data retrieval helpers."""

from __future__ import annotations

from typing import List, Dict, Optional

import MetaTrader5 as mt5

from .client_connection import MT5Connection
from .types import Timeframe


class MT5Market:
    def __init__(self, connection: MT5Connection) -> None:
        self._connection = connection

    def get_symbols(self) -> List[str]:
        symbols = mt5.symbols_get()
        return [s.name for s in symbols] if symbols else []

    def get_symbol_info(self, symbol: str) -> Optional[Dict]:
        info = mt5.symbol_info(symbol)
        return info._asdict() if info else None

    def get_symbol_price(self, symbol: str) -> Optional[Dict]:
        tick = mt5.symbol_info_tick(symbol)
        return tick._asdict() if tick else None

    def get_candles_latest(self, symbol: str, timeframe: Timeframe, count: int) -> List[Dict]:
        rates = mt5.copy_rates_from_pos(symbol, timeframe.value, 0, count)
        return [r._asdict() for r in rates] if rates is not None else []

    def get_candles_by_date(
        self, symbol: str, timeframe: Timeframe, from_date, to_date
    ) -> List[Dict]:
        rates = mt5.copy_rates_range(symbol, timeframe.value, from_date, to_date)
        return [r._asdict() for r in rates] if rates is not None else []
