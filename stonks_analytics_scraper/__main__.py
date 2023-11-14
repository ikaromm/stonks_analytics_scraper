from stonks_analytics_scraper.db.mapper.stock_mapper import StockMapper
from stonks_analytics_scraper.db.repository.stock_repository import (
    StockRepository,
)
from stonks_analytics_scraper.db.service.stock_service import StockService
from stonks_analytics_scraper.scraper.scraper import Scraper
from stonks_analytics_scraper.scraper.shape.stocks import STOCK_SHAPE

from sqlalchemy import URL, create_engine

from threading import Thread


def thread_worker(resource: str, results: list):
    results.append(Scraper(data_shape=STOCK_SHAPE).scrape(resource))


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

    companies = [
        "petr4",
        "vale3",
        "bbas3",
        "bbdc4",
        # "itub4",
        # "abev3",
        # "bbse3",
        # "brfs3",
        # "brkm5",
        # "brml3",
        # "ccro3",
        # "cple6",
    ]

    threads = []
    results = []
    for company in companies:
        thread = Thread(target=thread_worker, args=(company, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    STOCK_MAPPER = StockMapper()
    for data in results:
        parsed_data = STOCK_MAPPER.map(data)

        stock_service.save_scrapped_data(parsed_data)


if __name__ == "__main__":
    main()
