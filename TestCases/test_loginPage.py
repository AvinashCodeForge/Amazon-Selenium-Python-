import time
from PageObject.searchBar import LandingPage


class Test_001:
    def test_title(self, setup):
        self.driver = setup
        self.driver.get('https://www.amazon.in/ref=nav_logo')
        title= self.driver.title
        assert title == 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
        time.sleep(2)

    def test_searchBox(self, setup):
        self.driver = setup
        self.driver.get('https://www.amazon.in/ref=nav_logo')
        self.lp = LandingPage(self.driver)
        self.lp.searchBar()
        time.sleep(5)
        self.lp.clickOnSearchIcon()
        time.sleep(2)
        self.driver.close()
