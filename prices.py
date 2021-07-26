#a program to pull the last 20 years of closing stock prices when ticket is passed to command line and output them as a text file

import requests
import sys
import json

def create_txt():
    ticker = sys.argv[1].upper()
    f = open(f'prices.{ticker}.txt', 'w')
    filename = f'prices.{ticker}.txt'
    f.close()
    return filename

#will call alphavantage API and pull in time series stock price data, then write to a txt file the close prices
def api_call():
    
    #call API and then put that data into a JSON dictionary {sys.argv[1].upper()}
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={sys.argv[1].upper()}&outputsize=full&apikey=IMJ3EQ99Q09J1UW0'
    r = requests.get(url)
    stock_data = r.json()
    
    entry_to_add = ''
    close_price = 0
    str_index = 0
    
    f = open(f'prices.{sys.argv[1].upper()}.txt', 'w')
    
    for dates in stock_data['Time Series (Daily)']:
        close_price = stock_data['Time Series (Daily)'][dates]['4. close']
        entry_to_add = (f'{dates} {close_price}')
        f.write(entry_to_add)
        f.write('\n')

    f.close()

def main():
    if len(sys.argv) != 2:
        print('Must provide proper call')
        return
    create_txt()
    api_call()


    
main()
