from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base


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
    def get_goods_quantity_value(self, index):
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
            (By.XPATH, f"({self.goods_price})[{index}]"))
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


# Methods