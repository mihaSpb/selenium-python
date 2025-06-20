import time
import platform

import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def login_user(self, login_name, login_password):
        user_name = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys(login_name)
        print('Input user name')

        user_password = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        user_password.send_keys(login_password)
        print('Input password')

        button_login = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        button_login.click()
        print('Click Login button')

    @staticmethod
    def press_escape_to_dismiss_alert(timeout = 2):
        system = platform.system()
        print(f"Detected OS: {system}")

        time.sleep(timeout)
        print("Simulating ESC key press to close sistem alert")
        pyautogui.press('esc')

    def add_to_cart(self, product_name: str, timeout: int = 5):
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

    def open_cart(self, locator: str):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()
        print("Opened cart")

    def check_shopping_cart(self, timeout: int = 20, check_name_cart: str = None, locator: str = None):
        success_test = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
        value_success_test = success_test.text
        assert value_success_test == check_name_cart
        print(f"Test Success")