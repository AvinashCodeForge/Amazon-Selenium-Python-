from TestCases.test_home_page import navigateToSearchItemPage


class Test_003:

    # def test_verifyItemAddedToCartSuccessfully(self, login):
    #     self.test_verifyProductPage(login)
    #     time.sleep(10)

    def test_verifyProductPage(self, login):
        navigateToSearchItemPage(login)
        title = login.getTitle()
        assert title == 'Apple iPhone 15 (128 GB) - Yellow : Amazon.in: Electronics'


def navigateToCart(login):
    test = Test_003()
    test.test_verifyProductPage(login)
