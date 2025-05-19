from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestSuite:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator: str, message: str = ""):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        print(f"Clicked {message}")

    def alert_and_push(self,
        check_text_locator: str,
        dialog_type: str,
        reaction: str,
        check_result: str,
        prompt_text: str = ""
    ):
        """
        - dialog_type: 'alert' , 'confirm' , 'prompt'
        - reaction: 'OK' , 'Cancel'
        - check_result: expected text to appear in page element
        - prompt_text:  text to send into prompt (only for prompt + OK)
        """
        alert = self.driver.switch_to.alert

        if dialog_type == 'alert':
            alert.accept()
            print("Accepted alert")

        elif dialog_type == 'confirm':
            if reaction == 'OK':
                alert.accept()
                print("Accepted confirm")
            else:
                alert.dismiss()
                print("Dismissed confirm")

        elif dialog_type == 'prompt':
            if reaction == 'OK':
                alert.send_keys(prompt_text)
                alert.accept()
                print(f"Sent '{prompt_text}' to prompt and accepted")
            else:
                alert.dismiss()
                print("Dismissed prompt without input")

        else:
            raise ValueError(f"Unknown dialog_type: {dialog_type}")

        result_el = self.driver.find_element(By.XPATH, check_text_locator)
        actual = result_el.text.strip()
        assert actual == check_result, (f"Expected result '{check_result}', but got '{actual}'")
        print(f"Dialog result correct: '{actual}'")