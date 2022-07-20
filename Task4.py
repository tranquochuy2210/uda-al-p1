"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
numberSendTextList = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    AllNumberSendText = []
    for line in texts:
        num1 = line[0]
        num2 = line[1]
        if num1 not in numberSendTextList:
            numberSendTextList.append(num1)
        if num2 not in numberSendTextList:
            numberSendTextList.append(num2)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    telephoneMarketingNumbers = []
    recieveCallNumbers = []
    for call in calls:
        if call[1] not in recieveCallNumbers:
            recieveCallNumbers.append(call[1])
    for call in calls:
        if call[0] not in recieveCallNumbers and call[0] not in numberSendTextList:
            if call[0] not in telephoneMarketingNumbers:
                telephoneMarketingNumbers.append(call[0])
    telephoneMarketingNumbers.sort()
    dropLine = '\n'
    listString = dropLine.join(telephoneMarketingNumbers)
    print("These numbers could be telemarketers: " + dropLine + listString)

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

