# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:28:20 2020

@author: Alex
"""

"""
Running the program requires tensorflow to be installed within your venv. 
If it isn't': 
    > pip install --upgrade tensorflow in the cmd, in your virtual environment folder.
It also needs the mnist dataset from tflow.keras.datasets, you can just add those from the conda gui.
"""

"""
Implementation of a basic CNN with a sequential model to classify the MNIST dataset with 6 simple layers. 

After playing around with other structures (some of which took forever), I settled on using this one due to time/ efficiency trade offs. 

Running results for 8 epochs can be found in the results.png photo.
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Conv2D, MaxPooling2D, Dropout
import matplotlib.pyplot as plt

RELU = tf.nn.relu
SOFTMAX = tf.nn.softmax
LOSS = tf.keras.losses.categorical_crossentropy
OPTIMIZER = tf.keras.optimizers.Adam

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()


#check that data was read correctly
plt.imshow(x_train[0])
plt.show()

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# we need to normalize the rgb codes
x_train /= 255
x_test /= 255

# convert class vectors to categories, in order to be able to use categorical crossentropy as a loss function
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

model = Sequential()

model.add(Conv2D(32,
                 kernel_size=(3, 3), 
                 activation=RELU,
                 input_shape=input_shape))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(128,activation=RELU))

model.add(Dropout(0.2))

model.add(Dense(10, activation=SOFTMAX))

opt=OPTIMIZER(learning_rate=0.01) 

model.compile(optimizer=opt,
              loss=LOSS,
              metrics=['accuracy'])

model.fit(x_train,y_train,
          batch_size=128,
          epochs=8)

test_loss, test_acc = model.evaluate(x_test, y_test)
print("\n")
print("Test loss:{} and test accuracy:{}".format(test_loss, test_acc))