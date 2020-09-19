#!/usr/bin/env python3
"""
Main Freqtrade bot script.
Read the documentation to know what cli arguments you need.
"""
from com.ddm.tradingbot.data.financialDataProvider import financialDataProvider

import sys
# check min. python version
if sys.version_info < (3, 6):
    sys.exit("Freqtrade requires Python version >= 3.6")

import logging
from typing import Any, List

logger = logging.getLogger('tradingbot')


def main(sysargv: List[str] = None) -> None:
    """
    This function will initiate the bot and start the trading loop
    """

    return_code: Any = 1
    try:
        dataProvider = financialDataProvider()
        value = dataProvider.getCloseData("MSFT", "2020-01-01", "2020-02-01", "daily")
        print(value)
    except SystemExit as e:
        return_code = e
    except KeyboardInterrupt:
        logger.info('SIGINT received, aborting ...')
        return_code = 0
    finally:
        sys.exit(return_code)


# if __name__ == '__main__':
main()
