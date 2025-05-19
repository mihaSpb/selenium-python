import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.lambdatest.com/selenium-playground/upload-file-demo"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    path_to_file = "/Volumes/SSD/PycharmProjects/ijuniorProject/selenium-python/selenium-python/Upload_load files/Sl8EKR35AQc.jpg"
    upload_file_button = "//*[@id='file']"

    # Tests
    tests.upload_file(upload_file_button, path_to_file)
    time.sleep(1)

    chrome_browser.close()