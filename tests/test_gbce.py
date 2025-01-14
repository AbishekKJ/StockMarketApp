import pytest
from decimal import Decimal, getcontext
from stock_market.models.common_stock import CommonStock
from stock_market.models.preferred_stock import PreferredStock
from stock_market.enums import TradeType
from stock_market.gbce import GBCE


# Fixture for GBCE
@pytest.fixture
def gbce():
    return GBCE()


# Fixture for CommonStock
@pytest.fixture
def common_stock():
    return CommonStock(symbol="TEA", par_value=Decimal("100"), last_dividend=Decimal("8"))


# Fixture for PreferredStock
@pytest.fixture
def preferred_stock():
    return PreferredStock(symbol="GIN", par_value=Decimal("100"), last_dividend=Decimal("2"),
                          fixed_dividend=Decimal("0.02"))


# Test for adding stocks to the GBCE
def test_add_stock(gbce, common_stock, preferred_stock):
    assert len(gbce.stocks) == 0
    gbce.add_stock(common_stock)
    gbce.add_stock(preferred_stock)
    assert len(gbce.stocks) == 2
    assert gbce.stocks[0] == common_stock
    assert gbce.stocks[1] == preferred_stock


# Test for calculating the geometric mean
def test_calculate_geometric_mean():
    values = [Decimal("100"), Decimal("200"), Decimal("300")]
    expected_mean = Decimal((100 * 200 * 300) ** (1 / 3))
    result = GBCE.calculate_geometric_mean(values)
    # Set a small tolerance for comparing the results (e.g., 1e-10)
    tolerance = Decimal('0.0000000001')
    assert abs(result - expected_mean) <= tolerance, f"Expected: {expected_mean}, Got: {result}"


# Test for calculating GBCE All Share Index with trades
def test_calculate_gbce_all_share_index(gbce, common_stock, preferred_stock):
    gbce.add_stock(common_stock)
    gbce.add_stock(preferred_stock)
    common_stock.record_trade(quantity=10, trade_type=TradeType.BUY, price=Decimal("105"))
    preferred_stock.record_trade(quantity=5, trade_type=TradeType.BUY, price=Decimal("110"))
    index = gbce.calculate_gbce_all_share_index()
    vwsp_common = common_stock.calculate_volume_weighted_stock_price()
    vwsp_preferred = preferred_stock.calculate_volume_weighted_stock_price()
    expected_index = GBCE.calculate_geometric_mean([vwsp_common, vwsp_preferred])

    assert index == expected_index


# Test for calculating GBCE All Share Index when there are no trades
def test_calculate_gbce_all_share_index_no_trades(gbce, common_stock, preferred_stock):
    gbce.add_stock(common_stock)
    gbce.add_stock(preferred_stock)
    index = gbce.calculate_gbce_all_share_index()
    assert index == 0
