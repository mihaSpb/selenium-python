import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://the-internet.herokuapp.com/javascript_alerts"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    push_confirm_button = "//*[@id='content']/div/ul/li[2]/button"
    push_text_OK = "You clicked: Ok"
    push_text_cancel = "You clicked: Cancel"

    push_promt_button = "//*[@id='content']/div/ul/li[3]/button"
    incert_promt = "You entered: "
    not_incert_promt = "You entered: "
    promt = "Hi!"

    check_result_text = "//*[@id='result']"

    # Alert
    tests.click("//*[@id='content']/div/ul/li[1]/button", "open alert")
    time.sleep(1)
    tests.alert_and_push(
        check_text_locator = "//*[@id='result']",
        dialog_type = "alert",
        reaction = "OK",
        check_result = "You successfully clicked an alert"
    )
    time.sleep(1)

    # Popup OK
    tests.click("//*[@id='content']/div/ul/li[2]/button", "open confirm")
    time.sleep(1)
    tests.alert_and_push(
        check_text_locator = "//*[@id='result']",
        dialog_type = "confirm",
        reaction = "OK",
        check_result = "You clicked: Ok"
    )
    time.sleep(1)

    # Popup Cancel
    tests.click("//*[@id='content']/div/ul/li[2]/button", "open confirm")
    time.sleep(1)
    tests.alert_and_push(
        check_text_locator = "//*[@id='result']",
        dialog_type = "confirm",
        reaction = "Cancel",
        check_result = "You clicked: Cancel"
    )
    time.sleep(1)

    # Prompt OK
    tests.click("//*[@id='content']/div/ul/li[3]/button", "open prompt")
    time.sleep(1)
    tests.alert_and_push(
        check_text_locator = "//*[@id='result']",
        dialog_type = "prompt",
        reaction = "OK",
        check_result = "You entered: Hi!",
        prompt_text = "Hi!"
    )
    time.sleep(1)

    # Prompt Cancel
    tests.click("//*[@id='content']/div/ul/li[3]/button", "open prompt")
    time.sleep(1)
    tests.alert_and_push(
        check_text_locator = "//*[@id='result']",
        dialog_type = "prompt",
        reaction = "Cancel",
        check_result = "You entered: null"
    )
    time.sleep(1)

    chrome_browser.close()
