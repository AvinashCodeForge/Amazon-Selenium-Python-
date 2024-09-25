import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators.loginPageLocators import LoginPageLocators
import pickle


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginPageLocators(self.driver)

    def getTitle(self):
        return self.driver.title

    def hoverOnSignIn(self):
        self.locators.hoverOverAndClickOnSignInButton()

    def userEmail(self):
        self.locators.emailInputField('ap_email')
        time.sleep(3)

    def userPassword(self):
        self.locators.passwordInput('ap_password')
        time.sleep(3)

    def clickContinue(self):
        self.locators.continueButton()
        time.sleep(2)

    def clickOnSignIn(self):
        self.locators.signInButton()

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
        self.locators.searchItem()

    def clickOnSearchIcon(self):
        self.locators.clickOnSearchIcon()

    def getAllLinks(self, setup):
        self.driver = setup
        self.driver.get('https://www.amazon.in/ref=nav_logo')
        self.lp = LoginPageLocators(self.driver)
        nums_link = self.lp.countUrlsFromHomePage()
        print(f"Number of links on the homepage: {nums_link}")
        self.driver.close()

    def linksInHamburger(self, setup):
        self.driver = setup
        self.driver.get('https://www.amazon.in/ref=nav_logo')
        self.lp = LoginPageLocators(self.driver)
        nums_link = self.lp.clickOnHamburgerMenuAndGetCOuntOfLinks()
        print(f"Number of links on the hamburger: {nums_link}")
        self.driver.close()

    def verify_search_results(self):
        wait = WebDriverWait(self.driver, 10)
        search_results = wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")))
        search_item = 'Apple iPhone 15 (128 GB) - Yellow'

        for item in search_results:
            if search_item == item.text:
                item.click()
                time.sleep(10)
                break

    def addToCartButton(self):
        # item_check= locatorPage.checkItemIsAvailable()
        # print('Item check:', item_check)
        # if item_check == 'Currently unavailable.':
        #     return
        self.locators.clickOnAddToCartButton()

    def goToCart(self):
        self.locators.clickOnCartButton()

    def cartItemPrice(self):
        subtotal = self.driver.find_element(By.XPATH, "//span[@id='sc-subtotal-amount-activecart']").text
        print(f"Total: {subtotal}")

    def selectQuantity(self):
        wait = WebDriverWait(self.driver, 10)
        select = Select(wait.until(EC.element_to_be_clickable(self.locators.clickDropdown())))
        select.select_by_value('2')
