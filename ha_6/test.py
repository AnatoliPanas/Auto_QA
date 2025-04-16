import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ha_6.page import LoginPage, InventoryPage


class TestInventory:

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        LoginPage(driver).success_login(id_tag_username="user-name",
                                        id_tag_password="password",
                                        id_tag_button="login-button",
                                        username="standard_user",
                                        password="secret_sauce")
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)

    def test_item_amount(self, inventory_page):
        assert inventory_page.get_items_amount() == 6, 'кол-во товаров не соответствует'

    def test_add_product(self, inventory_page):
        id_products = ["add-to-cart-sauce-labs-backpack",
                       "add-to-cart-sauce-labs-bolt-t-shirt",
                       "add-to-cart-sauce-labs-onesie"]

        for id_product in id_products:
            assert inventory_page.add_product(By.ID, id_product)

    def test_click_shopping_cart(self, inventory_page):
        assert inventory_page.click_tag(By.CLASS_NAME, "shopping_cart_link") == "https://www.saucedemo.com/cart.html"

    def test_click_checkout(self, inventory_page):
        assert inventory_page.click_tag(By.ID, "checkout") == "https://www.saucedemo.com/checkout-step-one.html"

    def test_enter_information(self, inventory_page):
        id_tags = {
            "first-name": "Anatoli",
            "last-name": "Panas",
            "postal-code": "12345"
        }
        assert inventory_page.enter_information(id_tags, "continue") == "https://www.saucedemo.com/checkout-step-two.html"

    def test_check_total(self, inventory_page):
        assert "58.29" in inventory_page.check_total(By.CLASS_NAME, "summary_total_label").text