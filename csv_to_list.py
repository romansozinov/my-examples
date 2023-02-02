
# https://stackoverflow.com/questions/24662571/python-import-csv-to-list

import csv

with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)