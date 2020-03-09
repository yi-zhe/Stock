import time

from StockModel import StockModel
from basic import Stock

# 获得当天的日期
timestamp = time.time()
today = time.strftime("%Y%m%d", time.localtime(timestamp))

stocks = []
stock_codes = []
stocksFileContent = open('observed_stocks.txt', 'r')
for stockLineData in stocksFileContent:
    stockLineData = stockLineData.strip('\n')
    stock_detail = stockLineData.split()
    name = stock_detail[0]
    code = stock_detail[1]
    stock_codes.append(code)
    start = stock_detail[2]
    to = stock_detail[3]
    stock = StockModel.StockModel(name, code, start, to)
    stocks.append(stock)

allData = Stock.get_stock_basic(','.join(stock_codes), today)

for index, row in allData.iterrows():
    stock = stocks[index]
    stock.openP = row[2] * 100
    stock.low = row[4] * 100
    stock.close = row[5] * 100
    stock.calc()
    if stock.is_leak:
        print(stock.name)
