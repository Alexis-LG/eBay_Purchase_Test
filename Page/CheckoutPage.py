from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def insert_address_information(self, address, optional_address, city, state, zip, phone):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'¿Adónde entregamos tu pedido?')]")))

            input_address = self.driver.find_element_by_name("address1")
            input_address.send_keys(address)
            input_optional_address = self.driver.find_element_by_name("address2")
            input_optional_address.send_keys(optional_address)
            input_city = self.driver.find_element_by_name("city")
            input_city.send_keys(city)
            input_state = self.driver.find_element_by_name("state")
            input_state.send_keys(state)
            input_zip = self.driver.find_element_by_name("zip")
            input_zip.send_keys(zip)
            input_phone = self.driver.find_element_by_name("phoneFlagComp1")
            input_phone.send_keys(phone)

        except TimeoutException:
            self.wait.until(EC.presence_of_element_located((By.NAME, "reviewbin")))
            self.driver.close()
            # Test would end here since the account would be legally binded to make the purchase in the next step

    def is_submit_button_clickable(self):
        button_submit = self.driver.find_element_by_id("sbtBtn")
        return button_submit.is_enabled() & button_submit.is_displayed()
