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
    pereod = __getWorkDayPeriod(40)
    data = stock.get_historical(share.PERIOD_TYPE_DAY, pereod, share.FREQUENCY_TYPE_DAY, 1)
    return data

def getAtr20DaysEma(stock_prices):
    tr_data = []
    for i in range(1, len(stock_prices['close'])):
        tr = __getTr(stock_prices['close'][i-1], stock_prices['high'][i],stock_prices['low'][i])
        tr_data.append(tr)
    
    return list(pd.Series(tr_data).ewm(span = 20).mean())

# True Rangeを計算して返す
def __getTr(close_price_yesterday, high_price_today, low_price_today):
    tr_cadidate = np.abs([high_price_today - low_price_today, close_price_yesterday - high_price_today, close_price_yesterday - low_price_today])
    return max(tr_cadidate)


# X日前まで遡れば、営業日が所望の日数になるのか計算して、そのX日を返す
# 所望の日数は引数のrequired_work_dayで指定する
def __getWorkDayPeriod(required_work_day):
    period = required_work_day
    work_day = 0
    while True:
        check_day = datetime.date.today() - datetime.timedelta(period)
        end_day = datetime.date.today()
        while check_day <= end_day:
            if jpholiday.is_holiday(check_day) == False:
                if check_day.weekday() != 5 and check_day.weekday() != 6:
                    work_day+=1

            check_day = check_day + datetime.timedelta(days=1)
        if work_day == required_work_day:
            break
        else:
            work_day = 0
            period+=1

    return period

