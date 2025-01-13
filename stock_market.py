import logging
from stock_market.models.common_stock import CommonStock
from stock_market.models.preferred_stock import PreferredStock
from stock_market.gbce import GBCE
from stock_market.enums import TradeType

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    # Initialize stocks
    tea = CommonStock("TEA", 0, 100)
    pop = CommonStock("POP", 8, 100)
    gin = PreferredStock("GIN", 8, 0.02, 100)
    ale = CommonStock("ALE", 8, 100)
    joe = CommonStock("JOE", 13,250)

    # Record trades
    tea.record_trade(100, TradeType.BUY, 105)
    pop.record_trade(200, TradeType.SELL, 120)
    gin.record_trade(150, TradeType.BUY, 130)

    # Market Service and GBCE Index Calculation
    market_service = GBCE()
    market_service.add_stock(tea)
    market_service.add_stock(pop)
    market_service.add_stock(gin)

    # Log results instead of printing
    logging.info(f"TEA Dividend Yield (price=105): {tea.calculate_dividend_yield(105)}")
    logging.info(f"POP P/E Ratio (price=120): {pop.calculate_pe_ratio(120)}")
    logging.info(f"GIN Volume Weighted Stock Price: {gin.calculate_volume_weighted_stock_price()}")
    logging.info(f"GBCE All Share Index: {market_service.calculate_gbce_all_share_index()}")
