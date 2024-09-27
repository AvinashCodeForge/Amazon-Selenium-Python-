import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from PageObject.loginpage import LoginPage
from Utilities.config_utils import ConfigUtilities

config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')
URL = config.get_config("url")


@pytest.fixture(scope='function')
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(setup):
    driver = setup
    driver.get(URL)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.hoverOverAndClickOnSignInButton()
    time.sleep(2)
    loginPage.emailInputField('ap_email')
    loginPage.continueButton()
    loginPage.userPassword('ap_password')
    loginPage.signInButton()
    time.sleep(2)
    return loginPage
