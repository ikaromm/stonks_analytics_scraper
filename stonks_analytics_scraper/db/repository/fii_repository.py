from stonks_analytics_scraper.db.entity.base import Base
from stonks_analytics_scraper.db.entity.fiis import (
    Fii,
    FiiPrice,
    FiiStatistics,
)

from sqlalchemy.engine import Engine


class FiiRepository:
    def __init__(self, engine: Engine):
        self.engine = engine

        Base.metadata.create_all(engine)

    def save_fii(self, fii: Fii):
        pass

    def save_fii_price(self, fii_price: FiiPrice):
        pass

    def save_fii_statistics(self, fii_statistics: FiiStatistics):
        pass

    def get_fii(self, fii_ticker: str) -> Fii:
        pass

    def get_fii_price(self, fii_ticker: str) -> FiiPrice:
        pass

    def get_fii_statistics(self, fii_ticker: str) -> FiiStatistics:
        pass
