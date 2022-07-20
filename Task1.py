"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

uniqueNumberList = []
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for line in texts:
        num1 = line[0]
        num2 = line[1]
        if num1 not in uniqueNumberList:
            uniqueNumberList.append(num1)
        if num2 not in uniqueNumberList:
            uniqueNumberList.append(num2)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for line in calls:
        num1 = line[0]
        num2 = line[1]
        if num1 not in uniqueNumberList:
            uniqueNumberList.append(num1)
        if num2 not in uniqueNumberList:
            uniqueNumberList.append(num2)

print("There are " + str(len(uniqueNumberList)) + " different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
