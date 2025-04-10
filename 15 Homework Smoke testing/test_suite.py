import re
import time
import datetime
from pathlib import Path

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = WebDriver = driver

    def test_login(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name_cont = self.driver.find_element(By.XPATH, "//div[@id='login_credentials']")
        user_name_value = user_name_cont.text.splitlines()
        user_name.send_keys(user_name_value[1].strip())

        user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        user_name.send_keys(Keys.CONTROL, "a")
        print('Input login')

    def test_password(self):
        user_password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        user_password_cont = self.driver.find_element(By.XPATH, "//div[@class='login_password']")
        user_password_value = user_password_cont.text.splitlines()
        user_password.send_keys(user_password_value[1].strip())
        print('Input password')

    def test_button_login(self):
        button_login = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        button_login.click()
        print('Click button login')

    def test_current_url(self):
        get_url = self.driver.current_url
        test_url = 'https://www.saucedemo.com/inventory.html'
        assert get_url == test_url
        print(f'Current url = {get_url} is correct')

    def test_element(self, element):
        text_element = self.driver.find_element(By.XPATH, "//span[@class='title']")
        value_test_element = text_element.text
        assert value_test_element == element
        print('Text element = {} is correct'.format(value_test_element))

    def page_refresh(self):
        self.driver.refresh()
        print('Refresh page')

    def highlight_and_clear_login(self):
        login_element = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        login_element.send_keys(Keys.COMMAND + 'a')
        print('Highlight login')
        time.sleep(1)
        login_element.send_keys(Keys.BACKSPACE)
        print('Clear login')

    def highlight_and_clear_password(self):
        password_element = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password_element.send_keys(Keys.COMMAND + 'a')
        print('Highlight password')
        time.sleep(1)
        password_element.send_keys(Keys.BACKSPACE)
        print('Clear password')

    def press_enter_for_login_button(self):
        button_login = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        button_login.send_keys(Keys.ENTER)
        print('Press Enter for button login')

    def make_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        screenshot_dir = Path('screens')
        name_screenshot = screenshot_dir / f"screenshot_ {now_date}.png"
        time.sleep(0.5)
        self.driver.save_screenshot(name_screenshot)
        print(f'Screenshot saved at {name_screenshot}')

    def add_all_items_to_cart(self):
        # add_backpack
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        print('Add backpack')
        # add_bike
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        print('Add bike')
        # add_t_shirt
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        print('Add T-shirt')
        # add_jacket
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        print('Add jacket')
        # add_onessie
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
        print('Add onessie')
        # add_t_short_red
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
        print('Add T-shirt red')

    def open_cart(self):
        self.driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
        print('View cart click')

    def find_element_and_move(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.ID, 'item_3_title_link')
        actions.move_to_element(element).perform()
        print('Moved to element')

    def clear_user_name(self):
        self.test_login()
        time.sleep(1)
        clear_user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        clear_user_name.clear()
        print('Clear username')

    def delete_user_name(self):
        self.test_login()
        time.sleep(1)
        delete_user_name = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        delete_user_name.send_keys(Keys.COMMAND + 'a')
        time.sleep(0.5)
        delete_user_name.send_keys(Keys.DELETE)
        print('Delete username')

    def clear_password(self):
        self.test_password()
        time.sleep(1)
        clear_password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        clear_password.clear()
        print('Clear password')

    def delete_password(self):
        self.test_password()
        time.sleep(1)
        delete_password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        delete_password.send_keys(Keys.COMMAND + 'a')
        time.sleep(0.5)
        delete_password.send_keys(Keys.DELETE)
        print('Delete password')

    def open_hidden_menu(self):
        self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        print('Open hidden menu')

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
        print('Click logout button')

    def add_product_1(self):
        product_1 = self.driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
        self.value_product_1 = product_1.text
        print(f'Product 1 title = {self.value_product_1}')

        price_product_1 = self.driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
        self.value_price_product_1 = price_product_1.text
        print(f'Product 1 price = {self.value_price_product_1}')

        # Add to cart product_1
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()

    def add_product_2(self):
        product_2 = self.driver.find_element(By.XPATH, "//*[@id='item_0_title_link']")
        self.value_product_2 = product_2.text
        print(f'Product 2 title = {self.value_product_2}')

        price_product_2 = self.driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
        self.value_price_product_2 = price_product_2.text
        print(f'Product 2 price = {self.value_price_product_2}')

        # Add to cart product_2
        self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()

    def make_order(self):
        self.driver.find_element(By.XPATH, "// *[ @ id = 'checkout']").click()
        print('Make order')

    def data_for_order_form(self):
        fake = Faker()
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_zip_code = fake.zipcode()

        order_first_name = self.driver.find_element(By.XPATH, "//*[@id='first-name']")
        order_first_name.send_keys(fake_first_name)
        print(f'First name = {fake_first_name}')

        order_last_name = self.driver.find_element(By.XPATH, "//*[@id='last-name']")
        order_last_name.send_keys(fake_last_name)
        print(f'Last name = {fake_last_name}')

        order_zip_code = self.driver.find_element(By.XPATH, "//*[@id='postal-code']")
        order_zip_code.send_keys(fake_zip_code)
        print(f'Zip code = {fake_zip_code}')

    def open_order_for_check_sum(self):
        self.driver.find_element(By.XPATH, "//*[@id='continue']").click()

    def check_product_1(self):
        order_product_1_title = self.driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")
        value_order_product_1_title = order_product_1_title.text
        order_product_1_price = self.driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        self.value_order_product_1_price = order_product_1_price.text

        assert value_order_product_1_title == self.value_product_1
        print(f'Product 1 title = {value_order_product_1_title} OK')

        assert self.value_order_product_1_price == self.value_price_product_1
        print(f'Product 1 price = {self.value_order_product_1_price} OK')

    def check_product_2(self):
        order_product_2_title = self.driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
        value_order_product_2_title = order_product_2_title.text
        order_product_2_price = self.driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
        self.value_order_product_2_price = order_product_2_price.text

        assert value_order_product_2_title == self.value_product_2
        print(f'Product 2 title = {value_order_product_2_title} OK')

        assert self.value_order_product_2_price == self.value_price_product_2
        print(f'Product 2 price = {self.value_order_product_2_price} OK')

    def parse_price_items(self,price_str: str) -> float:
        # Замена запятой на точку
        price_str= price_str.replace(',', '.')
        # Удаление всех символов, кроме запятой и точки
        price_cleaned = re.sub(r'[^\d.]', '', price_str)
        return float(price_cleaned)

    def check_order_sum(self):
        order_sum = self.driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
        value_order_sum_text = order_sum.text
        value_order_sum = self.parse_price_items(value_order_sum_text)
        print(f'Order sum = {value_order_sum}')

        check_order_sum = self.parse_price_items(self.value_order_product_1_price) + self.parse_price_items(self.value_order_product_2_price)
        print(f'Check sum = {check_order_sum}')
        assert value_order_sum == check_order_sum
        print(f'Order sum = {value_order_sum} OK')

    def finish_order(self):
        self.driver.find_element(By.XPATH, "// *[ @ id = 'finish']").click()
        print('Finish order')
