import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ajax_request(driver):
    driver.get("http://www.uitestingplayground.com/ajax")
    wait = WebDriverWait(driver, 90)
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()

    ajax_text = wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "bg-success"), "Data loaded with AJAX get request."
        )
    )
    assert ajax_text, "Искомый текст не отобразился"


def test_ajax_request_implict(driver):
    driver.get("http://www.uitestingplayground.com/ajax")
    driver.implicitly_wait(20)
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()

    ajax_text = driver.find_element(By.CLASS_NAME, "bg-success")
    assert "Data loaded with AJAX get request." in ajax_text.text, "Искомый текст не отобразился"


def test_ajax_request_with_sleep(driver):
    driver.get("http://www.uitestingplayground.com/ajax")
    ajax_button = driver.find_element(By.ID, 'ajaxButton')
    ajax_button.click()
    time.sleep(20)
    ajax_text = driver.find_element(By.CLASS_NAME, "bg-success")
    assert "Data loaded with AJAX get request." in ajax_text.text, "Искомый текст не отобразился"


def test_wait_for_button(driver):
    driver.get("http://www.uitestingplayground.com/loaddelay")
    wait = WebDriverWait(driver, 10)
    # element = wait.until(
    #     EC.text_to_be_present_in_element(
    #         (By.CLASS_NAME, "btn-primary"), "Button Appearing After Delay"
    #     )
    # )

    element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//button[text()="Button Appearing After Delay"]')
        )
    )
    assert element, "Элемент не найден"


def test_authoriz(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 5)

    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))

    # username_field =  driver.find_element(By.NAME, "username")
    # password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("Admin")
    password_field.send_keys("admin123")

    button_field = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button_field.click()

    assert "dashboard" in driver.current_url.lower(), "Авторизация не прошла."
