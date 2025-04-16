import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_success_login_valid_data(driver):
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys("standard_user")
    password_name = driver.find_element(By.ID, 'password')
    password_name.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    inventory_list = driver.find_element(By.CLASS_NAME, 'inventory_list')
    assert inventory_list, "Список товаров не отображается!"

def test_successfull_login_valid_data(driver):
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys("standard_user")
    password_name = driver.find_element(By.ID, 'password')
    password_name.send_keys("secret_sauce1")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    error_message_div = driver.find_element(By.CLASS_NAME, "error-message-container")
    # error_message = error_message_div.find_element(By.TAG_NAME, 'h3')
    assert error_message_div.text == "Epic sadface: Username and password do not match any user in this service"