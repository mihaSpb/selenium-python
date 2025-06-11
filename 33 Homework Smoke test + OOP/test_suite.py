import time
import platform

import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_button(self, locator: str, message: str = ""):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()
        if message:
            print(message)

    def input_login(self):
        wait = WebDriverWait(self.driver, 20)
        user_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        # Считываем имя пользователя из блока имён
        user_name_cont = self.driver.find_element(By.XPATH, "//div[@id='login_credentials']")
        user_name_value = user_name_cont.text.splitlines()
        user_name.send_keys(user_name_value[1].strip())

        user_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(Keys.CONTROL, "a")
        print('Input login')

    def input_password(self):
        wait = WebDriverWait(self.driver, 20)
        user_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))

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

    def check_shopping_cart(self, timeout: int = 20, check_name_cart: str = None, locator: str = None):
        success_test = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
        value_success_test = success_test.text
        assert value_success_test == check_name_cart
        print(f"Test Success")