import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import Base


class CartPage(Base):
    """Класс, включающий действия на странице Корзина"""

    # Locators
    title = "//h1[@class='shopping_cart_title']"
    goods_name = "//a[@class='title']"
    goods_price = "//div[@class='shopping_cart_goods_list_item_price_block_item_pr']"
    goods_quantity_minus = "//a[@class='basket__form__table__coll__input__btn form__group__btn minus']"
    goods_quantity_value = "//input[@class='basket__form__table__coll__input form__group__input']"
    goods_quantity_plus = "//a[@class='basket__form__table__coll__input__btn form__group__btn plus']"
    goods_cost = "//div[@class='shopping_cart_goods_list_item_sum_item']"
    delete_btn = "//div[@class='shopping_cart_goods_list_item_delete']"
    clear_cart_btn = "//div[@class='shopping_cart_action_item shopping_cart_action_clear']"
    total_cost = "(//div[@class='catalog__goods__blockwithdots__value'])[4]"
    goods_card_in_cart_add_btn = "//a[@class='goods_card_cart_link ']"
    goods_card_in_cart_price_value = "//div[@class='goods_card_price_discount_value']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters

    def get_title(self):
        """Локатор заголовка"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, self.title))
        )

    def get_goods_name_by_index(self, index):
        """Локатор имени товара по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, f"({self.goods_name})[{index}]"))
        )

    def get_goods_price_by_index(self, index):
        """Локатор цены единицы товара по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, f"({self.goods_price})[{index}]"))
        )

    def get_goods_quantity_minus(self, index):
        """Локатор кнопки - на счетчике товара по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"({self.goods_quantity_minus})[{index}]"))
        )

    def get_goods_quantity_value_by_index(self, index):
        """Локатор значения на счетчике товара по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, f"({self.goods_quantity_value})[{index}]"))
        )

    def get_goods_quantity_plus(self, index):
        """Локатор кнопки + на счетчике товара по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"({self.goods_quantity_plus})[{index}]"))
        )

    def get_goods_cost_by_index(self, index):
        """Локатор общей стоимости за количество товара по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, f"({self.goods_cost})[{index}]"))
        )

    def get_delete_btn_by_index(self, index):
        """Локатор кнопки удалить товар по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"({self.delete_btn})[{index}]"))
        )

    def get_clear_cart_btn(self):
        """Локатор кнопки очистить корзину"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.delete_btn))
        )

    def get_total_cost(self):
        """Локатор финальной стоимости корзины"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, self.total_cost))
        )

    def get_goods_card_in_cart_add_btn_by_index(self, index):
        """Локатор кнопки Добавить в корзину на карточках сопутсвующих товаров по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"({self.goods_card_in_cart_add_btn})[{index}]"))
        )

    def get_goods_card_in_cart_price_value_by_index(self, index):
        """Локатор цены на карточках сопутсвующих товаров по индексу"""
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, f"({self.goods_card_in_cart_price_value})[{index}]"))
        )

    # Actions



    def click_goods_quantity_minus_btn_by_index(self, index):
        print("Клик на кнопку  - в счетчике товара по индексу")
        self.get_goods_quantity_minus(index).click()
        time.sleep(2)


    def click_goods_quantity_plus_btn_by_index(self, index):
        print("Клик на кнопку  + в счетчике товара по индексу")
        self.get_goods_quantity_plus(index).click()
        time.sleep(2)
    def click_delete_btn_by_index(self, index):
        print("Удаление товара из корзины")
        self.get_delete_btn_by_index(index).click()

    def click_clear_cart_btn(self):
        print("Очистка корзины от всех товаров")
        self.get_clear_cart_btn().click()

    def click_add_recommendet_goods_to_cart_by_index(self, index):
        self.get_goods_card_in_cart_add_btn_by_index().click()
        print("Добавить в корзину рекомендуемый товар")




# Methods

    def reading_text_title(self):
        print("Получить текст заголовка экрана")
        return self.get_title().text

    def reading_text_goods_name_by_index(self, index):
        print("Получить текст имени товара")
        return self.get_goods_name_by_index(index).text

    def assert_value_goods_price_by_index(self, index, goods_catalog_cost_price, goods_catalog_full_price):

        price_text = self.get_goods_price_by_index(index).text
        cleaned_price = re.sub(r'[^\d.]', '', price_text)
        normal_price = cleaned_price.replace(",", ".")
        goods_cart_price = float(normal_price)
        if goods_cart_price == goods_catalog_cost_price:
            print("Товар в корзине с учетом скидки")
        elif goods_cart_price == goods_catalog_full_price:
            print("Товар добавлен в корзину без учета скидки")
        else:
            print(f"Стоимость единицы товара {goods_cart_price}")
        assert goods_cart_price == goods_catalog_cost_price or goods_cart_price == goods_catalog_full_price, "Цена в корзине установлена некорректно"
        return goods_cart_price


    def replace_goods_quantity_value_input(self, index, value):
        quantity_input = self.get_goods_quantity_value_by_index(index)
        quantity_input.click()
        quantity_input.clear()
        quantity_input.send_keys(str(value))
        print(f"В инпут количества товара введено {value} ")

    def reading_value_goods_cost_by_index(self, index):
        cost_text = self.get_goods_cost_by_index(index).text
        cleaned_cost = re.sub(r'[^\d.]', '', cost_text)
        normal_cost = cleaned_cost.replace(",", ".")
        goods_cost = float(normal_cost)

        print(f"Общая стоимость за количество товара {goods_cost}")
        return goods_cost

    def reading_value_goods_quantity_by_index(self, index):
        print("Получить количество товара в строке")
        return int(self.get_goods_quantity_value_by_index(index).text)

    def reading_price_of_recomendet_goods_by_index(self, index):
        price_text = self.get_goods_cost_by_index(index).text
        cleaned_price = price_text.replace(" ", '')
        normal_price = cleaned_price.replace(",", ".")
        goods_price = float(normal_price)

        print(f"Стоимость рекомендованного товара {goods_price}")
        return goods_price



    def reading_total_cost(self):
        cost_text = self.get_total_cost().text
        cleaned_cost = cost_text.replace(" ", '')
        normal_cost = cleaned_cost.replace(",", ".")
        total_cost = float(normal_cost)

        print(f"Финальная стоимость корзины {total_cost}")
        return total_cost

