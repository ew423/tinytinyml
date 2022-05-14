import os
import numpy as np
from mlxtend.data import loadlocal_mnist
from t_pattern import TPattern
# A quick script to load the data we'll be using for this project.
# Used mlxtend package to process the raw MNIST files from Yann LeCunn's website

parent_dir = os.pardir

train_image_path = os.path.join(parent_dir, 'data', 'MNIST', 'train-images.idx3-ubyte')
train_label_path = os.path.join(parent_dir, 'data', 'MNIST', 'train-labels.idx1-ubyte')
test_image_path = os.path.join(parent_dir, 'data', 'MNIST', 't10k-images.idx3-ubyte')
test_label_path = os.path.join(parent_dir, 'data', 'MNIST', 't10k-labels.idx1-ubyte')

t_pat_path = os.path.join(parent_dir, 'data', 'T_Pattern', 't_pattern_3.csv')
t_pattern = TPattern(t_pat_path)

train_images, train_labels = loadlocal_mnist(images_path=train_image_path, labels_path=train_label_path)
test_images, test_labels = loadlocal_mnist(images_path=test_image_path, labels_path=test_label_path)

train_images = t_pattern.apply(train_images)
test_images = t_pattern.apply(test_images)

np.savetxt(fname=os.path.join(parent_dir, 'data', 'MNIST', 'train_images.csv'), X=train_images, delimiter=',', fmt='%d')
np.savetxt(fname=os.path.join(parent_dir, 'data', 'MNIST', 'train_labels.csv'), X=train_labels, delimiter=',', fmt='%d')


# We will be splitting the test set into 'packages' of 400 images each.
# Why? Memory allocation!

# Each pixel of each image is represented by a 'depth' value in range [0, 255]
# Which is exactly one byte of data

# Thus, since each image contains 784 pixels, we need to set aside 784 bytes of 
# memory for each 'image' we plan to load

# And 400 seems like a good amount of images to give us a general idea of how
# our low precision model is working (taking up roughly 340 kB, about a third of the 
# device's available flash RAM!)

test_image_batches = np.split(test_images, 25)
test_label_batches = np.split(test_labels, 25)

for i in range(25):
    t_img_pth = 'test_images_' + str(i) + '.csv'
    t_lbl_pth = 'test_labels_' + str(i) + '.csv'
    np.savetxt(fname=os.path.join(parent_dir, 'data', 'MNIST', t_img_pth), X=test_image_batches[i], delimiter=',', fmt='%d')
    np.savetxt(fname=os.path.join(parent_dir, 'data', 'MNIST', t_lbl_pth), X=test_label_batches[i], delimiter=',', fmt='%d')