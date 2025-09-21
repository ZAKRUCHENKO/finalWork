from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import Base


class CatalogPage(Base):
    """Класс включающий действия на странице раздела Окна и Двери"""

    # Locators
    sort_by_price_btn = "//div[@data-name='price']"
    goods_price = "//span[@class='js-price-value']"
    add_to_cart_btn = "//a[@class='goods_card_cart_link ']"



    def __init__(self, driver):
        super().__init__(driver)

    # Getters
    def get_sort_by_price_btn(self):
        """Локатор кнопки Сортировать по цене"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.sort_by_price_btn))
        )
    def get_goods_first_price_by_index(self, goods_index):
        """Локатор первой цены товара"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, f"({self.goods_price})[{goods_index}]"))
        )

    def get_add_to_cart_btn_by_index(self, goods_index):
        """"Локатор кнопки Добавить в корзину по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH,f"({self.add_to_cart_btn})[{goods_index}]"))
        )


    # Actions
    def click_sort_by_price_btn(self):
        print("Клик по кнопке Сортировать по цене")
        self.get_sort_by_price_btn().click()

    def click_add_to_cart_btn(self, goods_index):
        print("Клик по кнопе Добавить в корзину")
        self.get_add_to_cart_btn_by_index(goods_index).click()

    # Methods

    def reading_first_price_by_index(self, goods_index):
        price_text = self.get_goods_first_price_by_index(goods_index * 2 - 1).text
        cleaned_price = price_text.replace(" ", '')
        normal_price = cleaned_price.replace(",", ".")
        goods_catalog_price = float(normal_price)

        print(f"Стоимость товара со скидкой {goods_catalog_price}")
        return goods_catalog_price

    def reading_second_price_by_index(self, goods_index):
        price_text = self.get_goods_first_price_by_index(goods_index * 2).text
        cleaned_price = price_text.replace(" ", '')
        normal_price = cleaned_price.replace(",", ".")
        goods_catalog_price = float(normal_price)

        print(f"Полная стоимость товара {goods_catalog_price}")
        return goods_catalog_price