import random
import numpy as np
import tensorflow as tf

from shared_functions import *

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, LSTM
from tensorflow.keras.optimizers.legacy import RMSprop


# Create a list of sentences
sentences = []

# Create a list of next characters
next_chars = []

# Loop through the corpus
for i in range(0, len(corpus) - SEQUENCE_LENGTH, STEP_SIZE):
    if i % 10000 == 0:
        print(f'Processing {i}/{len(corpus)}')
    sentences.append(corpus[i: i + SEQUENCE_LENGTH])
    next_chars.append(corpus[i + SEQUENCE_LENGTH])

# Create a list of one-hot encoded sentences
train_x = np.zeros((len(sentences), SEQUENCE_LENGTH, len(chars)), dtype=bool)
train_y = np.zeros((len(sentences), len(chars)), dtype=bool)

# Loop through the sentences
for i, sentence in enumerate(sentences):
    if i % 10000 == 0:
        print(f'Processing {i}/{len(sentences)}')
    # Loop through the characters in the sentence
    for j, char in enumerate(sentence):
        # Set the current character to 1
        train_x[i, j, chars_to_indices[char]] = 1
    # Set the next character to 1
    train_y[i, chars_to_indices[next_chars[i]]] = 1

# Create the model
model = Sequential()

# Add an LSTM layer with 128 units
model.add(LSTM(128, input_shape=(SEQUENCE_LENGTH, len(chars))))

# Add a dense layer with the same number of units as characters
model.add(Dense(len(chars)))

# Add a softmax activation layer
model.add(Activation('softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(learning_rate=0.01))

# Train the model
model.fit(train_x, train_y, epochs=32, verbose=1)

# Save the model
model.save('models/lstm_100K_Corpus_32_Epochs.model')