import requests
import time

url = 'http://hq.sinajs.cn/list=sh000001'
res = requests.get(url)
res.encoding = 'gb2312'

data = res.text.split(',')

timestamp = time.time()
today = time.strftime("%Y/%m/%d", time.localtime(timestamp))

A3 = float(data[2])
B3 = float(data[1])
C3 = float(data[3])
D6 = A3 + 4
D8 = A3 - 4
E6 = A3 + 3
E8 = A3 - 3

if B3 > A3:
    openType = '高开'
elif B3 == A3:
    openType = '平开'
else:
    openType = '低开'

indexSays = ''

if A3 < B3 < C3:
    indexSays = '风险'
if B3 > C3 > A3:
    indexSays = '弱势'
if B3 > A3 > C3:
    indexSays = '最佳选时'
if A3 == B3 and C3 > E6:
    indexSays = '风险'
if A3 == B3 and D8 < C3 < D6:
    indexSays = '弱势'
if A3 == B3 and C3 < E8:
    indexSays = '最佳选时'
if C3 > A3 > B3:
    indexSays = '最佳选时'
if A3 > C3 > B3:
    indexSays = '弱势'
if A3 > B3 > C3:
    indexSays = '洗盘'

result = today + ' ' + data[-3] + '\n'
result += '昨收:' + str(A3) + ' 今开:' + str(B3) + ' 今10点:' + str(C3) + '\n'
result += '开盘类型: ' + openType + '\n'
result += '盘口语言: ' + indexSays + '\n'
file = open('/Users/liuyang/Desktop/stock.txt', 'a')
file.write(result)
file.write('\n')
file.close()
