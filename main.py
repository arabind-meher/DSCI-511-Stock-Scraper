import os
import pandas as pd
from selenium import webdriver

from stock_analysis import StockAnalysis

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.mkdir("data")

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("-private")
    browser = webdriver.Firefox(options=firefox_options)
    browser.maximize_window()

    stock_scraper = StockAnalysis(browser)
    links = stock_scraper.get_snp500_list()
    stock_df = stock_scraper.get_stock_data(links, action="save", directory="test_data")

    browser.quit()
