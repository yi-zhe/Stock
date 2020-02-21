from decimal import Decimal

stocks = open('../stocks_line.txt', 'r')

writer = open('../a.md', 'w')

writer.write('|日期|名字|级别|0|0.618|1|1.618|2.618|破绽|\n')
writer.write('|---|---|---|---|---|---|---|---|---|\n')

for line in stocks:
    line = line.strip('\n')
    stock = line.split()
    date = stock[0]
    name = stock[1]
    level = stock[2]
    low = float(stock[3])
    high = float(stock[4])
    sign = stock[5]

    v0 = str(Decimal(low / 100).quantize(Decimal('0.00')))
    v0618 = str(Decimal(((high - low) * 0.618 + low) / 100).quantize(Decimal('0.00')))
    v1 = str(Decimal(high / 100).quantize(Decimal('0.00')))
    v1618 = str(Decimal(((high - low) * 0.618 + high) / 100).quantize(Decimal('0.00')))
    v2618 = str(Decimal(((high - low) * 1.618 + high) / 100).quantize(Decimal('0.00')))

    writer.write(
        '|' + date + '|' + name + '|' + level + '|' + v0 + '|' + v0618 +
        '|' + v1 + '|' + v1618 + '|' + v2618 + '|' + sign + '|\n')
writer.flush()
stocks.close()
