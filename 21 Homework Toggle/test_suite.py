from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.elements = {}  # для хранения данных о проверяемых объектах

    def move_slider(self, locator: str, offset_str: str):
        actions = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, locator)
        offset_px = int(offset_str.rstrip('px'))

        actions.click_and_hold(slider).move_by_offset(offset_px,0).release().perform()
        print(f'Слайдер перемещен на {offset_px}px')

    def check_move_slider(self, slider_locator: str, value_locator: str):
        slider = self.driver.find_element(By.XPATH, slider_locator)
        actual = int(slider.get_attribute('value')) # Фактическое значение слайдера

        # Значение поля Value
        displayed_value = int(self.driver.find_element(By.XPATH, value_locator).text)

        assert displayed_value == actual, (
            f"В поле Value {displayed_value}, а значение слайдера – {actual}"
        )
        print(f'Проверка пройдена: {displayed_value} == {actual}')