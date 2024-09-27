from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators.loginPageLocators import LoginPageLocators
from Utilities.config_utils import ConfigUtilities


class CartPage:
    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    def __init__(self, driver):
        self.driver = driver
        self.LocatorsPage = LoginPageLocators()

    def cartItemPrice(self):
        subtotal = self.driver.find_element(*self.LocatorsPage.TOTAL_CART_PRICE).text
        print(f"Total: {subtotal}")

    def selectQuantity(self):
        wait = WebDriverWait(self.driver, 10)
        select = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@tabindex='-1']"))))
        select.select_by_value('2')

    def itemPrice(self):
        self.driver.find_element(*self.LocatorsPage.ITEM_PRICE).text()

    def clickOnAddToCartButton(self):
        self.driver.find_element(*self.LocatorsPage.ADD_TO_CART_BUTTON).click()

    def clickOnCartIcon(self):
        self.driver.find_element(*self.LocatorsPage.CLICK_CART_ICON).click()
