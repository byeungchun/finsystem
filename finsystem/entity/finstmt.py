from dataclasses import dataclass, field
from finsystem.logger import get_logger

log = get_logger('util')

#def validate_input_values(val,)

@dataclass
class BalanceSheet:
    release_freq: str
    release_date: str # format: yyyymmdd
    asst_total_asset: float = field(repr=False, init=False, metadata={'fitchcode': '2350'})
    liab_total_liabilities: float = field(repr=False, init=False, metadata={'fitchcode': '2750'})
    equt_total_equity: float = field(repr=False, init=False, metadata={'fitchcode': '2840'})

    def assign_values(self, vals):
        self.asst_total_asset = vals['asst_total_asset'] if 'asst_total_asset' in vals.keys() else None
        self.liab_total_liabilities = vals['liab_total_liabilities'] if 'liab_total_liabilities' in vals.keys() else None
        self.equt_total_equity = vals['equt_total_equity'] if 'equt_total_equity' in vals.keys() else None