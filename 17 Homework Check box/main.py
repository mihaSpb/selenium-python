import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://demoqa.com/checkbox"
    element_locator = "//*[@id='tree-node']/ol/li/span/label/span[1]"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    tests.universal_click(element_locator, "Select check box")
    tests.is_element_selected(element_locator)
    time.sleep(2)

    chrome_browser.close()