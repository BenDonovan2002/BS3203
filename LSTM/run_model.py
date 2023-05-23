import json
import random
import numpy as np
import tensorflow as tf

from shared_functions import *

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, LSTM
from tensorflow.keras.optimizers.legacy import RMSprop

model_name = 'NAME_OF_MODEL'


def generate_prediction(predictions, temperature=1.0):
    predictions = np.asarray(predictions).astype('float64')
    predictions = np.log(predictions) / temperature
    exp_predictions = np.exp(predictions)
    predictions = exp_predictions / np.sum(exp_predictions)
    probabilities = np.random.multinomial(1, predictions, 1)
    return np.argmax(probabilities)


def generate_text(length, temp):
    start_ind = random.randint(0, len(corpus) - SEQUENCE_LENGTH - 1)
    generated = ''
    corpus_trim = sentence = corpus[start_ind: start_ind + (SEQUENCE_LENGTH-len(generated))]
    generated = sentence + generated
    for i in range(length):
        x_pred = np.zeros((1, SEQUENCE_LENGTH, len(chars)))
        for t, char in enumerate(sentence):
            x_pred[0, t, chars_to_indices[char]] = 1.
        predictions = model.predict(x_pred, verbose=0)[0]
        ind_next = generate_prediction(predictions, temp)
        char_next = indices_to_chars[ind_next]
        generated += char_next
        sentence = sentence[1:] + char_next
    return generated[len(corpus_trim):]


model = tf.keras.models.load_model('models/' + model_name + '.model')

emails = []

print(model_name)

for i in range(100):
    print("Generating email " + str(i) + "...")
    emails.append(generate_text(300, 0.3))

# Save stringified emails to file
with open('../generated/emails_' + model_name + '.json', 'w') as f:
    x = json.dumps(emails)
    f.write(x)