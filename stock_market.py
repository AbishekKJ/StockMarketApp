import logging
import random
from decimal import Decimal
from datetime import datetime, timedelta
from stock_market.models.common_stock import CommonStock
from stock_market.models.preferred_stock import PreferredStock
from stock_market.gbce import GBCE
from stock_market.enums import TradeType
from stock_market.exceptions import NoTradesAvailableError
from config import USE_INPUT_DATA

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def preload_data():
    """Preload sample stock data with random trades."""
    tea = CommonStock("TEA", Decimal("0"), Decimal("100"))
    pop = CommonStock("POP", Decimal("8"), Decimal("100"))
    gin = PreferredStock("GIN", Decimal("8"), Decimal("2"), Decimal("100"))
    ale = CommonStock("ALE", Decimal("23"), Decimal("60"))
    joe = CommonStock("JOE", Decimal("13"), Decimal("250"))

    stocks = [tea, pop, gin, ale, joe]

    # Preload 5 random trades for each stock
    for stock in stocks:
        for _ in range(5):
            quantity = random.randint(10, 200)
            trade_type = random.choice(list(TradeType))
            price = Decimal(random.uniform(90, 150)).quantize(Decimal("0.01"))
            timestamp_offset = random.randint(0, 4)
            trade_timestamp = datetime.now() - timedelta(minutes=timestamp_offset)

            # Record the trade directly
            stock.trades.append({
                "timestamp": trade_timestamp,
                "quantity": quantity,
                "trade_type": trade_type,
                "price": price
            })
            logging.info(f"Preloaded trade for {stock.symbol}: {trade_type.value} {quantity} @ {price}")

    return stocks


def display_menu():
    """Display user options for interactive input."""
    print("\nSelect an option:")
    print("1. Add a trade")
    print("2. Calculate Dividend Yield")
    print("3. Calculate P/E Ratio")
    print("4. Calculate VWSP")
    print("5. Calculate GBCE All Share Index")
    print("6. Exit")


def handle_user_input(stocks, market_service):
    """Handle user actions for stock operations."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol (TEA, POP, GIN, ALE, JOE): ").upper()
            stock = next((s for s in stocks if s.symbol == symbol), None)
            if not stock:
                print(f"No stock found with symbol {symbol}.")
                continue
            quantity = int(input("Enter quantity: "))
            trade_type = TradeType[input("Enter trade type (BUY/SELL): ").upper()]
            price = Decimal(input("Enter price: "))
            stock.record_trade(quantity, trade_type, price)

        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            price = Decimal(input("Enter price: "))
            stock = next((s for s in stocks if s.symbol == symbol), None)
            if not stock:
                print(f"No stock found with symbol {symbol}.")
                continue
            print(f"{symbol} Dividend Yield: {stock.calculate_dividend_yield(price)}")

        elif choice == "3":
            symbol = input("Enter stock symbol: ").upper()
            price = Decimal(input("Enter price: "))
            stock = next((s for s in stocks if s.symbol == symbol), None)
            if not stock:
                print(f"No stock found with symbol {symbol}.")
                continue
            print(f"{symbol} P/E Ratio: {stock.calculate_pe_ratio(price)}")

        elif choice == "4":
            symbol = input("Enter stock symbol: ").upper()
            stock = next((s for s in stocks if s.symbol == symbol), None)
            if not stock:
                print(f"No stock found with symbol {symbol}.")
                continue
            try:
                print(f"{symbol} VWSP: {stock.calculate_volume_weighted_stock_price()}")
            except NoTradesAvailableError as e:
                print(f"Error: {e}")

        elif choice == "5":
            try:
                gbce_index = market_service.calculate_gbce_all_share_index()
                print(f"GBCE All Share Index: {gbce_index}")
            except NoTradesAvailableError as e:
                print(f"Error: {e}")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Load stocks based on configuration
    stocks = preload_data() if not USE_INPUT_DATA else []

    if USE_INPUT_DATA:
        logging.info("Please enter trade and calculation data via the input menu.")
    else:
        logging.info("Preloaded data mode activated.")

    # Market Service Initialization
    market_service = GBCE()
    for stock in stocks:
        market_service.add_stock(stock)

    # Interactive user input handling
    handle_user_input(stocks, market_service)
