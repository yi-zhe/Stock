import time

from StockModel import StockModel
from basic import Stock

# 获得当天的日期
timestamp = time.time()
today = time.strftime("%Y%m%d", time.localtime(timestamp))

stocks = []
stock_codes = []
stocksFileContent = open('observed_stocks.data', 'r')
for stockLineData in stocksFileContent:
    if stockLineData.startswith('#'):
        continue
    stockLineData = stockLineData.strip('\n')
    stock_detail = stockLineData.split()
    name = stock_detail[0]
    code = stock_detail[1]
    stock_codes.append(code)
    start = stock_detail[2]
    to = stock_detail[3]
    stock = StockModel.StockModel(name, code, int(start), int(to))
    stocks.append(stock)

todayStockData = Stock.get_stock_basic(','.join(stock_codes), today)

# 保证请求股票的数量与返回的数量是一致的
assert (todayStockData.shape[0] == len(stocks))

codeStockDict = {}

for index, row in todayStockData.iterrows():
    codeStockDict[row[0]] = row

for stock in stocks:
    series = codeStockDict[stock.code]
    stock.openP = series[2] * 100
    stock.low = series[4] * 100
    stock.close = series[5] * 100
    stock.calc()
    if stock.is_leak:
        print(stock.name)
