# The architecture for this neural net was designed by H. Heidari and A. A. Velichko
# in their paper [An Improved LogNNet Classifier for IoT Applications]. Here is the 
# link to their paper: https://arxiv.org/ftp/arxiv/papers/2105/2105.14412.pdf

# The main contribution of the paper wasn't the original LogNNet itself - rather, a 
# method of tuning the model. But the architecture they built works on small devices,
# so I will be using it for this experiment. I may implement the tuning stuff later
# if time allows. 

import tensorflow as tf
from tensorflow import keras

class LogNNet:
    pass