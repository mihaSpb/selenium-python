import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    login_button = "//input[@id='login-button']"
    visible_button = "//*[@id='visibleAfter']"

    # Tests
    tests.input_login()
    tests.input_password()
    tests.universal_click(login_button, "Login")

    tests.press_escape_to_dismiss_alert(10)
    time.sleep(2)

    chrome_browser.close()

    def user_menu(self):
        product = {
            "1": "Sauce Labs Backpack",
            "2": "Sauce Labs Bike Light",
            "3": "Sauce Labs Bolt T-Shirt",
            "4": "Sauce Labs Fleece Jacket",
            "5": "Sauce Labs Onesie",
            "6": "Test.allTheThings() T-Shirt (Red)"
        }

        print("Приветствую тебя в нашем интернет-магазине")
        print("Выбери один из следующих товаров и укажи его номер:\n"
              "1 - Sauce Labs Backpack,\n"
              "2 - Sauce Labs Bike Light,\n"
              "3 - Sauce Labs Bolt T-Shirt,\n"
              "4 - Sauce Labs Fleece Jacket,\n"
              "5 - Sauce Labs Onesie,\n"
              "6 - Test.allTheThings() T-Shirt (Red)")