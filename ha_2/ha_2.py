import time

from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver = webdriver.Chrome()

web_driver.get("https://itcareerhub.de/ru")
web_driver.fullscreen_window()
time.sleep(1)
accept_cookies_button = web_driver.find_element(By.XPATH, '//button[text()="Подтвердить"]')
accept_cookies_button.click()
payment_link = web_driver.find_element(By.LINK_TEXT, 'Способы оплаты')
payment_link.click()
time.sleep(1)
web_driver.save_screenshot('screenshot_payment.png')

time.sleep(2)
web_driver.quit()