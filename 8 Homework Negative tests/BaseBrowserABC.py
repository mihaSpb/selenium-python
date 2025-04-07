from abc import ABC, abstractmethod


class BaseBrowser(ABC):
    def __init__(self, url: str):
        self.url = url
        self.driver = None

    @abstractmethod
    def init_driver(self):
        pass

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