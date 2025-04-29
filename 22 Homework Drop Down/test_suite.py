from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        print(f"Clicked {message}")

    def input_text(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(message)
        element.send_keys(Keys.RETURN)
        print(f"Input {message}")

    def select_dropdown(self, locator: str, value: str):
        select_element = self.driver.find_element(By.XPATH, locator)
        select = Select(select_element)

        select.select_by_visible_text(value)
        print(f"Selected {value}")

    def input_text_to_drop_element(self, locator: str, input_text: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(input_text)
        element.send_keys(Keys.RETURN)