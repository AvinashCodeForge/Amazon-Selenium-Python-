import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators.loginPageLocators import LoginPageLocators
from Utilities.config_utils import ConfigUtilities


class LoginPage:

    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    def __init__(self, driver):
        self.driver = driver
        self.LocatorsPage = LoginPageLocators()

    def getTitle(self):
        return self.driver.title

    def hoverOverAndClickOnSignInButton(self):
        actions = ActionChains(self.driver)
        # Step 1: Trigger verification email via Selenium
        element = self.driver.find_element(*self.LocatorsPage.HOVER_OVER_ELEMENT)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

    def emailInputField(self, input):
        email_field = self.driver.find_element(By.XPATH, f"//input[@id='{input}']")
        email = "avinashch9998@gmail.com"
        for char in email:
            email_field.send_keys(char)
            time.sleep(0.2)

    def userPassword(self, input):
        password_field = self.driver.find_element(By.XPATH, f"//input[@id='{input}']")
        password = "demoaccount@9"
        for char in password:
            password_field.send_keys(char)
            time.sleep(0.2)

    def continueButton(self):
        self.driver.find_element(*self.LocatorsPage.CONTINUE_BUTTON).click()
        time.sleep(2)

    def signInButton(self):
        self.driver.find_element(*self.LocatorsPage.SIGN_IN_BUTTON).click()

