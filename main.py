from selenium import webdriver

from stock_analysis import StockAnalysisScraper

if __name__ == "__main__":
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--private")
    browser = webdriver.Firefox(options=firefox_options)
    browser.maximize_window()

    stock_scraper = StockAnalysisScraper(browser)
    links = stock_scraper.get_snp500_list()
    stock_df = stock_scraper.get_stock_data(links[:10])

    browser.quit()
