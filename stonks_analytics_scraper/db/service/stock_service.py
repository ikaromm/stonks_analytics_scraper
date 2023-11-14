from stonks_analytics_scraper.db.mapper.namedtuple import StockTuple

from collections import namedtuple
from datetime import datetime


class StockService:
    def __init__(self, stock_repository):
        self.stock_repository = stock_repository

    def save_scrapped_data(self, data: StockTuple):
        stock = self.stock_repository.get_stock_native(data.stock.ticker)
        if stock is None:
            self.stock_repository.save_stock(data.stock)
        else:
            data.stock.id = stock.id
            self.stock_repository.update_stock(data.stock)

        # data.stock_price.stock = data.stock
        # self.stock_repository.save_stock_price(data.stock_price)

        current_datetime = datetime.now()
        data.stock_statistics.stock_id = data.stock.id
        data.stock_statistics.month = current_datetime.month
        data.stock_statistics.year = current_datetime.year

        stock_statistics = self.stock_repository.get_stock_statistics_native(
            data.stock.ticker,
            data.stock_statistics.month,
            data.stock_statistics.year,
        )
        if stock_statistics is None:
            self.stock_repository.save_stock_statistics(data.stock_statistics)
