'''
This is my learning note on the S&P Equal weight project. I don't have Jupyter Notebook, so I'll use this method instead :)

libraries:
numpy: a numerical computing library, fast execution speed. C++-based module. Often used in finance
and other places because of its fast execution speed

pandas: Panel Datas, Makes easy to work with tabular data(spreadsheet). Most used for its pandas dataframe
    dataframe: A structure use to hold tabular data

requests: A widely-used http request. Http request is a internet request to an api to get data.
We are gonna used it to called API in the library in this project

xlsxwriter: A easy wat to store excel document from a python script

math: basic library provide mathematical functions

yfinance: open source python package for public available api on yahoo finance
'''
#library

import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
import yfinance as yf


'''
this is a build-in pandas function to read csv
for csv in the same level: use name
or, I can use directionary path to called the csv
'''
#read the stock list
stocks = pd.read_csv('sp_500_stocks.csv')


#first call API
symbol = 'AAPL'

#Get market cap
AAPL = yf.Ticker(symbol)

#get price
price = AAPL.info['bid']

#get market cap
market_cap = AAPL.info['marketCap']
