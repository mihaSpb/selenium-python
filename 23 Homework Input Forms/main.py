import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://lambdatest.com/selenium-playground/simple-form-demo"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    # Single Input Field
    input_element = "//*[@id='user-message']"
    input_message = "Hello World!"
    check_button = "//*[@id='showInput']"
    check_text_element = "//*[@id='message']"

    tests.input_text(input_element, input_message)
    time.sleep(2)
    tests.click(check_button)
    time.sleep(1)

    tests.check_text_in_element(input_message, check_text_element)
    time.sleep(1)

    # Two Input Fields
    tests.sum_and_validate(first_locator = "//*[@id='sum1']",
                           second_locator = "//*[@id='sum2']",
                           button_locator = "//*[@id='gettotal']/button",
                           result_locator = "//*[@id='addmessage']",
                           first_value = "25",
                           second_value = "50"
                           )
    time.sleep(2)
    chrome_browser.close()