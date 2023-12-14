from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PANTS_COLORS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(10)


@then('Verify user can click through pants colors')
def verify_colors(context):
    expected_colors = ['Black', 'Green', 'Oatmeal', 'Red']
    actual_colors = []

    colors = context.driver.find_elements(*PANTS_COLORS)
    for color in colors:
        color.click()
        select_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        actual_colors.append(select_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
