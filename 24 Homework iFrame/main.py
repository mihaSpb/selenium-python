import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.lambdatest.com/selenium-playground/iframe-demo/"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    text_message = 'New text'
    iframe_locator = "//*[@id='iFrame1']"
    input_area_locator = "//*[@id='__next']/div/div[2]"
    italic_bolt_font = "//*[@id='__next']/div/div[1]/button[2]"
    strike_through_font = "//*[@id='__next']/div/div[1]/button[4]"

    check_text = "//*[@id='__next']/div/div[2]/i/strike"

    tests.switch_to_iframe(iframe_locator)
    time.sleep(1)

    tests.input_text(input_area_locator, text_message)
    time.sleep(2)

    tests.select_all_text(input_area_locator)
    time.sleep(1)

    tests.click(italic_bolt_font, 'italic font')
    time.sleep(1)

    tests.click(strike_through_font, 'strike through font')
    time.sleep(1)

    tests.check_text_in_element(text_message, check_text)
    time.sleep(2)

    chrome_browser.close()