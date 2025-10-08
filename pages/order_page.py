from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

from base.base_page import Base


class OrderPage(Base):
    # Locators
    pickup_btn = "//label[@for='delivery_off']"
    full_name_input = "//input[@id='shopping_cart_details_fio_client']"
    phone_input_label = "//label[@for='shopping_cart_details_phone_client']"
    phone_input = "//input[@id='shopping_cart_details_phone_client']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker('ru_RU')

        # Getters

    def get_pickup_btn(self):
        """Локатор таба Самовывоз"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.pickup_btn))
        )

    def get_full_name_input(self):
        """Локатор инпута ФИО"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.full_name_input))
        )

    def get_phone_input_label(self):
        """Локатор поля инпута Телефон"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.phone_input_label))
        )

    def get_phone_input(self):
        """Локатор инпута Телефон"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.phone_input))
        )

    # Actions

    def click_pickup_btn(self):
        self.get_pickup_btn().click()
        print("Клик по табу Самовывоз")

    # Methods

    def set_random_fullname(self):
        """"Заполнит инпут ФИО клиента"""
        #name = self.fake.name()
        f_name = self.fake.first_name()
        s_name = self.fake.last_name()
        self.get_full_name_input().click()
        self.get_full_name_input().send_keys(f"{f_name} {s_name}")
        print(f"Случайный клиент -  {f_name} {s_name}")

    def set_random_phone(self):
        """"Заполнит инпут Телефон клиента"""
        phone = self.fake.phone_number()
        print(f"Случайный номер телефона - {phone}")
        self.get_phone_input_label().click()
        self.get_phone_input().send_keys(phone[2:])
