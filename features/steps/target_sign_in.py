from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click sign in')
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('Click sign in from navigation menu')
def navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify sign in form opened')
def sign_in_form(context):
    sign_in_results = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert 'Sign into your Target account' in sign_in_results, f'Expected text Sign into your Target account not in {sign_in_results}'
    sleep(4)