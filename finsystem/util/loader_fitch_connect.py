import math
import datetime
import pandas as pd
from typing import List
from dataclasses import fields

from finsystem.entity.finstmt import BalanceSheet
from finsystem.entity.fininst import Bank
from finsystem.logger import get_logger


def load_raw_file(fc_data, fc_mapping):
    """
    fc_data format should be Excel. fc_mapping contains fitch connect codes.
    
    """
    
    fmap = dict(map(lambda y: (y[1],y[0]), [x.rstrip().split(',') for x in open(mapping_file,'r')]))
    fdf = pd.read_excel(sample_file)
    
    return fmap, fdf


def generate_institution_class(fmap, fdf):
    default_col = ['Fitch_Entity_Id','Issuer_Name','Fitch_Country_Code','Agent_LEI','Swift_BIC','Period_Type','Period_Date']
    fcol = [fmap[x.metadata.get('fitchcode')] for x in fields(BalanceSheet) if x.metadata.get('fitchcode') is not None]   
    fdf_sel = fdf.loc[:, default_col+fcol]

    banks = list()
    for fitch_id in fdf_sel.Fitch_Entity_Id.drop_duplicates():
        # Extract one instituion about annual data
        df = fdf_sel[(fdf_sel.Fitch_Entity_Id == fitch_id) & (fdf_sel.Period_Type == 0)] 
        _name = df.Issuer_Name.drop_duplicates()
        _country = df.Fitch_Country_Code.drop_duplicates()
        _lei = df.Agent_LEI.drop_duplicates()
        _bic = df.Swift_BIC.drop_duplicates()

        for _val in [_name,_country,_lei,_bic]:
            if len(_val) > 1: 
                logger.error('more than two values per one fitch id {0}'.format(_val.to_string()))

        bank = Bank(_name.iloc[0], _country.iloc[0])
        if type(_lei.iloc[0]) == str: 
            bank.lei = _lei.iloc[0]
        if type(_bic.iloc[0]) == str:
            bank.bic = _bic.iloc[0]

        balancesheets = list()
        for rindex in df.index:
            balancesheet = BalanceSheet('Y', df.loc[rindex]['Period_Date'].strftime('%Y%m%d'))
            vals = {'asst_total_asset': df.loc[rindex]['Total_Assets'],
                   'liab_total_liabilities': df.loc[rindex]['Total_Liabilities_excl_Pref_Shares_and_Hybrid_Capital_accounted_for_as_Debt'],
                   'equt_total_equity': df.loc[rindex]['Total_Equity_excluding_Pref_Shares_and_Hybrid_Capital_accounted_for_as_Equity']}
            balancesheet.assign_values(vals) 
            balancesheets.append(balancesheet)

        bank.balance_sheet = balancesheets
        banks.append(bank)
        
    return banks
