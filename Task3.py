"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

codes = []
called_fix_numbers = {"sum": 0, "counted": 0}


def store_code(code):
    if code not in codes:
        codes.append(code)


def fixed_line_call_stat(is_to_fixed_coded_number):
    called_fix_numbers["sum"] += 1
    if is_to_fixed_coded_number:
        called_fix_numbers["counted"] += 1


for call in calls:
    fixed_line_match = re.match(r'\(0\d+\)', call[0])
    if fixed_line_match:
        store_code(fixed_line_match.group()[1:-1])
        if fixed_line_match.group() == "(080)":
            fixed_line_to_match = re.match(r'\(0\d+\)', call[1])
            fixed_line_call_stat(fixed_line_to_match)
    else:
        mobile_match = re.match(r'([789]\d{4}\s\d+)', call[0])
        if mobile_match:
            store_code(mobile_match.group()[0:4])
        else:
            marketing_match = re.match(r'(140\d+)', call[0])
            if marketing_match:
                store_code(marketing_match.group()[0:3])

"""
Part A
"""
print("The numbers called by people in Bangalore have codes:\n", '\n'.join(map(str, sorted(codes))))

"""
Part B
"""
print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.".format(called_fix_numbers["sum"] / called_fix_numbers["counted"]))
