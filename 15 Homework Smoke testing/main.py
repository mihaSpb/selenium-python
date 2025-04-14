import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    tests.input_login()
    tests.input_password()
    tests.universal_click("//input[@id='login-button']", "Click button login")
    time.sleep(3)

    cart_product = tests.add_something_product("//*[@id='item_4_title_link']", "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div",
                                "//button[@id='add-to-cart-sauce-labs-backpack']", "Sauce Labs Backpack")
    cart_product = tests.add_something_product("//*[@id='item_0_title_link']", "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div",
                                "//*[@id='add-to-cart-sauce-labs-bike-light']", "Sauce Labs Bike Light")
    time.sleep(0.5)
    tests.universal_click("//a[@data-test='shopping-cart-link']", "Open cart")

    time.sleep(0.5)
    tests.universal_click("//*[@id='checkout']", "Make order")
    tests.data_for_order_form()
    time.sleep(0.5)
    tests.universal_click("//*[@id='continue']", "Open order for check sum")

    tests.check_product("//*[@id='item_4_title_link']/div", "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div",
                        "Sauce Labs Backpack")
    tests.check_product("//*[@id='item_0_title_link']/div", "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div",
                        "Sauce Labs Bike Light")

    tests.check_order_sum(cart_product)
    tests.universal_click("//*[@id='finish']", "Finish order")

    chrome_browser.close()