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

    tests.highlight_and_clear_login()
    tests.highlight_and_clear_password()
    tests.press_enter_for_login_button()

    chrome_browser.wait_for_enter()
    chrome_browser.close()