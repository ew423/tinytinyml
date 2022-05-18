import unittest
import numpy as np
from python_src.data_loader import DataSet

class DataSetTest(unittest.TestCase):
    def setUp(self):
        self.dummy_x = np.zeros([100, 10])
        self.dummy_y = np.zeros([100, 1])
        self.dummy_percent = 0.8
        self.harder_x = np.reshape(np.arange(1000), [100, 10])
        self.harder_y = np.reshape(np.arange(100), [100, 1])
    
    def test_init(self):
        dataset = DataSet(self.dummy_x, self.dummy_y, self.dummy_percent)
        self.assertEquals(len(dataset.train_x), 80)
        self.assertEquals(len(dataset.train_y), 80)
        self.assertEquals(len(dataset.train_x[0]), 10)
        self.assertEquals(len(dataset.train_y[0]), 1)
        self.assertEquals(len(dataset.val_x), 20)
        self.assertEquals(len(dataset.val_y), 20)
        self.assertEquals(len(dataset.val_x[0]), 10)
        self.assertEquals(len(dataset.val_y[0]), 1)
    
    def test_splitting(self):
        dataset = DataSet(self.harder_x, self.harder_y, self.dummy_percent)
        self.assertEquals(dataset.train_x[0, 0], 0.0)
        self.assertEquals(dataset.train_x[79, 9], 799)
        self.assertEquals(dataset.train_y[0, 0], 0)
        self.assertEquals(dataset.train_y[79, 0], 79)
        self.assertEquals(dataset.val_x[0, 0], 800)
        self.assertEquals(dataset.val_x[19, 9], 999)
        self.assertEquals(dataset.val_y[0, 0], 80)
        self.assertEquals(dataset.val_y[19, 0], 99)

    def test_shuffle(self):
        dataset = DataSet(self.harder_x, self.harder_y, self.dummy_percent)
        shuffled_dataset = DataSet(self.harder_x, self.harder_y, self.dummy_percent)
        shuffled_dataset.shuffle()

        for i in range(len(dataset.train_x)):
            self.assertEqual(dataset.train_y[i, 0], int(dataset.train_x[i, 0] / 10))
        
        for i in range(len(shuffled_dataset.train_x)):
            self.assertEqual(shuffled_dataset.train_y[i, 0], int(shuffled_dataset.train_x[i, 0] / 10))
        
        for i in range(len(dataset.val_x)):
            self.assertEqual(dataset.val_y[i, 0], int(dataset.val_x[i, 0] / 10))
        
        for i in range(len(shuffled_dataset.val_x)):
            self.assertEqual(shuffled_dataset.val_y[i, 0], int(shuffled_dataset.val_x[i, 0] / 10))
        