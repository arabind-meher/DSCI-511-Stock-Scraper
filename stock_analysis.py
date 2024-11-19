import os
import re
import time
from tqdm import tqdm

from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from utils import save_local
from logger import Logs


class StockAnalysis:
    """A class to perform stock data analysis using web scraping."""

    def __init__(self, driver: webdriver.Firefox) -> None:
        """Initialize the StockAnalysis class with a WebDriver and set up logging."""
        logs = Logs()
        self.file_logger = logs.get_file_logger("file_logger")
        self.console_logger = logs.get_console_logger("console_logger")

        self.driver = driver
        self.file_logger.info("StockAnalysis initialized with WebDriver.")
        self.console_logger.info("StockAnalysis initialized with WebDriver.")

    def load_driver(self, url: str, wait_time: float = 0) -> None:
        """Load the given URL and wait for a specified time."""

        self.driver.get(url)
        self.file_logger.info(f"Loaded URL: {url}")
        self.console_logger.info(f"Loaded URL: {url}")
        time.sleep(wait_time)

    def get_snp500_list(self) -> list:
        """Retrieve S&P 500 stock list from the webpage."""

        url = "https://stockanalysis.com/list/sp-500-stocks/"
        self.load_driver(url)
        self.file_logger.info("Fetching S&P 500 list.")
        self.console_logger.info("Fetching S&P 500 list.")

        table = (
            self.driver.find_element(By.ID, "main-table")
            .find_element(By.TAG_NAME, "tbody")
            .find_elements(By.TAG_NAME, "tr")
        )

        links = list(
            map(
                lambda row: row.find_element(By.TAG_NAME, "a").get_attribute("href"),
                table,
            )
        )

        self.file_logger.info(f"Retrieved {len(links)} stock links from S&P 500 list.")
        self.console_logger.info(
            f"Retrieved {len(links)} stock links from S&P 500 list."
        )
        return links

    def get_stock_data(self, urls: list, **kwargs) -> DataFrame | None:
        """Retrieve stock data for each URL in the provided list."""

        action_options = {"return", "save"}

        directory: str = kwargs.get("directory", "data")
        filename: str = kwargs.get("filename", "stock")
        action: str = kwargs.get("action", "return")

        if action not in action_options:
            raise ValueError(
                f"Invalid value for action: `{action}`. Allowed values are `{action_options}`."
            )

        stock_list = list()
        for iter, url in tqdm(
            enumerate(urls, 1), desc="Processing urls", total=len(urls)
        ):
            self.load_driver(url)
            xpath = self.__get_xpath()
            stock_data = dict()

            # Populate stock data with primary fields

            # Symbol
            stock_data["symbol"] = self.__scrap_text(xpath["symbol"])

            # Name
            name = self.__scrap_text(xpath["name"])
            stock_data["name"] = (
                re.sub(r"\s*\(.*?\)", "", name).strip() if name else name
            )

            # Price
            stock_data["price"] = self.__scrap_text(xpath["price"])

            # Process stock overview data
            overview_list = [
                self.driver.find_element(By.XPATH, xpath["overview"].get(0)),
                self.driver.find_element(By.XPATH, xpath["overview"].get(1)),
            ]

            process_row = lambda row_data: (
                re.sub(r"[()\']", "", row_data[0].text)
                .strip()
                .lower()
                .replace(" ", "_")
                .replace("-", "_"),
                row_data[1].text.strip(),
            )

            for overview in overview_list:
                for row in overview.find_elements(By.TAG_NAME, "tr"):
                    key, value = process_row(row.find_elements(By.TAG_NAME, "td"))
                    stock_data[key] = value

            # Aditional stock fields

            # Industry
            stock_data["industry"] = self.__scrap_text(xpath["industry"])

            # Sector
            stock_data["sector"] = self.__scrap_text(xpath["sector"])

            # IPO Date
            stock_data["ipo_date"] = self.__scrap_text(xpath["ipo_date"])

            # Stock Exchange
            stock_data["stock_exchange"] = self.__scrap_text(xpath["stock_exchange"])

            # Employees
            stock_data["employees"] = self.__scrap_text(xpath["employees"])

            # Website
            stock_data["website"] = self.__scrap_text(xpath["website"])

            # Log to both the main log file and the console for this line
            log_message = (
                f"{str(iter):<{3}}: {stock_data['symbol']:<{6}} - {stock_data['name']}"
            )
            self.file_logger.info(log_message)
            self.console_logger.info(log_message)

            stock_list.append(stock_data)

        stock_data_frame = DataFrame(stock_list)

        if action == "return":
            return stock_data_frame

        if action == "save":
            save_local(stock_data_frame, directory=directory, filename=filename)
            self.file_logger.info(f"Data saved to {directory}/{filename}")
            self.console_logger.info(f"Data saved to {directory}/{filename}")

    def __scrap_text(self, xpath) -> str | None:
        try:
            return self.driver.find_element(By.XPATH, xpath).text.strip()
        except NoSuchElementException:
            return None

    def __get_xpath(self) -> dict:
        """Return dictionary of XPaths for various stock details."""

        return {
            "symbol": "/html/body/div/div[1]/div[2]/main/div[3]/div[1]/div[1]/div/div[6]/span[2]",
            "name": "/html/body/div/div[1]/div[2]/main/div[1]/div[1]/div[1]/h1",
            "price": "/html/body/div/div[1]/div[2]/main/div[1]/div[2]/div[1]/div[1]",
            "overview": {
                0: "/html/body/div/div[1]/div[2]/main/div[2]/div[2]/table[1]",
                1: "/html/body/div/div[1]/div[2]/main/div[2]/div[2]/table[2]",
            },
            "industry": "/html/body/div/div[1]/div[2]/main/div[3]/div[1]/div[1]/div/div[1]/a",
            "sector": "/html/body/div/div[1]/div[2]/main/div[3]/div[1]/div[1]/div/div[2]/a",
            "ipo_date": "/html/body/div/div[1]/div[2]/main/div[3]/div[1]/div[1]/div/div[3]/span[2]",
            "stock_exchange": "/html/body/div/div[1]/div[2]/main/div[3]/div[1]/div[1]/div/div[5]/span[2]",
            "employees": "/html/body/div/div[1]/div[2]/main/div[3]/div[1]/div[1]/div/div[4]/a",
            "website": "/html/body/div/div[1]/div[2]/main/div[3]/div[1]/div[1]/div/div[7]/a",
        }
