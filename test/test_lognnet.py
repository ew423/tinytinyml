import unittest
import tensorflow as tf
from python_src.logNNet import LogNNet

class LogNNetTest(unittest.TestCase):

    def setUp(self):
        self.lognnet = LogNNet(10, 10, 10, 10, 10, 10)
    
    def test_lognnet_shape(self):
        print(self.lognnet.dense_1.weights)
        self.assertIsNotNone(self.lognnet.dense_1)