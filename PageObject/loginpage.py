import time
import pickle

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
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

    def saveCookies(self):
        # Once logged in, extract cookies
        cookies = self.driver.get_cookies()

        # Save cookies to a file for future use
        with open("amazon_cookies.pkl", "wb") as f:
            pickle.dump(cookies, f)

        self.driver.refresh()

    def switchTab(self):
        handles = self.driver.window_handles
        # Switch to a new tab
        self.driver.switch_to.window(handles[1])

    def searchItem(self):
        self.driver.find_element(*self.LocatorsPage.SEARCH_BAR_ICON).send_keys(self.LocatorsPage.ITEM)

    def clickOnSearchIcon(self):
        self.driver.find_element(*self.LocatorsPage.SEARCH_ICON).click()

    def verify_search_results(self):
        wait = WebDriverWait(self.driver, 10)
        search_results = wait.until(EC.visibility_of_all_elements_located(
            self.LocatorsPage.SEARCH_RESULTS))
        search_item = 'Apple iPhone 15 (128 GB) - Yellow'

        for item in search_results:
            if search_item == item.text:
                item.click()
                time.sleep(10)
                break

        # item_check= locatorPage.checkItemIsAvailable()
        # print('Item check:', item_check)
        # if item_check == 'Currently unavailable.':
        #     return
        # def checkItemIsAvailable(self):
        #     return self.driver.find_element(self.CHECK_ITEM).text

    def clickOnAddToCartButton(self):
        self.driver.find_element(*self.LocatorsPage.ADD_TO_CART_BUTTON).click()

    def clickOnCartIcon(self):
        self.driver.find_element(*self.LocatorsPage.CLICK_CART_ICON).click()

    def cartItemPrice(self):
        subtotal = self.driver.find_element(*self.LocatorsPage.TOTAL_CART_PRICE).text
        print(f"Total: {subtotal}")

    def selectQuantity(self):
        wait = WebDriverWait(self.driver, 10)
        select = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@tabindex='-1']"))))
        select.select_by_value('2')

    def clickOnHamburgerMenuAndGetCountOfLinks(self):

        hamburgerMenu = self.driver.find_element(*self.LocatorsPage.HAMBURGER_MENU_URLS)
        hamburgerMenu.click()
        elements = self.driver.find_elements(By.TAG_NAME, 'a')
        count = len([element for element in elements if element.get_attribute('href')])
        return count

    def itemPrice(self):
        self.driver.find_element(*self.LocatorsPage.ITEM_PRICE).text()
