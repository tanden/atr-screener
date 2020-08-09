import csv

def getStockCodeArray():
    stock_codes = []
    with open('/app/data/screener_result.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].isnumeric():
                stock_codes.append(row[0])

    return stock_codes