"""
Using yfinance library to obtain the stock data
"""

import datetime as dt
import yfinance as yf
import pandas as pd

from com.ddm.tradingbot.data.provider.providerBase import providerBase


class yFinanceProvider(providerBase):

    ticker = ""
    valor = "yyyiii"

    def __init__(self, ticker):
        self.ticker = ticker

    def getOHLCV(self, start_date, end_date) -> dict:
        return yf.download(self.ticker, start_date, end_date)

    def getOHLCV(self, ticker_list, start_date, end_date) -> dict:
        ohlcv_data = {}
        for ticker in ticker_list:
            ohlcv_data[ticker] = yf.download(ticker, start_date, end_date)

    def getClosePrice(self, start_date, end_date, interval) -> dict:
        return yf.download(self.ticker, start_date, end_date)["Adj Close"]

    def getClosePrice_list(self, ticker_list: list, start_date, end_date) -> dict:
        close_price = pd.DataFrame()
        for ticker in ticker_list:
            close_price[ticker] = yf.download(ticker, start_date, end_date)["Adj Close"]
        return close_price
