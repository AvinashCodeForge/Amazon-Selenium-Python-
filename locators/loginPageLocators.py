import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class LoginPageLocators:

    SEARCH_BAR_ICON = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    ITEM = 'apple iphone 15 128 gb - yellow'
    SEARCH_ICON = (By.CSS_SELECTOR, "input[type='submit']")
    URLS = (By.TAG_NAME, 'a')
    HAMBURGER_MENU_URLS = (By.XPATH, "//div[@class='nav-left']//parent::div[@id='nav-main']")
    ADD_TO_CART_BUTTON = (By.XPATH, ("//div[@class='a-section a-spacing-none a-padding-none']//input["
                                     "@id='add-to-cart-button']"))
    CONTINUE_BUTTON = (By.XPATH, "//span[@id='continue']")
    SIGN_IN_BUTTON = (By.XPATH, "//input[@id='signInSubmit']")
    ITEM_PRICE = (By.XPATH, "//span[@id='sc-subtotal-amount-activecart']")
    CLICK_CART_ICON = (By.XPATH, "//div[@id='attach-desktop-sideSheet']//div[@class='a-fixed-left-grid']//form//input")
    CHECK_ITEM = (By.XPATH, "//span[text()='Currently unavailable.']")
    CLICK_DROPDOWN = (By.XPATH, "//span[@tabindex='-1']")
    HOVER_OVER_ELEMENT = (By.ID, "nav-link-accountList")
    SIGN_IN = (By.XPATH, "//span[text()='Sign in']")
    SEARCH_RESULTS = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    TOTAL_CART_PRICE = (By.XPATH, "//span[@id='sc-subtotal-amount-activecart']")





