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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_marketers = set()
receivers = set()


def remove_number(phone_number):
    if phone_number in possible_marketers:
        possible_marketers.remove(phone_number)


for call in calls:
    possible_marketers.add(call[0])
    receivers.add(call[1])

for text in texts:
    remove_number(text[0])
    remove_number(text[1])

possible_marketers -= receivers

print("These numbers could be telemarketers: \n", '\n'.join(map(str, sorted(possible_marketers))))
