from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('http://www.amazon.com')

# search by CSS, ID:
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# search by CSS, classes:
driver.find_element(By.CSS_SELECTOR, 'input.nav-progressive-attribute.nav-input')
driver.find_element(By.CSS_SELECTOR, 'input,nav-progressive-attribute.nav-input#twotabsearchtextbox')

# search by CSS, attributes:
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][aria-label='Search Amazon']")
# search by CSS, attributes + classes + IDs
driver.find_element(By.CSS_SELECTOR, "input.nav-input[placeholder='Search Amazon'][aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "nav-input.nav-progressive-attribute[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon']")

# search by CSS, attributes, contains with *
driver.find_element(By.CSS_SELECTOR, "[data-csa-c-content-id*='cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "[href*='nav_cs_bestsellers']")

