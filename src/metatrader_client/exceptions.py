"""Custom exceptions for the MT5 client library."""


class MT5Error(Exception):
    """Base error for the library."""


class MT5ConnectionError(MT5Error):
    """Raised when connection to terminal fails."""


class MT5TradeError(MT5Error):
    """Raised on trading operation errors."""


class MT5SymbolError(MT5Error):
    """Symbol not found or invalid."""


class MT5TimeframeError(MT5Error):
    """Invalid timeframe specified."""


class MT5NotConnectedError(MT5Error):
    """Operation attempted without active connection."""
