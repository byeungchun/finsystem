#encoding: utf-8

from finsystem.util.util import *
from finsystem.util.loader_fitch_connect import create_bank, load_raw_file
from finsystem.entity.fininst import BalanceSheet


def get_totalasset_by_country():
    """

    Return value can be convert to Pandas dataframe 
    ex. pd.DataFrame(lst_bs)
    """
    banks = load_banks_pickle()
    lst_bs = list()
    for _bank in banks:
        for _bs in _bank.balance_sheet:
            _val = _bs.__dict__.copy()
            for _key in ['issuer_name','fitch_id','country_code','mkt_sec']:
                _val[_key] = _bank.__dict__[_key]
            lst_bs.append(_val)
    return lst_bs
