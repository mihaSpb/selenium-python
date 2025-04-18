import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://demoqa.com/radio-button"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    tests.universal_click("(//label[@class='custom-control-label'])[2]", "Select radio button")
    tests.is_element_selected("//*[@id='impressiveRadio']")

    chrome_browser.wait_for_enter()
    chrome_browser.close()