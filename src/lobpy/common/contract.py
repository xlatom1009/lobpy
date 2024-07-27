
import dataclasses


class Contract:
    pass


@dataclasses.dataclass(frozen=True, kw_only=True)
class Stock(Contract):
    name: str
    lot_size: int
