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
    allNumber= {}
    for call in calls:
        if allNumber.get(call[0], None) is None:
            allNumber[call[0]] = int(call[3])
        else:
            allNumber[call[0]] += int(call[3])
        if allNumber.get(call[1], None) is None:
            allNumber[call[1]] = int(call[3])
        else:
            allNumber[call[1]] += int(call[3])
    longestCall = []
    for key in allNumber:
        if len(longestCall) == 0:
            longestCall.append(key)
            longestCall.append(allNumber[key])
        elif allNumber[key] > longestCall[1]:
            longestCall[0] = key
            longestCall[1] = allNumber[key]

    print(str(longestCall[0]) + " spent the longest time, " + str(longestCall[1]) + " seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

