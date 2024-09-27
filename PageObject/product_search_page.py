import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.config_utils import ConfigUtilities


class ProductSearchPage:
    # Instance of the config.yaml
    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    # Locators
    SEARCH_BAR_ICON = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    ITEM = 'apple iphone 15 128 gb - yellow'
    SEARCH_ICON = (By.CSS_SELECTOR, "input[type='submit']")
    SEARCH_RESULTS = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Get the search item from the search results.
    def verify_search_results(self):
        wait = WebDriverWait(self.driver, 10)
        search_results = wait.until(EC.visibility_of_all_elements_located(
            self.SEARCH_RESULTS))
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

    # Method to switch to a new tabs.
    def switchTab(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])



