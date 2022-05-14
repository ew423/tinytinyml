import unittest
import numpy as np
import os
from setuptools import setup
from python_src.t_pattern import TPattern

class TPatternTest(unittest.TestCase):
    def setUp(self):
        csv_path = os.path.join(os.curdir, 'data', 'T_Pattern', 't_pattern_3.csv')
        self.tpattern = TPattern(csv_path)
        self.x_data = np.reshape(np.arange(7840), (10, 784))
    
    def test_applyT(self):
        applied = self.tpattern.apply(self.x_data)
        rmvd = self.tpattern.remove(applied)
        eqls = np.equal(self.x_data, rmvd)
        self.assertEquals(np.count_nonzero(np.equal(self.x_data, rmvd)), 7840)