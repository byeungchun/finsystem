from dataclasses import dataclass, field
from finsystem.logger import get_logger

log = get_logger('util')

@dataclass
class BalanceSheet:
    asst_total_asset: float = field(repr=False, init=False, metadata={'fitchcode': '2350'})
    liab_total_liabilities: float = field(repr=False, init=False, metadata={'fitchcode': '2750'})
    equt_total_equity: float = field(repr=False, init=False, metadata={'fitchcode': '2840'})
