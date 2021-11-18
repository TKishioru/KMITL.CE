#แบกโดยรุ่นพี่ -/\-
#https://colab.research.google.com/drive/1mTEYdyvHAuxEXUD_asjNhaxGIN_NzsKD?usp=sharing#scrollTo=eN1pWRAHLaIM
#--------------------------------------------------------

from keras.models import Sequential
from keras.layers.core import Dense
from tensorflow.keras.optimizers import SGD, Adam

import numpy as np
import matplotlib.pyplot as plt

# input of XOR gate
training_data = [[0, 0], [0, 1], [1, 0], [1, 1]]

# expected output
target_data = [[0], [1], [1], [0]]