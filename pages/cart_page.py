from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def verify_cart_header(self):
        expected = 'Your cart is empty'
        actual = self.find_element(*self.CART_HEADER).text
        assert expected == actual, f'Expected text {expected} did not match actual {actual}'
