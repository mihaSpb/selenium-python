import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser:
    def __init__(self, url: str, download_dir: str):
        self.url = url

        # Проверяем наличие папки для скачивания
        os.makedirs(download_dir, exist_ok=True)

        options = webdriver.ChromeOptions()

        # Отключаю менеджер сохранения паролей Chrome и задаем путь для скачивания файлов
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            #"download.default_directory": os.path.expanduser("/Volumes/SSD/PycharmProjects/ijuniorProject/selenium-python/selenium-python/download_files/")
            "download.default_directory": download_dir,
        }
        options.add_experimental_option("prefs", prefs)

        # Отключаем предупреждение о скомпрометированном пароле
        options.add_argument("--disable-features=PasswordLeakDetection")

        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    def launch(self):
        if self.driver:
            self.driver.get(self.url)
            self.driver.set_window_size(1920, 1080)
        else:
            raise RuntimeError("Драйвер не инициализирован!")

    def close(self):
        if self.driver:
            self.driver.quit()

    @staticmethod
    def wait_for_enter():
        input("Нажмите Enter, чтобы закрыть браузер и продолжить...")