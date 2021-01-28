# Ordered Dictionary
from csv import DictReader
with open('File1.csv','r') as f:
    csv_reader=DictReader(f)
    for row in csv_reader:
        print(row)
    for row in csv_reader:
        print(row['name'])
    for row in csv_reader:
        print(row['email'])