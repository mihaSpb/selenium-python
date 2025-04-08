from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"

    # Запуск Chrome
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()

    # Инициализация тестов
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    tests.clear_user_name()
    tests.delete_user_name()
    tests.test_login()

    tests.clear_password()
    tests.delete_password()
    tests.test_password()

    tests.test_button_login()

    chrome_browser.wait_for_enter()
    chrome_browser.close()