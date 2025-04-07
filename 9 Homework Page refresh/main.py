import time
from selenium.webdriver.common.by import By

# Импортируем класс BaseBrowser из папки classes
from chrome_browser import ChromeBrowser
# Импортируем класс test_suite из папки classes
from test_suite import TestSuite


# Переопределенные методы класса с тестами
class NegativeTestSuite(TestSuite):
    def test_incorrect_password(self):
        user_password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        user_password.send_keys("incorrect_password")
        print('Send incorrect password')

    def check_error_message(self):
        error_text = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        value_error_text = error_text.text
        assert value_error_text == 'Epic sadface: Username and password do not match any user in this service'
        print('Error text is correct')

    def close_error_message(self):
        error_button = self.driver.find_element(By.XPATH, "//button[@class='error-button']")
        error_button.click()
        print('Closed error message')


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"

    # Запуск Chrome
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()

    # Инициализация тестов
    tests = TestSuite(chrome_browser.driver)
    negative_tests = NegativeTestSuite(chrome_browser.driver)

    # Тесты
    tests.test_login()
    # Ввод не валидного пароля
    negative_tests.test_incorrect_password()
    tests.test_button_login()
    # Проверка сообщения об ошибке
    negative_tests.check_error_message()

    time.sleep(3)
    tests.page_refresh()
