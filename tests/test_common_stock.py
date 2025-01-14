import pytest
from datetime import datetime, timedelta
from decimal import Decimal
from stock_market.models.common_stock import CommonStock
from stock_market.models.trade import Trade
from stock_market.enums import TradeType


# Fixture for CommonStock
@pytest.fixture
def common_stock():
    return CommonStock(symbol="TEA", par_value=Decimal("100"), last_dividend=Decimal("8"))


# Test for calculating dividend yield
def test_common_stock_dividend_yield(common_stock):
    price = Decimal("100")
    expected_dividend_yield = common_stock.last_dividend / price
    assert common_stock.calculate_dividend_yield(price) == expected_dividend_yield


# Test for calculating P/E ratio
def test_common_stock_pe_ratio(common_stock):
    price = Decimal("100")
    expected_pe_ratio = price / common_stock.last_dividend
    assert common_stock.calculate_pe_ratio(price) == expected_pe_ratio


# Test for recording a trade
def test_record_trade(common_stock):
    # Initially, there should be no trades
    assert len(common_stock.trades) == 0

    # Record a trade
    quantity = 10
    trade_type = TradeType.BUY
    price = Decimal("105")
    common_stock.record_trade(quantity=quantity, trade_type=trade_type, price=price)

    # There should be one trade recorded now
    assert len(common_stock.trades) == 1

    # The recorded trade should have the correct properties
    trade = common_stock.trades[0]
    assert trade.quantity == quantity
    assert trade.trade_type == trade_type
    assert trade.price == price

    # Check if the trade timestamp is close to the current time
    time_difference = datetime.now() - trade.timestamp
    assert time_difference.total_seconds() < 1


# Test for calculating volume-weighted stock price
def test_calculate_volume_weighted_stock_price(common_stock):
    # Adding trades
    trade1 = Trade(datetime.now() - timedelta(minutes=1), 100, TradeType.BUY, Decimal("105"))
    trade2 = Trade(datetime.now() - timedelta(minutes=3), 150, TradeType.SELL, Decimal("110"))
    common_stock.trades = [trade1, trade2]

    expected_vwsp = (Decimal("105") * 100 + Decimal("110") * 150) / (100 + 150)
    assert common_stock.calculate_volume_weighted_stock_price() == expected_vwsp
