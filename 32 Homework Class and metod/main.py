from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    login_button = "//input[@id='login-button']"

    # Tests
    tests.input_login()
    tests.input_password()
    tests.click_button(login_button, "Login")

    tests.press_escape_to_dismiss_alert()

    chrome_browser.close()