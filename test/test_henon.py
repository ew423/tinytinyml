import unittest
import tensorflow as tf
from python_src.henon import HenonLayerInitializer

class HenonTest(unittest.TestCase):

    def test_henon_class(self):
        henon = HenonLayerInitializer(10, 10, 10, 10, 10, 10)
        henon_dict = {
            "A": 10,
            "B": 10,
            "r_1": 10,
            "r_2": 10,
            "r_3": 10,
            "r_4": 10
        }
        self.assertDictEqual(henon.get_config(), henon_dict)
    
    def test_henon_call(self):
        henon = HenonLayerInitializer(10, 10, 10, 10, 10, 10)
        layer = henon((10, 784))
        self.assertIsNotNone(layer)
