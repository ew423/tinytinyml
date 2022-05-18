from tensorflow import keras
import tensorflow as tf
import numpy as np
import os
from henon import HenonLayerInitializer
from logNNet import create_Henon_LogNNet, create_LogNNet
from data_loader import loadCSVs, loadTestData

data = loadCSVs(0.3)
test_data = loadTestData()
henon_model = create_Henon_LogNNet(1, 1, 1, 1, 1, 1)
standard_logNN = create_LogNNet(1, 1, 1, 1, 1, 1)

henon_model.compile(optimizer=keras.optimizers.Adam(), 
              loss=keras.losses.SparseCategoricalCrossentropy(), 
              metrics=['accuracy'])
standard_logNN.compile(optimizer=keras.optimizers.Adam(), 
              loss=keras.losses.SparseCategoricalCrossentropy(), 
              metrics=['accuracy'])

henon_history = henon_model.fit(
    data.train_x,
    data.train_y,
    batch_size=25,
    epochs=40,
    validation_data=(data.val_x, data.val_y)
)

logNN_history = standard_logNN.fit(
    data.train_x,
    data.train_y,
    batch_size=25,
    epochs=5,
    validation_data=(data.val_x, data.val_y)
)
print('Henon Results:')
henon_results = henon_model.evaluate(test_data.train_x, test_data.train_y, batch_size=100)

print('Standard Results:')
standard_logNN_results = standard_logNN.evaluate(test_data.train_x, test_data.train_y, batch_size=100)

def representative_dataset():
    for i in range(200):
      yield [data.train_x[i].reshape(1, 784)]

henon_converter = tf.lite.TFLiteConverter.from_keras_model(henon_model)
henon_converter.optimizations = [tf.lite.Optimize.DEFAULT]
henon_converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
henon_converter.inference_input_type = tf.int8
henon_converter.inference_output_type = tf.int8
henon_converter.representative_dataset = representative_dataset

standard_logNN_converter = tf.lite.TFLiteConverter.from_keras_model(standard_logNN)
standard_logNN_converter.optimizations = [tf.lite.Optimize.DEFAULT]
standard_logNN_converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
standard_logNN_converter.inference_input_type = tf.int8
standard_logNN_converter.inference_output_type = tf.int8
standard_logNN_converter.representative_dataset = representative_dataset

tflite_henon = henon_converter.convert()
tflite_standard_logNN = standard_logNN_converter.convert()

parent_dir = os.pardir
henon_model_fp = os.path.join(parent_dir, 'models', 'henon_model.tflite')
standard_logNN_fp = os.path.join(parent_dir, 'models', 'standard_logNN.tflite')

with open(henon_model_fp, 'wb') as fp:
    fp.write(tflite_henon)

with open(standard_logNN_fp, 'wb') as fp:
    fp.write(tflite_standard_logNN)

