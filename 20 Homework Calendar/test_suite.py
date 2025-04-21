from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.products = {}  # для хранения данных о проверяемых объектах

    def press_key_for_button(self, button_locator: str, key, expected_text: str):
        key_names = {
            Keys.ENTER: "ENTER",
            Keys.BACKSPACE: "BACKSPACE",
            Keys.DELETE: "DELETE",
            Keys.ESCAPE: "ESCAPE",
            Keys.CLEAR: "CLEAR",
            Keys.COMMAND + 'a': "SELECT ALL",
        }

        element = self.driver.find_element(By.XPATH, button_locator)
        # Отправляем либо нажатие клавиши, либо значение key
        element.send_keys(key)

        if key in key_names:
            key_names = key_names[key] # Здесь будут кнопки
        else:
            key_names = key # Здесь будет любая строка или значение переменной

        # key_names = key_names.get(key, str(key))
        print(f'Press {key_names} for {expected_text}')