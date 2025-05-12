from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_user_name(self, locator: str):
        user_name = self.driver.find_element(By.XPATH, locator)

        fake = Faker()
        fake_user_name = fake.user_name()
        user_name.send_keys(fake_user_name)
        print(f'User name = {fake_user_name}')