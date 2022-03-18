import csv
from rich import print
from datetime import datetime

now = datetime.now()
TODAY = now.strftime("%A")

timings = []

with open('A2 Classes.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        timings.append(row)
        line_count += 1


# get number of classes
classes = []
for i, time in enumerate(timings):
    classes.append(time["Class"])
    classes = list(set(classes))

# print(len(classes)) # 4
# print(classes) # ['Mathematics', 'Physics', 'Chemistry', 'Computer Science']

for i, time in enumerate(timings):
    if time["Day"] == TODAY:
        print(time)
