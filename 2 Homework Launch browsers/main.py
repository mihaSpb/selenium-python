from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


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


class ChromeBrowser(BaseBrowser):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = self.init_driver()

    @staticmethod
    def init_driver():
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', False)
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


class EdgeBrowser(BaseBrowser):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = self.init_driver()

    @staticmethod
    def init_driver():
        options = webdriver.EdgeOptions()
        options.binary_location = "/Volumes/SSD/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)


class FirefoxBrowser(BaseBrowser):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = self.init_driver()

    @staticmethod
    def init_driver():
        options = webdriver.FirefoxOptions()
        options.binary_location = "/Volumes/SSD/Applications/Firefox.app/Contents/MacOS/firefox"
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)


def wait_for_enter():
    input("Нажмите Enter, чтобы закрыть браузер и продолжить...")


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"

    # Запуск Chrome
    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    wait_for_enter()
    chrome_browser.close()

    # Запуск Edge
    edge_browser = EdgeBrowser(default_url)
    edge_browser.launch()
    wait_for_enter()
    edge_browser.close()

    # Запуск Firefox
    firefox_browser = FirefoxBrowser(default_url)
    firefox_browser.launch()
    wait_for_enter()
    firefox_browser.close()
