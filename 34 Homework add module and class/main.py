from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    login_button = "//input[@id='login-button']"
    open_cart_button = "//*[@id='shopping_cart_container']/a"
    check_name_cart_locator = "//span[@class='title']"

    # Tests
    tests.authorization(login_name="standard_user", login_password="secret_sauce")
    tests.click_button(login_button, "Login")

    tests.press_escape_to_dismiss_alert()
    product_name = tests.user_menu()

    tests.add_to_cart(product_name)
    tests.click_button(open_cart_button, "Open cart")
    tests.check_shopping_cart(20,'Your Cart', check_name_cart_locator)

    chrome_browser.close()