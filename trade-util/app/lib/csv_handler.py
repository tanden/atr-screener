import csv

def getStockCodeArray():
    stock_codes = []
    with open('/Users/sumita_takaki/go/src/github.com/tanden/ATR-Screener/atr-screener/data/screener_result.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].isnumeric():
                stock_codes.append(row[0])

    return stock_codes