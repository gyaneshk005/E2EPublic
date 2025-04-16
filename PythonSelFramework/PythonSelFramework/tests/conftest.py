import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
       driver: WebDriver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver: WebDriver = webdriver.Firefox()
    elif browser_name == 'IE':
        driver: WebDriver = webdriver.Ie()
        driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver
    yield
    driver.close()
