import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_browser(driver):
    driver.get("https://www.example.com")
    heading = driver.find_element(By.TAG_NAME, 'h1').text
    time.sleep(3)
    assert heading == "Example Domain", "тест не прошел"

def test_open_google(driver):
    driver.get("https://www.google.com")
    time.sleep(3)
    heading = driver.find_element(By.XPATH, "//*[contains(text(),'Google')]")
    print(heading.tag_name)
    assert heading

def test_open_google1(driver):
    driver.get("https://www.google.com")
    time.sleep(3)
    heading1 = driver.find_element(By.TAG_NAME, 'body')
    assert 'Google' in heading1.text
