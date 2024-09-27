from TestCases.test_cart_page import Test_004
from TestCases.test_home_page import Test_002
from TestCases.test_loginPage import Test_001
from TestCases.test_product_search_page import Test_003


class TestEnd2End:

    def __init__(self):
        self.login_test = Test_001()
        self.home_pageTest = Test_002()
        self.cart_pageTest = Test_003()
        self.product_pageTest = Test_004()


if __name__ == '__main__':
    e2eTests = TestEnd2End()

