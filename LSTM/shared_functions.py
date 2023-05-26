# Definitions
SEQUENCE_LENGTH = 40
STEP_SIZE = 3
CORPUS_SIZE = 1000000

try:
    # Validate constants
    assert isinstance(SEQUENCE_LENGTH, int), "Sequence length must be an integer."
    assert isinstance(STEP_SIZE, int), "Step size must be an integer."
    assert isinstance(CORPUS_SIZE, int), "Corpus size must be an integer."

    # Read the generated corpus file
    filepath = '../data/out/concatenated.txt'
    if not os.path.exists(filepath):
        print("The file {} does not exist. Please run the script 'generate_corpus.py' first.".format(filepath))
        exit()
    corpus = open(filepath, 'rb').read().decode('utf-8').lower()
    # Limit the corpus to 1 million characters
    corpus = corpus[:CORPUS_SIZE]
    # Create a list of unique characters in the corpus
    chars = sorted(set(corpus))

    # Create a dictionary mapping each unique character to an index
    chars_to_indices = dict((c, i) for i, c in enumerate(chars))

    # Create a dictionary mapping each index to a unique character
    indices_to_chars = dict((i, c) for i, c in enumerate(chars))
except Exception as e:
    print(e)