from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@then('Verify sign in form opened')
def sign_in_form(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'
    sleep(4)