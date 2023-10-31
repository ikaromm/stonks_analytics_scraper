import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from stonks_analytics_scraper.scraper.format.stocks import STOCK_FORMAT
from stonks_analytics_scraper.utils.data_type import DataType


class Scraper:
    browser: WebDriver

    def __init__(self, base_url="https://investidor10.com.br", data_format=None):
        self.base_url = base_url
        self.data_format = data_format

        if self.data_format is None:
            raise ValueError("data_format must be specified")

    def scrape(self, resource: str) -> dict:
        self._open_resource(resource)

        data = {}

        for data_type in self.data_format:
            data[data_type["name"]] = self._get_data(data_type)

        self._close_browser()

        return data

    def _open_resource(self, resource: str):
        self.browser = webdriver.Chrome(options=self._set_chrome_options())
        wait = WebDriverWait(self.browser, 10)

        self.browser.get(self.base_url)

        search_bar = self.browser.find_element(
            "xpath",
            "/html/body/div[3]/div/div/section[1]/div/div/div[1]/div/form/div/span/input[2]",
        )
        wait.until(EC.visibility_of(search_bar))
        search_bar.send_keys(resource)
        search_bar.submit()

        try:
            first_result = self.browser.find_element(
                "xpath", '//*[@id="results"]/div/div[2]/div[1]/div/div/a/div/div[1]/img'
            )
            wait.until(EC.visibility_of(first_result))
            first_result.click()

        except:
            self.browser.quit()

            raise ValueError("resource not found")

    def _close_browser(self):
        self.browser.quit()
        del self.browser

    def _get_data(self, data_type: dict) -> any:
        match data_type["type"]:
            case DataType.STRING:
                return self._get_string(data_type["path"])
            case DataType.NUMERIC:
                return self._get_numeric(data_type["path"])
            case DataType.DATE:
                return self._get_date(data_type)
            case _:
                raise ValueError("data type not supported")

    def _get_string(self, xpath: str) -> str:
        return self._wait_value(xpath)

    def _get_numeric(self, xpath: str) -> float:
        value = self._wait_value(xpath)
        return float(value.replace(".", "").replace(",", "."))

    def _get_date(self, data_type: dict) -> datetime:
        value = self._wait_value(data_type["path"])
        return datetime.strptime(value, data_type["format"])

    def _wait_value(self, xpath: str) -> str:
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        return self.browser.find_element("xpath", xpath).text

    def _set_chrome_options(self):
        """Sets chrome options for Selenium.
        Chrome options for headless browser is enabled.
        """
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        return chrome_options


if __name__ == "__main__":
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
