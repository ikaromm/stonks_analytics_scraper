from multiprocessing import Process
from threading import Thread

from stonks_analytics_scraper.scraper.shape.stocks import STOCK_SHAPE
from stonks_analytics_scraper.scraper.scraper import Scraper


def create_scraper_worker(args, results):
    def worker():
        result = None
        try:
            result = Scraper(data_shape=STOCK_SHAPE).scrape(*args)
        except Exception as e:
            print(e)
            return

        results.append(result)

    return worker


def main():
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
        "ccro3",
        "cple6",
    ]

    results = []
    threads = []
    for company in companies:
        thread = Thread(target=create_scraper_worker((company,), results))
        thread.start()

        threads.append(thread)

    for thread in threads:
        thread.join()

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
