from StockModel import StockModel
from basic import Stock


def get_stocks():
    stocks = []
    stock_codes = []
    stocks_file_content = open('observed_stocks.data', 'r')
    for stock_line_data in stocks_file_content:
        if stock_line_data.startswith('#'):
            continue
        stock_line_data = stock_line_data.strip('\n')
        stock_detail = stock_line_data.split()
        name = stock_detail[0]
        code = stock_detail[1]
        stock_codes.append(code)
        start = stock_detail[2]
        to = stock_detail[3]
        stock = StockModel.StockModel(name, code, int(start), int(to))
        stocks.append(stock)
    return stocks, stock_codes


def get_stock_data_and_calc(day):
    stocks, stock_codes = get_stocks()
    today_stock_data = Stock.get_stock_basic(','.join(stock_codes), day)
    # 保证请求股票的数量与返回的数量是一致的
    if today_stock_data.shape[0] != len(stocks):
        print(day + ' 数据有些问题')
        print(today_stock_data)
        return

    code_stock_dict = {}

    for index, row in today_stock_data.iterrows():
        code_stock_dict[row[0]] = row

    today_leaks = []
    for stock in stocks:
        series = code_stock_dict[stock.code]
        stock.openP = series[2] * 100
        stock.low = series[4] * 100
        stock.close = series[5] * 100
        stock.calc()
        if stock.is_leak:
            today_leaks.append(stock.name)
    print(day + '的破绽票有:')
    print(today_leaks)


if __name__ == '__main__':
    trade_days = Stock.get_trade_cal(5)
    for day in trade_days:
        get_stock_data_and_calc(day)
