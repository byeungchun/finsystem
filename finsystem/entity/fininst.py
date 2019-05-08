from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List

from .finstmt import BalanceSheet

@dataclass
class FinancialInstitution(ABC):
    issuer_name: str
    country_code: str
    lei: str = field(init=False, default=None)
    swift_bic: str = field(init=False, default=None)
    balance_sheet: List[BalanceSheet] = field(repr=False, init=False)
    
    @abstractmethod
    def generate_balancesheet(self):
        pass

    
class Bank(FinancialInstitution):
    
    def generate_balancesheet(self):
        print('generate balance sheet')

