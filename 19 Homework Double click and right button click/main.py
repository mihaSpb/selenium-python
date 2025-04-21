import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://demoqa.com/buttons"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    tests.universal_click("//*[@id='doubleClickBtn']", "Double click", "double_click")
    tests.universal_click("//*[@id='rightClickBtn']", "Right click", "right_click")

    chrome_browser.wait_for_enter()
    chrome_browser.close()