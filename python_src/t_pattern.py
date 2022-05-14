# T-Pattern Object management - applies (and unapplies) the T-Pattern transformation 
# detailed in the CSV.

# A T-Pattern tells the computer how to unroll a multi-dimensional object into a one-dimensional
# array. In example, numpy's standard unrolling T-Pattern (the pattern it uses to flatten your
# arrays) would look something like this:

#                       0----->----->----->----->
#                       5----->----->----->----->
#                      10----->----->----->----->
#                                 ...

# The T-Pattern I use was published by Andrei Velichko in one of his earlier LogNNet papers. 
# He did not go into much detail about why this specific transformation improved performance,
# but the numbers he published showed a ~30% improvement in performance when using T-Pattern 3
# over standard array flattening, and you can't argue with results.

import numpy as np
import pandas as pd
import os

# Creates a new TPattern Object.
#
# [csv_path]: The path to the CSV with the T-Pattern numbers from the 2021 paper.
# [img_dims]: The dimensions of the images. Expects a tuple of two integers. The first item
#             represents the number of rows in the image. The second item represents the number of 
#             columns.
class TPattern:
    def __init__(self, csv_path, img_dims=(28, 28)):
        csv = pd.read_csv(csv_path, header=None)
        self.raw_mapping = np.asarray(csv)
        self.mapping = np.ndarray(len(self.raw_mapping))
        for i in range(len(self.raw_mapping)):
            self.mapping[i] = int( (self.raw_mapping[i, 0] - 1) * (img_dims[1]) + self.raw_mapping[i, 1] - 1 )
    
    # Applies the T-Pattern to some numpy array of image samples
    #
    # [images]: A N x (img_dims[0] * img_dims[1]) array containing N samples. They have
    #           not been processed before. 
    def apply(self, images):
        mapped = np.ndarray(np.shape(images))
        for ind in range(len(self.mapping)):
            mapped[:, ind] = images[:, int(self.mapping[ind])]
        return mapped
    
    # Removes the T-Pattern from some numpy array of image samples
    #
    # [images]: A N x (img_dims[0] * img_dims[1]) array containing N samples. They have
    #           been processed before. 
    def remove(self, images):
        removed = np.ndarray(np.shape(images))
        for ind in range(len(self.mapping)):
            removed[:, int(self.mapping[ind])] = images[:, ind]
        return removed

