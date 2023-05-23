# Definitions
SEQUENCE_LENGTH = 40
STEP_SIZE = 3

# Read the generated corpus file
corpus = open('../data/out/concatenated.txt', 'rb').read().decode('utf-8').lower()
# Limit the corpus to 1 million characters
corpus = corpus[:100000]
# Create a list of unique characters in the corpus
chars = sorted(set(corpus))

# Create a dictionary mapping each unique character to an index
chars_to_indices = dict((c, i) for i, c in enumerate(chars))

# Create a dictionary mapping each index to a unique character
indices_to_chars = dict((i, c) for i, c in enumerate(chars))