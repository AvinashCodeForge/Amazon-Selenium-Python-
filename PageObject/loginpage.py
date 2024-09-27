import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Utilities.config_utils import ConfigUtilities


class LoginPage:
    # Instance of the config.yaml
    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    # Locators for the login page
    CONTINUE_BUTTON = (By.XPATH, "//span[@id='continue']")
    SIGN_IN_BUTTON = (By.XPATH, "//input[@id='signInSubmit']")
    HOVER_OVER_ELEMENT = (By.ID, "nav-link-accountList")
    SIGN_IN = (By.XPATH, "//span[text()='Sign in']")

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Method to get the title of the page
    def getTitle(self):
        return self.driver.title

    # Method to hover over on the element and clicks the sign in button
    def hoverOverAndClickOnSignInButton(self):
        actions = ActionChains(self.driver)
        # Step 1: Trigger verification email via Selenium
        element = self.driver.find_element(*self.HOVER_OVER_ELEMENT)
        actions.move_to_element(element).perform()
        self.driver.find_element(*self.SIGN_IN).click()

    # Method to send input to the username field
    def emailInputField(self, input):
        email_field = self.driver.find_element(By.XPATH, f"//input[@id='{input}']")
        data = self.config.get_config('credentials')
        email = data['username']
        for char in email:
            email_field.send_keys(char)
            time.sleep(0.2)

    # Method to send input to the password field
    def userPassword(self, input):
        password_field = self.driver.find_element(By.XPATH, f"//input[@id='{input}']")
        data = self.config.get_config('credentials')
        password = data['password']
        for char in password:
            password_field.send_keys(char)
            time.sleep(0.2)

    # Method to click on the continue button after entering the username
    def continueButton(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        time.sleep(2)

    # Method to click on signIn button
    def signInButton(self):
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()
