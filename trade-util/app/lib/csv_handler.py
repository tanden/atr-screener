import csv
import pathlib
import glob
import logging
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def getStockCode() -> list:
    stock_codes = []
    csv_path = pathlib.Path('data/screener_result.csv')
    with open(csv_path.resolve()) as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].isnumeric():
                stock_codes.append(row[0])

    return stock_codes

def getEliminateStockCode() -> list:
    eliminate_stock_codes = []
    csv_files = glob.glob('data/New_file*.csv')
    for csv_file in csv_files:
        with open(csv_file, 'r', encoding='shift_jis') as file:
            rows = list(csv.reader(file))
            total_number = getTotalNumber(rows)
            trimed_rows = trimUnusedHeaders(rows)
            for i in range(total_number):
                eliminate_stock_codes.append(getEliminateStockCodes(trimed_rows[i]))

    return eliminate_stock_codes

def getTotalNumber(rows: list) -> int:
    pattern = r'\d+'
    return [int(match) for match in re.findall(pattern, rows[3][0])][0]

def getEliminateStockCodes(row: list) -> int:
    pattern = r'\d+'
    return [int(match) for match in re.findall(pattern, row[0])][0]

def trimUnusedHeaders(rows: list) -> list:
    start_index = 0
    end_index = 8
    del rows[start_index:end_index]
    return rows
