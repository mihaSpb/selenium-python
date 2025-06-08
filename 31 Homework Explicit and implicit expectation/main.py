from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    login_button = "//input[@id='login-button']"
    open_cart_button = "//*[@id='shopping_cart_container']/a"
    checkout_button = "//*[@id='checkout']"
    continue_button = "//*[@id='continue']"
    finish_button = "//*[@id='finish']"
    back_home_button = "//*[@id='back-to-products']"

    # Tests
    tests.input_login()
    tests.input_password()
    tests.click_button(login_button, "Login")

    tests.press_escape_to_dismiss_alert()
    product_name = tests.user_menu()

    tests.add_to_cart(product_name)
    name_on_detail, price_on_detail = tests.get_product_details()

    tests.click_button(open_cart_button, "Open cart")
    tests.verify_in_cart(name_on_detail, price_on_detail)

    tests.click_button(checkout_button, "Start checkout")
    tests.data_for_order_form()

    tests.click_button(continue_button, "Click continue")
    expected_prices = tests.parse_price(price_on_detail)
    tests.check_order_sum(expected_prices)
    tests.check_tax_and_total()

    tests.click_button(finish_button, "Finish")
    tests.verify_order_complete()

    tests.click_button(back_home_button, "Back to products")

    chrome_browser.close()