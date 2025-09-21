import time

from selenium import webdriver
from selenium.webdriver import ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from base.base_page import Base
from components.filter import FilterComponent
from components.navigation import NavigationComponent
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.order_page import OrderPage

class TestBuyDoor:
    """Тест покупки двери"""



    def test_buy_door(self, set_up):
        """Тест покупки самой дешевой двери в диапазине 4000-5000 рублей по акции, с увеличением количества товара в корзине """
        driver = set_up
        base = Base(driver)

        print("Старт теста")

        menu = NavigationComponent(base)
        # Открыть Каталог
        menu.open_catalog()

        # Выбрать категорию 2
        menu.select_category_by_position(category_position=2)

        # Выбрать подкатегорию Двери
        menu.select_sub_category_by_route(route='/catalog/dveri/')

        # Выбрать ценовой диапазон 4000 - 5000 и товары по акции
        goods_filter = FilterComponent(base)
        goods_filter.set_min_price(4000)
        goods_filter.set_max_price(5000)
        goods_filter.click_stock_switcher()
        time.sleep(5)



        # Отсортировать по возрастанию цены
        doors_catalog = CatalogPage(base)
        doors_catalog.click_sort_by_price_btn()
        time.sleep(5)

        # Выбрать самый дешевый товар в заданном диапазоне
        goods_index = 1
        goods_catalog_cost_price = doors_catalog.reading_first_price_by_index(goods_index)
        goods_catalog_full_price = doors_catalog.reading_second_price_by_index(goods_index)
        doors_catalog.click_add_to_cart_btn(goods_index)
        print(f"Добавлен товар стоимостью  {goods_catalog_cost_price} со скидкой и полной стоимостью {goods_catalog_full_price}")

        # Перейти в корзину
        menu.click_to_cart_btn()

        cart = CartPage(driver)
        cart.assert_url("https://sam.saturn.net/cart/")

        #Проверка стоимости товара
        goods_cart_price = cart.assert_value_goods_price_by_index(index=1,goods_catalog_cost_price=goods_catalog_cost_price, goods_catalog_full_price=goods_catalog_full_price)

        #Увеличить количество товара до 3 единиц с помошью кнопки +
        for i in range(2):
            cart.click_goods_quantity_plus_btn_by_index(index=1)




        #Проверк итоговой цены в корзине
        goods_cost = cart.reading_value_goods_cost_by_index(index=1)
        assert goods_cost == goods_cart_price * 3, "Стоимость количества товара некорректна"
        cart_total = cart.reading_total_cost()
        assert goods_cost == cart_total, "Итоговая стоимость корзины некорректна"

        #Переход на страницу оформления
        cart.click_go_to_order_page_btn()
        order = OrderPage(driver)
        order.assert_url("https://sam.saturn.net/cart/?order")

        # Заполнение персональных данных

        order.set_random_fullname()
        order.set_random_phone()


        """TODO"""
        # Проверка на соответсвие введенных данных на странице оформления товара с данными на странице подтверждения заказа

        """Не завершаю оформление товара по этическим причинам"""




















