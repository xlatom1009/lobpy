__author__ = "nap"
__copyright__ = "nap"
__license__ = "MIT"

import abc
import copy
import dataclasses
import uuid
from typing import Self

from lobpy.common.contract import Contract
from lobpy.util.constant import Side, TimeInForce
from lobpy.util.meta import EnforcedAttributeMeta


class OrderMeta(EnforcedAttributeMeta, abc.ABCMeta):
    """
    Component Meta
    Enforce child classes to have name, dependencies, builder and version.
    Also being able to have abstract methods.
    """

    pass


@dataclasses.dataclass(frozen=True, kw_only=True)
class OrderBase:
    id: str = None
    contract: Contract
    size: float
    side: Side
    traded: float = 0
    time_in_force: TimeInForce = TimeInForce.GTC

    def __post_init__(self) -> None:
        object.__setattr__(self, "id", self.id or uuid.uuid4())

    def _check_required_attributes(self):
        req_attrs = [self.id, self.contract, self.size, self.side, self.time_in_force]
        if any([(rt is None) for rt in req_attrs]):
            msg = "All required attributes must not be None."
            raise ValueError(msg)

    def copy(self, **changes) -> Self:
        order = copy.deepcopy(self)
        return dataclasses.replace(order, **changes)


@dataclasses.dataclass(frozen=True, kw_only=True)
class MarketOrder(OrderBase, metaclass=OrderMeta):
    """
    A market order is an instruction to buy or sell a security
      immediately at the current price.


    :param id: identifier of order
    :param contract: instrument identifier

    """

    pass


@dataclasses.dataclass(frozen=True, kw_only=True)
class LimitOrder(OrderBase, metaclass=OrderMeta):
    price: float

    def _check_required_attributes(self):
        super()._check_required_attributes()
        req_attrs = [self.price]
        if any([(rt is None) for rt in req_attrs]):
            msg = "All required attributes must not be None."
            raise ValueError(msg)
