import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import jpholiday
import datetime

def getStockPriceData(stock_code):
    symbol = stock_code + '.T'
    stock = share.Share(symbol)
    pereod = getWorkDayPeriod()
    data = stock.get_historical(share.PERIOD_TYPE_DAY, pereod, share.FREQUENCY_TYPE_DAY, 1)
    return data

def getWorkDayPeriod():
    period = 20
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

