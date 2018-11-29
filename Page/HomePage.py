from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.input_search = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//input[@placeholder='Buscar artículos']")))

    def visit_login_page(self):
        button_login = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//a[text()='Inicia sesión']")))
        button_login.click()

    def search_item(self, item_name):
        self.input_search.send_keys(item_name, Keys.ENTER)
