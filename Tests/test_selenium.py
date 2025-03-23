from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_google_search():
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open a website
        driver.get("https://www.google.com")

        # Find the search box and type 'Salesforce'
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Salesforce")

        # Wait for a moment
        time.sleep(2)

        # Assert that the search box contains 'Salesforce' (basic test)
        assert "Salesforce" in search_box.get_attribute("value")
    finally:
        # Close the browser
        driver.quit()
