import platform
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def switch_to_iframe (self, iframe_locator: str):
        iframe = self.driver.find_element(By.XPATH, iframe_locator)
        self.driver.switch_to.frame(iframe)
        print("Switching to iFrame")

    def click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        print(f"Clicked {message}")

    def input_text(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(message)
        print(f"Input {message}")

    def select_all_text(self, locator: str):
        element = self.driver.find_element(By.XPATH, locator)
        chain = ActionChains(self.driver)

        if platform.system() == "Darwin":
            chain.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND)
        else:
            chain.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        chain.perform()

    def check_text_in_element(self, expected_text: str, result_locator: str):
        result_text = self.driver.find_element(By.XPATH, result_locator).text.strip()

        assert result_text == expected_text, f"Expected {expected_text} but got {result_text}"
        print(f"Text matches: {expected_text}")