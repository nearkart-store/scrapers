from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def flipkart_scraper():
    # Set up Chrome options for headless mode (optional)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
    chrome_options.add_argument("--window-size=1920x1080")  # Ensures the webpage renders fully
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, useful in Docker
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resource problems
    chrome_options.add_argument("start-maximized")  # Start browser maximized

    # Optional: Setup Proxy if needed
    # proxy = "your_proxy_ip:your_proxy_port"
    # chrome_options.add_argument(f'--proxy-server={proxy}')

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open the Flipkart homepage
        driver.get("https://www.flipkart.com/")

        # Wait for the page to load (increase time if needed)
        time.sleep(5)

        # Optional: Bypass login or popup window (for demonstration purposes)
        try:
            # Close the login popup if it appears
            close_button = driver.find_element_by_xpath("//button[contains(text(), '✕')]")
            close_button.click()
        except Exception as e:
            print("No login popup to close. Continuing...")

        # Get the page source after dynamic content is loaded
        page_source = driver.page_source

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Example: Extract product names from Flipkart homepage (you can customize this)
        product_names = soup.find_all('a', class_='IRpwTa')  # Customize class to match the site

        # Print the extracted product names
        for product in product_names:
            print(product.get_text())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser once scraping is done
        driver.quit()

if __name__ == "__main__":
    flipkart_scraper()