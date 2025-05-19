import ntpath
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def upload_file(self, upload_button_locator: str, path_file: str, timeout: int = 2):
        upload_button = self.driver.find_element(By.XPATH, upload_button_locator)
        upload_button.send_keys(path_file)
        print(f"File uploaded: {path_file}")

        time.sleep(timeout)

        value_uploaded_file_name = upload_button.get_attribute("value")
        actual_name = ntpath.basename(value_uploaded_file_name)
        expected_name = os.path.basename(path_file)

        assert actual_name == expected_name, (f"{actual_name} != {expected_name}")
        print(f"File uploaded correctly: {actual_name}")