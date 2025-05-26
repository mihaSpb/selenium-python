import os
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver, download_dir: str):
        self.driver = driver
        self.download_dir = download_dir

    def click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        print(f"Clicked {message}")

    # Не использует self внутри себя, поэтому делаю данный метод статичным
    @staticmethod
    def verify_file_downloaded(file_name: str, download_dir: str):
        file_path = download_dir + "/" + file_name

        assert os.access(file_path, os.F_OK) is not True
        print (f"File {file_name} downloaded")

        files = glob.glob(os.path.join(download_dir, "*"))
        for file in files:
            a = os.path.getsize(file)
            if a > 10:
                print(f"{file} size is not null")
            else:
                print(f"{file} size is null")

    # Не использует self внутри себя, поэтому делаю данный метод статичным
    @staticmethod
    def remove_files(download_dir: str):
        files = glob.glob(os.path.join(download_dir, "*"))
        for file in files:
            os.remove(file)
        print(f"Removed {len(files)} files")


