import pytest
from decimal import Decimal
from datetime import datetime, timedelta
from stock_market.models.preferred_stock import PreferredStock
from stock_market.enums import TradeType
from stock_market.models.trade import Trade


# Fixture for PreferredStock
@pytest.fixture
def preferred_stock():
    return PreferredStock(symbol="GIN", par_value=Decimal("100"), last_dividend=Decimal("2"),
                          fixed_dividend=Decimal("2"))


# Test for calculating dividend yield
def test_preferred_stock_dividend_yield(preferred_stock):
    price = Decimal("100")
    expected_dividend_yield = (preferred_stock.fixed_dividend / 100 * preferred_stock.par_value) / price
    assert preferred_stock.calculate_dividend_yield(price) == expected_dividend_yield


# Test for calculating P/E ratio
def test_preferred_stock_pe_ratio(preferred_stock):
    price = Decimal("100")
    expected_pe_ratio = price / preferred_stock.last_dividend
    assert preferred_stock.calculate_pe_ratio(price) == expected_pe_ratio


# Test for recording a trade without mocking
def test_record_trade(preferred_stock):
    # Initially, there should be no trades
    assert len(preferred_stock.trades) == 0

    # Record a trade
    quantity = 10
    trade_type = TradeType.BUY
    price = Decimal("105")
    preferred_stock.record_trade(quantity=quantity, trade_type=trade_type, price=price)

    # There should be one trade recorded now
    assert len(preferred_stock.trades) == 1

    # The recorded trade should have the correct properties
    trade = preferred_stock.trades[0]
    assert trade.quantity == quantity
    assert trade.trade_type == trade_type
    assert trade.price == price

    # Check if the trade timestamp is close to the current time
    time_difference = datetime.now() - trade.timestamp
    assert time_difference.total_seconds() < 1  # Ensure the trade timestamp is within 1 second of the current time


# Test for calculating volume-weighted stock price
def test_calculate_volume_weighted_stock_price(preferred_stock):
    # Adding trades
    trade1 = Trade(datetime.now() - timedelta(minutes=1), 100, TradeType.BUY, Decimal("105"))
    trade2 = Trade(datetime.now() - timedelta(minutes=3), 150, TradeType.SELL, Decimal("110"))
    preferred_stock.trades = [trade1, trade2]

    expected_vwsp = (Decimal("105") * 100 + Decimal("110") * 150) / (100 + 150)
    assert preferred_stock.calculate_volume_weighted_stock_price() == expected_vwsp
