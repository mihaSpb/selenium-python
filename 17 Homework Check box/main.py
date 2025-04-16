import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://demoqa.com/checkbox"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    tests.universal_click("//*[@id='tree-node']/ol/li/span/label/span[1]", "Select check box")
    tests.is_element_selected("//*[@id='tree-node-home']")
    time.sleep(2)

    chrome_browser.close()