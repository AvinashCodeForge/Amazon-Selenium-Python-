import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.amazon.in/ref=nav_signin'


@pytest.fixture(scope='function')
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()
    return driver

