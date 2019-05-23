import math
import datetime
import pandas as pd
from typing import List
from dataclasses import fields

from finsystem.entity.finstmt import BalanceSheet
from finsystem.entity.fininst import Bank
from finsystem.logger import get_logger

log = get_logger('util')

def load_raw_file(fc_data, fc_mapping):
    """
    fc_data format should be tab seperated txt file. fc_mapping contains fitch connect codes.
    
    Arguments:
        fc_data {[type]} -- [description]
        fc_mapping {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    
    fmap = dict(map(lambda y: (y[1],y[0]), [x.rstrip().split(',') for x in open(fc_mapping,'r')]))
    fdf = pd.read_csv(fc_data, sep='\t')
    fdf.Period_Date = pd.to_datetime(fdf.Period_Date)
    return fmap, fdf


def create_bank(fmap, fdf, maxrow=None):
    """[summary]
    
    Arguments:
        fmap {[type]} -- [description]
        fdf {[type]} -- [description]
    
    Keyword Arguments:
        maxrow {[type]} -- [description] (default: {None})
    
    Returns:
        [type] -- [description]
    """
    default_col = ['Fitch_Entity_Id','Issuer_Name','Fitch_Country_Code','Agent_LEI','Swift_BIC','Period_Type','Period_Date','Market_Sector_Description']
    #fcol = [fmap[x.metadata.get('fitchcode')] for x in fields(BalanceSheet) if x.metadata.get('fitchcode') is not None]
    fcol = dict()
    for _field in fields(BalanceSheet):
        if _field.metadata.get('fitchcode') is None:
            continue
        else:
            fcol[_field.name] = fmap[_field.metadata.get('fitchcode')]
    fdf_sel = fdf.loc[:, default_col+list(fcol.values())]

    banks = list()
    for i, fitch_id in enumerate(fdf_sel.Fitch_Entity_Id.drop_duplicates()):
        # Extract annual data rows for this institution
        df = fdf_sel[(fdf_sel.Fitch_Entity_Id == fitch_id) & (fdf_sel.Period_Type == 0)] 
        # If it is bigger than one row, it is error
        _fitch_id = df.Fitch_Entity_Id.drop_duplicates()
        _name = df.Issuer_Name.drop_duplicates()
        _country = df.Fitch_Country_Code.drop_duplicates()
        _lei = df.Agent_LEI.drop_duplicates()
        _bic = df.Swift_BIC.drop_duplicates()
        _mkt_sec = df.Market_Sector_Description.drop_duplicates()

        for _val in [_name,_country,_lei,_bic,_mkt_sec]:
            if len(_val) > 1: 
                log.error('more than two values per one fitch id {0}'.format(_val.to_string()))

        bank = Bank(_name.iloc[0], _country.iloc[0])
        bank.mkt_sec = _mkt_sec.iloc[0]
        bank.fitch_id = _fitch_id.iloc[0]
        if type(_lei.iloc[0]) == str: 
            bank.lei = _lei.iloc[0]
        if type(_bic.iloc[0]) == str:
            bank.bic = _bic.iloc[0]

        balancesheets = list()
        for rindex in df.index:
            balancesheet = BalanceSheet('Y', df.loc[rindex]['Period_Date'].strftime('%Y%m%d'))
            vals = dict()
            for _key in fcol:
                vals[_key] = df.loc[rindex][fcol[_key]]
            # vals = {'asst_total_asset': df.loc[rindex]['Total_Assets'],
            #        'liab_total_liabilities': df.loc[rindex]['Total_Liabilities_excl_Pref_Shares_and_Hybrid_Capital_accounted_for_as_Debt'],
            #        'equt_total_equity': df.loc[rindex]['Total_Equity_excluding_Pref_Shares_and_Hybrid_Capital_accounted_for_as_Equity']}
            balancesheet.assign_values(vals) 
            balancesheets.append(balancesheet)
        if (maxrow is not None) and (i == maxrow):
            break
        bank.balance_sheet = balancesheets
        banks.append(bank)
        
    return banks
