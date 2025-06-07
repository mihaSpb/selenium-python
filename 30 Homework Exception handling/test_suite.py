import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_to_invisible_button(self, locator: str, message: str = ""):
        try:
            element = self.driver.find_element(By.XPATH, locator)
            element.click()
            print(f"Clicked {message}")
        except NoSuchElementException:
            print(f"No such element {locator}")
            #time.sleep(5)
            self.driver.refresh()
            time.sleep(5)
            element = self.driver.find_element(By.XPATH, locator)
            element.click()
            print(f"Clicked {message} after refresh page")

    def wait_invisible_button(self, locator: str, timeout: int, message: str = ""):
        visible_button = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
        visible_button.click()
        print(f"Clicked {message}")
