import time
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

    # Пауза на появление сообщения о скомпрометированном пароле и нажатии кнопки ESС для его закрытия
    time.sleep(3)

    tests.add_product_1()
    tests.add_product_2()
    time.sleep(0.5)
    tests.open_cart()

    time.sleep(0.5)
    tests.make_order()
    tests.data_for_order_form()
    time.sleep(0.5)

    tests.open_order_for_check_sum()
    tests.check_product_1()
    tests.check_product_2()
    tests.check_order_sum()
    tests.finish_order()

    chrome_browser.wait_for_enter()
    chrome_browser.close()