import sys


def portfolio_cost(filename):
    value = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            row = line.split(',')
            value += int(row[1]) * float(row[2])
    print('Total cost:', value)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)

portfolio_cost('Data/portfolio.csv')
