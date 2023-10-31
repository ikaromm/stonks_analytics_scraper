from stonks_analytics_scraper.scraper.format.stocks import STOCK_FORMAT
from stonks_analytics_scraper.scraper.scraper import Scraper


def main():
    scraper = Scraper(data_format=STOCK_FORMAT)

    companies = [
        "petr4",
        # "vale3",
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

    for company in companies:
        print(scraper.scrape(company))


if __name__ == "__main__":
    main()