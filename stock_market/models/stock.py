from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from decimal import Decimal

from stock_market.enums import TradeType
from stock_market.models.trade import Trade

import logging

logger = logging.getLogger(__name__)


class Stock(ABC):
    """Abstract base class for stocks."""

    def __init__(self, symbol: str, par_value: Decimal):
        self.symbol = symbol
        self.par_value = par_value
        self.trades = []

    @abstractmethod
    def calculate_dividend_yield(self, price: Decimal) -> Decimal:
        """Calculate the dividend yield for a given price"""
        pass

    def calculate_pe_ratio(self, price: Decimal) -> Decimal:
        """Calculate the P/E Ratio for a given price."""
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        last_dividend = self.get_last_dividend()
        return price / last_dividend if last_dividend > 0 else Decimal("inf")

    @abstractmethod
    def get_last_dividend(self) -> Decimal:
        """Retrieve the last dividend value."""
        pass

    def record_trade(self, quantity: int, trade_type: TradeType, price: Decimal) -> None:
        """Record a trade with the specified parameters."""
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be greater than 0")
        trade = Trade(datetime.now(), quantity, trade_type, price)
        self.trades.append(trade)
        logger.info(f"Recorded {self.symbol} trade: {trade_type.value} {quantity} @ {price}")

    def calculate_volume_weighted_stock_price(self) -> Decimal:
        """Calculate the Volume Weighted Stock Price based on trades in the last 5 minutes."""
        if not self.trades:
            raise ValueError("No trades available to calculate VWSP")
        current_time = datetime.now()
        relevant_trades = [
            trade for trade in self.trades
            if current_time - trade.timestamp <= timedelta(minutes=5)
        ]
        total_trade_value = sum(Decimal(trade.price) * Decimal(trade.quantity) for trade in relevant_trades)
        total_quantity = sum(Decimal(trade.quantity) for trade in relevant_trades)
        return total_trade_value / total_quantity if total_quantity > 0 else 0
