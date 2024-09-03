import time
from PageObject.searchBar import LandingPage


class Test_001:
    def test_title(self, setup):
        self.driver = setup
        self.driver.get('https://www.amazon.in/ref=nav_logo')
        title= self.driver.title
        assert title == 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
        time.sleep(2)
        self.driver.close()

    def test_searchBox(self, setup):
        self.driver = setup
        self.driver.get('https://www.amazon.in/ref=nav_logo')
        self.lp = LandingPage(self.driver)
        self.lp.searchBar()
        self.lp.clickOnSearchIcon()
        time.sleep(2)
        self.driver.close()

    def test_getAllLinks(self, setup):
        self.driver = setup
        self.driver.get('https://www.amazon.in/ref=nav_logo')
        self.lp = LandingPage(self.driver)
        nums_link=self.lp.countUrlsFromHomePage()
        print(f"Number of links on the homepage: {nums_link}")
        time.sleep(2)
        self.driver.close()

