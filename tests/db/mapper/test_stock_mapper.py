from stonks_analytics_scraper.db.entity.stocks import (
    Stock,
    StockPrice,
    StockStatistics,
)
from stonks_analytics_scraper.db.mapper.stock_mapper import StockMapper

from unittest import TestCase


class TestStockMapper(TestCase):
    def setUp(self) -> None:
        self.stock_data = {
            "name": "PETROLEO BRASILEIRO S.A. PETROBRAS",
            "cnpj": "33.000.167/0001-01",
            "foundation_year": 1953,
            "sector": "Petróleo, Gás e Biocombustíveis",
            "segment": "Exploração . Refino e Distribuição",
            "net_revenue": 536320000000.00006,
            "ebitda": 207530000000.0,
            "ebit": 273209999999.99997,
            "tax": -58280000000.0,
            "gross_debt": 305450000000.0,
            "gross_profit": 273940000000.0,
            "gross_margin": 51.08,
            "net_debt": 238300000000.0,
            "net_profit": 137510000000.0,
            "net_margin": 25.64,
            "ebitda_margin": 50.94,
            "cost": -262370000000.0,
            "roe": 9.03,
            "roa": 13.41,
            "roic": 21.58,
            "dy": 25.6,
            "pvp": 1.21,
            "pl": 3.4,
            "vpa": 29.59,
            "lpa": 10.5,
            "tag_along": 100.0,
            "free_float": 63.39,
            "cagr_revenue": 8.92,
            "cagr_profit": 8.92,
            "debt_to_equity": 0.79,
            "passives_to_actives": 0.62,
        }

    def test_instance(self):
        stock_mapper = StockMapper()

        self.assertIsInstance(stock_mapper, StockMapper)

    def test_parse_data(self):
        stock_mapper = StockMapper()

        data = stock_mapper.parse_data(self.stock_data, ["name"])

        self.assertIn("name", data)
        self.assertNotIn("cnpj", data)

    def test_parse_stock(self):
        stock_mapper = StockMapper()

        stock = stock_mapper.parse_stock(self.stock_data)

        self.assertEqual(stock.name, self.stock_data["name"])
        self.assertEqual(stock.cnpj, self.stock_data["cnpj"])
        self.assertEqual(stock.foundation_date, self.stock_data["foundation_date"])
        self.assertEqual(stock.sector, self.stock_data["sector"])
        self.assertEqual(stock.segment, self.stock_data["segment"])

        self.assertIsInstance(stock, Stock)

    def test_parse_stock_price(self):
        stock_mapper = StockMapper()

        stock_price = stock_mapper.parse_stock_price(self.stock_data)

        self.assertNotIn("value", stock_price.__dict__)

        self.assertIsInstance(stock_price, StockPrice)

    def test_parse_stock_statistics(self):
        stock_mapper = StockMapper()

        stock_statistics = stock_mapper.parse_stock_statistics(self.stock_data)

        self.assertEqual(stock_statistics.net_revenue, self.stock_data["net_revenue"])
        self.assertEqual(stock_statistics.ebitda, self.stock_data["ebitda"])
        self.assertEqual(stock_statistics.ebit, self.stock_data["ebit"])
        self.assertEqual(stock_statistics.tax, self.stock_data["tax"])

        self.assertIsInstance(stock_statistics, StockStatistics)

    def test_map(self):
        stock_mapper = StockMapper()

        parsed_data = stock_mapper.map(self.stock_data)

        self.assertIsInstance(parsed_data, StockMapper.parsed_data)
        self.assertIsInstance(parsed_data.stock, Stock)
        self.assertIsInstance(parsed_data.stock_price, StockPrice)
        self.assertIsInstance(parsed_data.stock_statistics, StockStatistics)
