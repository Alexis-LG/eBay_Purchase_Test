import pytest
from chromedriver_binary.utils import get_chromedriver_filename
from selenium.webdriver.chrome.webdriver import WebDriver

from Page.HomePage import HomePage
from Page.LoginPage import LoginPage
from Page.SearchPage import SearchPage


@pytest.fixture
def browser():
    with WebDriver(get_chromedriver_filename()) as browser:
        browser.maximize_window()
        browser.get("https://www.ebay.com")
        yield browser


@pytest.fixture()
def homepage(browser):
    return HomePage(browser)


@pytest.fixture()
def loginpage(browser):
    return LoginPage(browser)


@pytest.fixture()
def searchpage(browser):
    return SearchPage(browser)
