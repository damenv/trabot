'''
Class to obtain data provider, and in case that call fails, switch to secondary provider
'''
import sys

from com.ddm.tradingbot.data.provider.dataProviderSwitcher import dataProviderSwitcher
from com.ddm.tradingbot.data.provider.yFinanceProvider import yFinanceProvider
from com.ddm.tradingbot.data.provider.yahooFinancialsProvider import yahooFinancialsProvider


class financialDataProvider(dataProviderSwitcher):
    __primaryProvider = "yfinance"
    __secondaryProvider = "yahooFinancials"
    __dataProvider: yFinanceProvider
    __dataProviderSecondary: yahooFinancialsProvider
    defaultSecondary = False

    def __init__(self, primaryProvider: str = None, secondaryProvider: str = None):
        if primaryProvider is not None:
            self.__primaryProvider = primaryProvider

        if secondaryProvider is not None:
            self.__secondaryProvider = secondaryProvider

        self.__dataProvider = self.getProvider(self.__primaryProvider, "MSFT")
        self.__dataProviderSecondary = self.getProvider(self.__secondaryProvider, "MSFT")

    def getCloseData(self, ticker, start_date, end_date, interval) -> dict:
        if self.defaultSecondary:
            self.__dataProviderSecondary.getClosePrice(ticker, start_date, end_date, interval)
        else:
            try:
                return self.__dataProvider.getClosePrice(start_date, end_date, interval)
            except Exception as e:
                print("Unexpected error: ", e)
                self.defaultSecondary = True
                return self.__dataProviderSecondary.getClosePrice(ticker, start_date, end_date, interval)

    def getOHCLV(self, ticker, start_date, end_date, interval) -> dict:
        if self.defaultSecondary:
            self.__dataProviderSecondary.getOHLCV(ticker, start_date, end_date, interval)
        else:
            try:
                return self.__dataProvider.getOHLCV(ticker, start_date, end_date, interval)
            except:
                self.defaultSecondary = True
                return self.__dataProviderSecondary.getOHLCV(ticker, start_date, end_date, interval)