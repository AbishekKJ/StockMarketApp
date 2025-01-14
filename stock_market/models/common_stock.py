from decimal import Decimal
from stock_market.models.stock import Stock


class CommonStock(Stock):
    """A common stock implementation"""

    def __init__(self, symbol: str, last_dividend: Decimal, par_value: Decimal):
        super().__init__(symbol, par_value)
        self.last_dividend = last_dividend

    def calculate_dividend_yield(self, price: Decimal) -> Decimal:
        """Calculate the dividend yield for common stock."""
        return self.last_dividend / price if price > 0 else 0

    def get_last_dividend(self) -> Decimal:
        """Return the last dividend for the common stock"""
        return self.last_dividend
