class BaseBrowser:
    def __init__(self, url: str):
        self.url = url
        self.driver = None

    def launch(self):
        if self.driver:
            self.driver.get(self.url)
            self.driver.set_window_size(1920, 1080)
        else:
            raise RuntimeError("Драйвер не инициализирован!")

    def close(self):
        if self.driver:
            self.driver.quit()

    def wait_for_enter(self):
        input("Нажмите Enter, чтобы закрыть браузер и продолжить...")