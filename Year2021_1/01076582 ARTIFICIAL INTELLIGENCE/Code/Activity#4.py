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

#--------------------------------------------------------------------------------------------------------------------------
# Train model #1
#--------------------------------------------------------------------------------------------------------------------------
model_sgd = Sequential()
model_sgd.add(Dense(32, input_shape=(2,), activation='sigmoid'))
model_sgd.add(Dense(1, activation='sigmoid'))

optimizer_sgd = SGD(learning_rate=0.1)

model_sgd.compile(loss='binary_crossentropy',
              optimizer=optimizer_sgd,
              metrics=['accuracy'])

epochs = 15000
batch_size = 4

history_sgd = model_sgd.fit(training_data, target_data, epochs=epochs, batch_size=batch_size)

predict = model_sgd.predict(training_data)
print(np.round(predict))

model_sgd.summary()

# plot model: loss
plt.plot(history_sgd.history['loss'])
plt.ylabel('loss')
plt.xlabel('epochs')
plt.show()

#--------------------------------------------------------------------------------------------------------------------------
# Train model #2
#--------------------------------------------------------------------------------------------------------------------------
model_adam = Sequential()
model_adam.add(Dense(32, input_shape=(2,), activation='sigmoid'))
model_adam.add(Dense(1, activation='sigmoid'))

optimizer_adam = Adam(learning_rate=0.1)

model_adam.compile(loss='binary_crossentropy',
              optimizer=optimizer_adam,
              metrics=['accuracy'])

epochs = 150
batch_size = 4

history_adam = model_adam.fit(training_data, target_data, epochs=epochs, batch_size=batch_size)

predict = model_adam.predict(training_data)
print(np.round(predict))

# plot model: loss
plt.plot(history_adam.history['loss'])
plt.ylabel('loss')
plt.xlabel('epochs')
plt.show()
model_adam.summary()
