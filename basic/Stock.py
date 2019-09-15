# 获取股票基本信息
import tushare as ts


# 获取一只股票在指定日期的交易数据
def get_stock_basic(ts_code, date):
    ts.set_token('3e91d9e988c8b6c6632024fe3b14de2f0cf74fdb2e6835b7f925e9a5')
    pro = ts.pro_api()
    return pro.daily(ts_code=ts_code, start_date=date, end_date=date)


# 获取指定日期正常上市的股票列表
def get_all_stocks():
    ts.set_token('3e91d9e988c8b6c6632024fe3b14de2f0cf74fdb2e6835b7f925e9a5')
    pro = ts.pro_api()
    return pro.stock_basic(exchange='', list_status='L')
