import time
from selenium.webdriver.common.by import By

def test_1(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    element = driver.find_element(By.TAG_NAME, "h1")
    assert element.text == "Cat memes", "тест не прошел"

def test_2(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    elements = driver.find_elements(By.XPATH, "//*[@class='text-muted']")
    print(elements[1].text)
    assert elements[1].text == "9 mins", "тест не прошел"

def test_3(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    element = driver.find_element(By.XPATH, "//*[text()='I love you so much']")
    assert element, "тест не прошел"


def test_4(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    element = driver.find_element(By.CLASS_NAME, "navbar-brand")

    assert element is not None, "Элемент не найден"

    child_elements = element.find_elements(By.XPATH, ".//*")

    element_svg = any(el.tag_name.lower() == 'svg' for el in child_elements)
    element_strong = any(el.tag_name.lower() == 'strong' and el.text == 'Cats album' for el in child_elements)
    assert element_svg and element_strong, "тест не прошел"