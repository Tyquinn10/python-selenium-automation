from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def click_on_cart(context):
    context.app.main_page.cart_icon()


@then('Verify cart is empty')
def verify_empty_cart(context):
    cart_results = context.driver.find_element(By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0').text
    assert 'Your cart is empty' in cart_results, f'Expected text Your cart is empty not in {cart_results}'


@then('Verify "Your cart is empty" message is shown')
def cart_empty_message(context):
    context.app.cart_page.verify_cart_header()
