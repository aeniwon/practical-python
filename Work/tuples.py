import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
print(next(rows))
row = next(rows)
# t = (row[0], int(row[1]), float(row[2]))
# print(t)
# cost = t[1] *t[2]
# print(f'{cost:0.2f}')



d = {
    'name': row[0],
    'shares':int(row[1]),
    'price':float(row[2])
}


print(d['shares']*d['price'])
