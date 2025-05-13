from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        print(f"Clicked {message}")

    def switch_to_tab_or_window(self, switch_to: int, message: str = ""):
        self.driver.switch_to.window(self.driver.window_handles[switch_to])
        print(f"Switch to {message}")