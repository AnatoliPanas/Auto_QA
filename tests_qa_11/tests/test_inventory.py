import pytest
from selenium import webdriver
from tests_qa_11.pages.inventory_page import InventoryPage
from tests_qa_11.pages.login_page import LoginPage

class TestInventory:

    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        LoginPage(driver).success_login()
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)

    def test_item_amount(self, inventory_page):
        assert inventory_page.get_items_amount() == 6, 'кол-во товаров не соответствует'

    def test_all_items_are_displayed(self, inventory_page):
        assert inventory_page.all_items_are_displayed(), 'не все товары отобразились'

    def test_all_items_names_are_displayed(self, inventory_page):
        assert inventory_page.all_items_names_are_displayed(), "Не все названия товаров отображаются."

    def test_all_item_names_are_not_empty(self, inventory_page):
        assert inventory_page.all_item_names_are_not_empty(), "Есть товары с пустыми названиями."

    def test_all_item_names_contains_sauce_labs(self, inventory_page):
        assert inventory_page.all_item_names_contains_sauce_labs(), "Не все товары начинаются с 'Sauce Labs'."