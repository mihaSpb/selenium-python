from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Импортируем класс BaseBrowser из папки classes
from clasases.BaseBrowser import BaseBrowser


class ChromeBrowser(BaseBrowser):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = self.init_driver()

    def init_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', False)
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"

    # Запуск Chrome
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()

    # Заполнение поля логин
    user_name = chrome_browser.driver.find_element(By.ID,"user-name")
    user_name.send_keys("standard_user")

    # Заполнение поля пароль
    user_password = chrome_browser.driver.find_element(By.ID,"password")
    user_password.send_keys("secret_sauce")

    chrome_browser.wait_for_enter()
    chrome_browser.close()
