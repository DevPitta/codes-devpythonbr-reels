"""
This code uses the yfinance library and results in the information of a stock.

-> Requirements:
    . pip install yfinance
"""

import yfinance as yf

ticker = yf.Ticker('HGLG11.SA')
print(ticker)

stored_information = ticker.info

for description, value in stored_information.items():
    print(description, ':', value)
