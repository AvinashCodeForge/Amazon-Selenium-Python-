from PageObject.home_page import HomePage
from PageObject.product_search_page import ProductSearchPage


class Test_002:
    TITLE = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'

    def test_verifyHomePageTitle(self, login):
        title = login.getTitle()
        assert title == self.TITLE, f"Sign-in page title mismatch! Expected '{self.TITLE}', but got '{title}'"

    def test_verifySearchItemDisplayed(self, login):
        homePage = HomePage(login.driver)
        homePage.searchItem()
        homePage.clickOnSearchIcon()
        title = login.getTitle()
        assert title == 'Amazon.in : apple iphone 15 128 gb - yellow'


def navigateToSearchItemPage(login):
    test = Test_002()
    test.test_verifySearchItemDisplayed(login)
    result_page = ProductSearchPage(login.driver)
    result_page.verify_search_results()
    result_page.switchTab()
