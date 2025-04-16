import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("hey@abc.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("22334455")
driver.find_element(By.ID, "exampleCheck1").click()


# To find custom xpath --> //tagname[@attribute='value'] --> //input[@type='submit']
# # To find custom cssselector --> tagname[attribute='value'] --> input[name='name'] -- #id = cssselector(FOR ID ONLY) --> FOR CLASS IT IS  = .CLASSNAME

driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("GYAN")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "success" in message

time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("heylooo")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()
time.sleep(2)

#static dropdown

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
time.sleep(3)
