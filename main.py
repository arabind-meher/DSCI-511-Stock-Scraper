import os
import pandas as pd
from selenium import webdriver

from stock_analysis import StockAnalysis

if __name__ == "__main__":
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("-private")
    browser = webdriver.Firefox(options=firefox_options)
    browser.maximize_window()

    stock_scraper = StockAnalysis(browser)
    links = stock_scraper.get_snp500_list()
    # print(f"{links[0] = }")
    stock_df = stock_scraper.get_stock_data(
        links[:10], action="save", directory="test_data"
    )

    browser.quit()
