"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    record = texts[0]
    print("First record of texts, "+record[0]+" texts "+record[1]+" at time "+record[2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    record = calls[len(calls)-1]
    print("Last record of calls, "+record[0]+" calls " + record[1] + " at time " + record[2]+", lasting " + record[3] + " seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

