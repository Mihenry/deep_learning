import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras.models import Sequential,Model
from keras.layers import LSTM, Dense,Input
from keras import callbacks
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import keras.backend.tensorflow_backend as KTF


def main():
    data_dim = 16
    timesteps = 8
    num_classes = 10
    batch_size = 32

    # Expected input batch shape: (batch_size, timesteps, data_dim)
    # Note that we have to provide the full batch_input_shape since the network is stateful.
    # the sample of index i in batch k is the follow-up for the sample i in batch k-1.
    model = Sequential()
    model.add(LSTM(32, return_sequences=True, stateful=True,batch_input_shape=(batch_size, timesteps, data_dim)))
    model.add(LSTM(32, return_sequences=True, stateful=True))
    model.add(LSTM(32, stateful=True))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics=['accuracy'])

    # Generate dummy training data
    x_train = np.random.random((batch_size * 10, timesteps, data_dim))
    y_train = np.random.random((batch_size * 10, num_classes))

    # Generate dummy validation data
    x_val = np.random.random((batch_size * 3, timesteps, data_dim))
    y_val = np.random.random((batch_size * 3, num_classes))

    model.fit(x_train, y_train, batch_size=batch_size, epochs=5, shuffle=False, validation_data=(x_val, y_val))

    x_test = np.random.random((batch_size * 5, timesteps, data_dim))
    y_test = np.random.random((batch_size * 5, num_classes))

    classes  = model.predict(x_test, batch_size=batch_size)

    print("\n classes \n")
    print(classes)


def fun_main():
    data_dim = 16
    timesteps = 8
    num_classes = 10
    batch_size = 32

    # Expected input batch shape: (batch_size, timesteps, data_dim)
    # Note that we have to provide the full batch_input_shape since the network is stateful.
    # the sample of index i in batch k is the follow-up for the sample i in batch k-1.
    input_tensor=Input(batch_shape=(batch_size,timesteps, data_dim))
    print(input_tensor.shape)
    x=LSTM(32, return_sequences=True, stateful=True,batch_input_shape=(batch_size, timesteps, data_dim))(input_tensor)
    x=LSTM(32, return_sequences=True, stateful=True,batch_input_shape=(batch_size, timesteps, data_dim))(x)
    x=LSTM(32, return_sequences=True, stateful=True)(x)
    x=LSTM(32, stateful=True)(x)
    x=Dense(10)(x)

    model=Model(inputs=[input_tensor],outputs=x)
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics=['accuracy'])

    # Generate dummy training data
    x_train = np.random.random((batch_size * 10, timesteps, data_dim))
    print(x_train.shape)
    y_train = np.random.random((batch_size * 10, num_classes))

    # Generate dummy validation data
    x_val = np.random.random((batch_size * 3, timesteps, data_dim))
    y_val = np.random.random((batch_size * 3, num_classes))

    model.fit(x_train, y_train, batch_size=batch_size, epochs=5, shuffle=False, validation_data=(x_val, y_val))

    x_test = np.random.random((batch_size * 5, timesteps, data_dim))
    y_test = np.random.random((batch_size * 5, num_classes))

    classes  = model.predict(x_test, batch_size=batch_size)
    print("\n classes \n")
    print(classes)


if __name__ == '__main__':
    # fun_main()

    main()
