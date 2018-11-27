import time

from Page.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def login(self, username, password):
        input_username = self.browser.find_element_by_id("userid")
        input_username.send_keys(username)
        input_password = self.browser.find_element_by_id("pass")
        input_password.send_keys(password)
        button_sign_in = self.browser.find_element_by_id("sgnBt")
        button_sign_in.click()
        time.sleep(5)
