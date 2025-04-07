from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Импортируем класс BaseBrowser из папки classes
from BaseBrowserABC import BaseBrowser
# Импортируем класс test_suite из папки classes
from clasases.test_suite import TestSuite


class ChromeBrowser(BaseBrowser):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver= self.init_driver()

    @staticmethod
    def init_driver():
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', False)
        # Запуск браузера в headless режиме
        options.add_argument("--headless")
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )


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
    tests = NegativeTestSuite(chrome_browser.driver)
    negative_tests = NegativeTestSuite(chrome_browser.driver)

    # Тесты
    tests.test_login()
    # Ввод не валидного пароля
    negative_tests.test_incorrect_password()
    tests.test_button_login()
    # Проверка сообщения об ошибке и его закрытие
    negative_tests.check_error_message()
    negative_tests.close_error_message()