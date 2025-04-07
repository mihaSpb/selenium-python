import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def test_login(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name_cont = self.driver.find_element(By.XPATH, "//div[@id='login_credentials']")
        user_name_value = user_name_cont.text.splitlines()
        user_name.send_keys(user_name_value[1].strip())

        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name.send_keys(Keys.CONTROL, "a")
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

    def page_refresh(self):
        self.driver.refresh()
        print('Refresh page')

    def highlight_and_clear_login(self):
        login_element = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        login_element.send_keys(Keys.COMMAND + 'a')
        print('Highlight login')
        time.sleep(1)
        login_element.send_keys(Keys.BACKSPACE)
        print('Clear login')

    def highlight_and_clear_password(self):
        password_element = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password_element.send_keys(Keys.COMMAND + 'a')
        print('Highlight password')
        time.sleep(1)
        password_element.send_keys(Keys.BACKSPACE)
        print('Clear password')

    def press_enter_for_login_button(self):
        button_login = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        button_login.send_keys(Keys.ENTER)
        print('Press Enter for button login')