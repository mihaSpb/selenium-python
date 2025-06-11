from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser:
    def __init__(self, url: str):
        self.url = url
        options = webdriver.ChromeOptions()

        # Настройка дополнительных параметров браузера Chrome
        self._configure_browser(options)

        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    @staticmethod
    def _configure_browser(options: webdriver.ChromeOptions):
        # Отключение менеджера сохранения паролей Chrome
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)

        # Отключение предупреждение о скомпрометированном пароле
        options.add_argument("--disable-features=PasswordLeakDetection")
        # Отключение автозакрытия браузера после выполнения тестов
        options.add_experimental_option('detach', True)

    def launch(self):
        if self.driver:
            self.driver.get(self.url)
            self.driver.set_window_size(1920, 1080)
        else:
            raise RuntimeError("Драйвер не инициализирован!")

    def close(self):
        if self.driver:
            self.driver.quit()