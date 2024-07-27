from enum import Enum, auto

__author__ = "nap"
__copyright__ = "nap"
__license__ = "MIT"


class Side(Enum):
    """
    Enum for side of the order.
    There are two sides:
    1. Buy
    2. Sell
    Order book is a representation of current market BUY and SELL orders.
    """

    BUY = auto()
    SELL = auto()


class TimeInForce(Enum):
    """
    Time in force represents a order's effective time.
    There are several common ones:
    1. GTC - Good till cancel
    2. GFD - Good for day
    3. FAK - Fill and Kill
    4. FOK - Fill or Kill
    Since we only planning to support single day orders, at current stage,
    we omit GTD(Good till day).
    See: https://www.jpx.co.jp/english/derivatives/rules/order-types/index.html
    """

    GTC = auto()
    GFD = auto()
    FAK = auto()
    FOK = auto()
