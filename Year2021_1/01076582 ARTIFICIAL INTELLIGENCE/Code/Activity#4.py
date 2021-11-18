#แบกโดยรุ่นพี่ -/\-
#https://colab.research.google.com/drive/1mTEYdyvHAuxEXUD_asjNhaxGIN_NzsKD?usp=sharing#scrollTo=eN1pWRAHLaIM
#--------------------------------------------------------------------------------------------------------------------------

from keras.models import Sequential
from keras.layers.core import Dense
from tensorflow.keras.optimizers import SGD, Adam

import numpy as np
import matplotlib.pyplot as plt

# input of XOR gate
training_data = [[0, 0], [0, 1], [1, 0], [1, 1]]

# expected output
target_data = [[0], [1], [1], [0]]
training_data = np.array(training_data)
target_data = np.array(target_data)
print(training_data.shape)
print(target_data.shape)

# Train model #1
* Dense ชั้นแรก: input_shape=2 เพราะ input มีทั้งหมด 2 gate
* Dense ชั้นสอง: output 2 แบบ ใช้ output 1 node
* activation function = sigmoid
-------------------------------------------------------------
- learning rate = 0.1
- optimizer = SGD
- epochs = 15,000
- loss = 0.0099 (loss เริ่มน้อยกว่า 0.01 ประมาณ epoch ที่ 13,500)
- training time = 7 min

(optimizer)
* SGD (Stochastic gradient descent) เป็น algorithm ที่ update ค่า parameters ต่าง ๆ ในทุกชุดข้อมูลที่ train โดย upadate 1 ครั้ง/epoch ทุกครั้งที่มีการ update จะทำให้ค่า parameter มีความแปรปรวนสูงและส่งผลต่อค่า loss
