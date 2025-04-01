# Импортируем класс BaseBrowser из папки classes
from clasases.BaseBrowser import BaseBrowser
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


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

    # Выбор поля логин
    user_name = chrome_browser.driver.find_element(By.XPATH, "//input[@id='user-name']")

    # Заполнение поля логин значением: поиск элемента, разбивка элемента на строки, выбор нужной строки для подстановки
    user_name_cont = chrome_browser.driver.find_element(By.XPATH, "//div[@id='login_credentials']")
    user_name_value = user_name_cont.text.splitlines()
    user_name.send_keys(user_name_value[1].strip())

    # Выбор поля логин
    user_password = chrome_browser.driver.find_element(By.XPATH,"//input[@id='password']")

    # Заполнение поля пароль: поиск элемента, разбивка элемента на строки, выбор нужной строки для подстановки
    user_password_cont = chrome_browser.driver.find_element(By.XPATH,"//div[@class='login_password']")
    user_password_value = user_password_cont.text.splitlines()
    user_password.send_keys(user_password_value[1].strip())

    # Нажатие кнопки
    button_login = chrome_browser.driver.find_element(By.XPATH, "//input[@id='login-button']")
    button_login.click()

    chrome_browser.wait_for_enter()
    chrome_browser.close()