import time
from typing import List, Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, ):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_tag_by_t(self, by_par: str,  by_name: By = By.ID) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((by_name, by_par)))

    def enter_field(self, id_tag: str, text: str) -> None:
        input_field = self.get_tag_by_t(id_tag)
        input_field.clear()
        input_field.send_keys(text)

    def success_login(self, authorization_data: Dict[str, str], id_tag_button: str, by_name: By = By.ID) -> None:
        for authorization_data_name, authorization_data_val in authorization_data.items():
            self.enter_field(authorization_data_name, authorization_data_val)
        self.get_tag_by_t(id_tag_button, by_name).click()


class InventoryPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self, by_name: By, by_par: str) -> bool:
        try:
            self.get_tag_by_t(by_par, by_name).click()
            time.sleep(2)
            return True
        except:
            return False

    def click_tag(self, by_name, by_par) -> str | None:
        try:
            self.get_tag_by_t(by_par, by_name).click()
            time.sleep(2)
            return self.driver.current_url
        except:
            return None

    def enter_information(self, id_tags: Dict[str, str], id_button: str, by_name: By = By.ID) -> str | None:
        for id_tag_name, id_tag_val in id_tags.items():
            self.enter_field(id_tag_name, id_tag_val)
        try:
            self.get_tag_by_t(id_button, by_name).click()
            return self.driver.current_url
        except:
            return None

    def check_total(self, by_name: By, by_par: str):
        time.sleep(2)
        return self.get_tag_by_t(by_par, by_name)