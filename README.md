# Flipkart Web Scraper

This project is a Python-based web scraper that uses **Selenium** and **BeautifulSoup** to scrape product information from the Flipkart website. The scraper mimics browser activity and can bypass JavaScript-rendered content, making it suitable for websites that use dynamic content loading.

## Features

- **Headless Browser**: The scraper runs Chrome in headless mode, allowing it to operate in the background without opening a visible browser window.
- **Dynamic Content Handling**: Using Selenium, the scraper waits for JavaScript-rendered content to load before scraping.
- **Popup Handling**: Automatically closes the login popup on Flipkart if it appears.
- **Customizable Scraping**: Modify the scraping logic to extract any kind of data from Flipkart’s homepage.

## Requirements

To run the scraper, ensure you have the following Python packages installed:

- `selenium`
- `beautifulsoup4`
- `webdriver-manager`

You can install the necessary packages using the following command:

```bash
pip install -r requirements.txt
```
Note: Make sure you have Google Chrome installed and that the version matches the ChromeDriver.

How to Use
Clone the repository:

```bash

git clone https://github.com/yourusername/flipkart-scraper.git
cd flipkart-scraper
```
Set up a virtual environment (optional but recommended):

```bash

python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
Install dependencies:

```bash

pip install -r requirements.txt
```
Run the scraper:

```bash

python3 main.py
```
## Customize the scraper:

Modify the flipkart_scraper() function in main.py to extract different data based on your needs. The example currently extracts product names from the homepage.

## Code Structure
* main.py: The main Python script that runs the web scraper.
* requirements.txt: A file listing the required Python packages.
* README.md: This documentation file.
### Notes
- Headless Mode: The scraper runs in headless mode by default. If you want to see the browser in action, remove or comment out the line in main.py:

```python
chrome_options.add_argument("--headless")
```
- Proxy Support: If you're facing rate limiting or IP blocking issues, you can use a proxy by uncommenting the proxy section in the script and adding your proxy details.

## Troubleshooting
403 Forbidden Error: If you encounter a 403 error, make sure you’re using a valid User-Agent header or consider using Selenium, which fully emulates browser behavior.
ChromeDriver Version Mismatch: Ensure that your installed Chrome browser version matches the ChromeDriver version. The script uses webdriver-manager to automatically download and install the appropriate version.