value = 0
with open('portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        value += int(row[1]) * float(row[2])
print(value)

import gzip
with gzip.open('portfolio.csv.gz') as f:
    for line in f:
        print(line, end='')
