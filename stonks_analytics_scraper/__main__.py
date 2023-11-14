from stonks_analytics_scraper.db.mapper.stock_mapper import StockMapper
from stonks_analytics_scraper.db.repository.fii_repository import FiiRepository
from stonks_analytics_scraper.db.repository.stock_repository import (
    StockRepository,
)
from stonks_analytics_scraper.db.service.stock_service import StockService
from stonks_analytics_scraper.scraper.scraper import Scraper
from stonks_analytics_scraper.scraper.shape.stocks import STOCK_SHAPE

from sqlalchemy import URL, create_engine


def main():
    url = URL.create(
        "postgresql+psycopg",
        host="localhost",
        port=5432,
        database="stonks_analytics",
        username="postgres",
        password="postgres",
    )
    engine = create_engine(url)

    stock_repository = StockRepository(engine)
    stock_service = StockService(stock_repository)
    # fii_repository = FiiRepository(engine)

    scraper = Scraper(data_shape=STOCK_SHAPE)

    companies = [
        # "petr4",
        "vale3",
        # "bbas3",
        # "bbdc4",
        # "itub4",
        # "abev3",
        # "bbse3",
        # "brfs3",
        # "brkm5",
        # "brml3",
        # "ccro3",
        # "cple6",
    ]

    STOCK_MAPPER = StockMapper()
    for company in companies:
        data = scraper.scrape(company)

        parsed_data = STOCK_MAPPER.map(data)

        stock_service.save_scrapped_data(parsed_data)


if __name__ == "__main__":
    main()
