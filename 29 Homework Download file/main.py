import time
from pathlib import Path
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    # Определения местоположения папки для загрузок в проекте
    dl_directory = Path(__file__).resolve().parent
    project_root = dl_directory.parent
    download_dir = project_root / "download_files"

    default_url = "https://www.lambdatest.com/selenium-playground/download-file-demo"
    file_name = "LambdaTest.pdf"

    chrome_browser = ChromeBrowser(default_url, str(download_dir))
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver, str(download_dir))

    download_file_button = "//*[@id='__next']/div/section[2]/div/div/div/div/a/button"

    # Tests
    tests.click(download_file_button, 'Download File button')
    time.sleep(2)

    tests.verify_file_downloaded(file_name, str(download_dir))
    time.sleep(2)

    tests.remove_files(str(download_dir))

    chrome_browser.close()