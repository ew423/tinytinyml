# This is the initialization mentioned in the Heidari-Velichko paper. 

# It's based off of a chaotic system.

# Normally, chaos isn't exactly a great thing. However, computers are a little 
# too un-chaotic. They're kind of conservative by nature; if they find a local 
# solution that is technically not the worst, they will not try to deviate from
# said technically-okay-but-not-ideal solution

# So we, as chaotic human beings, have to drag the computers out of their comfort
# zones and encourage them to 'explore' different ways to solve problems

# However, we don't want to be too chaotic - then, you might as well ask a class
# of kindergarteners to pick a number they feel good about

# It's a balancing game - we want to encourage our AI to try new things, but we 
# also want it to hold on to things that work well

# This conflict is more formally known as Exploration vs. Exploitation, and we 
# can tweak the balance to suit our specific purposes better.

import tensorflow as tf
import numpy as np
import math

# Henon is the name of a chaotic system that, depending on the values it is 
# initialized, may or may not converge.
class HenonLayerInitializer(tf.keras.initializers.Initializer):

    # Sets up all six variables.
    # [const_A]: Initial constant.
    # [const_B]: Initial constant.
    # [r_1]: Controls the function behavior.
    # [r_2]: Controls the function behavior.
    # [r_3]: Controls the function behavior.
    # [r_4]: Controls the function behavior.

    # These constants control the behavior of the initialization function.
    # When we try to optimize the model's hyperparameters, we are tweaking
    # these variables to get the best possible initial weight vector
    def __init__(self, const_A, const_B, r_1, r_2, r_3, r_4) -> None:
        self.A = const_A
        self.B = const_B
        self.r_1 = r_1
        self.r_2 = r_2
        self.r_3 = r_3
        self.r_4 = r_4
    
    # We set up this function so we can treat this class like a function. 
    # This function returns the actual tensorflow tensor
    # The first row is initialized with constant values
    # Then, the latter rows are initialized according to the equations from the paper

    # [shape]: The shape of the tensor we want to create.
    # [dtype]: The data type of the tensor we will create. Will most likely be a float.
    def __call__(self, shape, dtype=None):
        layer = np.zeros(shape)

        for i in range(shape[0]):
            layer[i, 0] = np.float32(self.A * math.sin((i / 784) * (math.pi / self.B)))
        
        x = np.float32(self.A)
        y = np.float32(self.B)
        x_n = x
        y_n = y
        
        for c in range(1, shape[1]):
            for r in range(shape[0]):
                x_n = y
                y_n = x + self.r_1 * x ** 2 + self.r_2 * y ** 2 - self.r_3 * x * y - self.r_4
                x = x_n
                y = y_n

                if math.fabs(y) > 10:
                    y = np.float32(1.0)
                
                layer[r, c] = y
        
        return layer
    
    # The tensorflow tutorial said that having one of these is quite nice for
    # building models. It's just a dictionary with the parameters we used to create
    # the layer. 
    def get_config(self):
        return {
            "A": self.A,
            "B": self.B,
            "r_1": self.r_1,
            "r_2": self.r_2,
            "r_3": self.r_3,
            "r_4": self.r_4
        }