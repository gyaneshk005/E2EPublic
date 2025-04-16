from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/loginpagePractise/')
driver.find_element(By.CLASS_NAME, "blinkingText").click()
win_handle = driver.window_handles
driver.switch_to.window(win_handle[1])

wait = WebDriverWait(driver, 20)
paragraph = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".im-para.red"))).text
email = paragraph[19:48]
print(paragraph)
driver.close()
driver.switch_to.window(win_handle[0])

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("Systems@1")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
message = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))).text
print(message)