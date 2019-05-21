from dataclasses import dataclass, field
from finsystem.logger import get_logger

log = get_logger('util')

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
    liab_total_funding: float = field(repr=False, init=False, metadata={'fitchcode': '2650'})
    liab_total_depmm_sterm_fund: float = field(repr=False, init=False, metadata={'fitchcode': '2580'})
    liab_cust_depo_curr: float = field(repr=False, init=False, metadata={'fitchcode': '2520'})
    liab_cust_depo_saving: float = field(repr=False, init=False, metadata={'fitchcode': '2530'})
    liab_cust_depo_term: float = field(repr=False, init=False, metadata={'fitchcode': '2540'})
    liab_depo_fr_bank: float = field(repr=False, init=False, metadata={'fitchcode': '2560'})
    liab_repo_cash_coll: float = field(repr=False, init=False, metadata={'fitchcode': '2565'})
    liab_otr_depo_sterm_brrow: float = field(repr=False, init=False, metadata={'fitchcode': '2570'})
    liab_total_lterm_fund: float = field(repr=False, init=False, metadata={'fitchcode': '2620'})
    liab_snir_debt_after1yr: float = field(repr=False, init=False, metadata={'fitchcode': '2590'})
    liab_subord_brrow: float = field(repr=False, init=False, metadata={'fitchcode': '2600'})
    liab_otr_funding: float = field(repr=False, init=False, metadata={'fitchcode': '2610'})
    liab_deriative: float = field(repr=False, init=False, metadata={'fitchcode': '2630'})
    liab_trad_liab:  float = field(repr=False, init=False, metadata={'fitchcode': '2640'})
    liab_crdt_impr_resv: float = field(repr=False, init=False, metadata={'fitchcode': '2680'})
    liab_resv_pens_otr: float = field(repr=False, init=False, metadata={'fitchcode': '2690'})
    liab_defr_tax_liab: float = field(repr=False, init=False, metadata={'fitchcode': '2700'})
    liab_disc_oper: float = field(repr=False, init=False, metadata={'fitchcode': '2720'})
    liab_fairval_port_debt: float = field(repr=False, init=False, metadata={'fitchcode': '2670'})
    liab_insu_liab: float = field(repr=False, init=False, metadata={'fitchcode': '2730'})
    liab_otr_defr_liab: float = field(repr=False, init=False, metadata={'fitchcode': '2710'})
    liab_otr_liab: float = field(repr=False, init=False, metadata={'fitchcode': '2740'})
    liab_curr_tax_liab: float = field(repr=False, init=False, metadata={'fitchcode': '2695'})

    equt_total_equity: float = field(repr=False, init=False, metadata={'fitchcode': '2840'})
    equt_comm_equity: float = field(repr=False, init=False, metadata={'fitchcode': '2800'})
    equt_non_cntr_intr: float = field(repr=False, init=False, metadata={'fitchcode': '2810'})
    equt_secu_reval_resv: float = field(repr=False, init=False, metadata={'fitchcode': '2820'})
    equt_fore_exch_reval_resv: float = field(repr=False, init=False, metadata={'fitchcode': '2825'})
    equt_fix_asst_reval_otr_accu: float = field(repr=False, init=False, metadata={'fitchcode': '2830'})


    def assign_values(self, vals):
        for _key in vals:
            self.__dict__[_key] = vals[_key]
        # self.asst_total_asset = vals['asst_total_asset'] if 'asst_total_asset' in vals.keys() else None
        # self.asst_total_earning_asset = vals['asst_total_earning_asset'] if 'asst_total_earning_asset' in vals.keys() else None
        # self.asst_net_loans = vals['asst_net_loans'] if 'asst_net_loans' in vals.keys() else None
        # self.asst_resid_mtge_loans = vals['asst_resid_mtge_loans'] if 'asst_resid_mtge_loans' in vals.keys() else None
        # self.asst_otr_mtge_loans = vals['asst_otr_mtge_loans'] if 'asst_otr_mtge_loans' in vals.keys() else None
        # self.asst_otr_cons_reta_loans = vals['asst_otr_cons_reta_loans'] if 'asst_otr_cons_reta_loans' in vals.keys() else None
        # self.asst_corp_comm_loans = vals['asst_corp_comm_loans'] if 'asst_corp_comm_loans' in vals.keys() else None
        # self.asst_otr_loans = vals['asst_otr_loans'] if 'asst_otr_loans' in vals.keys() else None
        # self.asst_less_rsv_impd_loans = vals['asst_less_rsv_impd_loans'] if 'asst_less_rsv_impd_loans' in vals.keys() else None
        # self.asst_loans_advc_banks = vals['asst_loans_advc_banks'] if 'asst_loans_advc_banks' in vals.keys() else None
        # self.asst_total_sec = vals['asst_total_sec'] if 'asst_total_sec' in vals.keys() else None
        # self.asst_revr_repo_cash_coll = vals['asst_revr_repo_cash_coll'] if 'asst_revr_repo_cash_coll' in vals.keys() else None
        # self.asst_trad_sec_fv_incm = vals['asst_trad_sec_fv_incm'] if 'asst_trad_sec_fv_incm' in vals.keys() else None
        # self.asst_derv_asst = vals['asst_derv_asst'] if 'asst_derv_asst' in vals.keys() else None
        # self.asst_aval_sale_sec = vals['asst_aval_sale_sec'] if 'asst_aval_sale_sec' in vals.keys() else None
        # self.asst_held_matu_sec = vals['asst_held_matu_sec'] if 'asst_held_matu_sec' in vals.keys() else None
        # self.asst_ateq_invs_asso = vals['asst_ateq_invs_asso'] if 'asst_ateq_invs_asso' in vals.keys() else None
        # self.asst_otr_sec = vals['asst_otr_sec'] if 'asst_otr_sec' in vals.keys() else None
        # self.asst_insu_asst = vals['asst_insu_asst'] if 'asst_insu_asst' in vals.keys() else None
        # self.asst_otr_earn_asst = vals['asst_otr_earn_asst'] if 'asst_otr_earn_asst' in vals.keys() else None
        # self.asst_inve_prop = vals['asst_inve_prop'] if 'asst_inve_prop' in vals.keys() else None
        # self.asst_cash_due_bank = vals['asst_cash_due_bank'] if 'asst_cash_due_bank' in vals.keys() else None
        # self.asst_foreclsd_real_este = vals['asst_foreclsd_real_este'] if 'asst_foreclsd_real_este' in vals.keys() else None
        # self.asst_fixd_asst = vals['asst_fixd_asst'] if 'asst_fixd_asst' in vals.keys() else None
        # self.asst_goodwill = vals['asst_goodwill'] if 'asst_goodwill' in vals.keys() else None
        # self.asst_otr_intangibles = vals['asst_otr_intangibles'] if 'asst_otr_intangibles' in vals.keys() else None
        # self.asst_defr_tax_asst = vals['asst_defr_tax_asst'] if 'asst_defr_tax_asst' in vals.keys() else None
        # self.asst_disc_operations = vals['asst_disc_operations'] if 'asst_disc_operations' in vals.keys() else None
        # self.asst_otr_assets = vals['asst_otr_assets'] if 'asst_otr_assets' in vals.keys() else None
        # self.asst_curr_tax_assets = vals['asst_curr_tax_assets'] if 'asst_curr_tax_assets' in vals.keys() else None
        # self.asst_total_impd_loans = vals['asst_total_impd_loans'] if 'asst_total_impd_loans' in vals.keys() else None

        # self.liab_total_liabilities = vals['liab_total_liabilities'] if 'liab_total_liabilities' in vals.keys() else None
        # self.liab_total_funding = vals['liab_total_funding'] if 'liab_total_funding' in vals.keys() else None
        # self.liab_total_depmm_sterm_fund = vals['liab_total_depmm_sterm_fund'] if 'liab_total_depmm_sterm_fund' in vals.keys() else None
        # self.liab_cust_depo_curr = vals['liab_cust_depo_curr'] if 'liab_cust_depo_curr' in vals.keys() else None
        # self.liab_cust_depo_saving = vals['liab_cust_depo_saving'] if 'liab_cust_depo_saving' in vals.keys() else None
        # self.liab_cust_depo_term = vals['liab_cust_depo_term'] if 'liab_cust_depo_term' in vals.keys() else None
        # self.liab_depo_fr_bank = vals['liab_depo_fr_bank'] if 'liab_depo_fr_bank' in vals.keys() else None
        # self.liab_repo_cash_coll = vals['liab_repo_cash_coll'] if 'liab_repo_cash_coll' in vals.keys() else None
        # self.liab_otr_depo_sterm_brrow = vals['liab_otr_depo_sterm_brrow'] if 'liab_otr_depo_sterm_brrow' in vals.keys() else None
        # self.liab_total_lterm_fund = vals['liab_total_lterm_fund'] if 'liab_total_lterm_fund' in vals.keys() else None
        # self.liab_snir_debt_after1yr = vals['liab_snir_debt_after1yr'] if 'liab_snir_debt_after1yr' in vals.keys() else None
        # self.liab_subord_brrow = vals['liab_subord_brrow'] if 'liab_subord_brrow' in vals.keys() else None
        # self.liab_otr_funding = vals['liab_otr_funding'] if 'liab_otr_funding' in vals.keys() else None
        # self.liab_deriative = vals['liab_deriative'] if 'liab_deriative' in vals.keys() else None
        # self.liab_trad_liab = vals['liab_trad_liab'] if 'liab_trad_liab' in vals.keys() else None
        # self.liab_crdt_impr_resv = vals['liab_crdt_impr_resv'] if 'liab_crdt_impr_resv' in vals.keys() else None
        # self.liab_resv_pens_otr = vals['liab_resv_pens_otr'] if 'liab_resv_pens_otr' in vals.keys() else None
        # self.liab_defr_tax_liab = vals['liab_defr_tax_liab'] if 'liab_defr_tax_liab' in vals.keys() else None
        # self.liab_disc_oper = vals['liab_disc_oper'] if 'liab_disc_oper' in vals.keys() else None
        # self.liab_fairval_port_debt = vals['liab_fairval_port_debt'] if 'liab_fairval_port_debt' in vals.keys() else None
        # self.liab_insu_liab = vals['liab_insu_liab'] if 'liab_insu_liab' in vals.keys() else None
        # self.liab_otr_defr_liab = vals['liab_otr_defr_liab'] if 'liab_otr_defr_liab' in vals.keys() else None
        # self.liab_otr_liab = vals['liab_otr_liab'] if 'liab_otr_liab' in vals.keys() else None
        # self.liab_curr_tax_liab = vals['liab_curr_tax_liab'] if 'liab_curr_tax_liab' in vals.keys() else None

        # self.equt_comm_equity = vals['equt_comm_equity'] if 'equt_comm_equity' in vals.keys() else None
        # self.equt_total_equity = vals['equt_total_equity'] if 'equt_total_equity' in vals.keys() else None
        # self.equt_non_cntr_intr = vals['equt_non_cntr_intr'] if 'equt_non_cntr_intr' in vals.keys() else None
        # self.equt_secu_reval_resv = vals['equt_secu_reval_resv'] if 'equt_secu_reval_resv' in vals.keys() else None
        # self.equt_fore_exch_reval_resv = vals['equt_fore_exch_reval_resv'] if 'equt_fore_exch_reval_resv' in vals.keys() else None
        # self.equt_fix_asst_reval_otr_accu = vals['equt_fix_asst_reval_otr_accu'] if 'equt_fix_asst_reval_otr_accu' in vals.keys() else None
