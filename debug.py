import tushare as ts
import pandas as pd



pro = ts.pro_api('3b467d8c12e4e79fefd3f83e18aab27ad948c459250b43ae96aa978a')
df = pro.daily(ts_code='000001.SZ', start_date='20200701', end_date='20210718')

print(df)
