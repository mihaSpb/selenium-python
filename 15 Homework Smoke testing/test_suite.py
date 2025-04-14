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

    def check_current_url(self):
        current_url = self.driver.current_url
        expected_url = 'https://www.saucedemo.com/inventory.html'
        assert current_url == expected_url, f'Expected {expected_url}, got {current_url}'
        print(f'Current url = {current_url} is correct')

    def check_text_in_element(self, element_locator: str, expected_text: str):
        title_element = self.driver.find_element(By.XPATH, element_locator)
        actual_text = title_element.text
        assert actual_text == expected_text, f'Expected {expected_text}, got {actual_text}'
        print(f'Text element = {actual_text} is correct')

    def highlight_element(self, input_locator: str, label: str):
        element = self.driver.find_element(By.XPATH, input_locator)
        element.send_keys(Keys.COMMAND + 'a')
        print(f'Highlight {label}')

    def press_key_for_button(self, button_locator: str, key, expected_text: str):
        key_names = {
            Keys.ENTER: "ENTER",
            Keys.BACKSPACE: "BACKSPACE",
            Keys.DELETE: "DELETE",
            Keys.ESCAPE: "ESCAPE",
            Keys.CLEAR: "CLEAR",
        }

        button = self.driver.find_element(By.XPATH, button_locator)
        button.send_keys(key)

        key_names = key_names.get(key, str(key))
        print(f'Press {key_names} for {expected_text}')

    def make_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        screenshot_dir = Path('screens')
        screenshot_dir.mkdir(exist_ok=True)
        name_screenshot = screenshot_dir / f"screenshot_{now_date}.png"
        time.sleep(0.5)
        self.driver.save_screenshot(str(name_screenshot))
        print(f'Screenshot saved at {name_screenshot}')

    def add_all_items_to_cart(self):
        items = {
            "sauce-labs-backpack": "Add backpack",
            "sauce-labs-bike-light": "Add bike",
            "sauce-labs-bolt-t-shirt": "Add T-shirt",
            "sauce-labs-fleece-jacket": "Add jacket",
            "sauce-labs-onesie": "Add onesie",
            "test.allthethings()-t-shirt-(red)": "Add T-shirt red"
        }
        for product_id, message in items.items():
            locator = f"//button[@id='add-to-cart-{product_id}']"
            self.universal_click(locator, message)

    def find_element_and_move(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.ID, 'item_3_title_link')
        actions.move_to_element(element).perform()
        print('Moved to element')

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

    def data_for_order_form(self):
        fake = Faker()
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_zip_code = fake.zipcode()

        order_first_name = self.driver.find_element(By.XPATH, "//*[@id='first-name']")
        order_first_name.send_keys(fake_first_name)
        print(f'First name = {fake_first_name}')

        order_last_name = self.driver.find_element(By.XPATH, "//*[@id='last-name']")
        order_last_name.send_keys(fake_last_name)
        print(f'Last name = {fake_last_name}')

        order_zip_code = self.driver.find_element(By.XPATH, "//*[@id='postal-code']")
        order_zip_code.send_keys(fake_zip_code)
        print(f'Zip code = {fake_zip_code}')

    def check_product(self, order_title_locator: str, order_price_locator: str, product_key: str):
        expected_title = self.products[product_key]["title"]
        expected_price = self.products[product_key]["price"]

        self.check_text_in_element(order_title_locator, expected_title)
        self.check_text_in_element(order_price_locator, expected_price)

    def parse_price_items(self, price_str: str) -> float:
        # Замена запятой на точку
        price_str = price_str.replace(',', '.')
        # Удаление всех символов, кроме запятой и точки
        price_cleaned = re.sub(r'[^\d.]', '', price_str)
        return float(price_cleaned)

    def check_order_sum(self, products_dist: dict):
        order_sum_element = self.driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
        order_sum_text = order_sum_element.text
        order_sum = self.parse_price_items(order_sum_text)
        print(f'Order sum = {order_sum}')

        total = 0.0
        for product_key, product_data in products_dist.items():
            total += self.parse_price_items(product_data["price"])
        print(f'Check sum = {total}')
        assert order_sum == total, f"Order sum {order_sum} does not match calculated sum {total}"
        print(f'Order sum = {order_sum} OK')