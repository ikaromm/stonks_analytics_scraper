from stonks_analytics_scraper.scraper.shape.fiis import FII_SHAPE
from stonks_analytics_scraper.scraper.shape.stocks import STOCK_SHAPE

from enum import Enum


class ResourceType(Enum):
    STOCK = "acoes"
    FII = "fiis"

    def get_shape(self):
        match self:
            case ResourceType.STOCK:
                return STOCK_SHAPE
            case ResourceType.FII:
                return FII_SHAPE
            case _:
                raise ValueError("resource type not supported")
