DSCI 511 Final Project - Stock Data Scraper and Analysis

Project Overview

This project provides a toolset for scraping and analyzing stock market data using Python. The project leverages Selenium for web scraping and includes various utilities for logging, data parsing, and stock analysis. The tools are designed to extract stock information from public websites like Nasdaq and provide detailed analytics, such as historical stock performance and company profiles.

Features

Scrape Stock Data:

Retrieves data from the Nasdaq website and S&P 500 stock list.

Collects detailed stock information including symbol, price, industry, sector, IPO date, employees, and more.

Historical Data Analysis:

Downloads and saves historical stock data as CSV files for further analysis.

Logging:

Comprehensive logging for debugging and monitoring, including both file-based and console-based logs.

Headless Browsing:

Utilizes Selenium's headless mode for efficient and resource-saving browsing.

Files and Structure

main.py

Entry point of the project.

Initializes the Firefox WebDriver and scrapes data from the S&P 500 stocks list.

nasdaq.py

Contains functions for scraping Nasdaq stock data and parsing HTML content.

Saves raw HTML content and displays stock name and price in a formatted table.

stock_analysis.py

Implements the StockAnalysisScraper class.

Includes methods for fetching S&P 500 stock list, retrieving stock details, and processing historical data.

logger.py

Provides logging utilities using Python's logging library.

Includes a file-based logger and a console logger compatible with progress bars.

Installation

Clone the repository to your local machine.

git clone <repository-url>
cd <repository-directory>

Install dependencies:

pip install -r requirements.txt

Ensure that Firefox and the corresponding geckodriver are installed and added to your system's PATH.

Usage

Running the Project

To scrape S&P 500 stock data, run the main.py script:

python main.py

To scrape and analyze a specific Nasdaq stock, run the nasdaq.py script:

python nasdaq.py

Outputs

Scraped stock data is saved in a data/ directory as CSV files.

Logs are stored in the logs/ directory.

Dependencies

Python 3.7+

Selenium

BeautifulSoup4

pandas

tqdm

geckodriver (for Selenium WebDriver)

Project Workflow

Initialize WebDriver:

Set up a headless Firefox browser instance.

Load target URLs for scraping.

Scrape Data:

Extract stock data from tables and detailed information pages.

Save Outputs:

Save scraped data as structured CSV files.

Log Events:

Record progress and errors in log files for troubleshooting.

Future Enhancements

Add support for additional stock exchanges and regions.

Implement data visualization for stock trends.

Enhance error handling for dynamic web content.

Incorporate parallel processing for faster data scraping.

Contributors

[Your Name/Team Name]

University of British Columbia

Course: DSCI 511

