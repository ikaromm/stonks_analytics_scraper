from stonks_analytics_scraper.db.mapper.stock_mapper import StockMapper
from stonks_analytics_scraper.db.repository.stock_repository import (
    StockRepository,
)
from stonks_analytics_scraper.db.service.stock_service import StockService
from stonks_analytics_scraper.scraper.scraper import Scraper
from stonks_analytics_scraper.scraper.shape.stocks import STOCK_SHAPE

from sqlalchemy import URL, create_engine

from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from threading import Thread


def thread_worker(resource: str):
    return Scraper(data_shape=STOCK_SHAPE).scrape(resource)


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
        "itub4",
        "abev3",
        "bbse3",
        "brfs3",
        "brkm5",
        "brml3",
        "ccro3",
        "cple6",
    ]

    futures = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        for company in companies:
            future = executor.submit(thread_worker, company)
            futures.append(future)

    STOCK_MAPPER = StockMapper()
    for future in as_completed(futures):
        parsed_data = STOCK_MAPPER.map(future.result())

        stock_service.save_scrapped_data(parsed_data)


if __name__ == "__main__":
    main()
