# pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver = webdriver.Chrome()

# web_driver.set_window_size(700, 400)
# web_driver.fullscreen_window()
web_driver.get("https://itcareerhub.de/ru")
about_link = web_driver.find_element(By.LINK_TEXT, 'О нас')
about_link.click()

# web_driver.save_screenshot("./scr/aaa.png")
# web_driver.refresh()
# web_driver.get("https://www.berlin.de")
# web_driver.back()
time.sleep(5)
web_driver.quit()