import numpy as np
import os
import pandas as pd
import tensorflow as tf

# DataSet object that manages the train data we load in
class DataSet:

    # Constructor takes in the train data and labels as well as a training:validation ratio
    # [train_data]: A numpy nd_array object containing the data you want to train on.
    # [train_labels]: A numpy nd_array object containing the labels for [train_data].
    # [percent_train]: A float in range [0.0, 1.0] indicating what fraction of the training
    #                  data you want to use to train the model and how much you want to set 
    #                  aside for validation. For example, setting [percent_train] to 0.8
    #                  tells the program to set aside twenty percent of the training set
    #                  for validation purposes.
    def __init__(self, train_data, train_labels, percent_train):
        self.n_train = int(percent_train * len(train_labels))
        self.raw_x = train_data
        self.raw_y = train_labels
        self.raw_x = self.raw_x
        self.train_x = np.float32(train_data[:self.n_train, :] / 255.0)
        self.train_y = tf.squeeze(self.raw_y[:self.n_train, :], axis=-1) 
        self.val_x = np.float32(train_data[self.n_train:, :] / 255.0)
        self.val_y = tf.squeeze(self.raw_y[self.n_train:, :], axis=-1) 

    # We shuffle the train/val sets between training runs so we don't overfit to a specific 
    # group of samples. 
    def shuffle(self):
        all_data = np.concatenate((self.raw_x, self.raw_y), axis=1)
        np.random.shuffle(all_data)
        self.train_x = all_data[:self.n_train, :len(self.raw_x[0])]
        self.train_y = all_data[:self.n_train, len(self.raw_x[0]):]
        self.val_x = all_data[self.n_train:, :len(self.raw_x[0])]
        self.val_y = all_data[self.n_train:, len(self.raw_x[0]):]

def loadCSVs(percent_train):
    parent_dir = os.pardir
    train_x_path = os.path.join(parent_dir, 'data', 'MNIST', 'train_images.csv')
    train_y_path = os.path.join(parent_dir, 'data', 'MNIST', 'train_labels.csv')
    x_train = pd.read_csv(train_x_path, header=None)
    y_train = pd.read_csv(train_y_path, header=None)
    x_tr = np.asarray(x_train)
    y_tr = np.asarray(y_train)
    return DataSet(x_tr, y_tr, percent_train=percent_train)

def loadTestData():
    parent_dir = os.pardir
    train_x_path = os.path.join(parent_dir, 'data', 'MNIST', 'test_images_0.csv')
    train_y_path = os.path.join(parent_dir, 'data', 'MNIST', 'test_labels_0.csv')
    x_train = pd.read_csv(train_x_path, header=None)
    y_train = pd.read_csv(train_y_path, header=None)
    x_tr = np.asarray(x_train)
    y_tr = np.asarray(y_train)
    return DataSet(x_tr, y_tr, percent_train=1)

