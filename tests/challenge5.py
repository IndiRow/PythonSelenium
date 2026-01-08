from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
baseLink = "https://itbooster.ru/#info"
driver.get(baseLink)
time.sleep(3)

studyButton = driver.find_element(By.ID, "radix-_R_2qmlb_")
studyButton.click()
time.sleep(3)

studyButtonLink = driver.find_element(By.XPATH, "//*[@id='radix-_R_2qmlbH1_']/a[4]")
studyButtonLink.click()
time.sleep(3)

driver.quit()
