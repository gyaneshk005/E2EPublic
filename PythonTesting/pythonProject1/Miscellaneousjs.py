from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scroll(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")



