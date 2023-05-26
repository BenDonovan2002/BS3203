import random
import numpy as np
import tensorflow as tf

from shared_functions import *

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, LSTM
from tensorflow.keras.optimizers.legacy import RMSprop

# Constants defining the model name, number of epochs and learning rate.
MODEL_NAME = 'MODEL_NAME'
EPOCHS = 32
LEARNING_RATE = 0.01

try:
    # Validate the defined constants. Ensures that the model name is a string,
    # the number of epochs is an integer, and the learning rate is a number (int or float).
    assert isinstance(MODEL_NAME, str), "Model name must be a string."
    assert isinstance(EPOCHS, int), "Epochs must be an integer."
    assert isinstance(LEARNING_RATE, (int, float)), "Learning rate must be a number."
    assert isinstance(corpus, str), "Corpus must be a string."

    # Create a list of text_sentences
    text_sentences = []

    # Create a list of next characters
    next_chars = []

    # Loop through the corpus
    # For each step, a sentence (of length LEN_SEQ)
    # and the next character following the sentence are appended to their respective lists.
    for j in range(0, len(corpus) - LEN_SEQ, STEP_SIZE):
        if j % 10000 == 0:
            print(f'Processing {j}/{len(corpus)}')
        text_sentences.append(corpus[j: LEN_SEQ+j])
        next_chars.append(corpus[LEN_SEQ+j])

    # One hot encode characters
    # train_x's shape corresponds to [number of sentences, length of sentences, number of unique characters in the text]
    # train_y's shape corresponds to [number of sentences, number of unique characters in the text]
    train_x = np.zeros(
        ( len(text_sentences),
        LEN_SEQ, len(text_chars) ), dtype=bool )
    train_y = np.zeros(
        ( len(text_sentences),
        len(text_chars) ), dtype=bool)

    # Loop through the text_sentences
    # For each sentence, it goes through every character and marks it as 1 in the train_x array.
    # Then, the next character (in train_y array) for that sentence is also marked as 1.
    for x, s in enumerate(text_sentences):
        if x % 10000 == 0:
            print(f'Processing {x}/{len(text_sentences)}')
        # Loop through the characters in the sentence
        for y, c in enumerate(s):
            # Set the current character to 1
            train_x[x, y, chars_to_indices[c]] = 1
        # Set the next character to 1
        train_y[x, chars_to_indices[next_chars[x]]] = 1

    # Create the model
    model = Sequential()

    # Add an LSTM layer with 128 units
    model.add(LSTM(128, input_shape=(LEN_SEQ, len(text_chars))))

    # Add a dense layer with the same number of units as characters
    model.add(Dense(len(text_chars)))

    # Add a softmax activation layer
    model.add(Activation('softmax'))

    # Compile the model
    model.compile(optimizer=RMSprop(learning_rate=LEARNING_RATE),
        loss='categorical_crossentropy')

    # Train the model
    model.fit(train_x, train_y, epochs=EPOCHS, verbose=1)

    # Save the model
    model.save('models/'+MODEL_NAME+'.model')
except Exception as e:
    print(e)