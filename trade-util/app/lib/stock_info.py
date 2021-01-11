import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import jpholiday
import datetime
import numpy as np
import pprint
import pandas as pd

# APIから38日分しか返ってこないので19日
def getAtr18DaysEma(stock_code):
    stock_prices = getStockPriceData(stock_code)
    tr_data = []
    for i in range(1, len(stock_prices['close'])):
        tr = __getTr(stock_prices['close'][i-1], stock_prices['high'][i],stock_prices['low'][i])
        tr_data.append(tr)
    
    return list(pd.Series(tr_data).ewm(span = 20).mean())

# 株式データの取得
def getStockPriceData(stock_code):
    symbol = stock_code + '.T'
    stock = share.Share(symbol)
    # max 38日分しかかえってこないのでperiodに100を入れておく
    data = stock.get_historical(share.PERIOD_TYPE_DAY, 100, share.FREQUENCY_TYPE_DAY, 1)
    return data

# True Rangeを計算して返す
def __getTr(close_price_yesterday, high_price_today, low_price_today):
    tr_cadidate = np.abs([high_price_today - low_price_today, close_price_yesterday - high_price_today, close_price_yesterday - low_price_today])
    return max(tr_cadidate)