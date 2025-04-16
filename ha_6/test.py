import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ha_6.page import LoginPage, InventoryPage


class TestInventory:

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        authorization_data = {
            "user-name": "standard_user",
            "password": "secret_sauce"
        }

        LoginPage(driver).login(credentials=authorization_data, button_id="login-button")
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)

    def test_add_product(self, inventory_page):
        product_ids = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for product_id in product_ids:
            assert inventory_page.add_product(locator_value=product_id, by=By.ID)

    def test_click_shopping_cart(self, inventory_page):
        result_url = inventory_page.open_page_via_element(locator_value="shopping_cart_link", by=By.CLASS_NAME)
        assert result_url == "https://www.saucedemo.com/cart.html"

    def test_click_checkout(self, inventory_page):
        result_url = inventory_page.open_page_via_element(locator_value="checkout", by=By.ID)
        assert result_url == "https://www.saucedemo.com/checkout-step-one.html"

    def test_enter_information(self, inventory_page):
        info = {
            "first-name": "Anatoli",
            "last-name": "Panas",
            "postal-code": "12345"
        }
        result_url = inventory_page.submit_product_form(fields=info, button_id="continue")
        assert result_url == "https://www.saucedemo.com/checkout-step-two.html"

    def test_check_total(self, inventory_page):
        total_text = inventory_page.check_total(locator_value="summary_total_label", by=By.CLASS_NAME).text
        assert "58.29" in total_text
