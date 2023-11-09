from stonks_analytics_scraper.db.repository.stock_repository import StockRepository
from stonks_analytics_scraper.scraper.shape.stocks import STOCK_SHAPE
from stonks_analytics_scraper.scraper.scraper import Scraper

from sqlalchemy import create_engine, URL



def main():
    # scraper = Scraper(data_shape=STOCK_SHAPE)

    # companies = [
    #     "petr4",
    #     # "vale3",
    #     # "bbas3",
    #     # "bbdc4",
    #     # "itub4",
    #     # "abev3",
    #     # "bbse3",
    #     # "brfs3",
    #     # "brkm5",
    #     # "brml3",
    #     # "ccro3",
    #     # "cple6",
    # ]

    # for company in companies:
    #     print(scraper.scrape(company))

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

if __name__ == "__main__":
    main()
