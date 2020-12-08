import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import jpholiday
import datetime
import numpy as np
import pprint
import pandas as pd

def getStockPriceData(stock_code):
    symbol = stock_code + '.T'
    stock = share.Share(symbol)
    pereod = __getWorkDayPeriod()
    data = stock.get_historical(share.PERIOD_TYPE_DAY, pereod, share.FREQUENCY_TYPE_DAY, 1)
    return data

def getAtr20DaysEma(stock_prices):

    tr_data = []
    for i in range(1, len(stock_prices['close'])):
        y_close_price = stock_prices['close'][i-1]
        t_high_price = stock_prices['high'][i]
        t_low_price = stock_prices['low'][i]

        atr_cadidate = np.abs([t_high_price - t_low_price, y_close_price - t_high_price, y_close_price - t_low_price])

        tr = max(atr_cadidate)
        tr_data.append(tr)
    
    return list(pd.Series(tr_data).ewm(span = 20).mean())

def __getWorkDayPeriod():
    period = 21
    work_day = 0
    while True:
        start_day = datetime.date.today() - datetime.timedelta(period)
        end_day = datetime.date.today()
        while start_day <= end_day:
            if jpholiday.is_holiday(start_day) == False:
                if start_day.weekday() != 5 and start_day.weekday() != 6:
                    work_day+=1

            start_day = start_day + datetime.timedelta(days=1)
        if work_day == 20:
            break
        else:
            work_day = 0
            period+=1

    return period

