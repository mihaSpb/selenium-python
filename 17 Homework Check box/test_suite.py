from select import select

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.products = {}  # для хранения данных о товарах

    def universal_click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        if message:
            print(message)

    def is_element_selected(self, locator: str):
        selected = self.driver.find_element(By.XPATH, locator)
        selected.is_selected()

        if selected:
            print("Element is selected")
        else:
            print("Element is not selected")