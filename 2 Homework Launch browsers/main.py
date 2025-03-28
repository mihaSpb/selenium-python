from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BaseBrowser:
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
            self.driver.close()


class ChromeBrowser(BaseBrowser):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = ChromeBrowser.init_driver()

    @staticmethod
    def init_driver():
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', False)
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


class EdgeBrowser(BaseBrowser):
    def __init__(self, url: str):
        super().__init__(url)
        self.driver = EdgeBrowser.init_driver()

    @staticmethod
    def init_driver():
        options = webdriver.EdgeOptions()
        return webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options=options)


class FirefoxBrowser(BaseBrowser):
    def __init__(self, url):
        super().__init__(url)
        self.driver = FirefoxBrowser.init_driver()

    @staticmethod
    def init_driver():
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()), options = options)


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"

    chrome_browser = ChromeBrowser(default_url)
    edge_browser = EdgeBrowser(default_url)
    firefox_browser = FirefoxBrowser(default_url)

    chrome_browser.launch()
    edge_browser.launch()
    firefox_browser.launch()

    input("Нажмите Enter для завершения работы программы...")

    chrome_browser.close()
    edge_browser.close()
    firefox_browser.close()