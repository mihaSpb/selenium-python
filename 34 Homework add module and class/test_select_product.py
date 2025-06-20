from selenium import webdriver
from login_page import LoginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class Test():
    def test_select_product(self):
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = "https://www.saucedemo.com/"
        driver.get(base_url)
        driver.maximize_window()

        login = LoginPage(driver)
        login.login_user(login_name="standard_user", login_password="secret_sauce")

        login.press_escape_to_dismiss_alert()

        login.add_to_cart("Sauce Labs Bolt T-Shirt")
        login.open_cart("//*[@id='shopping_cart_container']/a")

        login.check_shopping_cart(20,"Your Cart", "//span[@class='title']")

        driver.quit()


start_test = Test()
start_test.test_select_product()