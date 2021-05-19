# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
import tensorflow as tf
import tensorflow_datasets as tfds
tfds.disable_progress_bar()
import math
import keras
from keras.models import Sequential
train_data = pd.read_csv("/kaggle/input/digit-recognizer/train.csv")
test_data = pd.read_csv("/kaggle/input/digit-recognizer/test.csv")
print(train_data.shape)
print(test_data.shape)
x_train = train_data.drop(labels=["label"],axis=1)
y_train = train_data["label"]
x_train = x_train.astype("float32")/255
x_train = x_train.values.reshape(-1,28,28,1)
x_test = test_data.astype("float32")/255
x_test = x_test.values.reshape(-1,28,28,1)
print(x_test.shape)
print(x_train.shape)
print(y_train.shape)
model = tf.keras.Sequential([ tf.keras.layers.Conv2D(64, (3,3), padding='same', activation=tf.nn.relu, input_shape=(28, 28, 1)), tf.keras.layers.MaxPooling2D((2, 2), strides=2), tf.keras.layers.Conv2D(64, (3,3), padding='same', activation=tf.nn.relu), tf.keras.layers.MaxPooling2D((2, 2), strides=2), tf.keras.layers.Flatten(), tf.keras.layers.Dense(128, activation=tf.nn.relu), tf.keras.layers.Dense(10, activation=tf.nn.softmax) ])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=10, verbose=1)
pred = model.predict(x_test)
pred.shape
result = np.argmax(pred,axis=1)
result.shape
result = pd.Series(result, name="Label")
result.head()
submission = pd.concat([pd.Series(range(1,28001),name = "ImageId"),result],axis = 1)
submission.to_csv("submission.csv", index=False)
