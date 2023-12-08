from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan']")


@when('Click add to cart button')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(4)


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has {number} item(s)')
def verify_cart(context, number):
    subtotal_text = context.driver.find_element(*CART_SUMMARY).text
    assert number in subtotal_text, f"Expected '{number} item' not in {subtotal_text}"


