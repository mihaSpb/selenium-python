import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://demoqa.com/browser-windows"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    new_tab_button = "//*[@id='tabButton']"
    tests.click(new_tab_button, 'open new tab')
    time.sleep(2)

    tests.switch_to_tab_or_window(0, 'first tab')
    time.sleep(2)

    # New window
    new_window_button = "//*[@id='windowButton']"
    tests.click(new_window_button, 'open new window')
    time.sleep(2)

    tests.switch_to_tab_or_window(0,'first window')
    time.sleep(2)

    chrome_browser.close()
