from selenium.webdriver.common.by import By

class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    # Used Css selector for ID attribute
    def searchBar(self):
        self.driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox').send_keys('iphone')

    def clickOnSearchIcon(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

    def countUrlsFromHomePage(self):
        elements= self.driver.find_elements(By.TAG_NAME, 'a')
        count = len([element for element in elements if element.get_attribute('href')])
        return count
