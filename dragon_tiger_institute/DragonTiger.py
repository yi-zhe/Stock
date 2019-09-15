# 机构交易龙虎榜数据
import pandas as pd
import tushare as ts
import time
import os
from basic import Stock

# 初始化API
ts.set_token('3e91d9e988c8b6c6632024fe3b14de2f0cf74fdb2e6835b7f925e9a5')
pro = ts.pro_api()

# 获得当天的日期
timestamp = time.time()
today = time.strftime("%Y%m%d", time.localtime(timestamp))

file = today + '.csv'
if not os.path.exists(file):
    data = pro.top_inst(trade_date=today)
    grouped = data.groupby('ts_code')
    columns = ['ts_code', 'name', 'net_buy', 'percent']
    grouped_by_code = pd.DataFrame(columns=columns)
    all_stock = Stock.get_all_stocks()
    for ts_code, group in grouped:
        one_stock = all_stock[all_stock['ts_code'] == ts_code]
        if one_stock.empty:
            continue
        stock_name = one_stock['name'].iloc[0]
        net_buy = group['net_buy'].sum()
        percent = Stock.get_stock_basic(ts_code=ts_code, date=today)['pct_chg'].iloc[0]
        stock = pd.DataFrame({'ts_code': [ts_code], 'name': [stock_name], 'net_buy': [float('%.2f' % net_buy)],
                              'percent': [float('%.2f' % percent)]})
        if ('ST' not in stock_name) and ('退' not in stock_name):
            grouped_by_code = pd.concat([grouped_by_code, stock])
        grouped_by_code = grouped_by_code.sort_values(by=['percent', 'net_buy'], ascending=(False, False))
        time.sleep(0.8)
    grouped_by_code.to_csv(file, index=False)
    print(grouped_by_code)
else:
    print('文件以及生成')
