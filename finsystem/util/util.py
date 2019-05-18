# encoding: utf-8

import pickle
import bz2


__all__ = ['dump_banks_to_pickle','load_banks_pickle']

def dump_banks_to_pickle(pickle_file,banks):
    pickle.dump(banks, bz2.BZ2File(pickle_file, 'w'))
    return True

def load_banks_pickle(pickle_file):
    banks = pickle.load(bz2.BZ2File(pickle_file,'r'))
    return banks