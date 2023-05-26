import spamcheck
import json
import os

low = 100
high = -1
total = 0
count = 0

model_name = 'NAME_OF_MODEL'

try:
    # Validate model name
    assert isinstance(model_name, str), "Model name must be a string."

    # Read a file in generated directory
    file_path = 'generated/' + model_name + '.json'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file found at {file_path}.")

    with open(file_path, 'r') as f:
        emails = json.load(f)
        if not emails:
            raise ValueError("No emails found in file.")
        x = spamcheck.check(emails[0], report=True)
        print(x['report'])
        for email in emails:
            try:
                spam_score = float(spamcheck.check(email)['score'])
                if spam_score < low:
                    low = spam_score
                if spam_score > high:
                    high = spam_score
                total += spam_score
                count += 1
                print(f"{count}/{len(emails)} : {spam_score}")
            except Exception as e:
                print(f"{count + 1}/{len(emails)}: Unable to calculate spam score. Error: {str(e)}")
    if count == 0:
        print("Unable to calculate spam score for any email.")
    else:
        print(f"Low: {low}")
        print(f"High: {high}")
        print(f"Average: {round(total / count, 2)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
