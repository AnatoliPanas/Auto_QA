import math
import os.path
import time

from selenium.webdriver.common.alert import Alert
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

def test_fill_form_and_check_alert(driver):
    driver.get("http://suninjuly.github.io/huge_form.html")
    input_fields = driver.find_elements(By.TAG_NAME, 'input')

    for input_field in input_fields:
        input_field.clear()
        input_field.send_keys("Hello")

    submit_btn = driver.find_element(By.CLASS_NAME, "btn-default")
    submit_btn.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    alert_text = Alert(driver).text

    expected_substring = "Congrats, you've passed the task!"

    assert expected_substring in alert_text, "Строка не найдена!"

def test_fill_math_and_check_alert(driver):

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    driver.get("https://suninjuly.github.io/math.html")
    x_value = driver.find_element(By.ID, 'input_value')
    result = calc(x_value.text)

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(result)

    robotCheckbox = driver.find_element(By.ID, 'robotCheckbox')
    robotCheckbox.click()

    robotsRule = driver.find_element(By.ID, 'robotsRule')
    robotsRule.click()

    submit_btn = driver.find_element(By.CLASS_NAME, "btn-default")
    submit_btn.click()

    wait = WebDriverWait(driver, 10)
    alert  = wait.until(EC.alert_is_present())

    alert_text = Alert(driver).text

    expected_substring = "Congrats, you've passed the task!"

    assert expected_substring in alert_text, "Строка не найдена!"
    alert.accept()

def test_fill_upload(driver):
    driver.get("http://suninjuly.github.io/file_input.html")

    driver.find_element(By.NAME, "firstname").send_keys("John")
    driver.find_element(By.NAME, "lastname").send_keys("Doe")
    driver.find_element(By.NAME, "email").send_keys("test@example.com")

    file_path = os.path.abspath('test_file.txt')
    with open(file_path, 'w') as f:
        f.write('привет я новый файл')

    file_input = driver.find_element(By.ID, 'file')
    file_input.send_keys(file_path)

    submit_btn = driver.find_element(By.CLASS_NAME, 'btn-primary')
    submit_btn.click()

    wait = WebDriverWait(driver, 10)

    alert = wait.until(EC.alert_is_present())

    alert_text = Alert(driver).text
    expected_substring = "Congrats, you've passed the task!"
    assert expected_substring in alert_text, 'стока не найдена'
    alert.accept()
    os.remove(file_path)
    time.sleep(3)
