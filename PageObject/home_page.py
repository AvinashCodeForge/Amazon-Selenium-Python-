from selenium.webdriver.common.by import By
from Utilities.config_utils import ConfigUtilities


class HomePage:
    # Instance of the config.yaml
    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    # Locators
    SEARCH_BAR_ICON = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    ITEM = 'apple iphone 15 128 gb - yellow'
    SEARCH_ICON = (By.CSS_SELECTOR, "input[type='submit']")
    SEARCH_RESULTS = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    HAMBURGER_MENU_URLS = (By.XPATH, "//div[@class='nav-left']//parent::div[@id='nav-main']")

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Method to search for an item.
    def searchItem(self):
        self.driver.find_element(*self.SEARCH_BAR_ICON).send_keys(self.ITEM)

    # Method to click on search icon.
    def clickOnSearchIcon(self):
        self.driver.find_element(*self.SEARCH_ICON).click()

        # item_check= locatorPage.checkItemIsAvailable()
        # print('Item check:', item_check)
        # if item_check == 'Currently unavailable.':
        #     return
        # def checkItemIsAvailable(self):
        #     return self.driver.find_element(self.CHECK_ITEM).text

    # Method to click on hamburger menu to retrieve all the links
    def clickOnHamburgerMenuAndGetCountOfLinks(self):

        hamburgerMenu = self.driver.find_element(*self.HAMBURGER_MENU_URLS)
        hamburgerMenu.click()
        elements = self.driver.find_elements(By.TAG_NAME, 'a')
        count = len([element for element in elements if element.get_attribute('href')])
        return count

