import csv
import pathlib

def getStockCodeArray():
    stock_codes = []
    csv_path = pathlib.Path('data/screener_result.csv')
    with open(csv_path.resolve()) as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].isnumeric():
                stock_codes.append(row[0])

    return stock_codes