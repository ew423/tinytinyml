# The architecture for this neural net was designed by H. Heidari and A. A. Velichko
# in their paper [An Improved LogNNet Classifier for IoT Applications]. Here is the 
# link to their paper: https://arxiv.org/ftp/arxiv/papers/2105/2105.14412.pdf

# The main contribution of the paper wasn't the original LogNNet itself - rather, a 
# method of tuning the model. But the architecture they built works on small devices,
# so I will be using it for this experiment. I may implement the tuning stuff later
# if time allows. 

from numpy import dtype
import numpy as np
import tensorflow as tf
from tensorflow import keras
from henon import HenonLayerInitializer

def create_LogNNet(A, B, r_1, r_2, r_3, r_4) -> tf.keras.Model:
    model = keras.Sequential()
    model.add(keras.layers.Dense(25, input_shape=(784, )))
    model.add(keras.layers.Dense(10, activation='sigmoid'))
    return model

def create_Henon_LogNNet(A, B, r_1, r_2, r_3, r_4) -> tf.keras.Model:
    henon_weights = HenonLayerInitializer(A, B, r_1, r_2, r_3, r_4)
    weights = henon_weights((784, 25))
    model = keras.Sequential()
    model.add(keras.layers.Dense(25, input_shape=(784, ), kernel_initializer=tf.constant_initializer(weights)))
    model.add(keras.layers.Dense(10, activation='sigmoid'))
    return model
