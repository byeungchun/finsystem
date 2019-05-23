# mapping.py

__all__ = ['mkt_sector_val','mkt_sector_key']

mkt_sector ={'UCB':'Universal Commercial Banks'}

def mkt_sector_val(_key):
    """
    Return market sector description
    Arguments:
        _key {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return mkt_sector.get(_key)

def mkt_sector_key(_val):
    """[summary]
    
    Arguments:
        _val {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    for (k, v) in mkt_sector.items():
        if v == _val:
            return k
    return None
