import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    user_name_locator = "//input[@id='user-name']"

    tests.input_user_name(user_name_locator)
    time.sleep(2)

    chrome_browser.close()