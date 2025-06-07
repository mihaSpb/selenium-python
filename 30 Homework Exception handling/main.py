import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://demoqa.com/dynamic-properties"
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    visible_button = "//*[@id='visibleAfter']"

    # Tests
    #tests.click_to_invisible_button(visible_button, 'visible button')
    tests.wait_invisible_button(visible_button, 20, 'visible button')
    time.sleep(2)


    chrome_browser.close()