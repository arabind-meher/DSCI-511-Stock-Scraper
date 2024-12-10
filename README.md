# Analysis and Extraction of Stock Data (S&P 500 Index)

Group Z:
- Arabind Meher
- Neel Patel
- Sayali Sanjay Chougule
- Ameen Aghazadeh

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Usage Guide](#usage-guide)
6. [Project Structure](#project-structure)
7. [Challenges Scraping Stock Websites](#challenges-scraping-stock-websites)
8. [Future Enhancements](#future-enhancements)
9. [Acknowledgments](#acknowledgments)

---

## Overview

The Stock Scraper project is a comprehensive tool designed to automate the process of collecting and managing stock data for companies in the S&P 500 index. By leveraging Selenium WebDriver, the scraper efficiently extracts real-time stock details, historical data, and additional financial metrics for analysis and research purposes.

With the ability to collect 28 detailed fields per stock and historical data for the last 100 days, this project simplifies the process of acquiring stock information while ensuring data integrity and accessibility. The scraper has processed over 50,000 lines of data, combining detailed stock metrics and historical performance across all S&P 500 companies. The saved data can serve as a foundation for financial studies, predictions, and more.

---

## Features

1. **Initialization and Setup**:
   - The scraper initializes by loading required dependencies, setting up the Selenium WebDriver, and defining logging configurations.

2. **Real-Time Data Scraping**:
   - Extracts data fields such as symbol, name, price, market capitalization, EPS, PE ratio, dividend information, and more from the website.
   - Saves the real-time data in CSV format.

3. **Historical Data Retrieval**:
   - Collects the last 100 days of historical stock data for each company, including fields like date, open, high, low, close, adjusted close, change, and volume.
   - Data is processed and saved in CSV format.

4. **Logging and Debugging**:
   - Detailed logs are generated throughout the execution to monitor progress and debug issues.

5. **Final Output**:
   - All scraped data is organized and stored in the `data/` directory for easy access and further analysis.

---

## Technologies Used

- **Python**: The core programming language used to write the scraper, providing versatility and powerful libraries for data manipulation and automation.

- **Selenium WebDriver**: A browser automation tool that enables interaction with web pages. Selenium allows the scraper to navigate dynamic content, handle JavaScript, and extract data effectively from stock market websites.

- **Pandas**: A data analysis and manipulation library in Python. It is used to clean, process, and store the scraped data efficiently in tabular formats like CSV.

- **Firefox WebDriver**: The browser driver for Firefox that serves as the interface between the scraper and the browser. It is used to render web pages and execute scraping scripts. Other WebDrivers can also be used, such as ChromeDriver, with minor configuration changes.

---

## Setup Instructions

### Prerequisites

1. **Python 3.x**: Ensure you have Python installed. [Download Python](https://www.python.org/downloads/)
2. **Pip**: Package manager for Python.
3. Libraries used:
   ```bash
   beautifulsoup4==4.12.3
   lxml==5.3.0
   pandas==2.2.3
   selenium==4.26.1
   tqdm==4.67.0
   ```

### Clone the Repository

```bash
git clone https://github.com/arabind-meher/DSCI-511-Stock-Scraper.git
cd DSCI-511-Stock-Scraper
```

### Install Dependencies

Use the following command to install all required Python libraries:

```bash
pip install -r requirements.txt
```

---

## Usage Guide

1. **Set Up WebDriver**:
   - Download and configure the WebDriver compatible with your browser (e.g., Firefox GeckoDriver or ChromeDriver).
   - Place the WebDriver in a directory included in your system PATH.

2. **Run the Scraper**:
   - Execute the main script to scrape stock data:
   ```bash
   python main.py
   ```

3. **View Real-Time Data**:
   - Extracted real-time stock data will be saved in the `data/` directory as CSV files. Each file contains 28 fields of stock details.

4. **Access Historical Data**:
   - Historical stock data (last 100 days) is saved in CSV format, with a separate file for each stock, within the `data/` directory.

5. **Monitor Logs**:
   - Detailed logs are maintained in the `logs/` directory. Use these for tracking the scraper's progress and troubleshooting any issues.

6. **Customize Settings**:
   - Modify the script as needed to adjust the number of historical days or the stock fields being scraped.

---

## Project Structure

```plaintext
DSCI-511-Stock-Scraper/
|
├── data/                    # Directory for storing scraped data
    ├── historical_data/     # Subdirectory for historical stock data
        ├── A.csv            # Historical data for stock A (Agilent Technologies)
        ├── AAPL.csv         # Historical data for stock AAPL (Apple)
        ├── ABBV.csv         # Historical data for stock ABBV (AbbVie)
        ├── ...              # Historical data for other stocks
    ├── stock.csv            # Consolidated real-time stock data
├── logs/                    # Directory for storing logs
├── logger.py                # Logging functionality
├── main.py                  # Main script to run the scraper
├── nasdaq.py                # NASDAQ-specific scraping functions
├── stock_analysis.py        # StockAnalysisScraper class implementation
├── utils.py                 # Utility functions (e.g., saving data locally)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation (this file)
```

---

## Challenges Scraping Stock Websites

### Nasdaq
Nasdaq posed significant challenges for data extraction due to its use of JavaScript to dynamically render HTML content. The structure of the HTML differed each time the page was loaded, making it unreliable for consistent scraping. Additionally, rate-limiting measures made it difficult to extract large volumes of data without delays or errors.

### TradingView
Access to data on TradingView was restricted due to security concerns. These restrictions prevented automated scripts from interacting with the website effectively, resulting in blocked requests and incomplete data retrieval.

### Yahoo Finance
Yahoo Finance presented challenges due to its outdated structure and slow loading times. These inefficiencies caused delays in data collection and required additional retries, making the process less efficient for large-scale data scraping efforts.

### Why These Issues Occur
Dynamic websites often generate content after the initial page load, requiring additional handling for JavaScript execution. Security restrictions and outdated web structures further complicate data extraction efforts.

---

## Future Enhancements

### Expansion to Additional Data Sources
- Integrate more reliable and diverse stock market data sources to improve data coverage and accuracy.
- Incorporate APIs from established providers like Alpha Vantage or Quandl to avoid reliance on scraping dynamic websites.

### Advanced Data Processing
- Implement advanced preprocessing techniques, such as handling missing values and outliers, to improve data quality.
- Develop mechanisms for real-time updates of stock data for enhanced analysis and predictions.

### Improved Automation and Scalability
- Enable multi-threaded scraping to reduce execution time for large-scale data retrieval.
- Add support for cloud-based scraping tools to manage extensive workloads.

### Enhanced User Accessibility
- Create an intuitive GUI for users to interact with the scraper, configure settings, and view results.
- Provide options for exporting data in additional formats, such as JSON and Excel, for better usability.

### Robust Error Handling and Logging
- Enhance error handling to address dynamic website issues, such as timeouts or unexpected element changes.
- Improve logging to include detailed diagnostic information for easier debugging.

### Data Analysis and Visualization
- Develop built-in tools for basic data analysis, such as trend detection and performance comparisons.
- Incorporate visualization features to present key stock insights in charts and graphs.

---

## Acknowledgments

We would like to express our heartfelt gratitude to everyone who contributed to the success of this project:

- **Professor Pragati Awasthi**: For her invaluable guidance and support throughout the project development process.
- **Group Members**: For their teamwork, dedication, and hard work in tackling challenges and achieving the project goals.
- **Open-Source Community**: For providing access to tools, libraries, and resources such as Selenium, Pandas, and others that made this project possible.
- **Course Organizers**: For designing a curriculum that inspired innovative thinking and problem-solving.

This project would not have been possible without the collaborative effort and shared vision of everyone involved. Thank you for making it a success!

