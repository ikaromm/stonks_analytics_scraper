from stonks_analytics_scraper.db.entity.base import Base
from stonks_analytics_scraper.db.entity.stocks import (
    Stock,
    StockPrice,
    StockStatistics,
)

from sqlalchemy.engine import Engine


class StockRepository:
    def __init__(self, engine: Engine):
        self.engine = engine

        Base.metadata.create_all(engine)

    def save_stock(self, stock: Stock):
        pass

    def save_stock_price(self, stock_price: StockPrice):
        pass

    def save_stock_statistics(self, stock_statistics: StockStatistics):
        pass

    def get_stock(self, stock_ticker: str) -> Stock:
        pass

    def get_stock_price(self, stock_ticker: str) -> StockPrice:
        pass

    def get_stock_statistics(self, stock_ticker: str) -> StockStatistics:
        pass
