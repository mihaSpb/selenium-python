import re
import time
import platform
import pyautogui

from faker import Faker
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_button(self, locator: str, message: str = ""):
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

    @staticmethod
    def press_escape_to_dismiss_alert(timeout = 3):
        system = platform.system()
        print(f"Detected OS: {system}")

        time.sleep(timeout)
        print("Simulating ESC key press to close sistem alert")
        pyautogui.press('esc')

    def user_menu(self):
        products = {
            "1": "Sauce Labs Backpack",
            "2": "Sauce Labs Bike Light",
            "3": "Sauce Labs Bolt T-Shirt",
            "4": "Sauce Labs Fleece Jacket",
            "5": "Sauce Labs Onesie",
            "6": "Test.allTheThings() T-Shirt (Red)"
        }

        print("\nПриветствую тебя в нашем интернет-магазине\n"
              "Выбери один из следующих товаров и укажи его номер:")

        for num, name in products.items():
            print(f" {num} - {name},")
        while True:
            choice = input("Введите номер товара (1–6): ").strip()
            if choice in products:
                print(f"Вы выбрали: {products[choice]}")
                return products[choice]
            print("Неверный ввод, попробуйте ещё раз.")

    def add_to_cart(self, product_name: str, timeout: int = 5):
        # Ждём загрузки страницы и находим кнопку добавления товара в корзину
        xpath_button = (
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']"
            "//button[contains(text(), 'Add to cart')]"
        )

        add_to_cart = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath_button))
        )
        add_to_cart.click()
        print(f"Added to cart: {product_name}")

        self.driver.find_element(
            By.XPATH, f"//div[text()='{product_name}']"
        ).click()

    def get_product_details(self):
        name = self.driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        price = self.driver.find_element(By.CLASS_NAME, "inventory_details_price").text

        print(f"Detail page: {name} — {price}")
        return name, price

    def verify_in_cart(self, expected_name, expected_price):
        name = self.driver.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        price = self.driver.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        assert name == expected_name, f"Name mismatch: {name} != {expected_name}"
        assert price == expected_price, f"Price mismatch: {price} != {expected_price}"
        print("Verified item in cart")

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

    def parse_price(self, price_str: str) -> float:
        # убираем всё, кроме цифр и точки
        cleaned = re.sub(r'[^\d.]', '', price_str)
        return float(cleaned)

    def check_order_sum(self, expected_prices: float, timeout: int = 10):
        # Ждём, пока строка с суммой появится
        locator = (By.CLASS_NAME, "summary_subtotal_label")
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        item_total = self.parse_price(element.text)
        assert abs(item_total - expected_prices) < 1e-2, (
            f"Order sum mismatch: actual {item_total} vs expected {expected_prices}"
        )
        print(f"Item total OK: {item_total}")


    def check_tax_and_total(self, timeout: int = 10):
        wait = WebDriverWait(self.driver, timeout)
        sub_el = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_subtotal_label")))
        tax_el = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_tax_label")))
        tot_el = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))

        # Парсим общую сумму заказа и Tax
        item_total = self.parse_price(sub_el.text)
        tax = self.parse_price(tax_el.text)
        total_page = self.parse_price(tot_el.text)

        # Проверяем сумму
        expected_total = item_total + tax
        assert abs(total_page - expected_total) < 1e-2, (
            f"Total mismatch: item_total({item_total}) + tax({tax}) = {expected_total}, "
            f"but page shows {total_page}"
        )
        print(f"Tax and total OK: {item_total} + {tax} = {total_page}")

    def verify_order_complete(self, timeout = 10):
        try:
            el = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
            )
        except TimeoutException:
            raise AssertionError(
                f"Order confirmation message did not appear within {timeout} seconds"
            )

        msg = el.text.strip()
        expected = "Thank you for your order!"
        assert msg == expected, (
            f"Expected confirmation '{expected}', but got '{msg}'"
        )
        print(f"Order completed: '{msg}'")