from stonks_analytics_scraper.db.entity.fiis import Fii, FiiStatistics, FiiPrice
from stonks_analytics_scraper.db.mapper.mapper import Mapper
from stonks_analytics_scraper.scraper.shape.fiis import FII_SHAPE

from collections import namedtuple


class FiiMapper(Mapper):
    data_shape: list[dict] = FII_SHAPE

    parsed_data = namedtuple(
        'ParsedData', [
            'fii',
            'fii_statistics',
            'fii_price',
        ])
    
    def map(self, data: dict) -> parsed_data:
        fii = self.parse_fii(data)

        fii_statistics = self.parse_fii_statistics(data)

        fii_price = self.parse_fii_price(data)

        return self.parsed_data(
            fii=fii,
            fii_statistics=fii_statistics,
            fii_price=fii_price,
        )
    
    def parse_fii(self, data) -> Fii:
        fii_columns = [column.key for column in Fii.__table__.columns]

        return Fii(**self.parse_data(data, fii_columns))
    
    def parse_fii_statistics(self, data) -> FiiStatistics:
        fii_statistics_columns = [column.key for column in FiiStatistics.__table__.columns]

        return FiiStatistics(**self.parse_data(data, fii_statistics_columns))
    
    def parse_fii_price(self, data) -> FiiPrice:

        fii_price_columns = [column.key for column in FiiPrice.__table__.columns]

        return FiiPrice(**self.parse_data(data, fii_price_columns))
    

    def parse_data(self, data: dict, columns: list[str]) -> dict:
        parsed_data = {}
        for key, value in data.items():
            if key in columns:
                parsed_data[key] = value

        return parsed_data        