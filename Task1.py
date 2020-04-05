"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def check_number(num):
    if num not in unique_numbers:
        unique_numbers.append(num)


unique_numbers = []

for record in texts:
    check_number(record[0])
    check_number(record[1])

for record in calls:
    check_number(record[0])
    check_number(record[1])

print("There are %s different telephone numbers in the records." % len(unique_numbers))
