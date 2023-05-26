import json
import random
import numpy as np
import tensorflow as tf

from shared_functions import *

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, LSTM
from tensorflow.keras.optimizers.legacy import RMSprop

# Constants defining the model name, the length of the text to generate,
# the "temperature" to control randomness, and the number of emails to generate.
MODEL_NAME = 'MODEL_NAME'
TEXT_LENGTH = 300
TEMPERATURE = 0.3
EMAIL_COUNT = 100

try:
    # Validate the defined constants. Ensures that the model name is a string,
    # the text length and email count are integers, and the temperature is a number (int or float).
    assert isinstance(MODEL_NAME, str), "Model name must be a string."
    assert isinstance(TEXT_LENGTH, int), "Text length must be an integer."
    assert isinstance(TEMPERATURE, (int, float)), "Temperature must be a number."
    assert isinstance(EMAIL_COUNT, int), "Email count must be an integer."

    # Generate a prediction from the model output.
    # Temperature allows control over the randomness of predictions.
    # The higher the temperature, the more random the predictions; the
    # lower the temperature, the more deterministic the predictions.
    # (Chollet, 2017, p. 276)
    def generate_prediction(predictions, temperature=1.0):
        predictions = np.asarray(predictions).astype('float64')
        predictions = np.log(predictions) / temperature
        exp_predictions = np.exp(predictions)
        predictions = exp_predictions / np.sum(exp_predictions)
        probabilities = np.random.multinomial(1, predictions, 1)
        return np.argmax(probabilities)

    # Function to generate a text of a given length with a specified
    # "temperature" to control randomness. It starts from a randomly
    # chosen point in the corpus, generates characters one by
    # one, and then appends them to the generated text.
    def generate_text(txt_len, temp):
        # Start the index at a random point in the given corpus.
        # The range of the random index is limited to (len(corpus) - LEN_SEQ - 1)
        # to ensure that the sequence length does not exceed the remaining characters in the corpus.
        start_ind = random.randint(0, len(corpus) - LEN_SEQ - 1)

        generated_text = ''

        # Select a sequence of characters of length (LEN_SEQ - len(generated_text))
        # starting from the randomly selected index. The selected characters from the
        # corpus are assigned to 'corpus_trim' and 'output_text'.
        corpus_trim = output_text = corpus[start_ind: start_ind + (LEN_SEQ-len(generated_text))]

        generated_text = output_text + generated_text

        for _ in range(txt_len):

            # Initialize a tensor of shape ( 1, LEN_SEQ, len( text_chars ) ) with zeros.
            # This tensor will be used as input to the model for generating predictions.
            model_prediction_x = np.zeros((1, LEN_SEQ, len(text_chars)))
            model_prediction_x = np.zeros( (1, LEN_SEQ, len( text_chars ) ) )

            # Encode each character in 'output_text' to its corresponding index and
            # set the corresponding position in the tensor to 1.
            for model_prediction_y, pred_char in enumerate(output_text):
                model_prediction_x[0, model_prediction_y, chars_to_indices[pred_char]] = 1


            # Use the model to generate predictions on the input tensor.
            predictions = model.predict(model_prediction_x, verbose=0)

            # Use the 'generate_prediction' function to select the index of the next
            # character based on the predictions.
            text_index_next = generate_prediction(predictions[0], temp)

            # Map the index of the next character back to the actual character.
            text_character_next = indices_to_chars[text_index_next]

            # Append the next character to the 'generated_text'.
            generated_text += text_character_next

            # Slide the window of 'output_text' one character to the right by
            # removing the first character and appending the next character.
            output_text = output_text[1:] + text_character_next

        return generated_text[len(corpus_trim):]


    model = tf.keras.models.load_model('models/' + MODEL_NAME + '.model')

    emails = []

    print(MODEL_NAME)

    for i in range(EMAIL_COUNT):
        print("Generating email " + str(i) + "...")
        emails.append(generate_text(TEXT_LENGTH, TEMPERATURE))

    # Save stringified emails to file
    with open('../generated/emails_' + MODEL_NAME + '.json', 'w') as f:
        x = json.dumps(emails)
        f.write(x)
except Exception as e:
    print(e)