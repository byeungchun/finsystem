"""
Tests for balancesheet class in finstmt.py. 
Sample data is taken from Fitch connect.

"""
import os
import unittest
import pandas as pd
from dataclasses import fields
from nose.tools import eq_

from finsystem.entity.finstmt import BalanceSheet

#class TestBalanceSheet(unittest.TestCase):
class TestBalanceSheet():
    def setUp(self):
        sample_file = r'C:\Users\byeun\workspace\data\fitch_sample.xlsx'
        mapping_file = r'C:\Users\byeun\workspace\data\fitch_column.txt'
        self.fmap = dict(map(lambda y: (y[1],y[0]), [x.rstrip().split(',') for x in open(mapping_file,'r')]))
        self.fdf = pd.read_excel(sample_file)

    def test_find_column(self):
        fmap = self.fmap
        fdf = self.fdf
        fcol = [fmap[y] for y in [x.metadata['fitchcode'] for x in fields(BalanceSheet)]]
        fdf = fdf.loc[:,fcol]
        eq_(len(fcol), fdf.shape[1])
        
        #self.assertTrue(len(fcol) == fdf.shape[1])

if __name__ == "__main__":
    import sys
    import nose

    argv = sys.argv[:]
    argv.append('--verbose')
    argv.append('--nocapture')
    nose.main(argv=argv, defaultTest=__file__)
# if __name__ == "__main__":
#     import sys
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestBalanceSheet)
#     unittest.TextTestRunner(verbosity=1, stream=sys.stderr).run(suite)
