import time
from datetime import datetime, timedelta
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://demoqa.com/date-picker"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)
    input_element = "//*[@id='datePickerMonthYearInput']"

    # Тесты
    tests.press_key_in_element(input_element, "SELECT_ALL", "select date")
    time.sleep(1)
    tests.press_key_in_element(input_element, "DELETE", "delete date")

    current_date = (datetime.now() + timedelta(days = 10)).strftime("%m/%d/%Y")
    time.sleep(1)
    tests.press_key_in_element(input_element, current_date, "insert new date")
    time.sleep(1)
    chrome_browser.close()