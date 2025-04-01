from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BrowserBase:
    def __init__(self, url: str):
        self.url = url
        self.driver = None


    def launch(self):
        if self.driver:
            self.driver.get(self.url)
            self.driver.set_window_size(1920, 1080)
        else:
            raise RuntimeError("Драйвер не инициализирован")


    def close(self):
        if self.driver:
            self.driver.quit()


class ChromeBrowser(BrowserBase):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = ChromeBrowser.init_driver()


    @staticmethod
    def init_driver():
        options = webdriver.ChromeOptions()
        # Отключаем detach, чтобы окно закрылось после завершения работы программы
        options.add_experimental_option('detach', False)
        return webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options)


class FirefoxBrowser(BrowserBase):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = FirefoxBrowser.init_driver()


    @staticmethod
    def init_driver():
        options = webdriver.FirefoxOptions()
        # Указываем путь к исполняемому файлу Firefox
        options.binary_location = "/Volumes/SSD/Applications/Firefox.app/Contents/MacOS/firefox"
        return webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()), options = options)


class EdgeBrowser(BrowserBase):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = EdgeBrowser.init_driver()


    @staticmethod
    def init_driver():
        options = webdriver.EdgeOptions()
        # Указываем путь к исполняемому файлу Edge
        options.binary_location = "/Volumes/SSD/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
        return webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = options)


def main():
    default_url = "https://www.saucedemo.com/"
    user_input = input(f"Введите URL для открытия (по умолчанию: {default_url}): ").strip()
    url_to_open = user_input if user_input else default_url

    # Инициализация экземпляров для каждого браузера.
    chrome_browser = ChromeBrowser(url_to_open)
    firefox_browser = FirefoxBrowser(url_to_open)
    edge_browser = EdgeBrowser(url_to_open)

    # Запуск браузеров с заданным URL.
    chrome_browser.launch()
    firefox_browser.launch()
    edge_browser.launch()

    input("Нажмите Enter для завершения программы...")

    # Закрытие всех браузеров.
    chrome_browser.close()
    firefox_browser.close()
    edge_browser.close()


if __name__ == "__main__":
    main()