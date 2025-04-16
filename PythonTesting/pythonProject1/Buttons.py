import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[1].click()
time.sleep(2)
