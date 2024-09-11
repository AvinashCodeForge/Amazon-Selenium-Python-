import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.loginPageLocators import LoginPageLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def switchTab(self):
        handles = self.driver.window_handles
        # Switch to a new tab
        self.driver.switch_to.window(handles[1])

    def searchItem(self):
        locatorPage = LoginPageLocators(self.driver)
        locatorPage.searchItem()

    def clickOnSearchIcon(self):
        locatorPage = LoginPageLocators(self.driver)
        locatorPage.clickOnSearchIcon()

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

    def addItemToTheCart(self):
        pass

    # def clickOnItem(self):
    #     locatorPage = LoginPageLocators(self.driver)
    #     locatorPage.item()

    def verify_search_results(self):
        wait = WebDriverWait(self.driver, 10)
        search_results = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")))
        search_item = 'Apple iPhone 15 (128 GB) - Yellow'

        for item in search_results:
            if search_item == item.text:
                item.click()
                time.sleep(10)
                break
