import time
import pytest
from PageObject.loginpage import LoginPage


class Test_001:
    URL = 'https://www.amazon.in/ref=nav_signin'
    title = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
    SHORT_WAIT = 2

    @pytest.fixture(scope='function')
    def test_signIn(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        loginPage = LoginPage(self.driver)
        loginPage.hoverOnSignIn()
        time.sleep(self.SHORT_WAIT)
        loginPage.userEmail()
        loginPage.clickContinue()
        loginPage.userPassword()
        loginPage.clickOnSignIn()
        time.sleep(self.SHORT_WAIT)
        return loginPage

    def test_verifyHomePageTitle(self, test_signIn):
        loginPage = test_signIn
        title = loginPage.getTitle()
        assert title == self.title, f"Sign-in page title mismatch! Expected '{self.title}', but got '{title}'"

    def test_verifySearchItemDisplayed(self, test_signIn):
        loginPage = test_signIn
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        title = loginPage.getTitle()
        assert title == 'Amazon.in : apple iphone 15 128 gb - yellow'

    def test_verifyProductPage(self, test_signIn):
        loginPage = test_signIn
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        loginPage.verify_search_results()
        loginPage.switchTab()
        title = loginPage.getTitle()
        assert title == 'Apple iPhone 15 (128 GB) - Yellow : Amazon.in: Electronics'

    def test_verifyItemAddedToCartSuccessfully(self, test_signIn):
        loginPage = test_signIn
        self.driver.maximize_window()
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        loginPage.verify_search_results()
        loginPage.switchTab()
        loginPage.addToCartButton()
        time.sleep(10)

    def test_verifyItemInCart(self, test_signIn):
        loginPage = test_signIn
        self.driver.maximize_window()
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
