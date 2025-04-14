import re
import time
import datetime
from pathlib import Path

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.products = {}  # для хранения данных о товарах

    def universal_click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        if message:
            print(message)

    def input_login(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name_cont = self.driver.find_element(By.XPATH, "//div[@id='login_credentials']")
        user_name_value = user_name_cont.text.splitlines()
        user_name.send_keys(user_name_value[1].strip())

        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name.send_keys(Keys.CONTROL, "a")
        print('Input login')

    def input_password(self):
        user_password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        user_password_cont = self.driver.find_element(By.XPATH, "//div[@class='login_password']")
        user_password_value = user_password_cont.text.splitlines()
        user_password.send_keys(user_password_value[1].strip())
        print('Input password')


    def add_something_product(self, title_locator: str, price_locator: str, add_button_locator: str, product_key: str, target_dict: dict = None):
        title_element = self.driver.find_element(By.XPATH, title_locator)
        product_title = title_element.text
        price_element = self.driver.find_element(By.XPATH, price_locator)
        product_price = price_element.text

        if target_dict is None:
            target_dict = self.products

        target_dict[product_key] = {"title": product_title, "price": product_price}

        print(f'Product {product_key} title = {product_title}')
        print(f'Product {product_key} price = {product_price}')
        self.universal_click(add_button_locator, f'Add product {product_key} to cart')
        return target_dict