import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def setup():
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()
    return driver

