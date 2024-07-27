from lobpy.common.contract import Stock
from lobpy.common.order import MarketOrder
from lobpy.util.constant import Side, TimeInForce

__author__ = "nap"
__copyright__ = "nap"
__license__ = "MIT"


def test_order_instantiation():
    id = 1
    stock = Stock(name="7203", lot_size=100)
    size = 200
    side = Side.SELL
    time_in_force = TimeInForce.GFD
    mo = MarketOrder(
        id=id,
        sym=stock,
        size=size,
        side=side,
        time_in_force=time_in_force
    )
    assert mo.id == id
    assert mo.sym == stock
    assert mo.size == size
    assert mo.side == side
    assert mo.time_in_force == time_in_force


# def test_main(capsys):
#     """CLI Tests"""
#     # capsys is a pytest fixture that allows asserts against stdout/stderr
#     # https://docs.pytest.org/en/stable/capture.html
#     main(["7"])
#     captured = capsys.readouterr()
#     assert "The 7-th Fibonacci number is 13" in captured.out
