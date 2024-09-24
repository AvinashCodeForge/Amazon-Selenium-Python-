import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class LoginPageLocators:
    SEARCH_BAR = '#twotabsearchtextbox'
    ITEM = 'apple iphone 15 128 gb - yellow'
    click_on_search_icon = "input[type='submit']"
    count_Urls_From_HomePage = 'a'
    click_On_Hamburger_Menu_And_Get_COunt_Of_Links = "//div[@class='nav-left']//parent::div[@id='nav-main']"

    def __init__(self, driver):
        self.driver = driver

    def searchItem(self):
        self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_BAR).send_keys(self.ITEM)

    def clickOnSearchIcon(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_on_search_icon).click()

    def countUrlsFromHomePage(self):
        elements = self.driver.find_elements(By.TAG_NAME, self.count_Urls_From_HomePage)
        count = len([element for element in elements if element.get_attribute('href')])
        return count

    def clickOnHamburgerMenuAndGetCOuntOfLinks(self):
        #
        hamburgerMenu = self.driver.find_element(By.XPATH, self.click_On_Hamburger_Menu_And_Get_COunt_Of_Links)
        hamburgerMenu.click()
        elements = self.driver.find_elements(By.TAG_NAME, 'a')
        count = len([element for element in elements if element.get_attribute('href')])
        return count

    def clickOnAddToCartButton(self):
        self.driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-none a-padding-none']//input["
                                           "@id='add-to-cart-button']").click()

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
        self.driver.find_element(By.XPATH, "//span[@id='continue']").click()

    def signInButton(self):
        self.driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()

    def clickOnCartButton(self):
        self.driver.find_element(By.XPATH,
                                 "//div[@id='attach-desktop-sideSheet']//div[@class='a-fixed-left-grid']//form//input").click()

    def itemPrice(self):
        self.driver.find_element(By.XPATH, "//span[@id='sc-subtotal-amount-activecart']").text()

    def clickDropdown(self):
        self.driver.find_element(By.XPATH, "//span[@tabindex='-1']").click()

    def checkItemIsAvailable(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Currently unavailable.']").text
