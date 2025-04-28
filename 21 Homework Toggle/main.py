import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://html5css.ru/howto/howto_js_rangeslider.php"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)
    slider = "//*[@id='id1']"
    slider_value = "//*[@id='f']"

    # Тесты
    tests.move_slider(slider, '-229px')
    time.sleep(1)
    tests.check_move_slider(slider, slider_value)

    chrome_browser.close()