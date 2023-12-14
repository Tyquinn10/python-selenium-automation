from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")
SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")


@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)


@when('Click sign in')
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('Click sign in from navigation menu')
def navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify header is present')
def verify_header(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")


@then('Verify header has {number} links')
def verify_header_links(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='GlobalHeader/UtilityHeader']")
    print(links)
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'
