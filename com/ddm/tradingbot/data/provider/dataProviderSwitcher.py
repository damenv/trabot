"""
Switcher to select the data provider
"""
from com.ddm.tradingbot.data.provider import yFinanceProvider, yahooFinancialsProvider


class dataProviderSwitcher:

    def yfinance(self, ticker):
        yfinance_object = yFinanceProvider.yFinanceProvider(ticker)
        return yfinance_object

    def yahooFinancials(self, ticker) -> yahooFinancialsProvider:
        yahoo_financials_object = yahooFinancialsProvider.yahooFinancialsProvider(ticker)
        return yahoo_financials_object

    def getProvider(self, argument, ticker):
        # Get the function from switcher dictionary
        function_name = str(argument)
        function = getattr(self, function_name, lambda: "Invalid provider")
        return function(ticker)


