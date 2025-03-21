# pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver = webdriver.Chrome()

web_driver.get("https://itcareerhub.de/ru")
about_link = web_driver.find_element(By.LINK_TEXT, 'О нас')
assert about_link
about_link.click()
time.sleep(5)
