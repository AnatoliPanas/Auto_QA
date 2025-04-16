import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ha5_1(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    obj_iframe = driver.find_element(By.ID, 'my-iframe')

    driver.switch_to.frame(obj_iframe)

    obj_text = driver.find_element(By.XPATH,
                                   '//*[contains(normalize-space(text()), "semper posuere integer et senectus justo curabitur.")]')
    assert obj_text.is_displayed()


def test_ha5_2(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 2)
    accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.="Соглашаюсь"]')))
    accept_cookies_button.click()

    obj_iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
    driver.switch_to.frame(obj_iframe)

    source_draggable = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-draggable-handle')))
    target_droppable = driver.find_element(By.ID, 'trash')

    action = ActionChains(driver)
    action.drag_and_drop(source_draggable, target_droppable).perform()

    time.sleep(0.5)
    source_draggable_ul = driver.find_element(By.ID, "gallery")
    source_draggables_li = source_draggable_ul.find_elements(By.TAG_NAME, "li")

    assert len(source_draggables_li) == 3, "Не удалось переместить объект"

    target_droppables = driver.find_element(By.ID, 'trash')
    target_droppables_li = target_droppables.find_elements(By.TAG_NAME, "li")
    assert len(target_droppables_li) == 1, "В корзине нет объектов"


