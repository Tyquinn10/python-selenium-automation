from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle Page')
def target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are {number} benefit boxes')
def verify_benefit_boxes(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='BenefitCard-sc']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'
