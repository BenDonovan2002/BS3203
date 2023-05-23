import spamcheck
import json

low = 100
high = -1
total = 0
count = 0

model_name = 'NAME_OF_MODEL'

# Read a file in generated directory
with open('generated/' + model_name + '.json', 'r') as f:
    emails = json.load(f)
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
            print(f"{count + 1}/{len(emails)} : {spam_score}")
        except:
            print(f"{count + 1}/{len(emails)}")
            pass

print(f"Low: {low}")
print(f"High: {high}")
print(f"Average: {round(total / count, 2)}")