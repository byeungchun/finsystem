#encoding: utf-8

from finsystem.util.util import *
from finsystem.util.loader_fitch_connect import create_bank, load_raw_file
from finsystem.entity.fininst import BalanceSheet


pickle_file = r'e:/workspace/finsystem/banks.pickle.bz2'

def get_totalasset_by_country():
    banks = load_banks_pickle(pickle_file)
    return banks
