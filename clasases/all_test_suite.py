import platform
import re
import time
import datetime
from pathlib import Path
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.products = {}  # для хранения данных о товарах

    def universal_click(self, locator: str, message: str = "", action: str = "click"):
        element = self.driver.find_element(By.XPATH, locator)
        actions = ActionChains(self.driver)

        if action == "click":
            element.click()
            click_name = "Click"
        elif action == "double_click":
            actions.double_click(element).perform()
            click_name = "Double click"
        elif action == "right_click":
            actions.context_click(element).perform()
            click_name = "Right click"
        else:
            raise ValueError(f"Unknow action {action}. Use 'click' or 'double_click' or 'right_click'")

        print(f"{click_name}: {message}")

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

    def check_text_in_element(self, expected_text: str, result_locator: str):
        result_text = self.driver.find_element(By.XPATH, result_locator).text.strip()
        assert result_text == expected_text, f"Expected {expected_text} but got {result_text}"
        print(f"Text matches: {expected_text}")

    def press_key_in_element(self, button_locator: str, key_text: str, expected_text: str):
        mapping = {
            "ENTER": Keys.ENTER,
            "BACKSPACE": Keys.BACKSPACE,
            "DELETE": Keys.DELETE,
            "ESCAPE": Keys.ESCAPE,
        }

        element = self.driver.find_element(By.XPATH, button_locator)

        upper_key = key_text.strip().upper()

        if upper_key == "SELECT_ALL":
            element.click()
            chain = ActionChains(self.driver)
            if platform.system() == "Darwin":
                chain.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND)
            else:
                chain.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
            chain.perform()
            key_name = "SELECT_ALL"

        elif upper_key in mapping:
            if upper_key != "DELETE":
                element.click()
            element.send_keys(mapping[upper_key])
            key_name = upper_key

        else:
            element.click()
            element.send_keys(key_text)
            key_name = key_text

        print(f'Press {key_name} for {expected_text}')

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

    def is_element_selected(self, locator: str):
        selected = self.driver.find_element(By.XPATH, locator)

        assert selected.is_selected(), "Element is not selected"
        print("Element is selected")

    def move_slider(self, locator: str, offset_str: str):
        actions = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, locator)
        offset_px = int(offset_str.rstrip('px'))

        actions.click_and_hold(slider).move_by_offset(offset_px,0).release().perform()
        print(f'Слайдер перемещен на {offset_px}px')

    def check_move_slider(self, slider_locator: str, value_locator: str):
        slider = self.driver.find_element(By.XPATH, slider_locator)
        actual = int(slider.get_attribute('value')) # Фактическое значение слайдера

        # Значение поля Value
        displayed_value = int(self.driver.find_element(By.XPATH, value_locator).text)

        assert displayed_value == actual, (
            f"В поле Value {displayed_value}, а значение слайдера – {actual}"
        )
        print(f'Проверка пройдена: {displayed_value} == {actual}')

    def input_text(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(message)
        element.send_keys(Keys.RETURN)
        print(f"Input {message}")

    def select_dropdown(self, locator: str, value: str):
        select_element = self.driver.find_element(By.XPATH, locator)
        select = Select(select_element)

        select.select_by_visible_text(value)
        print(f"Selected {value}")

    def universal_select_dropdown(self, select_locator: str, by: str, value):
        """
        Универсальный выбор в <select> через Selenium Select.

        Аргументы:
          select_locator — XPath/локатор <select> элемента
          by — способ выбора: 'visible_text', 'value', 'index'
          value — строка текста / значение value / индекс (int)
        """
        select_el = self.driver.find_element(By.XPATH, select_locator)
        sel = Select(select_el)  # класс для <select> :contentReference[oaicite:0]{index=0}

        if by == 'visible_text':
            sel.select_by_visible_text(value)  # по видимому тексту :contentReference[oaicite:1]{index=1}
            method = f"visible text '{value}'"
        elif by == 'value':
            sel.select_by_value(value)  # по атрибуту value :contentReference[oaicite:2]{index=2}
            method = f"value '{value}'"
        elif by == 'index':
            sel.select_by_index(int(value))  # по индексу :contentReference[oaicite:3]{index=3}
            method = f"index {value}"
        else:
            raise ValueError("by должен быть 'visible_text', 'value' или 'index'")

        print(f"Selected option by {method} in {select_locator}")

    def input_text_to_drop_element(self, locator: str, input_text: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(input_text)
        element.send_keys(Keys.RETURN)

    def sum_and_validate(self, first_locator: str,
                         second_locator: str,
                         button_locator: str,
                         result_locator: str,
                         first_value: str,
                         second_value: str,
                         delay: float = 0.5):
        self.input_text(first_locator, first_value)
        time.sleep(delay)

        self.input_text(second_locator, second_value)
        time.sleep(delay)

        self.click(button_locator)
        time.sleep(delay)

        expected_sum = float(first_value) + float(second_value)
        result_element = self.driver.find_element(By.XPATH, result_locator)
        result_sum = float(result_element.text.strip())
        assert expected_sum == result_sum, f"Expected {expected_sum} but got {result_sum}"
        print(f"Text matches: {result_sum} == {expected_sum}")