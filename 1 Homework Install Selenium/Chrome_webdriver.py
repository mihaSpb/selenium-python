from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def init_driver():
    # Инициализация драйвера ChromeDriver и возврат его с заданными параметрами.
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def launch_browser(driver, url):
    # Запуск браузера с указанным URL.
    driver.get(url)
    driver.set_window_size(1920, 1080)


def main():
    default_url = "https://www.saucedemo.com/"
    user_input = input(f"Введите URL для открытия (по умолчанию: {default_url}): ").strip()
    # Если пользователь ничего не ввёл, используем URL по умолчанию.
    url_to_open = user_input if user_input else default_url

    driver = init_driver()
    launch_browser(driver, url_to_open)


if __name__ == "__main__":
    main()