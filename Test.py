from StockModel import StockModel

stock = StockModel.StockModel('hi', '002392.SZ', 304, 404)
stock.openP = 405
stock.low = 404
stock.close = 406
stock.calc()
if stock.is_leak:
    print("leak")
else:
    print("no leak")
