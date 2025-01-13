from datetime import datetime
from decimal import Decimal

from stock_market.enums import TradeType


class Trade:
    """Represents a trade in the stock market."""
    def __init__(self, timestamp: datetime, quantity: int, trade_type: TradeType, price: Decimal):
        self.timestamp = timestamp
        self.quantity = quantity
        self.trade_type = trade_type
        self.price = price
