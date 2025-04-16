from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver  = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def get_username_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    def get_password_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "password")))

    def get_login_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    def enter_username(self, username):
        username_field = self.get_username_input()
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.get_password_input()
        password_field.clear()
        password_field.send_keys(password)

    def click_on_login_button(self):
        self.get_login_button().click()

    def get_error_msg(self):
        return self.driver.find_element(By.CLASS_NAME, "error-message-container")

    def success_login(self):
        self.enter_username("standard_user")
        self.enter_password("secret_sauce")
        self.click_on_login_button()