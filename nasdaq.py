import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrap_nasdaq(driver: webdriver.Firefox, url: str, path: str):
    try:
        print("Driver Loading URL...")
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print(f"File saved in {path}")

    except Exception as error:
        print(error)


def parse_html(path: str):
    with open(path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    stock_name = soup.find("meta", {"name": "com.nasdaq.cms.taxonomy.quoteSymbol"})
    stock_price = soup.find("div", {"class": "symbol-page-header__pricing-price"})

    if stock_name:
        stock_name = stock_name.get("content")
    if stock_price:
        stock_price = stock_price.get_text(strip=True)

    width = 20
    print("\n+" + "-" * (width - 2) + "+")
    print(f"| Stock Name: {stock_name}".ljust(width - 1) + "|")
    print(f"| Stock Price: {stock_price}".ljust(width - 1) + "|")
    print("+" + "-" * (width - 2) + "+\n")


if __name__ == "__main__":
    if not os.path.exists("html"):
        os.mkdir("html")

    print("Initiating Driver...")
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("-private")

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()

    url = "https://www.nasdaq.com/market-activity/stocks/aapl"

    path = os.path.join("html", "nasdaq.html")

    scrap_nasdaq(driver, url, path)

    print("Closing Driver...")
    driver.quit()

    parse_html(path)
