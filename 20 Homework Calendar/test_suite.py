import platform
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.products = {}  # для хранения данных о проверяемых объектах

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