from pprint import pprint

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

    try:
        # Navigate to the NASDAQ Apple stock page
        url = "https://www.nasdaq.com/market-activity/stocks/aapl"
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )

        with open("nasdaq.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

    except Exception as error:
        print(error)

    finally:
        print("Closing Driver")
        driver.quit()
