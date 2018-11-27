from selenium.webdriver.common.keys import Keys

from Page.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def search_item(self, item_name):
        input_search = self.browser.find_element_by_xpath("//input[@placeholder='Buscar artículos']")
        input_search.send_keys(item_name, Keys.ENTER)
