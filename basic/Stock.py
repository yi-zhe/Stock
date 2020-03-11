# 获取股票基本信息
import tushare as ts
import time


# 获取一只股票在指定日期的交易数据
def get_stock_basic(ts_code, date):
    ts.set_token('3e91d9e988c8b6c6632024fe3b14de2f0cf74fdb2e6835b7f925e9a5')
    pro = ts.pro_api()
    return pro.daily(ts_code=ts_code, trade_date=date)


# 获取指定日期正常上市的股票列表
def get_all_stocks():
    ts.set_token('3e91d9e988c8b6c6632024fe3b14de2f0cf74fdb2e6835b7f925e9a5')
    pro = ts.pro_api()
    return pro.stock_basic(exchange='', list_status='L')


# 获取最近N个交易日日期
def get_trade_cal(n):
    ts.set_token('3e91d9e988c8b6c6632024fe3b14de2f0cf74fdb2e6835b7f925e9a5')
    pro = ts.pro_api()
    timestamp = time.time()
    today = time.strftime("%Y%m%d", time.localtime(timestamp))
    n_day_before_timestamp = timestamp - (n + 5) * 24 * 60 * 60
    n_day_before = time.strftime("%Y%m%d", time.localtime(n_day_before_timestamp))
    data = pro.trade_cal(start_date=n_day_before, end_date=today)
    data = data.reindex(index=data.index[::-1])
    trade_dates = []
    for index, row in data.iterrows():
        if row['is_open'] == 1:
            trade_dates.append(row['cal_date'])
        if len(trade_dates) == n:
            break
    return trade_dates
