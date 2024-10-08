import time

from TestCases.test_product_search_page import navigateToCart
from PageObject.cart_page import CartPage


class Test_004:

    # Method to verify searched item in cart
    def test_verifyItemInCart(self, login):
        navigateToCart(login)
        cartItem = CartPage(login.driver)
        cartItem.clickOnAddToCartButton()
        time.sleep(5)
        cartItem.clickOnCartIcon()
        cartItem.cartItemPrice()
        title = login.getTitle()
        time.sleep(5)
        assert title == "Amazon.in Shopping Cart"
