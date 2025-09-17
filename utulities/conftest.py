import pytest
from selenium import webdriver
from selenium.webdriver import ChromeService
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

    yield driver

    print("\nТест завершен!")
    driver.quit()
