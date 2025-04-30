import pytest
from selenium import webdriver
from tests_qa_11.pages.inventory_page import InventoryPage
from tests_qa_11.pages.login_page import LoginPage
from tests_qa_11.pages.cart_page import CartPage
import time

class TestCart:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        # LoginPage(driver).success_login()
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)

    @pytest.fixture(scope="class")
    def login_page(self, driver):
        return LoginPage(driver)

    @pytest.fixture(scope="class")
    def cart_page(self, driver):
        return CartPage(driver)

    def test_backpack_cost(self, login_page, inventory_page, cart_page):
        login_page.success_login()
        # login_page.alert_clic()
        price = inventory_page.get_item_price("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()
        cart_price = cart_page.get_cart_item_price("Sauce Labs Backpack")
        assert price == cart_price, 'цена в каталоге и в корзине отображаютс по разному'
