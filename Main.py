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
stocks = pd.read_csv('constituents.csv')


#first call API
symbol = 'AAPL'

#Get market cap
AAPL = yf.Ticker(symbol)

#get price
price = AAPL.info['bid']

#get market cap
market_cap = AAPL.info['marketCap']

#adding stock data to pandas dataframe
my_columns = ['Ticker', 'Price', 'Market Capitalization', 'Number of Shares to Buy']


#looping through the stock list
L = []
for stock in stocks['Symbol']:
    data = yf.Ticker(stock).info
    save_serie = pd.Series([stock, data['bid'], data['marketCap'], 'N/A'], index = my_columns)
    L.append(save_serie)
final_dataframe = pd.DataFrame(L)

#calculate how much share to bought
portfolio_size = input("Enter the value of your portfolio")

try:
    val = float(portfolio_size)
except ValueError:
    print("That's not a number. \nPlease try again: ")
    portfolio_size = input("Enter the value of your portfolio")
    val = float(portfolio_size)

position_size = val/len(final_dataframe.index)
for i in range(0, len(final_dataframe.index)):
    final_dataframe.loc[i, 'Number of Shares to Buy'] = math.floor(position_size/final_dataframe.loc[i, 'Price'])

#formatting excel output
with pd.ExcelWriter('recommended trade.xlsx') as writer:
    final_dataframe.to_excel(writer, sheet_name = 'Recommended Trade', index = False)

    background_color = '#0a0a23'
    font_color = '#ffffff'

    string_format = writer.book.add_format({
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1,
    })

    dollar_format = writer.book.add_format({
        'num_format': '$0.00',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1,
    })

    integer_format = writer.book.add_format({
        'num_format': '0',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1,
    })

    column_format = {
        'A': ['Ticker', string_format],
        'B': ['Share Price', dollar_format],
        'C': ['Market Capitalization', dollar_format],
        'D': ['Number of Shares to Buy', integer_format]
    }

    # Access the worksheet 'recommended trade'
    worksheet = writer.sheets['Recommended Trade']

    for column in column_format.keys():
        worksheet.set_column(f'{column}:{column}', 18, column_format[column][1])
        worksheet.write(f'{column}1', column_format[column][0], string_format)