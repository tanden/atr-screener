import lib.csv_handler as csv_handler
import lib.stock_info as stock_info
import pprint


def main():
    stocks = csv_handler.getStockCodeArray()
    stock_info.getStockPriceData(stocks[0])


main()