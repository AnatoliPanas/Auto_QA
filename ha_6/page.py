import time
from typing import List, Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_element(self, locator_value: str, by: By = By.ID) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((by, locator_value)))

    def click_element(self, locator_value: str, by: By = By.ID) -> bool:
        try:
            self.get_element(locator_value, by).click()
            time.sleep(2)
            return True
        except:
            return False

    def enter_text(self, locator_value: str, text: str, by: By = By.ID) -> None:
        input_field = self.get_element(locator_value, by)
        input_field.clear()
        input_field.send_keys(text)

    def fill_form(self, fields: Dict[str, str], by: By = By.ID) -> None:
        for locator, value in fields.items():
            self.enter_text(locator, value, by)

    def click_and_get_url(self, locator_value: str, by: By = By.ID) -> str | None:
        try:
            self.get_element(locator_value, by).click()
            time.sleep(2)
            return self.driver.current_url
        except:
            return None


class LoginPage(BasePage):
    def login(self, credentials: Dict[str, str], button_id: str, by: By = By.ID) -> None:
        self.fill_form(credentials, by)
        self.click_element(button_id, by)


class InventoryPage(BasePage):
    def add_product(self, locator_value: str, by: By = By.ID) -> bool:
        return self.click_element(locator_value, by)

    def open_page_via_element(self, locator_value: str, by: By = By.ID) -> str | None:
        return self.click_and_get_url(locator_value, by)

    def submit_product_form(self, fields: Dict[str, str], button_id: str, by: By = By.ID) -> str | None:
        self.fill_form(fields, by)
        return self.click_and_get_url(button_id, by)

    def check_total(self, locator_value: str, by: By = By.ID) -> WebElement:
        time.sleep(2)
        return self.get_element(locator_value, by)