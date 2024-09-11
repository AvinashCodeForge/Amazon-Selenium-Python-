from selenium.webdriver.common.by import By
from selenium import webdriver

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

    def verify_search_results(self, search_term):
        # time.sleep(3)  # Waiting for the page to load
        search_results = self.driver.find_elements(By.XPATH, "//div[@data-cy='title-recipe']")
        desired_product = self.ITEM
        for item in search_results:
            if desired_product == item:
                item.click()
                break
