from Page.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def select_rollerblade(self):
        item = self.browser.find_element_by_xpath("//h3/a[contains(text(),'Rollerblade')]")
        item.click()
