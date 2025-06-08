import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    login_button = "//input[@id='login-button']"
    open_cart_button = "//a[@data-test='shopping-cart-link']"

    # Tests
    tests.input_login()
    tests.input_password()
    tests.click_button(login_button, "Login")

    tests.press_escape_to_dismiss_alert()
    product_name = tests.user_menu()
    tests.add_to_cart(product_name)
    time.sleep(1)
    tests.click_button(open_cart_button, "Open cart")

    #chrome_browser.close()