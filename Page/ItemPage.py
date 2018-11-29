from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class ItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.button_buy_now = self.wait.until(EC.presence_of_element_located((By.ID, "binBtn_btn")))

    def add_item_to_cart(self):
        size = Select(self.wait.until(EC.presence_of_element_located((By.NAME, 'Model'))))
        size.select_by_value('0')  # selects first valid item size on the list
        self.button_buy_now.click()
