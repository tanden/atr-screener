import lib.csv_handler as csv_handler
import lib.stock_info as stock_info
import pprint
import webbrowser
import time

def buildUrl(stock_code):
    return 'https://site1.sbisec.co.jp/ETGate/?_ControlID=WPLETsiR001Control&_PageID=WPLETsiR001Idtl30&_DataStoreID=DSWPLETsiR001Control&_ActionID=DefaultAID&s_rkbn=&s_btype=&i_stock_sec=' \
    + stock_code \
    + '&i_dom_flg=1&i_exchange_code=TKY&i_output_type=2&exchange_code=TKY&stock_sec_code_mul=' \
    + stock_code \
    + '&ref_from=1&ref_to=20&wstm4130_sort_id=&wstm4130_sort_kbn=&qr_keyword=&qr_suggest=&qr_sort=' \


def main():
    stocks = csv_handler.getStockCodeArray()
    for stock_code in stocks:
        url = buildUrl(stock_code)
        time.sleep(1)
        webbrowser.open_new_tab(url)
main()