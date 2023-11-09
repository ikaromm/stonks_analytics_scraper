class Director:
    def __init__(self):
        pass

    def start_cron_job(self):
        """
        Start the chron job to scrape the data from the scraper
        """

    def populate(self, resource: str):
        """
        Populate the database with data from the scraper, it will accept as parameter the resource to be scraped
        """

    def _save_data(self, resource: str, data: list[dict]):
        """
        Save the data scraped from the scraper
        """