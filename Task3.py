"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def get_area_code(number):
    return number[slice((number.index('(') + 1), (number.index(')')))]


def is_fix_line(number):
    return '(' in number


def is_bang(number):
    if is_fix_line(number):
        if get_area_code(number) == '080':
            return True
        else:
            return False
    return False


def is_tele_market(number):
    try:
        return number.index('140') == 0
    except:
        return False


def is_phone_number(number):
    return number[0] in ['7', '8', '9'] and ' ' in number


def get_prefix_number(number):
    return number[slice(0, 4)]


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    neededList = []
    sumCallFromBang = 0
    callFromBangToBang = 0
    for call in calls:
        if is_bang(call[0]):
            sumCallFromBang += 1
            if is_bang(call[1]):
                callFromBangToBang += 1
            if is_phone_number(call[1]):
                prefix = get_prefix_number(call[1])
                if prefix not in neededList:
                    neededList.append(prefix)
            elif is_fix_line(call[1]):
                prefix = get_area_code(call[1])
                if prefix not in neededList:
                    neededList.append(prefix)
    neededList.sort()
    dropLine = '\n'
    listString = dropLine.join(neededList)
    # PARTB
    percent = float(callFromBangToBang / sumCallFromBang * 100)
    print("The numbers called by people in Bangalore have codes:" + '\n' + listString)
    print(str(percent)+" percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
