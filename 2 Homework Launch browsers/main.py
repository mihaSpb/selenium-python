from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import WebDriverException


class LaunchBrowser:
    def __init__(self, url: str):
        self.url = url
        self.drivers = {}
        self.driver_initializers = {
            "chrome": self.init_chrome,
            "firefox": self.init_firefox,
            "edge": self.init_edge
        }


    def init_chrome(self):
        # Инициализирует драйвер для Google Chrome.
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options)


    def init_firefox(self):
        # Инициализирует драйвер для Mozilla Firefox.
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()), options = options)


    def init_edge(self):
        # Инициализирует драйвер для Microsoft Edge.
        options = webdriver.EdgeOptions()
        return webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = options)


    def init_driver(self, browser: str):
        # Выбор и инициализация драйвера для указанного браузера через словарь инициализаторов.
        browser = browser.lower()
        if browser not in self.driver_initializers:
            raise ValueError(f"Неподдерживаемый браузер: {browser}")
        return self.driver_initializers[browser]()


    def launch_browser_instance(self, driver):
        # Запускает браузер с заданным URL с устанавленным размером окна.
        driver.get(self.url)
        driver.set_window_size(1920, 1080)


    def launch_all_browsers(self):
        # Запускает указанный URL во всех поддерживаемых браузерах с обработкой исключений.
        browsers = ["chrome", "firefox", "edge"]
        for browser in browsers:
            try:
                print(f"Запуск {browser.capitalize()}...")
                driver = self.init_driver(browser)
                self.launch_browser_instance(driver)
                self.drivers[browser] = driver
            except WebDriverException as e:
                print(f"Ошибка при запуске {browser.capitalize()}: {e}")
            except Exception as e:
                print(f"Непредвиденная ошибка при запуске {browser.capitalize()}: {e}")


if __name__ == "__main__":
    default_url = "https://www.saucedemo.com/"
    user_input = input(f"Введите URL для открытия (по умолчанию: {default_url}): ").strip()

    if user_input:
        launcher = LaunchBrowser(user_input)
        launcher.launch_all_browsers()
    else:
        launcher = LaunchBrowser(default_url)
        launcher.launch_all_browsers()

    input("Нажмите Enter для завершения...")