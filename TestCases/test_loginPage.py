import time
import pytest
from PageObject.loginpage import LoginPage
from Utilities.config_utils import ConfigUtilities
from Utilities.logger_utils import LoggerUtilities


@pytest.mark.usefixtures("setup")
class Test_001:
    config = ConfigUtilities('C:\\Users\\Avinash\\PycharmProjects\\Amazon\\Configuration\\config.yaml')

    URL = config.get_config("url")
    TITLE = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
    SHORT_WAIT = 2

    def test_verifyHomePageTitle(self, login):
        loginPage = login
        title = loginPage.getTitle()
        assert title == self.TITLE, f"Sign-in page title mismatch! Expected '{self.TITLE}', but got '{title}'"

    def test_verifySearchItemDisplayed(self, login):
        loginPage = login
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        title = loginPage.getTitle()
        assert title == 'Amazon.in : apple iphone 15 128 gb - yellow'

    def test_verifyProductPage(self, login):
        loginPage = login
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        loginPage.verify_search_results()
        loginPage.switchTab()
        title = loginPage.getTitle()
        assert title == 'Apple iPhone 15 (128 GB) - Yellow : Amazon.in: Electronics'

    def test_verifyItemAddedToCartSuccessfully(self, login):
        loginPage = login
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        loginPage.verify_search_results()
        loginPage.switchTab()
        loginPage.clickOnAddToCartButton()
        time.sleep(10)

    def test_verifyItemInCart(self, login):
        loginPage = login
        loginPage.searchItem()
        loginPage.clickOnSearchIcon()
        loginPage.verify_search_results()
        loginPage.switchTab()
        loginPage.clickOnAddToCartButton()
        time.sleep(5)
        loginPage.clickOnCartIcon()
        loginPage.cartItemPrice()
        loginPage.selectQuantity()
        time.sleep(10)
