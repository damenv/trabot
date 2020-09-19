"""
Using yahoofinancials library to obtain the stock data
"""

from yahoofinancials import YahooFinancials
import pandas as pd

from com.ddm.tradingbot.data.provider.providerBase import providerBase

class yahooFinancialsProvider(providerBase):

    yahooFinancials: YahooFinancials
    valor = "yyyfff"

    def __init__(self, ticker):
        self.yahooFinancials = YahooFinancials(ticker)

    def getOHLCV(self, ticker, start_date, end_date, interval: str) -> dict:
        ohlcv_data = {}
        json_obj = self.yahooFinancials.get_historical_price_data(start_date,end_date,interval)
        ohlcv = json_obj[ticker]['prices']
        temp = pd.DataFrame(ohlcv)[["formatted_date", "open", "high", "low", "adjclose", "volume"]]
        temp.set_index("formatted_date", inplace=True)
        temp.dropna(inplace=True)
        ohlcv_data[ticker] = temp
        return ohlcv_data

    def getClosePrice(self, ticker, start_date, end_date, interval: str) -> dict:
        close_prices = pd.DataFrame()
        json_obj = self.yahooFinancials.get_historical_price_data(start_date, end_date, interval)
        ohlv = json_obj[ticker]['prices']
        temp = pd.DataFrame(ohlv)[["formatted_date", "adjclose"]]
        temp.set_index("formatted_date", inplace=True)
        temp.dropna(inplace=True)
        close_prices[ticker] = temp["adjclose"]
        return close_prices