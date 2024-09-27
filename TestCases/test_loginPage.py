import pytest


class Test_001:
    LOGIN_PAGE_TITLE = 'Amazon Sign In'
    TITLE = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'

    # Method to verify the login page title
    @pytest.mark.order(1)
    def test_verifyLoginPageTitle(self, loginPage):
        title = loginPage.getTitle()
        assert title == self.LOGIN_PAGE_TITLE, f"Sign-in page title mismatch! Expected :{self.TITLE}, but got :{title}"

    # Method to verify the title after successful login
    @pytest.mark.order(2)
    def test_verifyLoginSuccessful(self, login):
        title = login.getTitle()
        assert title == self.TITLE, f"Sign-in page title mismatch! Expected :{self.TITLE}, but got :{title}"
