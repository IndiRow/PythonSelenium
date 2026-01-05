from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev")
time.sleep(3)
link = driver.find_element(By.CSS_SELECTOR, "a[href='/documentation']")
link.click()
time.sleep(3)
print('success')
driver.quit()