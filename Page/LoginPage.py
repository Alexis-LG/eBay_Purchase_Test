from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.input_username = self.wait.until(EC.presence_of_element_located((By.ID, "userid")))
        self.input_password = self.wait.until(EC.presence_of_element_located((By.ID, "pass")))
        self.button_sign_in = self.wait.until(EC.presence_of_element_located((By.ID, "sgnBt")))

    def login(self, username, password):
        self.input_username.send_keys(username)
        self.input_password.send_keys(password)
        self.button_sign_in.click()
