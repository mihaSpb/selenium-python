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

    time.sleep(0.5)
    tests.universal_click("//a[@data-test='shopping-cart-link']", "Open cart")

    time.sleep(1)
    chrome_browser.driver.back()

    time.sleep(1)
    chrome_browser.driver.forward()
    time.sleep(1)

    chrome_browser.close()