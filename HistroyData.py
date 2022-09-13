import json
from pprint import pprint

import ccxt
from datetime import datetime
import time


def ms_to_datetime(timeNum):
    ms_to_datetime = float(timeNum / 1000)
    _t = time.localtime(ms_to_datetime)
    _f = time.strftime("%Y-%m-%d %H:%M:%S", _t)
    return _f


exchange = ccxt.bitmex()
mk = exchange.market("BTC/USD")
print(mk)
# with open('./bitmex_markets.json', 'w') as o:
#     json.dump(mk, o)

# timestamp = datetime.strptime('2015-01-02 01:01:01.001', "%Y-%m-%d %H:%M:%S.%f")
# unix_timestamp = int(time.mktime(timestamp.timetuple()) * 1000.0 + timestamp.microsecond / 1000.0)
#
# exchange.fetch_ohlcv("BTC/USD", timeframe='1d', since=unix_timestamp, limit=100)
