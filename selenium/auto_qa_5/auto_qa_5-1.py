import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


web_driver = webdriver.Chrome()
web_driver.get("https://suninjuly.github.io/cats.html")

element = None
try:
    element = web_driver.find_element(By.TAG_NAME, "h1")
except NoSuchElementException as err:
    print(f"Ошибка: {err}")

print(element.text)

elements = None
try:
    elements = web_driver.find_elements(By.TAG_NAME, "p")
except NoSuchElementException as err:
    print(f"Ошибка: {err}")

print('=' * 30)
for elem in elements:
    print(elem.text)