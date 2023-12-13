from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then
from time import sleep


ADD_TO_CART = (By.CSS_SELECTOR, "[id*='85978614'][class*='styles__StyledBaseButtonInternal']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyleHeading']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan']")


@when('Click add to cart button')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()



@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not shown in side navigation'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@then('Verify search worked for {search_result}')
def verify_search(context, search_result):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert search_result in search_results_header, f'Expected text {search_result} not in {search_results_header}'


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    assert expected_keyword in context.driver.current_url, \
        f'Expected {expected_keyword} not in {context.driver.current_url}'
