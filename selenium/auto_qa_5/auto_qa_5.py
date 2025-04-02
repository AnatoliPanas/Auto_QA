import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver = webdriver.Chrome()

web_driver.get("https://suninjuly.github.io/cats.html")
element = web_driver.find_element(By.XPATH, "//*[contains(@id,'bulle')]")
element1 = web_driver.find_element(By.XPATH, "//*[@id='bullet']")
element2 = web_driver.find_element(By.ID, "bullet")
print(element == element1)
print(element1 == element2)

el_but = element.parent.find_element(By.XPATH, '//button[text()="View"]')
el_but.click()
time.sleep(3)

element_bt = web_driver.find_elements(By.XPATH, '//button[text()="View"]')
print(element_bt)
time.sleep(3)
assert element_bt


