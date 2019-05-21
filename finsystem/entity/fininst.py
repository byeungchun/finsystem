from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List

from .finstmt import BalanceSheet
from .mapping import *

@dataclass
class FinancialInstitution(ABC):
    issuer_name: str
    country_code: str
    fitch_id: str = field(init=False, default=None)
    lei: str = field(init=False, default=None)
    mkt_sec: str = field(init=False, default=None)
    balance_sheet: List[BalanceSheet] = field(repr=False, init=False)
    
    @abstractmethod
    def generate_balancesheet(self):
        pass
    
    def __post_init__(self):
        self.mkt_sec = mkt_sector_key(self.mkt_sec)

    
class Bank(FinancialInstitution):
    swift_bic: str = field(init=False, default=None)

    def generate_balancesheet(self):
        print('generate balance sheet')

