import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from base.base_page import Base


class FilterComponent(Base):

    # Locators
    price_min_input = "//input[@class='new_input_withoutLabel js-range-input-min min']"
    price_max_input = "//input[@class='new_input_withoutLabel js-range-input-max max']"
    stock_switcher = "//span[@class='new_switcher']"


    def __init__(self, driver):
        super().__init__(driver)
    # Getters
    def get_price_min_input(self):
        """Локатор инпута минимальной цены"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.price_min_input))
        )

    def get_price_max_input(self):
        """Локатор инпута максимальной цены"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.price_max_input))
        )

    def get_stock_switcher(self):
        """Локатор переключателя Акция"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.stock_switcher))
        )

    # Actions

    def click_stock_switcher(self):
        print("Клик по свитчеру Акция")
        self.get_stock_switcher().click()


    # Methods

    def set_min_price(self, min_value, ):
        print("Ввод в фильтр минимальной цены")
        self.get_price_min_input().click()
        time.sleep(2)
        self.get_price_min_input().send_keys(Keys.COMMAND + "a")
        time.sleep(2)
        self.get_price_min_input().send_keys(Keys.DELETE)
        self.get_price_min_input().send_keys(f"{min_value}" + Keys.RETURN)
        time.sleep(1)







    def set_max_price(self, max_value):
        print("Ввод в фильтр максимальной цены")
        self.get_price_max_input().click()
        time.sleep(2)
        self.get_price_max_input().send_keys(Keys.COMMAND + "a")
        time.sleep(2)
        self.get_price_max_input().send_keys(Keys.DELETE)
        self.get_price_max_input().send_keys(f"{max_value}" + Keys.RETURN)
        time.sleep(1)

