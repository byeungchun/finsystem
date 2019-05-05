from dataclasses import dataclass, field
from finsystem.logger import get_logger

log = get_logger('util')

@dataclass
class BalanceSheet:
    _asst_total_asset: float = field(repr=False, init=False, metadata={'fitchcode': '2350'})
    _liab_total_liabilities: float = field(repr=True, init=False, metadata={'fitchcode': '2750'})
    _equt_total_equity: float = field(repr=True, init=False, metadata={'fitchcode': '2840'})

    @property
    def asst_total_asset(self) -> float:
        return self._asst_total_asset

    @asst_total_asset.setter
    def asst_total_asset(self, asst_total_asset: float):
        try:
            float(str(asst_total_asset))
        except ValueError:
            log.error('input asst_total_asset({0}) is not float'.format(asst_total_asset))
            raise
        else:
            self._asst_total_asset = asst_total_asset
