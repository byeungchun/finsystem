# encoding: utf-8

import os, configparser
import pickle
import bz2
from finsystem.util.loader_fitch_connect import load_raw_file, create_bank


__all__ = ['dump_banks_to_pickle','load_banks_pickle']

config = configparser.ConfigParser()
config.read('conf/config.ini')
file_folder = config.get('FILESETUP','data_folder')
bank_pickle_file = config.get('FILESETUP','banks_pickle_file') # r'e:/workspace/finsystem/banks.pickle.bz2'
fc_datafile = config.get('FILESETUP','fitch_connenct_file')
fc_codefile = config.get('FILESETUP','fitch_code_file')

def dump_banks_to_pickle(banks=None):
    """
    It serializes Bank object to pickle file.
    If bank object is not exist, it creates the object from raw file

    Keyword Arguments:
        banks {[type]} -- [description] (default: {None})
    
    Returns:
        [type] -- [description]
    """
    if banks is None:
        fc_data = os.path.join(file_folder,fc_datafile)
        fc_mapping = os.path.join(file_folder,fc_codefile)
        fmap, fdf = load_raw_file(fc_data, fc_mapping)
        banks = create_bank(fmap, fdf)
    pickle_file = os.path.join(file_folder, bank_pickle_file)
    pickle.dump(banks, bz2.BZ2File(pickle_file, 'w'))
    return pickle_file

def load_banks_pickle():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    pickle_file = os.path.join(file_folder, bank_pickle_file)
    banks = pickle.load(bz2.BZ2File(pickle_file,'r'))
    return banks