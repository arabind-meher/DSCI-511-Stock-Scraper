import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__ == "__main__":
    firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument("--headless")
    firefox_options.add_argument("-private")

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()

    # url = "https://www.nasdaq.com/market-activity/stocks/aapl"
    # driver.get(url)

    try:
        # Navigate to the NASDAQ Apple stock page
        url = "https://www.nasdaq.com/market-activity/stocks/aapl"
        driver.get(url)

        # Wait until the stock price element is present (up to 10 seconds)
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="symbol-page-header__pricing-price"]')
            )
        )
        stock_price = price_element.text
        print(f"Stock Price: {stock_price}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()
