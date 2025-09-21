import time

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_up():
    """Открытие браузера переход на главную страницу магазина"""
    print("\nОткрытие браузера переход на главную страницу магазина")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")

    driver = webdriver.Chrome(
        options=options,
        service=ChromeService(ChromeDriverManager().install())
    )
    url = 'https://sam.saturn.net/'
    driver.get(url)

    # Ждем появления модального окна
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='application_popup system_popup system_popup_new']")
        )
    )

    if modal:
        try:
            print("Модальное окно обнаружено")
            close_button = modal.find_element(By.XPATH, ".//div[@class='system_popup_hide system_popup_hide_new js-close-modal-application']")
            close_button.click()
            print("Модальное окно закрыто")
        except Exception as e:
            print(f"Не удалось закрыть модальное окно: {e}")
    else:
        print("Модальное окно не обнаружено")

    yield driver
    time.sleep(5)
    print("\nТест завершен!")
    driver.quit()

