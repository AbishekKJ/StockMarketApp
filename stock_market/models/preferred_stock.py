from decimal import Decimal

from stock_market.models.stock import Stock


class PreferredStock(Stock):
    """A preferred stock implementation"""

    def __init__(self, symbol: str, last_dividend: Decimal, fixed_dividend: Decimal, par_value: Decimal):
        super().__init__(symbol, par_value)
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend

    def calculate_dividend_yield(self, price: Decimal) -> Decimal:
        """Calculate the dividend yield for preferred stock."""
        return (self.fixed_dividend * self.par_value) / price if price > 0 else 0

    def get_last_dividend(self) -> float:
        """Return the last dividend for preferred stock."""
        return self.last_dividend
