# Spam Email Generator and Classifier

This project consists of a spam email generator and classifier, harnessing the power of modern machine learning. The project is designed for use with a suitable dataset like the Enron Email Dataset which can be found [here](https://www.cs.cmu.edu/~enron/).

This README file provides you with a guide on how to get the project up and running on your local machine for development and testing purposes.

## Prerequisites

To be able to use this tool, you must have the following installed:

- Python 3 ( Tested on 3.10.9 )
- pip3 (Python Package Installer)

## Installation

1. Clone this repository to your local machine using `git clone`.

    ```bash
    git clone https://github.com/BenDonovan2002/BS3203.git
    ```

2. Navigate to the project directory and install the required packages.

    ```bash
    cd BS3203
    pip3 install numpy tensorflow
    ```

## Getting Started

1. Download the Enron Email Dataset by visiting the [link](https://www.cs.cmu.edu/~enron/). Unzip and store the .txt files in the `data` folder.

2. After storing the .txt files in the `data` folder, run the `compile_dataset.py` script to compile these into a valid corpus.

    ```bash
    python compile_dataset.py
    ```

This will transform the .txt files into a structured format that can be easily used by our machine learning models.

## Training the Model

With your data prepared and formatted, you can now train the machine learning model using the command below:

Run the script `train_model.py`.

	python train_model.py

### Parameters
All parameters can be found at the top of the script.

**MODEL_NAME**: A string which represents the name of the model. Do not add the 'models/' or the extension, as this is done automatically

**EPOCHS**: The number of epochs used for training the model. An epoch is a full pass over the entire training dataset.

**LEARNING_RATE**: Determines the size of the steps taken during optimization to reach the minimum of the loss function

## Generating the Emails

With your data prepared and formatted, you can now train the machine learning model using the command below:

Run the script `run_model.py`.

    python run_model.py

### Parameters
All parameters can be found at the top of the script.


**MODEL_NAME**: A string which represents the name of the model. Do not add the 'models/' or the extension, as this is done automatically

**TEXT_LENGTH**: This integer parameter represents the length of the text that will be generated. It's used in the `generate_text` function, which generates a string of this length using the model.

**TEMPERATURE**: Controls the randomness of predictions. With a small temperature, the model makes more predictable predictions. With a higher temperature, the model generates more diverse and potentially more creative but less accurate outputs.

**EMAIL_COUNT**: Defines the number of emails that the script will generate. The script will generate this many emails and save them in a list. Each email will be a string of length `TEXT_LENGTH`, generated using the model.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/BenDonovan2002/BS3203/blob/master/LICENSE.md) file for details.

## Acknowledgements

- [Enron Dataset](https://www.cs.cmu.edu/~enron/) - The dataset used


