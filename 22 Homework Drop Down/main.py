import time
from chrome_browser import ChromeBrowser
from test_suite import TestSuite


if __name__ == "__main__":
    default_url = "https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo"

    chrome_browser = ChromeBrowser(default_url)
    chrome_browser.launch()
    tests = TestSuite(chrome_browser.driver)

    # Тесты
    # Выбор страны из выпадающего списка
    drop_country = "//*[@id='__next']/div/section[2]/div/div/div/div[1]/div[2]/span/span[1]/span"
    input_country_area = "/html/body/span/span/span[1]/input"
    tests.click(drop_country, 'open country dropdown')
    time.sleep(1)
    tests.input_text(input_country_area, 'Denmark')
    time.sleep(3)

    # Множественный выбор
    input_multiple_element = "//*[@id='__next']/div/section[2]/div/div/div/div[2]/div[2]/span/span[1]/span/ul/li/input"
    for state in ['Alaska', 'Florida']:
        tests.input_text(input_multiple_element, state)
        time.sleep(0.5)

    # Выбор из списка с не активными элементами
    drop_with_disable_values = "//*[@id='__next']/div/section[2]/div/div/div/div[3]/div[2]/select"
    tests.select_dropdown(drop_with_disable_values,  'Virgin Islands')
    time.sleep(1)

    # Однозначный выбор элемента через Select
    drop_category = "//*[@id='files']"
    tests.select_dropdown(drop_category, 'Python')
    time.sleep(3)

    chrome_browser.close()