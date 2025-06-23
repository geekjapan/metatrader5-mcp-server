"""Trading operations for MetaTrader 5."""

from __future__ import annotations

from typing import List, Dict, Optional

import MetaTrader5 as mt5

from .client_connection import MT5Connection
from .types import OrderType


class MT5Order:
    def __init__(self, connection: MT5Connection) -> None:
        self._connection = connection

    def place_market_order(
        self, symbol: str, volume: float, order_type: OrderType, comment: str = ""
    ) -> Optional[Dict]:
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type.value,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(request)
        return result._asdict() if result else None

    def close_position(self, position_id: int, volume: float, order_type: OrderType) -> Optional[Dict]:
        position = mt5.positions_get(ticket=position_id)
        if not position:
            return None
        position = position[0]
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "position": position_id,
            "symbol": position.symbol,
            "volume": volume,
            "type": order_type.value,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(request)
        return result._asdict() if result else None

    def get_all_positions(self) -> List[Dict]:
        positions = mt5.positions_get()
        return [p._asdict() for p in positions] if positions else []
