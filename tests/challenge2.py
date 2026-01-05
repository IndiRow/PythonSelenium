from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev")

try:
    # Wait for the first element with explicit wait
    first_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "gsc-iw-id1"))
    )
    print("First element found:", first_element)
except (NoSuchElementException, TimeoutException) as e:
    print(f"First element not found: {e}")
    print("Trying alternative locators...")
    # Try alternative locators for search box
    try:
        first_element = driver.find_element(By.CSS_SELECTOR, "input.gsc-input")
        print("Found search input using CSS selector:", first_element)
    except NoSuchElementException:
        print("Search input not found with any locator")

try:
    second_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "submit"))
    )
    print("Second element found:", second_element)
except (NoSuchElementException, TimeoutException) as e:
    print(f"Second element not found: {e}")

try:
    third_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@class='d-1 fw-bold']"))
    )
    print("Third element found:", third_element)
except (NoSuchElementException, TimeoutException) as e:
    print(f"Third element not found: {e}")

time.sleep(2)
driver.quit()