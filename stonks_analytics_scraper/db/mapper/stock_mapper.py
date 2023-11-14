from stonks_analytics_scraper.db.entity.stocks import (
    Stock,
    StockPrice,
    StockStatistics,
)
from stonks_analytics_scraper.db.mapper.mapper import Mapper
from stonks_analytics_scraper.scraper.shape.stocks import STOCK_SHAPE

from collections import namedtuple


class StockMapper(Mapper):
    data_shape: list[dict] = STOCK_SHAPE

    parsed_data = namedtuple(
        "ParsedData",
        [
            "stock",
            "stock_price",
            "stock_statistics",
        ],
    )

    def map(self, data: dict) -> parsed_data:
        stock = self.parse_stock(data)

        stock_price = self.parse_stock_price(data)

        stock_statistics = self.parse_stock_statistics(data)

        return self.parsed_data(
            stock=stock,
            stock_price=stock_price,
            stock_statistics=stock_statistics,
        )

    def parse_stock(self, data) -> Stock:
        stocks_columns = [column.key for column in Stock.__table__.columns]

        return Stock(**self.parse_data(data, stocks_columns))

    def parse_stock_price(self, data) -> StockPrice:
        stock_price_columns = [column.key for column in StockPrice.__table__.columns]

        return StockPrice(**self.parse_data(data, stock_price_columns))

    def parse_stock_statistics(self, data) -> StockStatistics:
        stock_statistics_columns = [
            column.key for column in StockStatistics.__table__.columns
        ]

        return StockStatistics(**self.parse_data(data, stock_statistics_columns))

    def parse_data(self, data: dict, columns: list[str]) -> dict:
        parsed_data = {}
        for key, value in data.items():
            if key in columns:
                parsed_data[key] = value

        return parsed_data
