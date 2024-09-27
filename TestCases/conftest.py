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
def loginPage(setup):
    driver = setup
    driver.get(URL)
    driver.maximize_window()
    time.sleep(2)
    loginPage = LoginPage(driver)
    loginPage.hoverOverAndClickOnSignInButton()
    time.sleep(2)
    return loginPage


@pytest.fixture(scope='function')
def login(loginPage):
    log = loginPage
    log.emailInputField('ap_email')
    log.continueButton()
    log.userPassword('ap_password')
    log.signInButton()
    time.sleep(2)
    return log
