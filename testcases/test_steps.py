import unittest

import allure
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from Page.CheckoutPage import CheckoutPage
from Page.HomePage import HomePage
from Page.ItemPage import ItemPage
from Page.LoginPage import LoginPage
from Page.SearchPage import SearchPage

desired_capabilities = [DesiredCapabilities.CHROME,
                        DesiredCapabilities.FIREFOX
                        ]

selenium_grid_url = 'http://127.0.0.1:4444/wd/hub'


class Test(unittest.TestCase):

    def setUp(self):
        for capability in desired_capabilities:
            self.driver = webdriver.Remote(selenium_grid_url, capability)
            self.base_url = "https://www.ebay.com/"
            self.driver.maximize_window()
            self.driver.get(self.base_url)
            return self.driver

    def test_can_user_login(self):
        with allure.step("Check if user can make a purchase"):
            home_page = HomePage(self.driver)
            home_page.visit_login_page()
            login_page = LoginPage(self.driver)
            login_page.login('alexislopezg07@gmail.com', 'Yamero!')
            home_page = HomePage(self.driver)
            home_page.search_item('2017 Rollerblade Hombre')
            search_page = SearchPage(self.driver)
            search_page.select_rollerblade()
            item_page = ItemPage(self.driver)
            item_page.add_item_to_cart()
            checkout_page = CheckoutPage(self.driver)
            checkout_page.insert_address_information("Av. Buenos Aires #809",
                                                     "Res. Las Palmas",
                                                     "Santo Domingo",
                                                     "Distrito Nacional",
                                                     "10011",
                                                     "8095942092")

    def tearDown(self):
        self.driver.quit()
