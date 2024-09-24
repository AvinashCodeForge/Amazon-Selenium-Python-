import time
import pytest
from PageObject.loginpage import LoginPage
import imaplib
import email
import re
from selenium import webdriver


class Test_001:
    url = 'https://www.amazon.in/ref=nav_signin'
    title = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'

    def test_signIn(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        login_page = LoginPage(self.driver)
        login_page.hoverOnSignIn()
        time.sleep(2)
        login_page.userEmail()
        login_page.clickContinue()
        login_page.userPassword()
        login_page.clickOnSignIn()
        time.sleep(10)
        title = login_page.getTitle()
        assert title == self.title, f"Sign-in page title mismatch! Expected '{self.title}', but got '{title}'"

    @pytest.mark.skip
    def test_verifyHomePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        login_page = LoginPage(self.driver)
        title = login_page.getTitle()
        assert title == self.title, f"Sign-in page title mismatch! Expected '{self.title}', but got '{title}'"

    def test_verifySearchItemDisplayed(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        loginPage = LoginPage(self.driver)
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        title=loginPage.getTitle()
        assert title == 'Amazon.in : apple iphone 15 128 gb - yellow'

    def test_verifyProductPage(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        loginPage = LoginPage(self.driver)
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        loginPage.verify_search_results()
        loginPage.switchTab()
        title = loginPage.getTitle()
        assert title == 'Apple iPhone 15 (128 GB) - Yellow : Amazon.in: Electronics'

    def test_verifyItemAddedToCartSuccessfully(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        loginPage = LoginPage(self.driver)
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        loginPage.verify_search_results()
        loginPage.switchTab()
        loginPage.addToCartButton()
        time.sleep(10)

    def test_verifyItemInCart(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        loginPage = LoginPage(self.driver)
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        loginPage.verify_search_results()
        loginPage.switchTab()   
        loginPage.addToCartButton()
        time.sleep(5)
        loginPage.goToCart()
        loginPage.cartItemPrice()
        loginPage.selectQuantity()
        time.sleep(10)


