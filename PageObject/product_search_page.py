import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.loginPageLocators import LoginPageLocators
from Utilities.config_utils import ConfigUtilities


class ProductSearchPage:

    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    def __init__(self, driver):
        self.driver = driver
        self.LocatorsPage = LoginPageLocators()

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

    def switchTab(self):
        handles = self.driver.window_handles
        # Switch to a new tab
        self.driver.switch_to.window(handles[1])



