from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.config_utils import ConfigUtilities


class CartPage:
    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    # Locators for the cart page
    ADD_TO_CART_BUTTON = (By.XPATH, ("//div[@class='a-section a-spacing-none a-padding-none']//input["
                                     "@id='add-to-cart-button']"))

    ITEM_PRICE = (By.XPATH, "//span[@id='sc-subtotal-amount-activecart']")
    CLICK_CART_ICON = (By.XPATH, "//div[@id='attach-desktop-sideSheet']//div[@class='a-fixed-left-grid']//form//input")
    CHECK_ITEM = (By.XPATH, "//span[text()='Currently unavailable.']")
    CLICK_DROPDOWN = (By.XPATH, "//span[@tabindex='-1']")
    TOTAL_CART_PRICE = (By.XPATH, "//span[@id='sc-subtotal-amount-activecart']")

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Method to retrieve the cart price.
    def cartItemPrice(self):
        subtotal = self.driver.find_element(*self.TOTAL_CART_PRICE).text
        print(f"Total: {subtotal}")

    # Method to select the quantity.
    def selectQuantity(self):
        wait = WebDriverWait(self.driver, 10)
        select = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@tabindex='-1']"))))
        select.select_by_value('2')

    # Method to retrieve the item price.
    def itemPrice(self):
        self.driver.find_element(*self.ITEM_PRICE).text()

    # Method to click on Add to Cart button.
    def clickOnAddToCartButton(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    # Method to click on cart icon.
    def clickOnCartIcon(self):
        self.driver.find_element(*self.CLICK_CART_ICON).click()
