from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(6) # wait for ads to disappear


@then('Verify cart is empty')
def verify_empty_cart(context):
    cart_results = context.driver.find_element(By.CSS_SELECTOR, 'h1.styles__StyledHeading-sc-1xmf98v-0').text
    assert 'Your cart is empty' in cart_results, f'Expected text Your cart is empty not in {cart_results}'