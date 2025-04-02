import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_button_new_name(driver):
    driver.get("http://uitestingplayground.com/textinput")
    element_new_button_name = driver.find_element(By.ID, "newButtonName")
    element_new_button_name.send_keys("ITCH")
    element_button_set_name = driver.find_element(By.ID, "updatingButton")
    element_button_set_name.click()
    assert element_button_set_name.text == "ITCH", "Текст не изменился"

def test_image_upload(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    time.sleep(10)

    element_div = driver.find_element(By.ID, "image-container")

    elements_img = element_div.find_elements(By.TAG_NAME, "img")

    assert elements_img[2].get_attribute("alt") == "award"
