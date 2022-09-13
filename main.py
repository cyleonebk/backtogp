import pandas as pd
from datetime import datetime
import backtrader as bt
import backtrader.indicators as btind

import matplotlib.pyplot as mt

btc_data_file = r"D:\User\Downloads\BTC-1H\btc-1h-combine.csv"
btc = pd.read_csv(btc_data_file, usecols=[i for i in range(6)])
btc.columns = ["datetime", "open", "high", "low", "close", "volume"]
btc["datetime"] = pd.to_datetime(btc["datetime"], unit="ms")
btc.index = btc["datetime"]
start_date = datetime(2021, 3, 1)
end_date = datetime(2022, 9, 5)

data = bt.feeds.PandasData(dataname=btc, fromdate=start_date, todate=end_date)


class MyStrategy(bt.Strategy):
    params = dict(fast_period=20,slow_period=40)

    def __init__(self):
        self.order = None
        self.ma = bt.indicator.sma(self.data, period=self.params.ma_period)

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datatime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        if self.datas[0].close[0] > self.ema[0]:
            self.order = self.buy()
        else:
            self.order = self.sell()


# print(btc)

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.adddata(data)
    print('初始资金: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('策略运行资金：%.2f' % cerebro.broker.getvalue())
