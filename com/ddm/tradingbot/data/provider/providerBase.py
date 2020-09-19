"""
Base class for any data provider
"""

from abc import ABCMeta, abstractmethod


class providerBase(metaclass=ABCMeta):
    @abstractmethod
    def getOHLCV(self):
        return 0

    @abstractmethod
    def getClosePrice(self):
        return 0
