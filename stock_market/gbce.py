from decimal import Decimal
from functools import reduce
from typing import List
from stock_market.models.stock import Stock


class GBCE:
    """Service for managing stock market operations - GBCE."""

    def __init__(self):
        self.stocks = []

    def add_stock(self, stock: Stock) -> None:
        """Add a stock to the market."""
        self.stocks.append(stock)

    @staticmethod
    def calculate_geometric_mean(values: List[Decimal]) -> Decimal:
        """Calculate the geometric mean of a list of Decimal values."""
        if not values:
            raise ValueError("Values list cannot be empty for geometric mean calculation")

        product = reduce(lambda x, y: x * y, values)
        n = len(values)
        return product ** (Decimal(1) / Decimal(n))

    def calculate_gbce_all_share_index(self) -> Decimal:
        """Calculate the GBCE All Share Index."""
        vwsp_values = [stock.calculate_volume_weighted_stock_price() for stock in self.stocks if stock.trades]
        if not vwsp_values:
            return 0
        return self.calculate_geometric_mean(vwsp_values)
