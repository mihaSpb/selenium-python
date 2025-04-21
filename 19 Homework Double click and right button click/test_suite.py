from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.products = {}  # для хранения данных о проверяемых объектах

    def universal_click(self, locator: str, message: str = "", action: str = "click"):
        element = self.driver.find_element(By.XPATH, locator)
        actions = ActionChains(self.driver)

        if action == "click":
            element.click()
            click_name = "Click"
        elif action == "double_click":
            actions.double_click(element).perform()
            click_name = "Double click"
        elif action == "right_click":
            actions.context_click(element).perform()
            click_name = "Right click"
        else:
            raise ValueError(f"Unknow action {action}. Use 'click' or 'double_click' or 'right_click'")

        print(f"{click_name}: {message}")