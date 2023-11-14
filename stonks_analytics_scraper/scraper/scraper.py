from __future__ import annotations

from stonks_analytics_scraper.scraper.resource_type import ResourceType
from stonks_analytics_scraper.utils.data_type import DataType

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import re
import time
from datetime import datetime


class Scraper:
    browser: WebDriver

    def __init__(
        self, base_url="https://investidor10.com.br", resource_type: ResourceType = None
    ):
        self.base_url = base_url
        self.resource_type = resource_type

        if resource_type is None:
            raise ValueError("resource_type must be specified")

    def scrape(self, resource: str) -> dict:
        self._open_resource(resource)

        data = {"ticker": resource}

        for data_type in self.resource_type.get_shape():
            data[data_type["name"]] = self._get_data(data_type)

        self._close_browser()

        return data

    def _open_resource(self, resource: str):
        self.browser = webdriver.Chrome(options=self._set_chrome_options())
        wait = WebDriverWait(self.browser, 10)

        self.browser.get(f"{self.base_url}/{self.resource_type.value}/{resource}/")

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

    def _get_string(self, xpath: str) -> str | None:
        return self._wait_value(xpath)

    def _get_numeric(self, xpath: str) -> float | None:
        value = self._wait_value(xpath)
        if value is None:
            return None

        value = value.replace(".", "").replace(",", ".")

        scale = 10**0

        if "Bilhões" in value or "B" in value:
            scale = 10**9

        elif "Milhões" in value or "M" in value:
            scale = 10**6

        elif "Mil" in value or "K" in value:
            scale = 10**3

        # if numeric in % type return numeric + %
        if "%" in value:
            percentage_text = value.rstrip(
                "%"
            )  # Remove the percentage sign from the end
            return float(percentage_text)

        # if field empty return 0
        if "-" == value:
            return float(0)

        return float(re.sub("[^\\d.-]", "", value)) * scale

    def _get_date(self, data_type: dict) -> datetime:
        value = self._wait_value(data_type["path"])
        return datetime.strptime(value, data_type["format"])

    def _wait_value(self, xpath: str) -> str | None:
        try:
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

            return self.browser.find_element("xpath", xpath).text
        except:
            return None

    def _set_chrome_options(self):
        """Sets chrome options for Selenium.
        Chrome options for headless browser is enabled.
        """
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        return chrome_options
