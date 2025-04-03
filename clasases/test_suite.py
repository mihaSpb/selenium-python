from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def test_login(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name_cont = self.driver.find_element(By.XPATH, "//div[@id='login_credentials']")
        user_name_value = user_name_cont.text.splitlines()
        user_name.send_keys(user_name_value[1].strip())
        print('Input login')

    def test_password(self):
        user_password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        user_password_cont = self.driver.find_element(By.XPATH, "//div[@class='login_password']")
        user_password_value = user_password_cont.text.splitlines()
        user_password.send_keys(user_password_value[1].strip())
        print('Input password')

    def test_button_login(self):
        button_login = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        button_login.click()
        print('Click button login')

    def test_current_url(self):
        get_url = self.driver.current_url
        test_url = 'https://www.saucedemo.com/inventory.html'
        assert get_url == test_url
        print(f'Current url = {get_url} is correct')

    def test_element(self, element):
        text_element = self.driver.find_element(By.XPATH, "//span[@class='title']")
        value_test_element = text_element.text
        assert value_test_element == element
        print('Text element = {} is correct'.format(value_test_element))

    def check_error_message(self):
        pass

    def close_error_message(self):
        pass