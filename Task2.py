"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def register_call(num, duration):
    try:
        phone_numbers[num] += int(duration)
    except KeyError:
        phone_numbers[num] = int(duration)


phone_numbers = {}

for call in calls:
    register_call(call[0], call[3])
    register_call(call[1], call[3])

longest = max(phone_numbers, key=lambda k: phone_numbers[k])

print("{} spent the longest time, {} seconds, on the phone during September 2016"
      .format(longest, phone_numbers[longest]))
