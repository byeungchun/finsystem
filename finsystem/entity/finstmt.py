from dataclasses import dataclass, field
from finsystem.logger import get_logger

log = get_logger('util')

#def validate_input_values(val,)

@dataclass
class BalanceSheet:
    release_freq: str
    release_date: str # format: yyyymmdd
    asst_total_asset: float = field(repr=False, init=False, metadata={'fitchcode': '2350'})
    asst_total_earning_asset: float = field(repr=False, init=False, metadata={'fitchcode': '2250'})
    asst_net_loans: float = field(repr=False, init=False, metadata={'fitchcode': '2090'})
    asst_resid_mtge_loans: float = field(repr=False, init=False, metadata={'fitchcode': '2040'})
    asst_otr_mtge_loans: float = field(repr=False, init=False, metadata={'fitchcode': '2045'})
    asst_otr_cons_reta_loans: float = field(repr=False, init=False, metadata={'fitchcode': '2050'})
    asst_corp_comm_loans: float = field(repr=False, init=False, metadata={'fitchcode': '2060'})
    asst_otr_loans: float = field(repr=False, init=False, metadata={'fitchcode': '2070'})
    asst_less_rsv_impd_loans: float = field(repr=False, init=False, metadata={'fitchcode': '2080'})
    asst_loans_advc_banks: float = field(repr=False, init=False, metadata={'fitchcode': '2140'})
    asst_total_sec: float = field(repr=False, init=False, metadata={'fitchcode': '2210'})
    asst_revr_repo_cash_coll: float = field(repr=False, init=False, metadata={'fitchcode': '2145'})
    asst_trad_sec_fv_incm: float = field(repr=False, init=False, metadata={'fitchcode': '2150'})
    asst_derv_asst: float = field(repr=False, init=False, metadata={'fitchcode': '2160'})
    asst_aval_sale_sec: float = field(repr=False, init=False, metadata={'fitchcode': '2170'})
    asst_held_matu_sec: float = field(repr=False, init=False, metadata={'fitchcode': '2180'})
    asst_ateq_invs_asso: float = field(repr=False, init=False, metadata={'fitchcode': '2190'})
    asst_otr_sec: float = field(repr=False, init=False, metadata={'fitchcode': '2200'})
    asst_insu_asst: float = field(repr=False, init=False, metadata={'fitchcode': '2230'})
    asst_otr_earn_asst: float = field(repr=False, init=False, metadata={'fitchcode': '2240'})
    asst_inve_prop: float = field(repr=False, init=False, metadata={'fitchcode': '2220'})
    asst_cash_due_bank: float = field(repr=False, init=False, metadata={'fitchcode': '2270'})
    asst_foreclsd_real_este: float = field(repr=False, init=False, metadata={'fitchcode': '2280'})
    asst_fixd_asst: float = field(repr=False, init=False, metadata={'fitchcode': '2290'})
    asst_goodwill: float = field(repr=False, init=False, metadata={'fitchcode': '2300'})
    asst_otr_intangibles: float = field(repr=False, init=False, metadata={'fitchcode': '2310'})
    asst_defr_tax_asst: float = field(repr=False, init=False, metadata={'fitchcode': '2320'})
    asst_disc_operations: float = field(repr=False, init=False, metadata={'fitchcode': '2330'})
    asst_otr_assets: float = field(repr=False, init=False, metadata={'fitchcode': '2340'})
    asst_curr_tax_assets: float = field(repr=False, init=False, metadata={'fitchcode': '2315'})
    asst_total_impd_loans: float = field(repr=False, init=False, metadata={'fitchcode': '2127'})

    liab_total_liabilities: float = field(repr=False, init=False, metadata={'fitchcode': '2750'})
    equt_total_equity: float = field(repr=False, init=False, metadata={'fitchcode': '2840'})


    def assign_values(self, vals):
        self.asst_total_asset = vals['asst_total_asset'] if 'asst_total_asset' in vals.keys() else None
        self.liab_total_liabilities = vals['liab_total_liabilities'] if 'liab_total_liabilities' in vals.keys() else None
        self.equt_total_equity = vals['equt_total_equity'] if 'equt_total_equity' in vals.keys() else None