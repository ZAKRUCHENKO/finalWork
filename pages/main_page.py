from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base


class MainPage(Base):
    """Класс включающий действия на главной странице"""

# Locators
    catalog_btn = "//div[@class='top_catalog_btn']"
    cart_icon = "//a[@data-modal='basket_popup']"
    category_icon = "//div[@class='h_c_aside_icon_container']"

    def __init__(self, driver):
        super().__init__(driver)





# Getters


    def get_catalog_btn(self):
        """Локатор кнопки Каталог"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.catalog_btn))
        )

    def get_category_icon_by_position(self, category_position):
        """Локатор иконки категории товаров бокового меню по позиции"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"({self.category_icon})[{category_position}]"))
        )

    def get_sub_category_by_route(self, route):
        """Локатор раздела в подменю по ссылке на раздел"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"//a[@href='{route}']")))

    def get_cart_icon(self):
        """Локатор иконки корзины"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.cart_icon))
        )

# Actions

    def open_catalog(self):
        """Открыть боковое меню с каталогом"""
        self.get_catalog_btn().click()
        print("Клик по кнопке Каталог")
    def select_category_by_position(self, category_position):
        """Открыть категорию товаров по порядку"""
        self.get_category_icon_by_position(category_position).click()
        print("Клик по категории")

    def select_sub_category_by_route(self, route):
        """Открыть раздел в подменю по ссылке на раздел"""
        self.get_sub_category_by_route(route).click()
        print("Клик по подкатегории")

    def select_sub_category_by_route(self, route):
        """Открыть корзину"""
        self.get_sub_category_by_route(route).click()
        print("Клик по подкатегории")


# Methods


