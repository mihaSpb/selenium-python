import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        print(f"Clicked {message}")

    def input_text(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(message)
        element.send_keys(Keys.RETURN)
        print(f"Input {message}")

    def check_text_in_element(self, expected_text: str, result_locator: str):
        result_text = self.driver.find_element(By.XPATH, result_locator).text.strip()
        assert result_text == expected_text, f"Expected {expected_text} but got {result_text}"
        print(f"Text matches: {expected_text}")

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

