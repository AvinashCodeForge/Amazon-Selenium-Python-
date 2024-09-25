import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class LoginPageLocators:
    SEARCH_BAR_ICON = By.CSS_SELECTOR, '#twotabsearchtextbox'
    ITEM = 'apple iphone 15 128 gb - yellow'
    SEARCH_ICON = By.CSS_SELECTOR, "input[type='submit']"
    URLS = By.TAG_NAME, 'a'
    HAMBURGER_MENU_URLS = By.XPATH, "//div[@class='nav-left']//parent::div[@id='nav-main']"
    ADD_TO_CART_BUTTON = By.XPATH, ("//div[@class='a-section a-spacing-none a-padding-none']//input["
                                    "@id='add-to-cart-button']")
    CONTINUE_BUTTON = By.XPATH, "//span[@id='continue']"
    SIGN_IN_BUTTON = By.XPATH, "//input[@id='signInSubmit']"
    ITEM_PRICE = By.XPATH, "//span[@id='sc-subtotal-amount-activecart']"
    CLICK_CART_ICON = By.XPATH, "//div[@id='attach-desktop-sideSheet']//div[@class='a-fixed-left-grid']//form//input"
    CHECK_ITEM = By.XPATH, "//span[text()='Currently unavailable.']"
    CLICK_DROPDOWN = By.XPATH, "//span[@tabindex='-1']"

    def __init__(self, driver):
        self.driver = driver

    def searchItem(self):
        self.driver.find_element(*self.SEARCH_BAR_ICON).send_keys(self.ITEM)

    def clickOnSearchIcon(self):
        self.driver.find_element(*self.SEARCH_ICON).click()

    def countUrlsFromHomePage(self):
        elements = self.driver.find_elements(self.URLS)
        count = len([element for element in elements if element.get_attribute('href')])
        return count

    def clickOnHamburgerMenuAndGetCOuntOfLinks(self):
        #
        hamburgerMenu = self.driver.find_element(self.HAMBURGER_MENU_URLS)
        hamburgerMenu.click()
        elements = self.driver.find_elements(By.TAG_NAME, 'a')
        count = len([element for element in elements if element.get_attribute('href')])
        return count

    def clickOnAddToCartButton(self):
        self.driver.find_element(self.ADD_TO_CART_BUTTON).click()

    def hoverOverAndClickOnSignInButton(self):
        actions = ActionChains(self.driver)
        # Step 1: Trigger verification email via Selenium
        element = self.driver.find_element(By.ID, "nav-link-accountList")
        actions.move_to_element(element).perform()
        self.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

    def emailInputField(self, input):
        email_field = self.driver.find_element(By.XPATH, f"//input[@id='{input}']")
        email = "avinashch9998@gmail.com"
        for char in email:
            email_field.send_keys(char)
            time.sleep(0.2)

    def passwordInput(self, input):
        password_field = self.driver.find_element(By.XPATH, f"//input[@id='{input}']")
        password = "demoaccount@9"
        for char in password:
            password_field.send_keys(char)
            time.sleep(0.2)

    def continueButton(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def signInButton(self):
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()

    def clickOnCartButton(self):
        self.driver.find_element(*self.CLICK_CART_ICON).click()

    def itemPrice(self):
        self.driver.find_element(*self.ITEM_PRICE).text()

    def clickDropdown(self):
        self.driver.find_element(*self.CLICK_DROPDOWN).click()

    def checkItemIsAvailable(self):
        return self.driver.find_element(*self.CHECK_ITEM).text
