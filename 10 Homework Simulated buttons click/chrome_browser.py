from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ChromeBrowser:
    def __init__(self, url: str):
        self.url = url
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        # Запуск в headless режиме
        # options.add_argument("--headless")
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