import MetaTrader5 as mt5
from typing import Optional, List, Dict

class MT5Client:
    """Simple wrapper around the MetaTrader5 package."""

    def __init__(self, login: int, password: str, server: str) -> None:
        self.login = login
        self.password = password
        self.server = server

    def connect(self) -> bool:
        """Initialize connection with provided credentials."""
        return mt5.initialize(login=self.login, password=self.password, server=self.server)

    def shutdown(self) -> None:
        """Close connection to MetaTrader5 terminal."""
        mt5.shutdown()

    def is_connected(self) -> bool:
        """Check if connection to MetaTrader5 terminal is active."""
        return mt5.terminal_info() is not None

    def account_info(self) -> Optional[Dict]:
        info = mt5.account_info()
        return info._asdict() if info else None

    def positions(self) -> List[Dict]:
        positions = mt5.positions_get()
        return [p._asdict() for p in positions] if positions else []

    def get_rates(self, symbol: str, timeframe: int, start_pos: int, count: int) -> List[Dict]:
        """Retrieve historical rates from the terminal."""
        rates = mt5.copy_rates_from_pos(symbol, timeframe, start_pos, count)
        return [r._asdict() for r in rates] if rates is not None else []

    def send_market_order(self, symbol: str, volume: float, order_type: int, comment: str = "") -> Optional[Dict]:
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(request)
        return result._asdict() if result else None
