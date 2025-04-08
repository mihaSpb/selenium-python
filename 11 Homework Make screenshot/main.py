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
    tests.test_login()
    tests.test_password()
    tests.test_button_login()
    tests.make_screenshot()

    chrome_browser.wait_for_enter()
    chrome_browser.close()