import pytest

from lobpy.common.contract import Stock
from lobpy.common.order import LimitOrder, MarketOrder
from lobpy.util.constant import Side, TimeInForce

__author__ = "nap"
__copyright__ = "nap"
__license__ = "MIT"


def test_market_order_none_param():
    id = 1
    stock = Stock(name="7203", lot_size=100)
    size = 200
    side = Side.SELL
    time_in_force = TimeInForce.GFD
    try:
        MarketOrder(
            id=None, contract=stock, size=size, side=side, time_in_force=time_in_force
        )
    except Exception:
        pytest.fail("Unexpected Error")
    with pytest.raises(ValueError):
        MarketOrder(
            id=id, contract=None, size=size, side=side, time_in_force=time_in_force
        )
    with pytest.raises(ValueError):
        MarketOrder(
            id=id, contract=stock, size=None, side=side, time_in_force=time_in_force
        )
    with pytest.raises(ValueError):
        MarketOrder(id=id, contract=stock, size=size, side=side, time_in_force=None)


def test_market_order():
    id = 1
    stock = Stock(name="7203", lot_size=100)
    size = 200
    side = Side.SELL
    time_in_force = TimeInForce.GFD
    mo = MarketOrder(
        id=id, contract=stock, size=size, side=side, time_in_force=time_in_force
    )
    assert mo.id == id
    assert mo.contract == stock
    assert mo.size == size
    assert mo.side == side
    assert mo.time_in_force == time_in_force


def test_market_order_copy():
    id = 1
    stock = Stock(name="7203", lot_size=100)
    size = 200
    side = Side.SELL
    time_in_force = TimeInForce.GFD
    mo = MarketOrder(
        id=id, contract=stock, size=size, side=side, time_in_force=time_in_force
    )
    size1 = 300
    mo1 = mo.copy(size=size1)
    assert mo1.id == id
    assert mo1.contract == stock
    assert mo1.size == size1
    assert mo1.side == side
    assert mo1.time_in_force == time_in_force

    mo2 = mo.copy(traded=100)
    assert mo2.traded == 100


def test_limit_order():
    id = 1
    stock = Stock(name="7203", lot_size=100)
    size = 200
    price = 100
    side = Side.SELL
    time_in_force = TimeInForce.GFD
    mo = LimitOrder(
        id=id,
        contract=stock,
        size=size,
        side=side,
        time_in_force=time_in_force,
        price=price,
    )
    assert mo.id == id
    assert mo.contract == stock
    assert mo.size == size
    assert mo.side == side
    assert mo.time_in_force == time_in_force
    assert mo.price == price


def test_limit_order_none_param():
    id = 1
    stock = Stock(name="7203", lot_size=100)
    size = 200
    side = Side.SELL
    time_in_force = TimeInForce.GFD
    with pytest.raises(ValueError):
        LimitOrder(
            id=id,
            contract=stock,
            size=size,
            price=None,
            side=side,
            time_in_force=time_in_force,
        )


# def test_main(capsys):
#     """CLI Tests"""
#     # capsys is a pytest fixture that allows asserts against stdout/stderr
#     # https://docs.pytest.org/en/stable/capture.html
#     main(["7"])
#     captured = capsys.readouterr()
#     assert "The 7-th Fibonacci number is 13" in captured.out
