from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
print("1. Браузер запущен")
driver.get("https://www.google.com")
print("2. Страница открыта")
search_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "APjFqb"))
)

search_input.send_keys("cute cats")
search_input.send_keys(Keys.RETURN)
images = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/div/div/div[1]/div/div/div[1]/div[3]/a")
time.sleep(10)

driver.quit()
