from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get("https://indirow.github.io/Zultra/")
time.sleep(3)
gamesNav = driver.find_element(By.CSS_SELECTOR, "a[href='#'][title='Games']")
gamesNav.click()
time.sleep(3)

gameFirefly = driver.find_element(By.CSS_SELECTOR, "a[href='html/fireflies.html']")
gameFirefly.click()
time.sleep(5)

driver.quit()