from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.products = {}  # для хранения данных о проверяемых объектах

    def universal_click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        if message:
            print(message)

    def is_element_selected(self, locator: str):
        selected = self.driver.find_element(By.XPATH, locator)

        assert selected.is_selected(), "Element is not selected"
        print("Element is selected")