from selenium.webdriver.common.by import By
from locators.loginPageLocators import LoginPageLocators
from Utilities.config_utils import ConfigUtilities


class HomePage:

    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    def __init__(self, driver):
        self.driver = driver
        self.LocatorsPage = LoginPageLocators()

    def searchItem(self):
        self.driver.find_element(*self.LocatorsPage.SEARCH_BAR_ICON).send_keys(self.LocatorsPage.ITEM)

    def clickOnSearchIcon(self):
        self.driver.find_element(*self.LocatorsPage.SEARCH_ICON).click()

        # item_check= locatorPage.checkItemIsAvailable()
        # print('Item check:', item_check)
        # if item_check == 'Currently unavailable.':
        #     return
        # def checkItemIsAvailable(self):
        #     return self.driver.find_element(self.CHECK_ITEM).text

    def clickOnHamburgerMenuAndGetCountOfLinks(self):

        hamburgerMenu = self.driver.find_element(*self.LocatorsPage.HAMBURGER_MENU_URLS)
        hamburgerMenu.click()
        elements = self.driver.find_elements(By.TAG_NAME, 'a')
        count = len([element for element in elements if element.get_attribute('href')])
        return count

