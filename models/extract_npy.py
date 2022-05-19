import numpy as np
import os
import pandas as pd

parent = os.pardir
data = np.load("henon_b2.npy")
string = ""
print("{ ")
for i in range(1):
    string = string + "{ "
    for j in range(10):
        string = string + str(data[j])
        if j != 9:
            string = string + ", "
    string = string + "}, "
    print(string)
    string = ""
print("}")